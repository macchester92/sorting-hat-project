import pathlib
import hashlib
import os


print('''
*************************

Welcome to Sorting Hat. I'm smart, elegant and fast.
Version 1.0

*************************
''')

user_path = input('Drag a folder inside this window: ')
directory_path = user_path.strip()

checksum_table = {}

# File checksum generator


def blake2b_update_from_file(filename, hash):
    assert Path(filename).is_file()
    with open(str(filename), "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash.update(chunk)
    return hash


def blake2b_file(filename):
    return blake2b_update_from_file(filename, hashlib.blake2b()).hexdigest()


# Directory checksum generator
def blake2b_update_from_dir(directory, hash):
    assert Path(directory).is_dir()
    for path in sorted(Path(directory).iterdir()):
        hash.update(path.name.encode())
        if path.is_file():
            hash = blake2b_update_from_file(path, hash)
        elif path.is_dir():
            hash = blake2b_update_from_dir(path, hash)
    return hash


def blake2b_dir(directory):
    return blake2b_update_from_dir(directory, hashlib.blake2b()).hexdigest()


# Main function
def get_blake2b_checksum(directory_path):
    for path in sorted(Path(directory_path).iterdir()):
        file_type_check = pathlib.Path(path).stem
        if not file_type_check.startswith('.'):
            if path.is_file():
                file_hash = blake2b_file(path)
                checksum_table[f'{path}'] = file_hash
            elif path.is_dir():
                dir_hash = get_blake2b_checksum(path)
                checksum_table.update(dir_hash)
    return checksum_table


get_blake2b_checksum(directory_path)

# Checks for duplicates using flipped dictionary
duplicates = {}
list_of_duplicates = []

for key, value in checksum_table.items():
    if value not in duplicates:
        duplicates[value] = [key]
    else:
        duplicates[value].append(key)

# Creates a list of duplicates for review
for key, value in duplicates.items():
    if len(value) > 1:
        list_of_duplicates.append(value)

# Counts number of duplicates
duplicate_count = 0
for item in list_of_duplicates:
    duplicate_count += len(item)

# Context menu for choosing an action
print(f'I have found {duplicate_count} duplicates')
while True:
    
    user_action = input(
        '\nWould you like to do: [R]eview  || [D]elete (!!!)  || [A]bort : ').lower()
    if user_action == 'r':
        for item in list_of_duplicates:
            for duplicate in item[:-1:]:
                print(duplicate)
    elif user_action == 'd':
        for item in list_of_duplicates:
            for duplicate in item[:-1:]:
                os.remove(duplicate)
                print(duplicate + " removed!")
        break
    elif user_action == 'a':
        break
    else:
        print('Something is wrong. Please try again!')
print('Thank you for using Sorting Hat App. Have a great day!')
