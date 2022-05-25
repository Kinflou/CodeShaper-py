## System Imports


## Application Imports
from Library.AST.VisitorController import VisitorState
from Library.Projects.Internal.Base import BaseTarget, BaseFile, BaseTargetFilesMap
from Library.Shaping.Operation.Actions.Frames import ActionFrames
from Library.Shaping.Project.data import ShapingConfiguration


## Library Imports
from stopwatch import Stopwatch


class ShapingOperation:
	
	def __init__(self, configuration, target):
		
		self.stopwatch = Stopwatch().reset().stop()
		
		self.configuration: ShapingConfiguration = configuration
		self.target: BaseTarget = target
		self.files_map = BaseTargetFilesMap(target)
		
		self.current_file: BaseFile | None = None
	
	def start(self):
		if not self.current_file:
			self.current_file = self.files_map.first()
		
		state = self.current_file.Controller.state
		
		if state == VisitorState.Ready or state == VisitorState.Paused or state == VisitorState.Stopped:
			self.current_file.Controller.state = VisitorState.Visit
			self.stopwatch.stop()
		else:
			self.current_file.Controller.state = VisitorState.Paused
			self.stopwatch.start()
	
	def stop(self):
		self.current_file.Controller.state = VisitorState.Stopped
		self.stopwatch.stop()
	
	def post_process_file(self):
		pass


class ActionOperations:
	
	def __init__(self):
		self.frames = ActionFrames

