## System Imports
import logging


## Application Imports
from Library.Projects import Types
from Library.AST.VisitorController import VisitorState
from Library.Shaping.Project.data import ShapingConfiguration
from Library.Projects.Internal.Base import BaseTarget, BaseFile, BaseTargetFilesMap


## Library Imports
from events import Events
from stopwatch import Stopwatch


class ShapingOperation(Events):
	
	__events__ = ('on_state', 'on_update')
	
	@property
	def ShapingProject(self):
		return self.configuration.shaping_project
	
	def __init__(self, configuration):
		super().__init__()
		
		self.stopwatch = Stopwatch().reset().stop()
		
		self.configuration: ShapingConfiguration = configuration
		self.target: BaseTarget | None = None
		self.files_map: BaseTargetFilesMap | None = None
		
		self.current_file: BaseFile | None = None
		
		self.__setup()
	
	def __setup(self):
		target = self.configuration.shaping_project.configuration.target
		found_type = Types.find_type(target)
		
		if not found_type:
			raise ModuleNotFoundError(f'No target type found with the alias {target}')
		
		self.target = found_type(self.configuration.target, self)
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
		
		if not self.current_file:
			logging.getLogger('applog').info('Finished target shaping')
			self.finalize()
			return
		
		self.start()
	
	def update(self):
		self.on_update()
	
	def finalize(self):
		pass
