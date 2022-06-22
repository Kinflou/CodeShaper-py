## System Imports


## Application Imports
from Library.Projects.Internal.Base import BaseTarget
from Library.Projects.Internal.interfaces import FileState, BaseFileInterface


## Library Imports
from kivy.utils import get_color_from_hex
from kivy.uix.treeview import TreeView, TreeViewLabel


class TargetFileNode(TreeViewLabel):
	
	def __init__(self, file: BaseFileInterface, **kwargs):
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
	
