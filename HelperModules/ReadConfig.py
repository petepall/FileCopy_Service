import sys
from HelperModules.CheckFileExistance import check_folder_exists, create_folder

sys.path += ['filecopy_service/HelperModules']

CONFIG_FOLDER = 'c:\\PyWinCopy\\'
CONFIG_FILE = 'c:\\PyWinCopy\\config.json'


def check_config_file_exists():
    import os.path

    if os.path.isfile(CONFIG_FILE):
        return True
    else:
        return False


def create_config_file():
    import json

    if not check_folder_exists(CONFIG_FOLDER):
            create_folder(CONFIG_FOLDER)

    originating_file: str = input('Enter copy from file location: ')
    destination_file: str = input('Enter copy to file location: ')

    config = {'origin': originating_file, 'dest': destination_file}

    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)


def read_config_file():
    import json

    with open(CONFIG_FILE, 'r') as file:
        config = json.load(file)

    return config
