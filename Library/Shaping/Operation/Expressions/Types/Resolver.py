## System Imports
from enum import Enum
from typing import TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Library.Shaping.Operation.Actions.Types import ResolverAction

from Library.Shaping.Operation.Expressions.base import BaseExpression
from Library.Shaping.Operation.Actions.interfaces import ActionInterface


## Library Import


class ResolverExpression(BaseExpression):
	
	def __init__(self, action: 'ResolverAction', parent: ActionInterface):
		super().__init__(action, parent)
		
		self.action = action
	
	def process_expression(self):
		if self.groups:
			return
		
		self.groups = []
		self.names = []
	
	def resolve_expression(self, content: str) -> str:
		if not Modes.has(self.action.resolver.mode):
			raise AttributeError(f"Specified mode '{self.action.resolver.mode}' does not exist in resolver modes")
		
		mode = Modes(self.action.resolver.mode)
		
		if mode == Modes.Switch:
			if content in self.action.resolver.cases:
				return self.action.resolver.cases[content]
			
			if not self.action.resolver.default:
				raise AttributeError(f"No case found for value '{content}' in '{self.action.Name}'")
			
			return self.action.resolver.default
		
		if mode == Modes.List:
			if not self.action.resolver.list_:
				raise AttributeError(f"A list is required in list mode at '{self.action.resolver.list_}'")
			
			if not self.action.resolver.index:
				raise AttributeError(f"An index integer or expression is required in '{self.action.resolver.index}'")
			
			index: int = self.resolve_index_expression(self.action.resolver.index)
			length = len(self.action.resolver.list_)
			
			if index <= length:
				return self.action.resolver.list_[index]
			
			if not self.action.resolver.default:
				raise AttributeError(f"No item found for index '{index}' with expression "
									 f"'{self.action.resolver.index}' in '{self.action.Name}'")
			
			return
	
	@classmethod
	def resolve_index_expression(cls, expression: str) -> int:
		return -1


class Modes(Enum):
	
	Switch = 'switch'
	List = 'list'
	
	@classmethod
	def has(cls, value: str):
		return any(member.value == value for member in cls)
