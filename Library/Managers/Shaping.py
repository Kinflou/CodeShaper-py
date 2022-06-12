## System Imports
from glob import glob
from pathlib import Path


## Application Imports
from Library import Constants
from Library.Shaping.Operation import ShapingOperation
from Library.Shaping.Project.data import ShapingConfiguration, ShapingProject


## Library Imports


configurations: list[ShapingConfiguration] = []
projects: list[ShapingProject] = []
operation: ShapingOperation | None = None


def Initialize():
	global configurations
	global projects
	
	for configuration in glob(f'{Constants.configurations_directory}/*.hjson'):
		shaping_configuration: ShapingConfiguration = ShapingConfiguration.from_hjson(Path(configuration).read_text())
		
		shaping_project: ShapingProject | None = None
		path = Path(shaping_configuration.project)
		
		if path.exists():
			for project in projects:
				if project.directory == path:
					shaping_project = project
			
			if not shaping_project:
				shaping_project = ShapingProject(str(path))
				projects.append(shaping_project)
		
		shaping_configuration.shaping_project = shaping_project
		
		configurations.append(shaping_configuration)


def MakeOperation(configuration: ShapingConfiguration) -> ShapingOperation:
	configuration.shaping_project.load_full()
	
	return ShapingOperation(configuration)

