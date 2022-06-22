## System Imports
from enum import Enum


## Application Imports
from Library.Shaping.Patch.data import ShapingResolver
from Library.AST.VisitorController import VisitorController
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.Types import ResolverExpression
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports


class ResolverAction(ActionInterface):
	
	ExpressionType = ResolverExpression
	
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
		return None
	
	@property
	def Result(self) -> str:
		return None
	
	def __init__(self, controller: 'PatchController', name: str, resolver: ShapingResolver):
		self.patch_controller = controller
		self.name = name
		self.resolver = resolver
		
		self.location: Enum | None = None
		self.content: str | None = None
		
		self.referenced_location: Enum | None = None
		
		self.built: str | None = None
		
		self.actions = []
		
		self.expressions: list[ExpressionInterface] = []
	
	def process(self, controller: VisitorController):
		pass
