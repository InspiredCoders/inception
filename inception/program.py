import os


def get_user_input():
    '''
    Function to read user input
    '''
    path = ''
    while True:
        path = input('Provide valid folder path: ')
        if not path.strip():
            continue
        break
    return path
