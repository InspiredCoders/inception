import os


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
