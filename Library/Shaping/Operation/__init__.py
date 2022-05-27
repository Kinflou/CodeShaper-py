## System Imports


## Application Imports
from Library.AST.VisitorController import VisitorState
from Library.Projects.Internal.Base import BaseTarget, BaseFile, BaseTargetFilesMap
from Library.Projects.Internal.Types.VCXSolution import VCXSolution
from Library.Shaping.Operation.Actions.Frames import ActionFrames
from Library.Shaping.Project.data import ShapingConfiguration


## Library Imports
from events import Events
from stopwatch import Stopwatch


class ShapingOperation(Events):
	
	__events__ = ('on_state', )
	
	def __init__(self, configuration):
		super().__init__()
		
		self.stopwatch = Stopwatch().reset().stop()
		
		self.configuration: ShapingConfiguration = configuration
		self.target: BaseTarget | None = None
		self.files_map: BaseTargetFilesMap | None = None
		
		self.current_file: BaseFile | None = None
		
		self.__setup()
	
	def __setup(self):
		# TODO: Do proper dynamic loading of targets, as this is temporary
		self.target = VCXSolution(self.configuration.source, self, self.configuration.shaping_project)
		self.files_map = BaseTargetFilesMap(self.target)
	
	def start(self):
		if not self.current_file:
			self.current_file = self.files_map.first()
		
		state = self.current_file.VisitorState
		
		if state == VisitorState.Ready or state == VisitorState.Paused or state == VisitorState.Stopped:
			self.current_file.VisitorState = VisitorState.Visit
			self.stopwatch.stop()
		else:
			self.current_file.VisitorState = VisitorState.Paused
			self.stopwatch.start()
		
		self.on_state()
	
	def stop(self):
		if not self.current_file:
			return
		
		self.current_file.VisitorState = VisitorState.Stopped
		self.stopwatch.stop()
		
		self.on_state()
	
	def next(self):
		self.current_file = self.files_map.next(self.current_file)
		self.start()


