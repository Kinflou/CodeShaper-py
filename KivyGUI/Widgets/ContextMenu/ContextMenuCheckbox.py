## System Imports


## Application Imports
from KivyGUI import utils


## Library Imports
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy_garden.contextmenu import ContextMenuItem


class ContextMenuCheckbox(ContextMenuItem):
	
	kv = utils.load_relative_kv(__file__)
	
	label = ObjectProperty(None)
	submenu_postfix = StringProperty(' ...')
	text = StringProperty()
	font_size = NumericProperty(14)
	color = ListProperty([1, 1, 1, 1])
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	@property
	def content_width(self):
		return self.label.texture_size[0] + 25
