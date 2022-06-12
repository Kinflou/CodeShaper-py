## System Imports
import re
from pathlib import Path


## Application Imports


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

