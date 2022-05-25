## System Imports


## Application Imports


## Library Imports
from antlr4 import ParseTreeVisitor, InputStream, ParserRuleContext


class CustomParseTreeVisitor(ParseTreeVisitor):
	
	def visitChildren(self, node):
		result = self.defaultResult()
		n = node.getChildCount()
		for i in range(n):
			if not self.shouldVisitNextChild(node, result):
				return result
			
			c = node.getChild(i)
			childResult = c.accept(self)
			result = self.aggregateResult(result, childResult)
		
		return result
	
	def aggregateResult(self, aggregate, nextResult):
		return aggregate if nextResult is None else nextResult
	
	def context_text(self, input_stream: InputStream, ctx: ParserRuleContext):
		start = ctx.start.start
		stop = ctx.stop.stop if ctx.stop is not None else ctx.start.stop
		
		if start > stop:
			return ''
		
		return input_stream.getText(start, stop)
