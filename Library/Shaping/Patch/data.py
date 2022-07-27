## System imports
from dataclasses import dataclass, field


## Application Imports


## Library Imports
import hjson
from dataclasses_json import config, dataclass_json


@dataclass(slots=True, order=True)
class ShapingResolver:
	
	mode: str
	cases: dict[str, str]
	
	list_: list[str] | None = field(default=None, metadata=config(field_name='list'))
	index: str | None = None
	default: str | None = None


@dataclass(slots=True, order=True)
class ShapingMaker:

	prepare: str
	make: str


@dataclass(slots=True, order=True)
class ShapingReplacer:
	
	location: str
	from_: str = field(metadata=config(field_name="from"))
	to: str
	flags: str = ''
	reference_location: str = ''
	reference: str = ''
	actions: 'ShapingActions' = field(default_factory=dict)


@dataclass(slots=True, order=True)
class ShapingBuilder:
	
	location: str
	build: str = ''
	reference_location: str = ''
	match: str = ''
	actions: 'ShapingActions' = field(default_factory=dict)


@dataclass(slots=True, order=True)
class ShapingActions:

	builders: dict[str, ShapingBuilder] = field(default_factory=dict)
	replacements: dict[str, ShapingReplacer] = field(default_factory=dict)
	makers: dict[str, ShapingMaker] = field(default_factory=dict)
	resolvers: dict[str, ShapingResolver] = field(default_factory=dict)

	
@dataclass_json
@dataclass(slots=True, order=True)
class ShapingPatch:
	
	alias: str
	file: str
	actions: ShapingActions
	project: str = ''  # TODO: Do matching of patches that only affect certain groups, and rename this field to groups
	enabled: bool = False
	
	@classmethod
	def from_hjson(cls, content):
		return cls.from_dict(hjson.loads(content))
