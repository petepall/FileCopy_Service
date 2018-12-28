CONFIG_FILE = 'c:\\PyWinCopy\\config.json'


def check_config_file_exists():
    import os.path

    if os.path.isfile(CONFIG_FILE):
        return True
    else:
        return False


def create_config_file():
    import json

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
