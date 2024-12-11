import os

def list_files(directory):
    try:
        files = os.listdir(directory)

        files = []
        directories = []

        for file in files:
            if os.path.isfile(file):
                files.append(file)
            elif os.path.isdir(file):
                directories.append(file)

        result = {
            "files": files,
            "directories": directories
        }

        print(result)

    except FileNotFoundError:
        print("not found")

direct= input("Enter the directory: ")
list_files(direct)
