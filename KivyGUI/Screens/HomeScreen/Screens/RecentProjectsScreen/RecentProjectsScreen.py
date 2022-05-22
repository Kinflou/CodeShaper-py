## System Imports


## Application Imports
from KivyGUI import utils


## Library Imports
from kivy.uix.screenmanager import Screen


class RecentProjectsScreen(Screen):
	
	kv = utils.load_relative_kv(__file__)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def open_project(self):
		self.parent.current = 'project_details_screen'

