## System imports
from typing import Optional
from dataclasses import dataclass, field


## Application Imports


## Library Imports
from dataclasses_json import config


@dataclass(order=True)
class ShapingReplacement:
	
	location: str
	reference_location: str
	reference: str
	from_: str = field(metadata=config(field_name="from"))
	to: str


@dataclass(order=True)
class ShapingBuilder:
	
	location: str
	build: str
	reference_location: str = ''
	match: str = ''
	actions: Optional['ShapingActions'] = None


@dataclass(order=True)
class ShapingActions:

	builders: dict[str, ShapingBuilder] = field(default_factory=dict)
	
	replacements: dict[str, ShapingReplacement] = field(default_factory=dict)

	
@dataclass(order=True)
class ShapingPatch:
	
	alias: str
	project: str
	file: str
	actions: ShapingActions
	enabled: bool = False
