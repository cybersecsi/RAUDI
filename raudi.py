import argparse
from python_on_whales import docker, DockerException
import questionary
import os
import sys
from manager import Manager
from helper import log, logErr
import helper
from dotenv import load_dotenv

# Default vars
DEFAULT_TOOL_DIR = os.path.dirname(os.path.abspath(__file__))+"/tools/"

# ArgParse
parser = argparse.ArgumentParser(prog="RAUDI", description='Regularly and Automatically Updated Docker Images.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--all", help="Build all tools", action='store_true')
group.add_argument("--single", help="Run a single tool build", type=str)
group.add_argument("--runsh", help="Run a container with /bin/sh as entrypoint (debug purposes)", type=str)
group.add_argument("--test", help="Run tests for a single tool", type=str)
group.add_argument("--list", help="List all tools", action='store_true')
group.add_argument("--bootstrap", help="Add a new tool", type=str)
group.add_argument("--readme", help="Check if every Image has a description on the Docker Hub", action='store_true')
parser.add_argument("--push", help="Whether automatically push the new images to the Docker Hub (default=false)", action='store_true')
parser.add_argument("--remote", help="Whether check against Docker Hub instead of local Docker before build (default=false)", action='store_true')
parser.add_argument("--force", help="Build the image no matter what (even if the same tag already exists)", action='store_true')

# Print out a Sexy intro
def sexy_intro():
  print(
    f'''
    ███████╗███████╗ ██████╗███████╗██╗
    ██╔════╝██╔════╝██╔════╝██╔════╝██║
    ███████╗█████╗  ██║     ███████╗██║
    ╚════██║██╔══╝  ██║     ╚════██║██║
    ███████║███████╗╚██████╗███████║██║
    ╚══════╝╚══════╝ ╚═════╝╚══════╝╚═╝
    ''')   

# Execute a test 
def runsh(args):
    name = args.runsh
    manager = Manager()
    organization = manager._organization
    cmd = "docker run -it --rm --entrypoint=/bin/sh {}/{}".format(organization, name)
    log("Executing the following command:")
    log(cmd)
    os.system(cmd)

def build(tool_name, config, args, tests):
    # Args and Vars
    push_image = args.push
    remote_src = args.remote
    force_build = args.force
    dirname = DEFAULT_TOOL_DIR + tool_name

    image_exists = helper.check_if_docker_image_exists("{name}:{tag}".format(name=config['name'], tag=config['version']), remote_src)
    if image_exists == False or force_build == True:
        log("Building {docker_image}...".format(docker_image="{name}:{tag}".format(name=config['name'], tag=config['version'])))
        helper.print_docker_build_command(config['name'], config['version'], config['buildargs'])
        # Build image with version tag
        enable_progress_env = helper.get_env('RAUDI_DOCKER_BUILD_PROGRESS', False)
        enable_progress = False if (enable_progress_env == False) or (enable_progress_env == "False") else "auto"
        try:
            docker.buildx.build(dirname, load=True, progress=enable_progress, build_args=config['buildargs'], tags="{name}:{tag}".format(name=config['name'], tag=config['version']))
            # Tag image as 'latest'
            docker.tag("{name}:{tag}".format(name=config['name'], tag=config['version']), "{name}:{tag}".format(name=config['name'], tag='latest'))
        except Exception as e:
            logErr(e)
            logErr(f"Unable to build {config['name']}:{config['version']}")
            Manager().set_exit_code(1) # only set the exit code to 1, but keep creating Docker images
    else:
        log("This version already exists, skipping build.")
    
    # Pushing if specified and the image exists LOCALLY
    if push_image and helper.check_if_docker_image_exists("{name}:{tag}".format(name=config['name'], tag=config['version']), False):
        try:
            helper.check_if_container_runs(config['name'], config['version'], tests)
            push(dirname, config['name'], config['version'], config['buildargs'])
        except Exception as e:
            logErr(e)
            logErr("Error running container, push aborted for {docker}:{version}.".format(docker=config['name'], version=config['version']))
            Manager().set_exit_code(1) # only set the exit code to 1, but keep creating Docker images

def build_one(args):
    # Get Manager Singleton
    manager = Manager()

    # Arguments
    tool_name = args.single

    # Build tool
    log("Checking if tool exists...")
    config = manager.get_single_tool(tool_name)
    if not config:
        logErr("Something is wrong, the tool does not exists!")
        sys.exit(1)

    log("Tool correctly found.")
    log(config)

    build(tool_name, config, args, config['tests'])

def build_all(args):
    # Get Manager Singleton
    manager = Manager()

    # Build tools
    tools = manager.get_tools()
    log("Getting config for every tool...")
    for tool in tools:
        tool_name = tool['name'].split('/')[1]
        build(tool_name, tool, args, tool['tests'])

def push(dirname, repo, version, build_args):
    docker_hub_version =  helper.get_latest_docker_hub_version(repo, org="")
    log("Docker Hub version is {version}".format(version=docker_hub_version))
    if version == docker_hub_version:
        log("Current version on the Docker Hub is the same as this one, skipping push.")
    else:
        log("Rebuilding and pushing image on Docker Hub...")
        enable_progress_env = helper.get_env('RAUDI_DOCKER_BUILD_PROGRESS', False)
        enable_progress = False if (enable_progress_env == False) or (enable_progress_env == "False") else "auto"
        try:
            docker.buildx.build(dirname, load=False, push=True, progress=enable_progress, build_args=build_args, tags=[f"{repo}:{version}",f"{repo}:latest"], platforms=["linux/amd64", "linux/arm64"])
            log("{name}:{tag} successfully pushed to Docker Hub for both amd64 and arm64 architectures".format(name=repo, tag=version))
        except:
            logErr("Error while pushing both amd64 and arm64, pushing just for amd64")
            docker.buildx.build(dirname, load=False, push=True, progress=enable_progress, build_args=build_args, tags=[f"{repo}:{version}",f"{repo}:latest"], platforms=["linux/amd64"])
            log("{name}:{tag} successfully pushed to Docker Hub for amd64 architecture".format(name=repo, tag=version)) 

def bootstrap(args):
    # Get Manager Singleton
    manager = Manager()

    log("Bootstrapping new tool...")
    new_tool_name = args.bootstrap
    config = manager.get_single_tool(new_tool_name)
    if config != None:
        logErr("Tool with this name already exists.")
        sys.exit(1)

    template = questionary.select("What template do you want to use?", choices=helper.get_list_templates()).ask()
    helper.create_tool_folder(new_tool_name, template)
    log("Tool bootstrapped. You may find it at /tools/{tool_name}".format(tool_name=new_tool_name))

def test_commands(args):
    # Get Manager Singleton
    manager = Manager()

    # Arguments
    tool_name = args.test

    log("This command should be executed AFTER building the image and BEFORE pushing it.")

    # Build tool
    log("Checking if tool exists...")
    config = manager.get_single_tool(tool_name)
    if not config:
        logErr("Something is wrong, the tool does not exists!")
        sys.exit(1)

    log("Tool correctly found.")
    log(config)
    
    image_exists = helper.check_if_docker_image_exists("{name}:{tag}".format(name=config['name'], tag=config['version']), False)
    if not image_exists:
        logErr("Image does not exist locally, cannot execute tests on it.")
        sys.exit(1)

    try:
        helper.check_if_container_runs(config['name'], config['version'], config['tests'])
        log("Tests passed, {docker}:{version} can be pushed safely.".format(docker=config['name'], version=config['version']))
    except Exception as e:
        logErr(e)
        logErr("Error running container, push aborted for {docker}:{version}.".format(docker=config['name'], version=config['version']))

def check_readme():
    # Build tools
    manager = Manager()
    tools = manager.get_tools()
    log("Getting tools...")
    for tool in tools:
        readme_set =  helper.check_if_readme_is_set(tool['name'])
        if not readme_set:
            log("Missing README for Docker Image {image}".format(image=tool['name']))

def main():
    sexy_intro()
    args = parser.parse_args()
    # Load .env file
    load_dotenv()
    # Init Singleton Manager
    manager = Manager()
    manager.init()

    try:
        # List available tools
        if args.list:
            log("Available tools")
            log(manager.list_tools())
        # Build everything
        elif args.runsh:
            runsh(args)
        elif args.all:
            build_all(args)
        # Build a specific Docker Image
        elif args.single:
            build_one(args)
        elif args.test:
            test_commands(args)
        elif args.bootstrap:
            bootstrap(args)
        # Check READMEs on Docker Hub
        elif args.readme:
            check_readme()
        else:
            parser.print_help()
    except Exception as e:
        logErr(e)
        manager.set_exit_code(1)

    log(f"RAUDI completed, exiting with return code {manager.get_exit_code()}")
    sys.exit(manager.get_exit_code())

if __name__ == "__main__":
    main()