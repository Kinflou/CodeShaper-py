## System Imports
from pathlib import Path


## Application Imports
from Library.Projects.External.RawVCXSolution import RawVCXSolution
from Library.Projects.Internal.Base import BaseGroup, BaseFile, BaseTargetFilesMap


## Library Imports


class VCXFile(BaseFile):
	
	@property
	def Name(self):
		return f"File {self.path.name}"
	
	def __init__(self, file):
		super().__init__()
		
		self.path = Path(file)
	
	def load_file(self):
		pass


class VCXProject(BaseGroup):
	
	@property
	def Name(self):
		return f"VCX Project {self.project.name}"
	
	@property
	def Groups(self):
		return []
	
	@property
	def Files(self):
		return self.__files
	
	def __init__(self, project):
		super().__init__()
		
		self.project = project
		
		self.__files: list[VCXFile] = []
		
		self.load_files()
	
	def load_files(self):
		
		for include in self.project.includes:
			vcx_include = VCXFile(include)
			
			self.on_shaping_target_load(self, vcx_include)
			self.__files.append(vcx_include)
		
		for module in self.project.modules:
			vcx_module = VCXFile(module)
			
			self.on_shaping_target_load(self, vcx_module)
			self.__files.append(vcx_module)
	

class VCXSolution(RawVCXSolution):
	
	@property
	def Name(self):
		return "VCX Solution 'test'"
	
	@property
	def Groups(self):
		return self.__groups
	
	@property
	def Files(self):
		return []
	
	def __init__(self, directory):
		super().__init__(f'{directory}/client.sln')
		
		self.__groups: list[VCXProject] = []
		self.load_groups()
		self.files_map = BaseTargetFilesMap(self)
	
	def load_groups(self):
		
		for project in self.projects:
			vcx_project = VCXProject(project)
			
			self.on_shaping_group_load(self, vcx_project)
			self.__groups.append(vcx_project)

