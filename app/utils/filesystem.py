import os


def find_root_dir(file_like_object):
    current_dir = os.path.dirname(os.path.abspath(file_like_object))

    while True:
        if 'setup.py' in os.listdir(current_dir):
            return current_dir
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached the root directory
            raise FileNotFoundError("setup.py not found in any parent directories")
        current_dir = parent_dir
