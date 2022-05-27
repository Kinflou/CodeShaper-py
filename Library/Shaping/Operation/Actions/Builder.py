## System Imports
import re


## Application Imports
from Library.AST.VisitorController import VisitorController
from Library.Shaping.Patch.data import ShapingBuilder


## Library Imports


class ActionBuilder:
	
	def __init__(self, builder: ShapingBuilder):
		self.__builder = builder
		
		self.__pattern = r"#\{(.*?)\}"
		self.__flags: re.RegexFlag | None = None
		
	def process(self, controller: VisitorController):
		content = controller.get_current_content()
		
		matches = re.findall(self.__builder.match, content, self.__flags)
		
		if not matches:
			return
		
		match = matches[0]
		variable = matches[1]
		