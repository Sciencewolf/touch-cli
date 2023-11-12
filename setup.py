import os
from items import _get_home_dir_path

SLASH = '\\'


def _create_bat_file():
    if not os.path.exists(f'{_get_home_dir_path()}{SLASH}commands{SLASH}touch.bat'):
        with open(f'{_get_home_dir_path()}{SLASH}commands{SLASH}touch.bat', 'w') as file:
            file.write("@echo off\n")
            file.write(f'python {_get_home_dir_path()}{SLASH}command{SLASH}create_file.py %1 %2 %3')
    else:  # remove this file
        # os.remove(f'{_get_home_dir_path()}{SLASH}')
        print('Exists')


def _add_path():
    current_path = os.environ.get('PATH')
    new_directory = f"{_get_home_dir_path()}{SLASH}commands{SLASH}"
    new_path = f'{new_directory};{current_path}'

    os.environ['PATH'] = new_path


_create_bat_file()
# _add_path()
