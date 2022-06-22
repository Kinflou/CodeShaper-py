## System Imports
from typing import TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Library.Shaping.Operation.Actions.Types import MakerAction

from Library.Shaping.Operation.Expressions import search
from Library.Shaping.Operation.Expressions.base import BaseExpression
from Library.Shaping.Operation.Actions.interfaces import ActionInterface


## Library Imports
import regex


class MakerExpression(BaseExpression):
	
	def __init__(self, action: 'MakerAction', parent: ActionInterface):
		super().__init__(action, parent)
		
		self.action = action
	
	def process_expression(self):
		if self._frames:
			return
		
		self._frames = search.search_expressions(self.action.Expression, self.action)
	
	def resolve_expression(self, content: str) -> str:
		result = self.parent.Expression
		
		for expression in self._frames:
			result = regex.sub(self.Pattern, expression.Result, result, 1)
		
		return result
	
