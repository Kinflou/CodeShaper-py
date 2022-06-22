## System Imports
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type


## Application Imports


## Library Imports
from Library.AST.VisitorController import VisitorController

if TYPE_CHECKING:
	from Library.Shaping.Patch.controller import PatchController
	from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


class ActionInterface(ABC):
	
	@property
	@abstractmethod
	def Name(self) -> str:
		pass
	
	@property
	@abstractmethod
	def ExpressionType(self) -> Type['ExpressionInterface']:
		pass
	
	@property
	@abstractmethod
	def Actions(self) -> list:
		pass
	
	@property
	@abstractmethod
	def PatchController(self) -> 'PatchController':
		pass
	
	@property
	@abstractmethod
	def Expression(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Result(self) -> str:
		pass
	
	@abstractmethod
	def process(self, control: VisitorController):
		pass
	
