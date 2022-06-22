## System Imports


## Application Imports
from KivyGUI import utils
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeView, TreeViewNode


class BreakpointNode(BoxLayout, TreeViewNode):
	
	def __init__(self, expression: ExpressionInterface):
		self.expression = expression
		
		super().__init__()
	
	def on_kv_post(self, base_widget):
		self.ids.label.text = self.expression.Name
	
	def on_touch_up(self, touch):
		self.parent.select_expression(self.expression)


class ExpressionTreeView(TreeView):
	
	kv = utils.load_relative_kv(__file__)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.hide_root = True
		
		self.expression: ExpressionInterface | None = None
	
	def make_nodes(self, expression: ExpressionInterface, parent_node: BreakpointNode):
		for frame in expression.Frames:
			self.add_node(BreakpointNode(frame), parent_node)
	
	def select_action(self, instance, action: ActionInterface):
		pass
	
	def select_expression(self, instance, expression: ExpressionInterface):
		self.expression = expression
		self.make_nodes(expression, self)
	
