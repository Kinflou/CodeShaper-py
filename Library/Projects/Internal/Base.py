## System Imports
import re
from abc import ABC, abstractmethod
from enum import IntEnum


## Application Imports
from Library.AST.VisitorController import VisitorController, VisitorState


## Library Imports
from events import Events


class FileState(IntEnum):
	
	Untouched = 0
	Waiting = 1
	Processing = 2
	Processed = 3
	Error = 4


class BaseFile(Events, ABC):
	
	__events__ = ('on_state', )
	
	@property
	@abstractmethod
	def Name(self):
		pass
	
	@property
	@abstractmethod
	def Controller(self) -> VisitorController:
		pass
	
	@property
	@abstractmethod
	def State(self) -> FileState:
		pass
	
	@property
	@abstractmethod
	def VisitorState(self) -> VisitorState:
		pass
	
	@VisitorState.setter
	@abstractmethod
	def VisitorState(self, value: VisitorState):
		pass
	
	def find_matching_patches(self, filename):
		matching = []
		
		for patch in self.root.shaping_project.patches:
			if re.match(patch.file, filename):
				matching.append(patch)
		
		return matching
		

class BaseGroup(Events, ABC):
	
	__events__ = ('on_shaping_group_load', 'on_shaping_target_load')
	
	@property
	@abstractmethod
	def Name(self):
		pass
	
	@property
	@abstractmethod
	def Groups(self) -> list['BaseGroup']:
		pass
	
	@property
	@abstractmethod
	def Files(self) -> list[BaseFile]:
		pass


class BaseTarget(Events, ABC):
	__events__ = ('on_shaping_group_load', 'on_shaping_target_load')
	
	@property
	@abstractmethod
	def Name(self):
		pass
	
	@property
	@abstractmethod
	def Groups(self) -> list[BaseGroup]:
		pass


# TODO: Perhaps this 'map' can be done simpler, or with a more proper conduct, though i don't know which is
class BaseTargetFilesMap:
	
	def __init__(self, project):
		self.project = project
		
		self.items = []
		self.__make_groups_list(project)
	
	def __make_groups_list(self, group):
		for file in group.Files:
			self.items.append(file)
		
		for group in group.Groups:
			self.__make_groups_list(group)
	
	def first(self):
		return self.items[0] if len(self.items) > 0 else None
	
	def previous(self, item):
		index = self.items.index(item)
		
		return self.items[index - 1] if index > -1 or index <= len(self.items) else None
	
	def next(self, item):
		index = self.items.index(item)
		
		return self.items[index + 1] if index + 1 <= len(self.items) else None
