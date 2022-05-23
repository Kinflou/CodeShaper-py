## System imports
from typing import Optional
from dataclasses import dataclass, field


## Application Imports


## Library Imports
import hjson
from dataclasses_json import config, dataclass_json


@dataclass(order=True)
class ShapingReplacement:
	
	location: str
	from_: str = field(metadata=config(field_name="from"))
	to: str
	flags: str = ''
	reference_location: str = ''
	reference: str = ''


@dataclass(order=True)
class ShapingBuilder:
	
	location: str
	build: str = ''
	reference_location: str = ''
	match: str = ''
	actions: Optional['ShapingActions'] = None


@dataclass(order=True)
class ShapingActions:

	builders: dict[str, ShapingBuilder] = field(default_factory=dict)
	
	replacements: dict[str, ShapingReplacement] = field(default_factory=dict)

	
@dataclass_json
@dataclass(order=True)
class ShapingPatch:
	
	alias: str
	project: str
	file: str
	actions: ShapingActions
	enabled: bool = False
	
	@classmethod
	def from_hjson(cls, content):
		return cls.from_dict(hjson.loads(content))
