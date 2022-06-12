## System Imports
from glob import glob
from pathlib import Path


## Application Imports
from Library.Projects.Internal.Base import BaseFile, BaseTarget


## Library Imports


class TextFile(BaseFile):
	pass


class TextTarget(BaseTarget):
	
	Alias = 'Text'
	
	@property
	def ASTSet(self):
		return self._ast_set
	
	@property
	def Name(self):
		return 'Text Files'
	
	def __init__(self, path: str, operation):
		super().__init__(path, operation, True)
		
		self.load_files()
		
	def load_files(self):
		for file in glob(f'{self._directory}/*.*', recursive=True):
			self._files.append(BaseFile(file, self))
		