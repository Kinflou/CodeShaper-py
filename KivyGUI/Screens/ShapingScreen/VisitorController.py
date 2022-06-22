## System Imports
import datetime


## Application Imports
from KivyGUI import utils
from Library.Managers import Shaping
from Library.AST.VisitorController import VisitorState


## Library Imports
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class VisitorController(BoxLayout):
	
	kv = utils.load_relative_kv(__file__)
	
	visitor_type = StringProperty()
	time_elapsed = StringProperty()
	file = StringProperty()
	
	def __init__(self, **kwargs):
		super().__init__()
		
		Clock.schedule_interval(self.update_frame, 0)
	
	@staticmethod
	def play():
		Shaping.operation.start()
	
	@staticmethod
	def stop():
		Shaping.operation.stop()
	
	def on_state(self):
		if not Shaping.operation.current_file:
			return
		
		state = Shaping.operation.current_file.VisitorState
		
		if state == VisitorState.Visit or state == VisitorState.Ready or state == VisitorState.Stopped:
			self.ids.play.text = 'Play'
			self.ids.play.icon = 'play'
		else:
			self.ids.play.text = 'Pause'
			self.ids.play.icon = 'pause'
		
		self.file = f'{Shaping.operation.current_file.Name}'
	
	def update_frame(self, t):
		if not Shaping.operation:
			return
		
		if Shaping.operation.stopwatch.elapsed < 1:
			return
		
		time = datetime.timedelta(seconds=Shaping.operation.stopwatch.elapsed)
		self.time_elapsed = f'Time Elapsed: {str(time).split(".")[0]}'
	
	def update_information(self):
		self.visitor_type = Shaping.operation.target.ASTSet.Name
		
		if Shaping.operation.current_file:
			self.file = Shaping.operation.current_file.Name
		
		Shaping.operation.on_state += self.on_state

