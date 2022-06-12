## System Imports
import pkgutil
from typing import Type


## Application Imports
from Library import Utils
from Library.AST.interfaces import ASTSetInterface


## Library Imports


def find_set(alias: str) -> Type[ASTSetInterface] | None:
	for importer, modname, is_pkg in pkgutil.walk_packages(path=__path__,
	                                                       prefix=__name__ + '.Set.',
	                                                       onerror=lambda x: None):
		
		module = importer.find_module(modname).load_module(modname)
		
		for cls in Utils.module_classes(module):
			if issubclass(cls, ASTSetInterface):
				if cls.Alias.lower() == alias.lower():
					return cls
	
	return None

