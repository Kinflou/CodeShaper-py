## System Imports


## Application Imports
from Library.AST.interfaces import ASTSetInterface
from Library.AST.ANtlr.CPP14.Visitor import CPP14ParserVisitor
from Library.AST.ANtlr.CPP14.Generated.CPP14Lexer import CPP14Lexer
from Library.AST.ANtlr.CPP14.Generated.CPP14Parser import CPP14Parser


## Library Imports


class CPP14ASTSet(ASTSetInterface):
	
	Name = 'CPP14 Antlr4 AST'
	Alias = 'cpp14'
	
	Lexer = CPP14Lexer
	Parser = CPP14Parser
	Visitor = CPP14ParserVisitor
	
	@staticmethod
	def get_root_context(parser: CPP14Parser):
		return parser.translationUnit()

