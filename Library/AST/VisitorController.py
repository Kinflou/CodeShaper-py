## System Imports
import time
import logging
from enum import IntEnum
from threading import Thread


## Application Imports
from Library.AST.interfaces import ASTSetInterface
from Library.AST.CustomParseTreeVisitor import CustomParseTreeVisitor


## Library Imports
from events import Events
from antlr4 import InputStream, CommonTokenStream, ParserRuleContext


class VisitorState(IntEnum):
	
	Ready = 0
	Visit = 1
	Paused = 2
	Stopped = 3
	Finished = 4


class VisitorController(Events):
	
	__events__ = ['on_visit', 'on_state', 'on_finish']
	
	@property
	def State(self) -> VisitorState:
		return self.__state
	
	@State.setter
	def State(self, value):
		if self.__state == value:
			return
		
		self.__state = value
		self.on_state(self.__state)
		Thread(name='Visitor Controller', target=self.process).start()
	
	def __init__(self, ast_set: ASTSetInterface, content: str):
		super().__init__()
		
		self.__ast_set = ast_set
		self.__content = content
		
		self.contexts = []
		self.locations = []
		self.contents = []
		
		self.__input_stream = None
		self.visitor = None
		
		self.__state = VisitorState.Ready
		self.__index = 0
		self.__processing = False
		
		self.__is_setup = False
	
	def __setup(self):
		self.__input_stream = InputStream(self.__content)
		lexer = self.__ast_set.Lexer(self.__input_stream)
		stream = CommonTokenStream(lexer)
		parser = self.__ast_set.Parser(stream)
		
		t = time.perf_counter()
		tree = self.__ast_set.get_root_context(parser)
		total_time = time.perf_counter() - t
		print(f'Took {total_time} to parse AST')
		
		self.visitor: CustomParseTreeVisitor = self.__ast_set.Visitor()
		
		context = self.visitor.visit(tree)
		content = self.__input_stream.getText(0, self.__input_stream.size)
		
		self.contexts.append(context)
		self.locations.append(context.__class__.__name__.replace('Context', ''))
		self.contents.append(content)
	
	def process(self):
		if not self.__is_setup:
			self.__setup()
		
		if self.__processing:
			return
		
		self.__processing = True
		
		while self.__index < len(self.contexts):
			
			if self.__state != VisitorState.Visit:
				self.__processing = False
				return
			
			context = self.contexts[self.__index]
			location = self.locations[self.__index]
			
			logging.getLogger('applog').info(f'Visiting {location}')
			context = self.visitor.visitChildren(context)
			
			if not context:
				self.__finish_process()
				return
			
			if not isinstance(context, ParserRuleContext):
				raise Exception('Visits should return one argument (the context)')
			
			content = self.visitor.context_text(self.__input_stream, context)
			
			self.contexts.append(context)
			self.locations.append(context.__class__.__name__.replace('Context', ''))
			self.contents.append(content)
			
			self.__index += 1
			
			self.__post_process()
	
	def __post_process(self):
		context = self.contexts[-1]
		previous_context = self.contexts[-2]
		
		self.on_visit(self)
		
		if context == previous_context:
			logging.getLogger('applog').info('Reached the end of visits')
			self.__state = VisitorState.Finished
			self.__processing = False
	
	def __finish_process(self):
		logging.getLogger('applog').info('Finished Visiting')
		self.__state = VisitorState.Finished
		self.__processing = False
		self.on_finish()


