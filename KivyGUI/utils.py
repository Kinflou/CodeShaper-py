## System Imports
import os
import sys
from pathlib import Path


## Application Imports


## Library Imports
from kivy.lang import Builder


if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_kv_relative_path(file):
    relative_path = file[len(application_path) + 1:]
    return f'{os.path.splitext(relative_path)[0]}.kv'


def load_relative_kv(file):
    return Builder.load_file(get_kv_relative_path(file))

