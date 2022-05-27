## System Imports
from enum import Enum


## Application Imports


## Library Imports

class CS6Location(Enum):

	Null = 'none'
	Module = 'module'
	Include = 'include'
	ModuleVariable = 'module.variable'
	ModuleVariableDefinition = 'variable.def'
	Declaration = 'declaration'
	DeclarationStatement = 'declaration.statement'
	Function = 'function'
	FunctionDefinition = 'function.definition'
	FunctionBody = 'function.body'
	FunctionCondition = 'function.condition'