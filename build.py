import os
import sys

def main():
    if len(sys.argv) != 2:
        print("You have to give me just one argument. More or less is not allowed.")
        return

    FILE_NAME = "./{}.csv".format(sys.argv[1])
    DOCKER_FILE = "./Dockerfile"
    OUTPUT_DIR_NAME = "./dist/{}".format(sys.argv[1])
    OUTPUT_FILE_NAME = "./dist/{}/Dockerfile".format(sys.argv[1])

    if not os.path.exists(FILE_NAME):
        print("There are no package lists named {}.".format(sys.argv[1]))
        return

    docker_content = ""
    with open(DOCKER_FILE, "r") as f:
        docker_content = f.read()

    with open(FILE_NAME, "r") as f:
        package_list = f.read()

        command_lists = ""
        for package in package_list.splitlines():
            print("Installing {}...".format(package))

            command_lists += "tlmgr install {}; \\\n".format(package)

        docker_content = docker_content.replace(
            "echo \"Do nothing. Yes. Do nothing.\"; \\\n",
            command_lists
        )

    if not os.path.exists(OUTPUT_DIR_NAME):
        os.mkdir(OUTPUT_DIR_NAME)

    with open(OUTPUT_FILE_NAME, "w") as f:
        f.write(docker_content)

    print("Done! Enjoy your tex life!")

if __name__ == "__main__":
    main()
