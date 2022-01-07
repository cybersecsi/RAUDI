import argparse
from art import text2art
import docker
import os
import sys
from tools.main import get_tools, get_single_tool, list_tools
from helper import log, logErr, check_if_docker_image_exists, get_latest_docker_hub_version, check_if_container_runs

# Default vars
DEFAULT_TOOL_DIR = os.path.dirname(os.path.abspath(__file__))+"/tools/"

# ArgParse
parser = argparse.ArgumentParser(prog="RAUDI", description='Regularly and Automatically Updated Docker Images.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--all", help="Build all tools", action='store_true')
group.add_argument("--single", help="Run a single tool build", type=str)
group.add_argument("--list", help="List all tools", action='store_true')
parser.add_argument("--push", help="Wheter automatically push the new images to the Docker Hub (default=false)", action='store_true')
parser.add_argument("--remote", help="Wheter check against Docker Hub instead of local Docker before build (default=false)", action='store_true')

# Print out a Sexy intro
def sexy_intro():
    secsi_art=text2art("SecSI",font='big')
    print() 
    print(secsi_art)

def build(tool_name, config, push_image, remote_src, tests):
    dirname = DEFAULT_TOOL_DIR + tool_name
    image_exists = check_if_docker_image_exists("{name}:{tag}".format(name=config['name'], tag=config['version']), remote_src)
    if image_exists == False:
        log("Building {docker_image}...".format(docker_image="{name}:{tag}".format(name=config['name'], tag=config['version'])))
        client = docker.from_env()
        client.images.build(buildargs=config['buildargs'], path=dirname, tag="{name}:{tag}".format(name=config['name'], tag=config['version']), rm=True)
        # Get the Docker Image to tag it also as latest
        docker_image = client.images.get("{name}:{tag}".format(name=config['name'], tag=config['version']))
        docker_image.tag(repository=config['name'], tag="latest") # Also tag as latest
    else:
        log("This version already exists, skipping build.")
    


    # Pushing, if specified
    if push_image:
        try:
            check_if_container_runs(config['name'], config['version'], tests)
            push(config['name'], config['version'])
        except docker.errors.ContainerError as e:
            logErr(e)
            logErr("Error running container, push aborted for {docker}:{version}.".format(docker=config['name'], version=config['version']))

def build_one(tool_name, push_image, remote_src):
    log("Checking if tool exists...")
    config = get_single_tool(tool_name)
    if not config:
        logErr("Something is wrong, the tool does not exists!")
        sys.exit(-1)

    log("Tool correctly found.")
    log(config)

    build(tool_name, config, push_image, remote_src, config['tests'])

def build_all(push_image, remote_src):
    tools = get_tools()
    log("Getting config for every tool...")
    for tool in tools:
        tool_name = tool['name'].split('/')[1]
        build(tool_name, tool, push_image, remote_src, tool['tests'])

def push(repo, version):
    docker_hub_version = get_latest_docker_hub_version(repo, org="")
    log("Docker Hub version is {version}".format(version=docker_hub_version))
    if version == docker_hub_version:
        log("Current version on the Docker Hub is the same as this one, skipping push.")
    else:
        log("Pushing image on Docker Hub...")
        client = docker.from_env()
        client.images.push(repository=repo, tag=version)
        if version != "latest":
            client.images.push(repository=repo, tag="latest")
        log("Image successfully pushed")

def main():
    sexy_intro()
    args = parser.parse_args()

    try:
        # List available tools
        if args.list:
            log("Available tools")
            log(list_tools())
        # Build everything
        elif args.all:
            build_all(args.push, args.remote)
        # Build a specific Docker Image
        elif args.single:
            build_one(args.single, args.push, args.remote)
        else:
            parser.print_help()
    except Exception as e:
        logErr(e)

if __name__ == "__main__":
    main()