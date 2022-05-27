## System Imports
import os
from glob import glob
from pathlib import Path


## Application Imports
from Library.AST.ANtlr.CPP14.Set import CPP14ASTSet
from Library.AST.VisitorController import VisitorController, VisitorState
from Library.Projects.External.RawVCXSolution import RawVCXSolution
from Library.Projects.Internal.Base import BaseGroup, BaseFile, BaseTarget, FileState


## Library Imports
from Library.Shaping.Patch import PatchController


class VCXFile(BaseFile):
	
	@property
	def Name(self):
		return f"File {self.path.name}"
	
	@property
	def Controller(self):
		return self.__controller
	
	@property
	def State(self) -> FileState:
		return self.__state
	
	@property
	def VisitorState(self) -> VisitorState:
		return self.__controller.State
	
	@VisitorState.setter
	def VisitorState(self, value) -> VisitorState:
		state = self.__state
		
		if len(self.patches) > 0:
			self.__controller.State = value
			self.__state = FileState.Processing
		
		if state != self.__state:
			self.on_state(self.__state)
		
		if len(self.patches) < 1:
			self.root.operation.next()
		
	def __init__(self, file, root: BaseTarget, parent: BaseGroup):
		super().__init__()
		
		self.path = Path(os.path.realpath(file))
		self.root = root
		self.parent = parent
		
		self.__controller = VisitorController(root.ast_set, self.path.read_text('latin1'))
		self.__controller.on_visit += self.on_visit
		self.__controller.on_finish += self.on_finish
		
		self.patches = self.find_matching_patches(self.path.name)
		self.__patch_controllers = [PatchController(patch, self) for patch in self.patches]
		
		self.__state = FileState.Waiting if len(self.patches) > 0 else FileState.Untouched
	
	def on_visit(self, controller):
		for patch_controller in self.__patch_controllers:
			patch_controller.on_visit(controller)
	
	def on_finish(self):
		self.__state = FileState.Processed
		self.root.operation.next()


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
	
	def __init__(self, project, root: BaseTarget, parent: BaseGroup = None):
		super().__init__()
		
		self.project = project
		self.project_directory = Path(project.path).parent
		
		self.root = root
		self.parent = parent
		
		self.__files: list[VCXFile] = []
		
		self.load_files()
	
	def load_files(self):
		
		for include in self.project.includes:
			vcx_include = VCXFile(f'{self.project_directory}/{include}', self.root, self)
			
			self.on_shaping_target_load(self, vcx_include)
			self.__files.append(vcx_include)
		
		for module in self.project.modules:
			vcx_module = VCXFile(f'{self.project_directory}/{module}', self.root, self)
			
			self.on_shaping_target_load(self, vcx_module)
			self.__files.append(vcx_module)
	

class VCXSolution(RawVCXSolution):
	
	@property
	def Groups(self):
		return self.__groups
	
	@property
	def Files(self):
		return []
	
	def __init__(self, directory, operation, shaping_project):
		super().__init__(self.find_solution_file(directory))
		
		self.ast_set = CPP14ASTSet()
		
		self.operation = operation
		self.shaping_project = shaping_project
		
		self.__groups: list[VCXProject] = []
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
			self.__groups.append(vcx_project)

