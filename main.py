"""This program peaks inside the inputted .zip file.
"""

import zipfile, os
from pathlib import Path


def main():
    file_name = input("Please enter the .zip filename: ")
    zip_file = zipfile.ZipFile(file_name)
    file_list = zip_file.namelist()
    print()
    #
    print(f"FILES AND FOLDERS IN \"{file_name}\":")
    for file in file_list[4:]:
        print(file)


if __name__ == "__main__":
    main()
