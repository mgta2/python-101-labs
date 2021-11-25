# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

import pathlib

desktop = pathlib.Path("C:\\Users\Matthew\Desktop")
destination = pathlib.Path("C:\\Users\Matthew\Desktop\Pics")
destination.mkdir(exist_ok=True)

for file in desktop.iterdir():
    if file.suffix == ".png":
        newfile = destination.joinpath(file.name)
        file.replace(newfile)
