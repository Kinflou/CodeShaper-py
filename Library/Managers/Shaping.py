## System Imports
from glob import glob
from pathlib import Path


## Application Imports
from Library import Constants
from Library.Shaping.Project.data import  ShapingConfiguration


## Library Imports


configurations = []
projects = []


def Initialize():
	global configurations
	
	for configuration in glob(f'{Constants.configurations_directory}/*.hjson'):
		shaping_configuration = ShapingConfiguration.from_hjson(Path(configuration).read_text())
		
		configurations.append(shaping_configuration)


