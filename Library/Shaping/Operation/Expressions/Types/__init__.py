## System Imports
from typing import Type, TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Library.Shaping.Patch.controller import PatchController

from Library.Shaping.Operation.Expressions import composition
from Library.Shaping.Operation.Expressions.Types.Maker import MakerExpression
from Library.Shaping.Operation.Expressions.interfaces import ExpressionInterface
from Library.Shaping.Operation.Expressions.Types.Builder import BuilderExpression
from Library.Shaping.Operation.Expressions.Types.Resolver import ResolverExpression


## Library Imports


expression_types: list[Type[ExpressionInterface]] = [
	BuilderExpression,
	MakerExpression,
	ResolverExpression
]


def get_expressions_and_names(controller: 'PatchController', expression: str) -> list[tuple[Type[ExpressionInterface], str]]:
	types = []
	
	for name in composition.get_expression_names(expression):
		action = controller.find_action(name)
		
		if action:
			types.append((action.ExpressionType, name))
	
	return types

