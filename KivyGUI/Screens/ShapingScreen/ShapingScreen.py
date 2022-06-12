## System Imports
import datetime
import logging


## Application Imports
from KivyGUI import utils
from Library.AST.VisitorController import VisitorState
from Library.Managers import Shaping
from Library.Projects.Internal.Base import BaseTarget, FileState
from Library.Projects.Internal.interfaces import BaseFileInterface
from Library.Shaping.Patch.data import ShapingPatch


## Library Imports
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class ShapingScreen(Screen):
	
	kd = utils.load_relative_kv(__file__)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.patches_tree_view = None
		self.target_tree_view = None
		
		self.logs = ''
		self.process_file = ''
		
		logging.getLogger('applog').handlers[0].events.on_emit += self.on_log_emit
		
		Clock.schedule_interval(self.update_information, 0)
	
	def on_kv_post(self, base_widget):
		self.patches_tree_view = PatchesTreeView(size_hint=[1, None])
		self.patches_tree_view.bind(minimum_height=self.patches_tree_view.setter('height'))
		self.ids.patches_layout.add_widget(self.patches_tree_view)
		
		self.target_tree_view = TargetTreeView(size_hint=[1, None])
		self.target_tree_view.bind(minimum_height=self.target_tree_view.setter('height'))
		self.ids.target_layout.add_widget(self.target_tree_view)
		
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
			self.ids.process_file.text = Shaping.operation.current_file.content
	
	def update(self):
		self.process_file = Shaping.operation.current_file.content


class Tab(MDFloatLayout, MDTabsBase):
	pass


class VisitorController(BoxLayout):
	
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


class PatchesTreeView(TreeView):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.hide_root = True
	
	def display_patches(self, patches: list[ShapingPatch]):
		for node in [i for i in self.iterate_all_nodes()]:
			self.remove_node(node)
		
		# TODO: Currently loading only cares about one depth layer, it is necessary to recurse for infinite children
		for patch in patches:
			patch_node = self.add_node(TreeViewLabel(text=patch.name))
			
			if patch.actions.builders:
				builders_node = self.add_node(TreeViewLabel(text='Builders'), patch_node)
				
				for key, val in patch.actions.builders.items():
					self.add_node(BreakpointNode(key, val), builders_node)
				
			if patch.actions.replacements:
				replacements_node = self.add_node(TreeViewLabel(text='Replacements'), patch_node)
				
				for key, val in patch.actions.replacements.items():
					self.add_node(BreakpointNode(key, val), replacements_node)


class BreakpointNode(BoxLayout, TreeViewNode):
	
	def __init__(self, name, action):
		self.name = name
		self.action = action
		super().__init__()
		
	def on_kv_post(self, base_widget):
		self.ids.label.text = self.name


class TargetTreeView(TreeView):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.hide_root = True
	
	def display_target(self, target: BaseTarget):
		for node in [i for i in self.iterate_all_nodes()]:
			self.remove_node(node)
		
		# TODO: Currently loading only cares about one depth layer, migh be necessary to recurse for hierarchical layers
		target_node = self.add_node(TreeViewLabel(text=target.Name))
		
		for group in target.Groups:
			group_node = self.add_node(TreeViewLabel(text=group.Name), target_node)
			
			for file in group.Files:
				self.add_node(TargetFileNode(file, text=file.Name), group_node)
		
		for file in target.Files:
			self.add_node(TargetFileNode(file, text=file.Name), target_node)
		
	
class TargetFileNode(TreeViewLabel):
	
	def __init__(self,  file: BaseFileInterface, **kwargs):
		self.file = file
		file.on_state += self.on_state
		self.on_state(file.State)
		
		super().__init__(**kwargs)
	
	def select(self, value):
		if value:
			self.color = [1, 1, 1, 1]
		else:
			self.color = [1, 1, .1, 1]
	
	def on_state(self, state):
		colors = {
			FileState.Untouched: get_color_from_hex('ffff00'),
			FileState.Waiting: get_color_from_hex('048fe0'),
			FileState.Processing: get_color_from_hex('bd2af7'),
			FileState.Processed: get_color_from_hex('02d34e'),
			FileState.Error: get_color_from_hex('c10303')
		}
		
		self.color = colors[state]
		
