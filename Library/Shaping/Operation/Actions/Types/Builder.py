## System Imports
from typing import TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Library.Shaping.Patch.controller import PatchController

from Library.Shaping.Patch.data import ShapingBuilder
from Library.Shaping.Operation.Expressions import search
from Library.AST.VisitorController import VisitorController
from Library.Shaping.Operation.Expressions.Types import BuilderExpression
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports
import regex


class BuilderAction(ActionInterface):
	
	ExpressionType = BuilderExpression
	
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
		return self.builder.build
	
	@property
	def Result(self) -> str:
		return self.built
	
	def __init__(self, controller: 'PatchController', name: str, builder: ShapingBuilder):
		self.patch_controller = controller
		self.name = name
		self.builder = builder
		
		self.actions: list[ActionInterface] = []
		
		self.location: str | None = None
		self.content: str | None = None
		
		self.expressions: list[ExpressionInterface] | None = None
		
		self.variables: list[str] | None = None
		self.built: str | None = None
		
	def process(self, controller: VisitorController):
		if self.built:
			return
		
		if self.location:
			self.process_expressions()
			return
		
		location = controller.locations[-1]
		content = controller.contents[-1]
		
		if self.builder.reference_location:
			if self.builder.reference_location.lower() != location.lower():
				return
		
		elif self.builder.location.lower() != location.lower():
			return
		
		if not self.matches(content):
			return
		
		self.location = location
		self.content = content
		
		self.process_expressions()
	
	def process_expressions(self):
		if not self.expressions:
			self.expressions = search.search_expressions(self.PatchController, self.builder.build, self)
		
		if self.expressions is not None:
			for expression in self.expressions:
				expression.prepare_expression()
				expression.process_expression(self.content)
				
				if expression.can_resolve():
					self.built = expression.resolve_expression(self.content)
			
			return
		
		self.built = build_groups(self.builder.match, self.builder.build, self.content)
	
	def matches(self, content: str):
		return regex.match(self.builder.match, content)


def build_groups(match, build, content):
	
	groups = ''
	for group in regex.match(match, content).groups():
		groups += f'!<{group}>'
	
	pattern = '!<(.*?)>'
	
	built = regex.sub(pattern, build, groups)
	
	return built

