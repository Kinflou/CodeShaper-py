## System Imports
from glob import glob
from pathlib import Path
from dataclasses import dataclass


## Application Imports
from Library.Projects.Internal.Types.VCXSolution import VCXSolution
from Library.Shaping.Patch.data import ShapingPatch


## Library Imports
import hjson
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(order=True)
class ShapingConfiguration:

	name: str
	shape_project: str
	source: str
	target: str
	backup: str
	result: str
	
	@classmethod
	def from_hjson(cls, content):
		return cls.from_dict(hjson.loads(content))


@dataclass_json
@dataclass(order=True)
class ProjectConfiguration:

	name: str
	projects: dict[str, str]
	target: str
	description: str
	
	@classmethod
	def from_hjson(cls, content):
		return cls.from_dict(hjson.loads(content))


class ShapingProject:
	
	def __init__(self, directory):
		self.directory = directory
		
		settings_path = f'{directory}/settings.hjson'
		self.configuration: ProjectConfiguration = ProjectConfiguration.from_hjson(Path(settings_path).read_text())
		
		self.patches: list[ShapingPatch] = []
		self.target = None
	
	def load_full(self):
		self.__load_patches()
	
	def __load_patches(self):
		for file in glob(f'{self.directory}/projects/**/*.hjson', recursive=True):
			path = Path(file)
			
			patch = ShapingPatch.from_hjson(path.read_text())
			patch.name = path.stem
			
			self.patches.append(patch)

