## System Imports
from typing import TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Library.Shaping.Patch.controller import PatchController

from Library.Shaping.Operation.Expressions import Types, composition
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface


## Library Imports


def search_expressions(controller: 'PatchController', expression: str, parent: ActionInterface) -> list[ExpressionInterface]:
	expressions = []
	
	if composition.has_expressions(expression):
		for expression_type, name in Types.get_expressions_and_names(controller, expression):
			action = parent.PatchController.find_action(name)
			
			if not action:
				raise AttributeError(f"Could not find action '{name}' required by action '{parent.Name}'")
			
			expressions.append(expression_type(action, parent))
		
	return expressions


