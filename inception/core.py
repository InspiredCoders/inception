# from collections import tuple
import os
Files = ""


def FetchFilesInFolder(directory):
    if os.path.isdir(directory):
        files = tuple(item for item in os.listdir(directory) if os.path.isfile(directory + '\\' + item))
        return(files)
    else:
        return(None)

'''
testpath = input("enter path\n")
Files = FetchFilesInFolder(testpath)
if(Files):
    for File in Files:
        print(File)
else:
    print('folder doesnt exist')
'''  