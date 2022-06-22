## System Imports
from enum import Enum
from typing import TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Library.Shaping.Patch.controller import PatchController

from Library.Shaping.Patch.data import ShapingReplacer
from Library.Shaping.Operation.Expressions import search
from Library.AST.VisitorController import VisitorController
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports
import regex


class ReplacerAction(ActionInterface):
	
	ExpressionType = None
	
	@property
	def Name(self) -> str:
		return self.name
	
	@property
	def Actions(self) -> list:
		return self.actions
	
	@Actions.setter
	def Actions(self, value: list):
		self.actions = value
	
	@property
	def PatchController(self) -> 'PatchController':
		return self.patch_controller
	
	@property
	def Expression(self) -> str:
		return self.replacement.to
	
	@property
	def Result(self) -> str:
		return self.substitution
	
	def __init__(self, controller: 'PatchController', name: str, replacement: ShapingReplacer):
		self.patch_controller = controller
		self.name = name
		self.replacement = replacement
		
		self.location: Enum | None = None
		self.content: str | None = None
		
		self.substitution: str | None = None
		
		self.actions = []
		
		self.expressions: list[ExpressionInterface] = []
		self.expression = None
		
	def process(self, controller: VisitorController):
		if self.content:
			self.process_expressions()
			return
		
		location = controller.locations[-1]
		content = controller.contents[-1]
		
		if self.replacement.reference_location.lower() != location.lower():
			return
		
		if not self.matches(content):
			return
		
		self.content = content
		
		self.process_expressions()
	
	def process_expressions(self):
		if not self.expressions:
			self.expressions = search.search_expressions(self.PatchController, self.replacement.from_, self)
		
		if self.expressions is not None:
			for expression in self.expressions:
				expression.prepare_expression()
				expression.process_expression()
				
				if expression.can_resolve():
					self.substitution = expression.resolve_expression(self.content)
			
			return
		
		self.substitution = regex.sub(self.replacement.from_, self.replacement.to, self.content)
	
	def matches(self, content: str):
		return regex.match(self.replacement.from_, content)
	


