## System Imports
from enum import Enum


## Application Imports
from Library.AST.interfaces import ASTSetInterface
from Library.AST.ANtlr.CS6.Visitor import CS6Visitor
from Library.AST.ANtlr.CS6.Generated.CSharpLexer import CSharpLexer
from Library.AST.ANtlr.CS6.Generated.CSharpParser import CSharpParser


## Library Imports
from antlr4 import InputStream


class CS6Location(Enum):

	Null = 'none'
	Module = 'module'
	Include = 'include'
	ModuleVariable = 'module.variable'
	ModuleVariableDefinition = 'variable.def'
	Declaration = 'declaration'
	DeclarationStatement = 'declaration.statement'
	Function = 'function'
	FunctionDefinition = 'function.definition'
	FunctionBody = 'function.body'
	FunctionCondition = 'function.condition'


class CS6Set(ASTSetInterface):
	
	Lexer = CSharpLexer
	Parser = CSharpParser
	Visitor = CS6Visitor
	
	Location = CS6Location
	
	@staticmethod
	def get_root_context(parser: CSharpParser):
		parser.compilation_unit()

