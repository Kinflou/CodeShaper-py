## System Imports


## Application Imports


## Pre Library Operations
ico = r'Assets/logo/logo_only.ico'

from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '700')

Config.set('kivy', 'window_icon', ico)


## Library Imports
from kivymd.app import MDApp


class App(MDApp):
	
	icon = ico
	
	def build(self):
		self.title = "CodeShaper"
		
		# TODO: Make a custom navigation top bar to replace OS based one
		# Window.borderless = True
		# Window.size = (1000, 600)
		
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'Gray'
		self.theme_cls.accent_palette = 'Gray'
		self.theme_cls.material_style = 'S3'
	
	def set_screen(self, name: str):
		self.root.current = name
	
	def close_project(self):
		self.root.current = 'home_screen'
	
	def close_app(self):
		self.stop()

	