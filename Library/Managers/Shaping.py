## System Imports
from glob import glob
from pathlib import Path


## Application Imports
from Library import Constants
from Library.Shaping.Operation import ShapingOperation
from Library.Projects.Internal.Types.VCXSolution import VCXSolution
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
		
		project: ShapingProject | None = None
		path = Path(shaping_configuration.shape_project)
		
		if path.exists():
			for project in projects:
				if project.configuration.target == path:
					project = project
			
			if not project:
				project = ShapingProject(str(path))
				projects.append(project)
		
		shaping_configuration.shaping_project = project
		
		configurations.append(shaping_configuration)


def MakeOperation(configuration: ShapingConfiguration) -> ShapingOperation:
	configuration.shaping_project.load_full()
	
	# TODO: Do proper dynamic loading of targets, as this is temporary
	target = VCXSolution(configuration.source)
	
	return ShapingOperation(configuration, target)

