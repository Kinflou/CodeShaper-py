## System Imports
import pkgutil
from typing import Type


## Application Imports
from Library import Utils
from Library.Projects.Internal.interfaces import BaseTargetInterface


## Library Imports


def find_type(alias: str) -> Type[BaseTargetInterface] | None:
	
	for importer, modname, is_pkg in pkgutil.walk_packages(path=__path__, onerror=lambda x: None):
		module = importer.find_module(modname).load_module(modname)
		
		for cls in Utils.module_classes(module):
			if issubclass(cls, BaseTargetInterface):
				if cls.Alias.lower() == alias.lower():
					return cls
	
	return None

