## System Imports
from pathlib import Path


## Application imports
from Library.Shaping.Patch.data import ShapingPatch


## Library Imports
import hjson
from dataclasses_json import dataclass_json


@dataclass_json()
class ShapingPatchHJSON(ShapingPatch):
	
	@classmethod
	def from_hjson(cls, content):
		return cls.from_dict(hjson.loads(content))

