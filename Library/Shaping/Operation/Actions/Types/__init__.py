## System Imports
from typing import Type


## Application Imports


## Library Imports
from Library.Shaping.Operation.Actions.Types.Maker import MakerAction
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Actions.Types.Builder import BuilderAction
from Library.Shaping.Operation.Actions.Types.Replacer import ReplacerAction
from Library.Shaping.Operation.Actions.Types.Resolver import ResolverAction


action_types: list[Type[ActionInterface]] = [
	BuilderAction,
	MakerAction,
	ReplacerAction,
	ResolverAction
]
