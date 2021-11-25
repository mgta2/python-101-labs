# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib

my_path = pathlib.Path().cwd()

my_str = 'C:\\Users'

while str(my_path) != my_str:
    print(f"{'Files in: ':>5} {my_path.name}")
    for filepath in my_path.iterdir():
        if filepath.suffix == ".py":
            print(f"{'- Filename: ':>5} {filepath.name}")
    my_path = my_path.parent