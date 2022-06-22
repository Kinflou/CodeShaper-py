## System Imports
from abc import ABC, abstractmethod


## Application Imports
from Library.Shaping.Operation.Actions.interfaces import ActionInterface


## Library Imports


class ExpressionInterface(ABC):

	@property
	@abstractmethod
	def Name(self) -> str:
		pass
	
	@property
	@abstractmethod
	def Frames(self) -> list['ExpressionInterface']:
		pass
	
	@abstractmethod
	def __init__(self, action: ActionInterface, parent: ActionInterface):
		pass
	
	@abstractmethod
	def prepare_expression(self):
		pass
	
	@abstractmethod
	def process_expression(self):
		pass
	
	@abstractmethod
	def can_resolve(self):
		pass
	
	@abstractmethod
	def resolve_expression(self, content: str):
		pass
	
