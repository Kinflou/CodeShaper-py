## System Imports


## Application Imports
from Library.Projects.Internal.interfaces import BaseFileInterface
from Library.Shaping.Operation.Actions.Builder import ActionBuilder
from Library.Shaping.Patch.data import ShapingPatch


## Library Imports


class PatchController:
	
	def __init__(self, patch: ShapingPatch, file: BaseFileInterface):
		self.__patch = patch
		self.__file = file
		
		self.__actions: list = []
		
		file.Controller.on_visit += self.on_visit
		
		self.__setup()
	
	def __setup(self):
		for key, val in self.__patch.actions.builders.items():
			self.__actions.append(ActionBuilder(val))
	
	def on_visit(self, controller):
		for action in self.__actions:
			action.process(controller)

