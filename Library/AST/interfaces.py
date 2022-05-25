## System Imports
from enum import Enum
from abc import ABC, abstractmethod


## Application Imports


## Library Imports
from antlr4 import Lexer, Parser, ParserRuleContext


class ASTVisitorInterface(ABC):
	pass
	

class ASTSetInterface(ABC):

	@property
	@abstractmethod
	def Lexer(self):
		pass
	
	@property
	@abstractmethod
	def Parser(self):
		pass

	@property
	@abstractmethod
	def Visitor(self):
		pass
	
	@property
	@abstractmethod
	def Location(self) -> Enum:
		pass
	
	@staticmethod
	@abstractmethod
	def get_root_context(parser: Parser) -> ParserRuleContext:
		pass
	
