import os
import requests

from items import _get_home_dir_path

SLASH = '\\'


def _create_bat_file():
    bat_path: str = f'{_get_home_dir_path()}{SLASH}commands{SLASH}touch.bat'
    py_path: str = f'{_get_home_dir_path()}{SLASH}commands{SLASH}create_file.py'
    py_items_path: str = f'{_get_home_dir_path()}{SLASH}commands{SLASH}items.py'

    if not os.path.exists(bat_path):
        with (open(bat_path, 'w') as file,
              open(py_path, 'w') as create_file,
              open(py_items_path, 'w') as items_file):
            file.write("@echo off\n")
            file.write(f'python {py_path} %*')

            py_create_file_text = requests.get(
                'https://raw.githubusercontent.com/Sciencewolf/touch-cli/main/create_file.py'
            )
            create_file.write(py_create_file_text.text)

            py_items_file_text = requests.get(
                'https://raw.githubusercontent.com/Sciencewolf/touch-cli/main/items.py'
            )
            items_file.write(py_items_file_text.text)

        os.system('start /B start cmd.exe @cmd /k touch -h')
    else:
        print("Error!")


def _add_path():
    current_path = os.environ.get('PATH')
    new_directory = f"{_get_home_dir_path()}{SLASH}commands{SLASH}"
    new_path = f'{new_directory};{current_path}'
    os.environ['PATH'] = new_path


_create_bat_file()
_add_path()
