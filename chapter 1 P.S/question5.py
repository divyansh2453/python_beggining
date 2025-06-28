import os

# Specify the path
path = "D:\\Games"

# Check if the folder exists
if os.path.exists(path):
    contents = os.listdir(path)
    print(f"Contents of directory: {path}")
    for item in contents:
        print(item)
else:
    print(f"The folder '{path}' does not exist.")
