import os


# Fetch files from the folder given as argument
def FetchFilesInFolder(directory):
    if os.path.isdir(directory):
        files = tuple(item for item in os.listdir(directory)
                      if os.path.isfile(os.path.join(directory, item)))
        return(files)
    else:
        return(None)

# test code for getting files a directory using
# FetchFilesInFolder() function and print them
'''
Files = ""
testpath = input("enter path\n")
Files = FetchFilesInFolder(testpath)
if(Files):
    for File in Files:
        print(File)
else:
    print('folder doesnt exist or it is empty')
'''
