## System Imports


## Application Imports
from Library.Projects.Internal.BaseGroup import BaseGroup


## Library Imports
from events import Events


class VCXTarget(BaseGroup):
	
	def __init__(self, target):
		super().__init__()
		
		self.result = None
	
	def load_file(self):
		pass


class VCXProject(BaseGroup):
	
	def __init__(self, project):
		super().__init__()
		
		self.project = project


class VCXSolution(Events):
	
	__events__ = ('on_shaping_group_load', 'on_shaping_target_load')
	
	def __init__(self):
		super().__init__()
		
		self.solution_information = None
		
		self.groups: list = []
	
	def load_groups(self):
		
		for project in self.solution_information:
			vcx_project = VCXProject(project)
			
			self.on_shaping_group_load(self, vcx_project)
			self.groups.append(vcx_project)

