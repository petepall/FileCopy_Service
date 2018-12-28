def check_file_exists(filename: str) -> bool:
    import os

    if os.path.isfile(filename):
        return True
    else:
        return False


def check_folder_exists(location: str) -> bool:
    import os

    if os.path.isdir(location):
        return True
    else:
        return False


def create_folder(location: str):
    import os

    print(location)
    try:
        os.mkdir(location)
    except FileExistsError:
        pass
