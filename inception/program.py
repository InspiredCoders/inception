import os


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
