## System Imports


## Application Imports
import Library
from KivyGUI.App import App


## Library Imports


def Initialize():
    Library.Initialize()
    App().run()


if __name__ == '__main__':
    Initialize()
