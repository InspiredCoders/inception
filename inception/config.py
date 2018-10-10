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


def get_mapping_dictionary(config_data):
    '''
    Function to convert configuration dictionary
    to mapping dictionary.
    '''
    return {
        '.' + extension.split()[0]: directory_name
        for directory_name, extensions in config_data.items()
        for extension in extensions.split(',')
        }
