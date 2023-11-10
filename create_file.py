import os
import sys
from items import _get_platform
from items import _get_home_dir_path
from items import _get_current_dir_path

SLASH = "\\"


def _hint():
    print("\n Try: ")
    print("\tHelp: touch -h\n")
    print("\tSee example's: touch -e\n")
    print(f"\tSystem: {_get_platform()}\n")


def _help():
    print('\t[-h, --help] help')
    print('\t[-d, --dirpath] directory path')
    print('\t[-e, --example] example\'s')
    print('\t[-r, --rename] rename file')
    print('\t[-ch, --currhomedir] see current and home directory')
    print('\t[-m, --multiple] create 2 or more files')
    print('\t[-a, --abspath] absolute path of the file')
    print('\tLinux: /home/<your_username>/ \n\tWindows: C:/Users/<your_username>/ is the default absolute path')
    # ----------------------------------------------------------------------
    print("\n Usage: ")

    print('\ttouch <option> <dirpath> <filename(s)>\n')

    print('\t- See current directory and home directory')
    print('\ttouch -ch')

    print('\t- Rename file')
    print('\ttouch -r <filename> <new_filename>')

    print("\t- Create file in current directory")
    print("\ttouch <filename>")

    print("\t- Create all files")
    print('\ttouch -m "<filename1 filename2 ...>"')

    print("\t- Create file(s) in current directory")
    print("\ttouch -d <dirpath> <filename(s)>")

    print("\t- Create file with absolute path")
    print("\ttouch --abspath <absolute_path>")
    # ---------------------------------------------------------------------
    print("\nDeveloped by Sciencewolf\n")


def _example():
    print("\n Example: ")

    print('\t- Rename file')
    print('\ttouch -r text.txt book.txt')

    print("\t- Create hello.txt file in current directory")
    print("\ttouch hello.txt")

    print("\t- Create hello.py file in current directory")
    print("\ttouch hello.py")

    print("\t- Create hello.txt and test.py file in current directory")
    print("\ttouch hello.txt test.py")

    print("\t- Create hello.txt in C:/Users/<your_username>/Documents directory")
    print("\ttouch -d C:/Users/<your_username>/Documents hello.txt")

    print("\t- Create file with absolute path")
    print("\ttouch -a C:/Users/<your_username>/Desktop/hello.py\n")


def _execute():
    if sys.argv[1] in ['-d', '--dirpath']:
        with open(f"{sys.argv[2]}/{sys.argv[3]}", 'w') as file:
            file.write("")
        print(f'\n\tFile created successfully: at [{sys.argv[2]}{SLASH}{sys.argv[3]}]')

    elif sys.argv[1] in ['-a', '--abspath']:
        with open(f"{sys.argv[2]}", 'w') as file:
            file.write("")
        print(f"\n\tFile created successfully: {sys.argv[2]}\n")

    elif sys.argv[1] in ['-r', '--rename']:
        os.rename(sys.argv[2], sys.argv[3])
        print(f"\n\tFile successfully renamed: from [{sys.argv[2]}] to [{sys.argv[3]}]\n")

    elif sys.argv[1] in ['-ch', '--currhomedir']:
        print(f"\n\tHome directory: {_get_home_dir_path()}\n")
        print(f"\tCurrent directory: {_get_current_dir_path()}\n")

    elif sys.argv[1] in ['-m', '--multiple']:
        args = [arg for arg in sys.argv[2].split(" ")]
        for arg in args:
            with open(arg, 'w') as file:
                file.write("")
        print(f'File(s) created')

    else:
        with open(f"{sys.argv[1]}", 'w') as file:
            file.write("")
        print(f"\n\tFile created successfully: {_get_current_dir_path()}{SLASH}{sys.argv[1]}\n")


def main():
    if len(sys.argv) == 1:
        _hint()
    elif sys.argv[1] in ['-h', '--help']:
        _help()
    elif sys.argv[1] in ['-e', '--example']:
        _example()
    else:
        _execute()


main()
