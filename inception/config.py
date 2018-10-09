import json


def read_config(file_path='config.json'):
    '''
    Function to read configuration file and
    return configuration dictionary.
    '''
    config_data = {}
    with open(file_path) as config_file:
        config_data = json.load(config_file)
    return config_data
