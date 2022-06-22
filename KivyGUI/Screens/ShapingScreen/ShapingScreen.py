## System Imports
import logging


## Application Imports
from KivyGUI import utils
from Library.Managers import Shaping
from KivyGUI.Screens.ShapingScreen.VisitorController import VisitorController
from KivyGUI.Widgets.TreeViews.ActionTreeView.ActionTreeView import ActionTreeView
from KivyGUI.Widgets.TreeViews.TargetTreeView.TargetTreeView import TargetTreeView
from KivyGUI.Widgets.TreeViews.PatchesTreeView.PatchesTreeView import PatchesTreeView
from KivyGUI.Widgets.TreeViews.ExpressionTreeView.ExpressionTreeView import ExpressionTreeView


## Library Imports
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout


class ShapingScreen(Screen):
	
	kd = utils.load_relative_kv(__file__)
	
	SelectedAction = ObjectProperty()
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.patches_tree_view = None
		self.target_tree_view = None
		self.action_tree_view = None
		self.expression_tree_view = None
		
		self.logs = ''
		self.process_file = ''
		
		logging.getLogger('applog').handlers[0].events.on_emit += self.on_log_emit
		
		Clock.schedule_interval(self.update_information, 0)
	
	def on_kv_post(self, base_widget):
		self.patches_tree_view = PatchesTreeView(self, size_hint=[1, None])
		self.patches_tree_view.bind(minimum_height=self.patches_tree_view.setter('height'))
		self.ids.patches_layout.add_widget(self.patches_tree_view)
		
		self.target_tree_view = TargetTreeView(size_hint=[1, None])
		self.target_tree_view.bind(minimum_height=self.target_tree_view.setter('height'))
		self.ids.target_layout.add_widget(self.target_tree_view)
		
		self.action_tree_view = ActionTreeView(size_hint=[1, None])
		self.action_tree_view.bind(minimum_height=self.action_tree_view.setter('height'))
		self.ids.action_properties_layout.add_widget(self.action_tree_view)
		self.bind(SelectedAction=self.action_tree_view.select_action)
		
		self.expression_tree_view = ExpressionTreeView(size_hint=[1, None])
		self.expression_tree_view.bind(minimum_height=self.expression_tree_view.setter('height'))
		self.ids.frames_layout.add_widget(self.expression_tree_view)
		self.bind(SelectedAction=self.expression_tree_view.select_action)
		
		self.ids.visitor_layout.add_widget(VisitorController(name='controller'))
	
	def open_configuration(self, configuration):
		Shaping.operation = Shaping.MakeOperation(configuration)
		
		self.patches_tree_view.display_patches(Shaping.operation.configuration.shaping_project.patches)
		self.target_tree_view.display_target(Shaping.operation.target)
		
		self.ids.visitor_layout.children[0].update_information()
		
		logging.getLogger('applog').info(f'Opened {Shaping.operation.configuration.name}')
		
		Shaping.operation.on_update += self.update
		
	def on_log_emit(self, log):
		self.logs += log
	
	def update_information(self, t):
		self.ids.logs.text = self.logs
		
		if self.ids.process_file.text != self.process_file:
			if Shaping.operation.current_file:
				self.ids.process_file.text = Shaping.operation.current_file.content
	
	def update(self):
		self.process_file = Shaping.operation.current_file.content


class Tab(MDFloatLayout, MDTabsBase):
	pass

