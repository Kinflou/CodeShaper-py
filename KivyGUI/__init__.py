## System Imports


## Application Imports
import Lib
from KivyGUI.App import App


## Library Imports


def Initialize():
    Lib.Initialize()
    App().run()


if __name__ == '__main__':
    Initialize()
