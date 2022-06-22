## System Imports
import os
import re
from abc import ABC
from pathlib import Path


## Application Imports
from Library.AST import ANtlr
from Library.Shaping.Patch.controller import PatchController
from Library.AST.VisitorController import VisitorController, VisitorState
from Library.Projects.Internal.interfaces import BaseFileInterface, BaseTargetInterface, BaseGroupInterface, FileState


## Library Imports
from events import Events


class BaseFile(Events, BaseFileInterface):
	
	__events__ = ('on_state', )
	
	@property
	def Name(self):
		return f"File {self.__path.name}"
	
	@property
	def Root(self):
		return self.__root
	
	@property
	def Parent(self):
		return self.__parent
	
	@property
	def Controller(self):
		return self.__controller
	
	@property
	def State(self) -> FileState:
		return self.__state
	
	@property
	def VisitorState(self) -> VisitorState:
		return self.__controller.State
	
	@VisitorState.setter
	def VisitorState(self, value) -> VisitorState:
		state = self.__state
		
		if len(self.patches) > 0:
			self.__controller.State = value
			self.__state = FileState.Processing
		
		if state != self.__state:
			self.on_state(self.__state)
		
		if len(self.patches) < 1:
			self.__root.Operation.next()
	
	def __init__(self, file: str, root: BaseTargetInterface, parent: BaseGroupInterface = None):
		super().__init__()
		
		self.__path = Path(os.path.realpath(file))
		self.__root = root
		self.__parent = parent
		
		self.__controller = VisitorController(root.ASTSet, self.__path.read_text('latin1'))
		self.__controller.on_visit += self.on_visit
		self.__controller.on_finish += self.on_finish
		
		self.patches = self.find_matching_patches(self.__path.name)
		self.__patch_controllers = [PatchController(patch, self) for patch in self.patches]
		
		self.__state = FileState.Waiting if len(self.patches) > 0 else FileState.Untouched
		
		self.content = self.__path.read_text()
		
		self.Root.Operation.update()
	
	def on_visit(self, controller):
		for patch_controller in self.__patch_controllers:
			patch_controller.on_visit(controller)
		
		self.Root.Operation.update()
	
	def on_finish(self):
		self.__state = FileState.Processed
		self.__root.Operation.next()
		
		self.on_state(self.__state)
	
	def find_matching_patches(self, filename):
		matching = []
		
		for patch in self.__root.Operation.ShapingProject.patches:
			if re.match(patch.file, filename):
				matching.append(patch)
		
		return matching
		

class BaseGroup(Events, BaseGroupInterface):
	
	__events__ = ('on_shaping_group_load', 'on_shaping_target_load')
	
	@property
	def Name(self):
		return f'Group {self.__path.stem}'
	
	@property
	def Root(self):
		return self.__root
	
	@property
	def Parent(self):
		return self.__parent
	
	@property
	def Groups(self):
		return None
	
	@property
	def Files(self):
		return None
	
	def __init__(self, file: str, root: BaseTargetInterface, parent: BaseGroupInterface = None):
		super().__init__()
		
		self._path = Path(file)
		self._root = root
		self._parent = parent
	

class BaseTarget(Events, BaseTargetInterface, ABC):
	
	__events__ = ('on_shaping_group_load', 'on_shaping_target_load')
	
	@property
	def Name(self):
		return 'Target'
	
	@property
	def Groups(self) -> list[BaseGroup]:
		return self._groups
	
	@property
	def Files(self) -> list[BaseFile]:
		return self._files
	
	@property
	def Operation(self):
		return self._operation
	
	def __init__(self, directory: str, operation, find_set: bool = False):
		super().__init__()
		
		self._directory = Path(directory)
		self._operation = operation
		
		self._groups = []
		self._files = []
		
		if find_set:
			ast_set = self._operation.configuration.shaping_project.configuration.ast_set
			self._ast_set = ANtlr.find_set(ast_set)
		

# TODO: Perhaps this 'map' can be done simpler, or with a more proper conduct, though i don't know which is
class BaseTargetFilesMap:
	
	def __init__(self, project):
		self.project = project
		
		self.items = []
		self.__make_target_list(project)
	
	def __make_target_list(self, group):
		for file in group.Files:
			self.items.append(file)
		
		for group in group.Groups:
			self.__make_target_list(group)
	
	def first(self):
		return self.items[0] if len(self.items) > 0 else None
	
	def previous(self, item):
		index = self.items.index(item)
		
		return self.items[index - 1] if index > -1 or index <= len(self.items) else None
	
	def next(self, item):
		index = self.items.index(item)
		
		return None if index + 1 >= len(self.items) else self.items[index + 1]
