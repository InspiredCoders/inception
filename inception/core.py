import os
from pathlib import Path


def get_file_names(folder_path):
    '''
    Function to get the file names inside the folder provided.
    File names from the nested directories are not included.
    '''
    if not os.path.isdir(folder_path):
        return None
    files = tuple(item for item in os.listdir(folder_path)
                  if os.path.isfile(os.path.join(folder_path, item)))
    return files


def create_folders_if_necessary(folder_name_list, target_path):
    '''
    Function to create directories
    '''
    folder_name_list.append('Others')
    for folder_name in folder_name_list:
        Path(target_path).joinpath(folder_name).mkdir(exist_ok=True)


def move_files(mapping_dictionary, target_path):
    '''
    Function to create directories
    '''
    for file_name in get_file_names(target_path):
        file_path = Path(target_path).joinpath(Path(file_name))
        extension = file_path.suffix.lower()
        output_folder_path = Path(target_path).joinpath(
            mapping_dictionary.get(extension, 'Others')
            )
        file_path.rename(output_folder_path.joinpath(file_name))
