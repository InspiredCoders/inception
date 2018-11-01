import os
from core import get_file_names, create_folders_if_necessary, move_files
from config import read_config, get_mapping_dictionary


def run_app(location):
    configured_data = read_config()
    create_folders_if_necessary(
        list(configured_data.keys()), location
    )
    mapping_dictionary = get_mapping_dictionary(read_config())
    move_files(mapping_dictionary, location)


if __name__ == '__main__':
    main()
