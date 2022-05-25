## System Imports
import logging
from enum import IntEnum
from threading import Thread


## Application Imports
from Library.AST.ANtlr.CPP14.Visitor import CPP14ParserVisitor
from Library.AST.interfaces import ASTSetInterface


## Library Imports
from events import Events
from antlr4 import InputStream, CommonTokenStream


class VisitorState(IntEnum):
	
	Ready = 0
	Visit = 1
	Paused = 2
	Stopped = 3
	Finished = 4


class VisitorController(Events):
	
	__events__ = ['on_visit', 'on_state_change']
	
	@property
	def state(self) -> VisitorState:
		return self.__state
	
	@state.setter
	def state(self, value):
		self.__state = value
		self.on_state_change(self.__state)
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
		
		tree = self.__ast_set.get_root_context(parser)
		self.visitor: CPP14ParserVisitor = self.__ast_set.Visitor()
		
		context, location = self.visitor.visit(tree)
		content = self.__input_stream.getText(0, self.__input_stream.size)
		
		self.contexts.append(context)
		self.locations.append(location)
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
			
			logging.info(f'Visiting {location.name}')
			result = self.visitor.visitChildren(context)
			
			if not result:
				self.__finish_process()
				return
			
			if len(result) != 2:
				raise Exception('Visits should return context and location')
			
			context, location = result
			content = self.visitor.context_text(self.__input_stream, context)
			
			self.contexts.append(context)
			self.locations.append(location)
			self.contents.append(content)
			
			self.__index += 1
			
			self.__post_process()
	
	def __post_process(self):
		context = self.contexts[:1]
		previous_context = self.contexts[:0]
		
		if context == previous_context:
			logging.info('Reached the end of visits')
			self.__state = VisitorState.Finished
			self.__processing = False
	
	def __finish_process(self):
		logging.info('Finished Visiting')
		self.__state = VisitorState.Finished
		self.__processing = False

