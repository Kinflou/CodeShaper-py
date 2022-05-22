## System Imports
import webbrowser
from typing import Optional


## Application Imports
from KivyGUI import utils
from Lib.Shaping.Project.data import ShapingConfiguration


## Library Imports
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.rst import RstDocument
from kivy.uix.screenmanager import Screen


class ProjectDetailsScreen(Screen):
	
	kv = utils.load_relative_kv(__file__)
	
	config_name = StringProperty('No Project')
	project_path = StringProperty('None')
	target_path = StringProperty('None')
	description = StringProperty()
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.configuration: Optional[ShapingConfiguration] = None
	
	def on_kv_post(self, base_widget):
		self.ids.description.colors = {
			'background': '404040',
			'link': '39a275',
			'paragraph': 'ffffff',
			'title': 'ffffff',
			'bullet': '39a275',
		}
	
	def show_configuration(self, configuration: ShapingConfiguration):
		self.configuration = configuration
		
		self.config_name = configuration.name
		self.project_path = configuration.shape_project
		self.target_path = configuration.target
		self.description = """
		"""
		
	def go_back(self):
		self.parent.current = 'recent_projects_screen'
	
	def open_project(self):
		App.get_running_app().set_screen('shaping_screen')


class DescriptionRstDocument(RstDocument):
	
	def on_ref_press(self, node, ref):
		webbrowser.open(ref)
