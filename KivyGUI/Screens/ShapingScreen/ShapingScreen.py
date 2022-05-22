## System Imports


## Application Imports
from KivyGUI import utils


## Library Imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase


class ShapingScreen(Screen):
	
	kd = utils.load_relative_kv(__file__)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def on_kv_post(self, base_widget):
		self.ids.patches_layout.add_widget(PatchesTreeView())
	
	
class Tab(MDFloatLayout, MDTabsBase):
	pass


class PatchesTreeView(TreeView):
	
	def __init__(self):
		super().__init__()
		self.hide_root = True
		
		n1 = self.add_node(TreeViewLabel(text='Test'))
		self.add_node(BreakpointNode(), n1)


class BreakpointNode(BoxLayout, TreeViewNode):
	
	def __init__(self):
		super().__init__()
	
