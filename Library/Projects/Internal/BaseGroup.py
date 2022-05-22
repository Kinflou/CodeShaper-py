## System Imports


## Application Imports


## Library Imports
from events import Events


class BaseGroup(Events):
	
	__events__ = ('OnShapingGroupLoad', 'OnShapingTargetLoad')
	
	@property
	def Name(self) -> str:
		return self.name
	
	def __init__(self, name: str):
		super().__init__()
		
		self.name = name

