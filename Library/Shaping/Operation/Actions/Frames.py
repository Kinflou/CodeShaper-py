## System Imports


## Application Imports
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports


class ActionFrames:
	
	def __init__(self, action: ActionInterface):
		self.__action = action
		
		self.frames: list = []
	
	def process(self):
		pass
		
	def process_expression(self, expression: ExpressionInterface):
		pass

