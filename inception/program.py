import os
from core import get_file_names, create_folders_if_necessary, move_files
from config import read_config, get_mapping_dictionary


def get_user_input():
    '''
    Function to read user input
    '''
    path = ''
    while True:
        path = input('Provide valid folder path: ')
        if not path.strip() or not validate_path(path):
            continue
        break
    return path


def validate_path(folder_path):
    '''
    Function to validate whether the path provided is a
    correct folder path or not.
    '''
    return os.path.isdir(folder_path)


def main():
    location = get_user_input()
    configured_data = read_config()
    create_folders_if_necessary(
        list(configured_data.keys()), location
        )
    mapping_dictionary = get_mapping_dictionary(read_config())
    move_files(mapping_dictionary, location)


if __name__ == '__main__':
    main()
