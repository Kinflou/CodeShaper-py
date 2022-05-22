## System Imports
from dataclasses import dataclass


## Application Imports


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
	projects: str
	target: str
	description: dict[str, str]
	
	@classmethod
	def from_hjson(cls, content):
		return cls.from_dict(hjson.loads(content))


