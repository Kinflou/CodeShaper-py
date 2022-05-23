## System Imports
from enum import Enum


## Application Imports
from Library.AST.interfaces import ASTSetInterface
from Library.AST.ANtlr.CPP14.Visitor import CPP14Visitor
from Library.AST.ANtlr.CPP14.Generated import CPP14Lexer


## Library Imports


class CPP14Location(Enum):

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
	

class CPP14ASTSet(ASTSetInterface):
	
	Lexer = CPP14Lexer
	Parser = None  # CPP14Parser
	Visitor = CPP14Visitor
	
	InputStream = None
	Location = CPP14Location
	
	def get_root_context(self):
		self.Parser.translationUnit()
	
