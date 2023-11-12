import os
import requests

import win10toast
from items import _get_home_dir_path

SLASH = '\\'


def _create_bat_file():
    bat_path: str = f'{_get_home_dir_path()}{SLASH}commands{SLASH}touch.bat'
    py_path: str = f'{_get_home_dir_path()}{SLASH}commands{SLASH}create_file.py'

    if not os.path.exists(bat_path):
        with (open(bat_path, 'w') as file, open(py_path, 'w') as create_file):
            file.write("@echo off\n")
            file.write(f'python {py_path} %*')

            r = requests.get('https://raw.githubusercontent.com/Sciencewolf/touch-cli/main/create_file.py')
            create_file.write(r.text)

        w = win10toast.ToastNotifier()
        w.show_toast("Alert!", 'Successfully installed!', duration=5, threaded=True)
        os.system('start /B start cmd.exe @cmd /k touch -h')
    else:
        w = win10toast.ToastNotifier()
        w.show_toast("Already installed!", "Try 'touch -h'", duration=5, threaded=True)


def _add_path():
    current_path = os.environ.get('PATH')
    new_directory = f"{_get_home_dir_path()}{SLASH}commands{SLASH}"
    new_path = f'{new_directory};{current_path}'
    os.environ['PATH'] = new_path

    w = win10toast.ToastNotifier()
    w.show_toast("Added to PATH! Type 'touch -h'", duration=5, threaded=True)


_create_bat_file()
_add_path()
