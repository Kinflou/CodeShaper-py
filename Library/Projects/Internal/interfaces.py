## System Imports
import re
from abc import ABC, abstractmethod
from enum import IntEnum


## Application Imports
from Library.AST.VisitorController import VisitorController, VisitorState


## Library Imports


class FileState(IntEnum):
	Untouched = 0
	Waiting = 1
	Processing = 2
	Processed = 3
	Error = 4


class BaseFileInterface(ABC):
	
	@property
	@abstractmethod
	def Name(self):
		pass
	
	@property
	@abstractmethod
	def Root(self):
		pass
	
	@property
	@abstractmethod
	def Parent(self):
		pass
	
	@property
	@abstractmethod
	def Controller(self) -> VisitorController:
		pass
	
	# TODO: Maybe State and Visitor State being here interfaced is funky, recheck their purposes
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
		
		for patch in self.Root.shaping_project.patches:
			if re.match(patch.file, filename):
				matching.append(patch)
		
		return matching


class BaseGroupInterface(ABC):
	
	@property
	@abstractmethod
	def Name(self):
		pass
	
	@property
	@abstractmethod
	def Root(self):
		pass
	
	@property
	@abstractmethod
	def Parent(self):
		pass
	
	@property
	@abstractmethod
	def Groups(self) -> list['BaseGroupInterface']:
		pass
	
	@property
	@abstractmethod
	def Files(self) -> list[BaseFileInterface]:
		pass


class BaseTargetInterface(ABC):
	
	@property
	@abstractmethod
	def Alias(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Name(self):
		pass
	
	@property
	@abstractmethod
	def Groups(self) -> list[BaseGroupInterface]:
		pass

	@property
	@abstractmethod
	def Operation(self):
		pass
	
	@property
	@abstractmethod
	def ASTSet(self):
		pass
	
	@abstractmethod
	def __init__(self, target, operation):
		pass
