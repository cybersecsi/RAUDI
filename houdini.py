import argparse
from art import text2art
import docker
import os
import sys
from tools.main import get_tools, get_single_tool
from helper import check_if_docker_image_exists, get_latest_docker_hub_version

# Default vars
DEFAULT_TOOL_DIR = os.path.dirname(os.path.abspath(__file__))+"/tools/"

# ArgParse
parser = argparse.ArgumentParser(prog="HOUDINI", description='Hacking Offensive Updated Docker Images for Network Intrusion.')
parser.add_argument("--all", help="Build all tools", action='store_true')
parser.add_argument("--single", help="Run a single tool build", type=str)
parser.add_argument("--push", help="Wheter automatically push the new images to the Docker Hub (default=false)", action='store_true')

# Print out a Sexy intro
def sexy_intro():
    secsi_art=text2art("SecSI",font='big')
    print()
    print(secsi_art)

def build(tool_name, config, push_image):
    dirname = DEFAULT_TOOL_DIR + tool_name
    current_image = check_if_docker_image_exists("{name}:{tag}".format(name=config['name'], tag=config['version']))
    if not current_image:
        print("Building {docker_image}...".format(docker_image="{name}:{tag}".format(name=config['name'], tag=config['version'])))
        client = docker.from_env()
        client.images.build(buildargs=config['buildargs'], path=dirname, tag="{name}:{tag}".format(name=config['name'], tag=config['version']))
        # Get the Docker Image to tag it also as latest
        docker_image = client.images.get("{name}:{tag}".format(name=config['name'], tag=config['version']))
        docker_image.tag(repository=config['name'], tag="latest") # Also tag as latest
    else:
        print("This version already exists, skipping build.")
    
    # Pushing, if specified
    if push_image:
        push(config['name'], config['version'])

def build_one(tool_name, push_image):
    print("Checking if tool exists...")
    config = get_single_tool(tool_name)
    if not config:
        print("Something is wrong, the tool does not exists!")
        sys.exit(-1)

    print("Tool correctly found.")
    print(config)

    build(tool_name, config, push_image)

def build_all(push_image):
    tools = get_tools()
    print("Getting config for every tool...")
    for tool in tools:
        tool_name = tool['name'].split('/')[1]
        build(tool_name, tool, push_image)

def push(repo, version):
    docker_hub_version = get_latest_docker_hub_version(repo, org="")
    print("Docker Hub version is {version}".format(version=docker_hub_version))
    if version == docker_hub_version:
        print("Current version on the Docker Hub is the same as this one, skipping push.")
    else:
        print("Pushing image on Docker Hub...")
        client = docker.from_env()
        client.images.push(repository=repo, tag=version)
        if version != "latest":
            client.images.push(repository=repo, tag="latest")
        print("Image successfully pushed")

def main():
    sexy_intro()
    args = parser.parse_args()

    # Build everything
    if args.all:
        build_all(args.push)
    # Build a specific Docker Image
    elif args.single:
        build_one(args.single, args.push)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()