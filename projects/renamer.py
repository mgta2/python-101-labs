# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib

desktop = pathlib.Path("C:\\Users\Matthew\Desktop")
new_path = pathlib.Path("C:\\Users\Matthew\Screenshots")
new_path.mkdir(exist_ok=True)

# Will rename screenshots as "Screenshot_1.png" etc.
counter = 0

for file in desktop.iterdir():
    if file.suffix == ".png":
        counter += 1
        my_str = f"Screenshot_{counter}.png"
        new_file = new_path.joinpath(my_str)
        file.replace(new_file)