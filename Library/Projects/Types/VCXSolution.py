## System Imports
import re
import uuid
from glob import glob
from pathlib import Path


## Application Imports
from Library.AST.ANtlr.CPP14.Set import CPP14ASTSet
from Library.Projects.External.RawVCXSolution import RawVCXProject
from Library.Projects.Internal.Base import BaseGroup, BaseFile, BaseTarget


## Library Imports


class VCXProject(BaseGroup):
	
	@property
	def Name(self):
		return f"VCX Project {self.project.name}"
	
	@property
	def Root(self):
		return self._root
	
	@property
	def Parent(self):
		return self._parent
	
	@property
	def Groups(self):
		return []
	
	@property
	def Files(self):
		return self._files
	
	def __init__(self, project, root: BaseTarget, parent: BaseGroup = None):
		super().__init__(project.path, root, parent)
		
		self.project = project
		self.project_directory = Path(project.path).parent
		
		self._files: list[BaseFile] = []
		
		self.load_files()
	
	def load_files(self):
		
		for include in self.project.includes:
			vcx_include = BaseFile(f'{self.project_directory}/{include}', self.Root, self)
			
			self.on_shaping_target_load(self, vcx_include)
			self._files.append(vcx_include)
		
		for module in self.project.modules:
			vcx_module = BaseFile(f'{self.project_directory}/{module}', self.Root, self)
			
			self.on_shaping_target_load(self, vcx_module)
			self._files.append(vcx_module)
	

class VCXSolution(BaseTarget):
	
	Alias = "VCX"
	ASTSet = CPP14ASTSet
	
	@property
	def Name(self):
		return f"VCX Solution {self.solution_path.stem}"
	
	def __init__(self, directory, operation):
		super().__init__(directory, operation)
		
		self.solution_path = Path(self.find_solution_file(directory))
		self.projects = self.load_projects()
		self.load_groups()
	
	@staticmethod
	def find_solution_file(directory):
		solution_path = glob(f'{directory}/*.sln')
		
		if len(solution_path) < 1:
			raise FileNotFoundError(f'Cannot find solution file in {directory}')
		
		return solution_path[0]
	
	def load_groups(self):
		for project in self.projects:
			vcx_project = VCXProject(project, self)
			
			self.on_shaping_group_load(self, vcx_project)
			self._groups.append(vcx_project)
	
	def load_projects(self) -> list:
		solution_file = self.solution_path.read_text()
		pattern = r"Project\(\"{(.*?)}\"\)\s=\s\"(.*?)\"\s?,\s?\"(.*?)\"\s?,\s?\"{(.*?)}"
		
		projects = []
		for project in re.findall(pattern, solution_file):
			guid = uuid.UUID(project[0])
			name = project[1]
			directory = f"{self._directory}/{project[2]}"
			other_guid = uuid.UUID(project[3])
			
			projects.append(RawVCXProject(name, directory, guid, other_guid))
		
		return projects
