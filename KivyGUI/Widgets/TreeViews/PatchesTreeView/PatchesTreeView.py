## System Imports


## Application Imports
from KivyGUI import utils
from Library.Shaping.Patch.data import ShapingPatch
from Library.Shaping.Operation.Actions.interfaces import ActionInterface


## Library Imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode


class ActionBreakpointNode(BoxLayout, TreeViewNode):
	
	def __init__(self, name: str, action: ActionInterface):
		self.name = name
		self.action = action
		super().__init__()
	
	def on_kv_post(self, base_widget):
		self.ids.label.text = self.name
	
	def on_touch_up(self, touch):
		self.parent.Root.SelectedAction = self.action


class PatchesTreeView(TreeView):
	
	kv = utils.load_relative_kv(__file__)
	
	def __init__(self, root, **kwargs):
		super().__init__(**kwargs)
		self.hide_root = True
		self.Root = root
	
	def display_patches(self, patches: list[ShapingPatch]):
		for node in [i for i in self.iterate_all_nodes()]:
			self.remove_node(node)
		
		# TODO: Currently loading only cares about one depth layer, it is necessary to recurse for infinite children
		for patch in patches:
			patch_node = self.add_node(TreeViewLabel(text=patch.name))
			
			if patch.actions.builders:
				builders_node = self.add_node(TreeViewLabel(text='Builders'), patch_node)
				
				for key, val in patch.actions.builders.items():
					self.add_node(ActionBreakpointNode(key, val), builders_node)
			
			if patch.actions.replacements:
				replacements_node = self.add_node(TreeViewLabel(text='Replacements'), patch_node)
				
				for key, val in patch.actions.replacements.items():
					self.add_node(ActionBreakpointNode(key, val), replacements_node)

