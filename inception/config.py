import json


def read_config():
    '''
    Function to read configuration file and
    return configuration dictionary.
    '''
    config_data = {}
    with open('config.json') as config_file:
        config_data = json.load(config_file)
    return config_data
