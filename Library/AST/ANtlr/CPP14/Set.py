## System Imports


## Application Imports
from Library.AST.ANtlr.CPP14.Location import CPP14Location
from Library.AST.ANtlr.CPP14.Visitor import CPP14ParserVisitor
from Library.AST.interfaces import ASTSetInterface
from Library.AST.ANtlr.CPP14.Generated.CPP14Parser import CPP14Parser
from Library.AST.ANtlr.CPP14.Generated.CPP14Lexer import CPP14Lexer


## Library Imports


class CPP14ASTSet(ASTSetInterface):
	
	Name = 'CPP14 Antlr4 AST'
	Alias = 'cpp14'
	
	Lexer = CPP14Lexer
	Parser = CPP14Parser
	Visitor = CPP14ParserVisitor
	
	Location = CPP14Location
	
	@staticmethod
	def get_root_context(parser: CPP14Parser):
		return parser.translationUnit()

