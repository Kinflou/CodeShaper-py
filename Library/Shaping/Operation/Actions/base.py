## System Imports
from abc import ABC


## Application Imports
from Library.Shaping.Operation.Expressions import search
from Library.AST.VisitorController import VisitorController
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports


class BaseAction(ActionInterface, ABC):
	
	def __init__(self):
		
		self.expressions: list[ExpressionInterface] | None = None
	
	def process(self, control: VisitorController):
		pass
	
	def process_expression(self):
		if not self.expressions:
			self.expressions = search.search_expressions(self.PatchController, self.builder.build, self)
	
