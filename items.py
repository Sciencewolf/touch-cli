import os.path as op
import os


def _get_home_dir_path():
    return op.expanduser('~')


def _get_current_dir_path():
    return os.getcwd()
