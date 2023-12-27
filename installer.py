import re
import os


def get_mod_directory(path: str):

    if os.path.exists(path) and os.path.isdir(path):
        return path

    else:
        print("The default Stellaris mod path is not found, please enter the correct one")
        alt_path = input("Path: ")

        return get_mod_directory(alt_path)


def check_available_mods(stellaris_mods: str):
    """Check user stellaris mods folder and return all available mods as mods and installed mods"""

    def is_number(name: str):
        """for checking if directory/file name is only consisting of numbers(workshop id)"""
        try:
            int(name)
            return True
        except ValueError:
            return False

    mods = {
        "installed": [],
        "missing": []
    }

    # get mods dir
    with os.scandir(stellaris_mods) as entries:
        available_mods = [
            mod.name for mod in entries if mod.is_dir() and is_number(mod.name)]

    # get mods pointer
    with os.scandir(stellaris_mods) as entries:
        available_pointers = [mod.name.split(".")[0] for mod in entries if mod.is_file() and mod.name.endswith(
            ".mod") and is_number(mod.name.split(".")[0])]

    # convert to set for faster operations
    mods_dir = set(available_mods)
    mods_pointer = set(available_pointers)

    # mods that have its pointer
    mods["installed"] = mods_dir.intersection(mods_pointer)

    # mods that doesn't have/missing its pointer
    mods["missing"] = mods_dir.difference(mods_pointer)

    return mods


def main():
    stellaris_path = os.path.join(os.path.expanduser(
        "~"), "OneDrive", "Documents", "Paradox Interactive", "Stellaris", "mod")

    MODS_DIRECTORY = get_mod_directory(stellaris_path)
    mods = check_available_mods(MODS_DIRECTORY)


if __name__ == "__main__":
    main()
