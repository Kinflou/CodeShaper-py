## System Imports
from abc import ABC


## Application Imports
from Library.Shaping.Operation.Expressions import search
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports


class BaseExpression(ExpressionInterface, ABC):
	
	@property
	def Name(self) -> str:
		return self.action.Name
	
	@property
	def Frames(self) -> list['ExpressionInterface']:
		return self._frames
	
	def __init__(self, action: ActionInterface | None = None, parent: ActionInterface | None = None):
		self.action = action
		self.parent = parent
		
		self._frames: list[ExpressionInterface] | None = None
		
		self.groups: list[list[str]] | None = None
		self.names: list[dict[str, int]] | None = None
	
	def resolve_expression_variables(self, content: str):
		local_groups = [
			content
		]
		
		local_names = {
			'args': 1
		}
		
		self.groups.append(local_groups)
		self.names.append(local_names)
	
	def prepare_expression(self):
		if self._frames:
			return
		
		self._frames = search.search_expressions(self.action.PatchController, self.action.Expression, self.action)
	
	def can_resolve(self) -> bool:
		# TODO: Check if parent is ready to resolve and if this action and expression are also ready
		if not self._frames:
			return False
		
		for expression in self._frames:
			if not expression.can_resolve():
				return False
		
		return True

