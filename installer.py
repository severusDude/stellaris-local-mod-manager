import re
import os


def get_mod_directory(path: str):

    if os.path.exists(path) and os.path.isdir(path):
        return path

    else:
        print("The default Stellaris mod path is not found, please enter the correct one")
        alt_path = input("Path: ")

        get_mod_directory(alt_path)


def main():
    stellaris_path = os.path.join(os.path.expanduser(
        "~"), "OneDrive", "Documents", "Paradox Interactive", "Stellaris", "mod")

    MODS_DIRECTORY = get_mod_directory(stellaris_path)


if __name__ == "__main__":
    main()
