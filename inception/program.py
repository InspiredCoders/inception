import os
from docopt import docopt
from core import get_file_names, create_folders_if_necessary, move_files
from config import read_config, get_mapping_dictionary


def validate_path(folder_path):
    '''
    Function to validate whether the path provided is a
    correct folder path or not.
    '''
    return os.path.isdir(folder_path)


def get_cli_args():
    '''
    Function to collect the command line arguments from user.
    '''
    doc = """Inception

            Usage:
            program.py <folder_path>
    """
    return docopt(doc, version='Inception 1.0')


def main():
    arguments = get_cli_args()
    location = arguments['<folder_path>']
    configured_data = read_config()
    create_folders_if_necessary(
        list(configured_data.keys()), location
    )
    mapping_dictionary = get_mapping_dictionary(read_config())
    move_files(mapping_dictionary, location)


if __name__ == '__main__':
    main()
