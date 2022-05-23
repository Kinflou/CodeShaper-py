## System Imports


## Application Imports
from Library.Projects.Internal.Base import BaseTarget, BaseFile
from Library.Shaping.Operation.Actions.Frames import ActionFrames
from Library.Shaping.Project.data import ShapingConfiguration, ShapingProject


## Library Imports
from stopwatch import Stopwatch


class ShapingOperation:
	
	def __init__(self, configuration, target):
		
		self.stopwatch = Stopwatch()
		
		self.configuration: ShapingConfiguration = configuration
		self.target: BaseTarget = target
		
		self.current_file: BaseFile | None = None
	
	def start(self):
		self.stopwatch.start()
	
	def stop(self):
		self.stopwatch.stop()
	
	def next(self):
		if not self.current_file:
			return
	
	def __next_group(self):
		pass
	
	def __next_file(self):
		pass


class ActionOperations:
	
	def __init__(self):
		self.frames = ActionFrames

