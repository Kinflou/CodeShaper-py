## System Imports
import os


## Application Imports


## Library Imports


class WindowsEnvironment:

	application_directory: str = f'{os.getenv("APPDATA")}/CodeShaper/'
	

class LinuxEnvironment:
	
	application_directory: str = "/usr/local/CodeShaper/"


# TODO: Do a proper environment pick regarding the current OS
environment = WindowsEnvironment

application_directory = environment.application_directory

configurations_directory = f'{application_directory}/configurations/'
user_settings_path = f'{application_directory}/user_settings.hjson'
