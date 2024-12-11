import os

def files_list(directory):
 try:
    files = os.listdir(directory)
    print(files)
    for file in files:
        print(file)
 except FileNotFoundError:
     print("File Not Found")

directory = input("directory name: ")
files_list(directory)
