## System Imports


## Application Imports
from KivyGUI import utils


## Library Imports
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App


class NavigationBar(FloatLayout):
	
	kv = utils.load_relative_kv(__file__)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def close_project(self):
		App.get_running_app().close_project()
		self.ids.app_menu.close_all()
	
	def exit_app(self):
		App.get_running_app().close_app()
		self.ids.app_menu.close_all()
