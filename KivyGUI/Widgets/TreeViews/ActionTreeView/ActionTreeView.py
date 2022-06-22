## System Imports


## Application Imports
from KivyGUI import utils
from Library.Shaping.Operation.Actions.interfaces import ActionInterface


## Library Imports
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.boxlayout import BoxLayout


class ActionPropertyNode(BoxLayout, TreeViewNode):
	
	def __init__(self, name, value):
		self.name = name
		self.value = value if value else ''
		
		super().__init__()
	
	def on_kv_post(self, base_widget):
		self.ids.label.text = self.name
		self.ids.value.text = self.value if self.name != 'actions' else 'actions...'


class ActionTreeView(TreeView):
	
	kv = utils.load_relative_kv(__file__)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.hide_root = True
		
		self.action: ActionInterface | None = None
		
	def select_action(self, instance, action: ActionInterface):
		self.action = action
		self.make_properties()
	
	def make_properties(self):
		for node in [i for i in self.iterate_all_nodes()]:
			self.remove_node(node)
			del node
		
		for name, value in self.action.__dict__.items():
			self.add_node(ActionPropertyNode(name, value))
	
