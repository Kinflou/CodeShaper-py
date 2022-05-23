## System Imports


## Application Imports
from Library.AST.interfaces import ASTSetInterface
from Library.AST.ANtlr.CS6.Visitor import CS6Visitor
from Library.AST.ANtlr.CS6.Generated.CSharpLexer import CSharpLexer
from Library.AST.ANtlr.CS6.Generated.CSharpParser import CSharpParser


## Library Imports


class CS6Set(ASTSetInterface):
	
	Lexer = CSharpLexer
	Parser = CSharpParser
	Visitor = CS6Visitor
	
	InputStream = None
	
	def get_root_context(self):
		self.Parser.compilation_unit()

