"""This program peaks inside the inputted .zip file.
"""

import zipfile, os
from pathlib import Path


def main():
    file_name = input("Please enter the entire filename: ")
    zip_file = zipfile.ZipFile(file_name)
    file_list = zip_file.namelist()
    print()
    # Prints the names of the files/folders in the enterred .zip file.
    print(f"FILES AND FOLDERS IN \"{file_name}\":")
    for element in file_list:
        print(f"\t{element}")
    print()
    # Prints out info of the enterred file.
    command = input("Please enter the name of the file/folder you would like info on: ")
    print()
    file_info = zip_file.getinfo(command)
    print("FILE OR FOLDER INFO:")
    print(f"\tOriginal File Name: {file_info.orig_filename}")
    print(f"\tDate & Time: {file_info.date_time}")
    print(f"\tThe compressed file is {round(file_info.file_size / file_info.compress_size, 2)}x smaller.")


if __name__ == "__main__":
    main()
