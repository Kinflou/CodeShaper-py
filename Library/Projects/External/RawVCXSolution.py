## System Imports
import re
import uuid
from pathlib import Path


## Application Imports
from Library.Projects.Internal.Base import BaseTarget


## Library Imports


class RawVCXProject:
	
	def __init__(self, name, path, guid, other_guid):
		self.name = name
		self.path = path
		self.guid = guid
		self.other_guid = other_guid
		
		self.project_file = Path(self.path).read_text()
		self.includes = self.load_includes()
		self.modules = self.load_modules()
	
	def load_includes(self):
		includes = []
		
		for include in re.findall(r'<ClInclude\s?Include\s?=\s?\"(.*?)\"\s?/>', self.project_file, re.I):
			includes.append(include)
		
		return includes
	
	def load_modules(self):
		modules = []
		
		for module in re.findall(r'<ClCompile\s?Include\s?=\s?\"(.*?)\"\s?/>', self.project_file, re.I):
			modules.append(module)
		
		return modules


class RawVCXSolution(BaseTarget):
	
	@property
	def Name(self):
		return f"VCX Solution {self.__name}"
	
	def __init__(self, path: str):
		super().__init__()
		
		self.path = Path(path)
		
		self.__name = self.path.stem
		
		self.directory = self.path.parent
		self.projects = self.load_projects()
	
	def load_projects(self) -> list:
		solution_file = self.path.read_text()
		pattern = r"Project\(\"{(.*?)}\"\)\s=\s\"(.*?)\"\s?,\s?\"(.*?)\"\s?,\s?\"{(.*?)}"
		
		projects = []
		for project in re.findall(pattern, solution_file):
			
			guid = uuid.UUID(project[0])
			name = project[1]
			directory = f"{self.directory}/{project[2]}"
			other_guid = uuid.UUID(project[3])
			
			projects.append(RawVCXProject(name, directory, guid, other_guid))
		
		return projects
	