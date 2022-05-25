## System Imports
import os
from pathlib import Path


## Application Imports
from Library.AST.ANtlr.CPP14.Set import CPP14ASTSet
from Library.AST.VisitorController import VisitorController
from Library.Projects.External.RawVCXSolution import RawVCXSolution
from Library.Projects.Internal.Base import BaseGroup, BaseFile


## Library Imports


class VCXFile(BaseFile):
	
	@property
	def Name(self):
		return f"File {self.path.name}"
	
	@property
	def Controller(self):
		return self.__controller
	
	def __init__(self, file, ast_set):
		super().__init__()
		
		self.path = Path(os.path.realpath(file))
		self.ast_set = ast_set
		
		self.__controller = VisitorController(ast_set, self.path.read_text('latin1'))
	
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
	
	def __init__(self, project, ast_set):
		super().__init__()
		
		self.project = project
		self.project_directory = Path(project.path).parent
		self.ast_set = ast_set
		
		self.__files: list[VCXFile] = []
		
		self.load_files()
	
	def load_files(self):
		
		for include in self.project.includes:
			vcx_include = VCXFile(f'{self.project_directory}/{include}', self.ast_set)
			
			self.on_shaping_target_load(self, vcx_include)
			self.__files.append(vcx_include)
		
		for module in self.project.modules:
			vcx_module = VCXFile(f'{self.project_directory}/{module}', self.ast_set)
			
			self.on_shaping_target_load(self, vcx_module)
			self.__files.append(vcx_module)
	

class VCXSolution(RawVCXSolution):
	
	@property
	def Groups(self):
		return self.__groups
	
	@property
	def Files(self):
		return []
	
	def __init__(self, directory):
		super().__init__(f'{directory}/client.sln')
		
		self.ast_set = CPP14ASTSet()
		
		self.__groups: list[VCXProject] = []
		self.load_groups()
	
	def load_groups(self):
		
		for project in self.projects:
			vcx_project = VCXProject(project, self.ast_set)
			
			self.on_shaping_group_load(self, vcx_project)
			self.__groups.append(vcx_project)

