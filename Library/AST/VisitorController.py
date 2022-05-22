## System Imports
import logging
from enum import IntEnum
from threading import Thread


## Application Imports


## Library Imports
from events import Events


class VisitorState(IntEnum):
	
	Ready = 0
	Visit = 1
	Paused = 2
	Finished = 3


class VisitorController(Events):
	
	__events__ = ['on_visit']
	
	@property
	def state(self) -> VisitorState:
		return self.state
	
	@state.setter
	def state(self, value):
		Thread(name='Visitor Controller', target=self.process)
		self.state = value
	
	def __init__(self, location: IntEnum):
		super().__init__()
		
		self.location = location
	
		self.contexts = []
		self.delegates = []
		self.locations = []
		
		self.__index = -1
		self.__processing = False
	
	def process(self):
		if self.__processing:
			return
		
		self.__processing = True
		
		while self.index < len(self.contexts):
			
			if self.state != VisitorState.Visit:
				self.__processing = False
				return
			
			context = self.contexts[self.index + 1]
			delegate = self.delegates[self.index + 1]
			location = self.locations[self.index + 1]
			
			logging.info(f'Visiting {location}')
			next_context, next_location = delegate(context)
			
			# TODO: Check if we got a valid next context
			self.contexts.append(next_context)
			
			self.__post_process()
	
	def __post_process(self):
		context = self.contexts[:1]
		previous_context = self.contexts[:-1]
		
		if context == previous_context:
			logging.info('Reached the end of visits')
			self.state = VisitorState.Finished

