## System Imports
from abc import ABC, abstractmethod


## Application Imports


## Library Imports


class ExpressionInterface(ABC):

	@abstractmethod
	def process_expression(self):
		pass

