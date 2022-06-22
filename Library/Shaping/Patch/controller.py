## System Imports


## Application Imports
from Library.Shaping.Operation.Actions.Types.Maker import MakerAction
from Library.Shaping.Operation.Actions.Types.Resolver import ResolverAction
from Library.Shaping.Patch.data import ShapingPatch, ShapingActions, ShapingBuilder, ShapingMaker, ShapingResolver, \
	ShapingReplacer
from Library.Projects.Internal.interfaces import BaseFileInterface
from Library.Shaping.Operation.Actions.interfaces import ActionInterface
from Library.Shaping.Operation.Actions.Types.Builder import BuilderAction
from Library.Shaping.Operation.Actions.Types.Replacer import ReplacerAction


## Library Imports


class PatchController:
	
	def __init__(self, patch: ShapingPatch, file: BaseFileInterface):
		self.__patch = patch
		self.__file = file
		
		self.__actions: list = make_actions_tree(self, patch)
		
		file.Controller.on_visit += self.on_visit
	
	def on_visit(self, controller):
		for action in self.__actions:
			action.process(controller)
	
	def find_action(self, name: str) -> ActionInterface | None:
		for action in self.__actions:
			act = self.find_action_inner(action, name)
			
			if act:
				return act
		
		return None
	
	def find_action_inner(self, action, name):
		if action.Name.lower() == name.lower():
			return action
		
		for action in action.Actions:
			child_action = self.find_action_inner(action, name)
			
			if self.find_action_inner(action, name):
				return child_action
		
		return None


def make_actions_tree(controller: PatchController, patch: ShapingPatch) -> list:
	actions_tree = []
	
	types = {
		ShapingBuilder: BuilderAction,
		ShapingReplacer: ReplacerAction,
		ShapingMaker: MakerAction,
		ShapingResolver: ResolverAction,
	}
	
	for _, actions in patch.actions.__dict__.items():
		for name, action in actions.items():
			if not type(action) in types:
				raise AttributeError(f'Unexpected action type {type(action)}')
		
			action_type = types[type(action)]
			action_instance = action_type(controller, name, action)
			actions_tree.append(action_instance)
			
			if getattr(action, 'actions'):
				setup_action(action_instance, action.actions, controller)
	
	return actions_tree


def setup_action(action: ActionInterface, action_children: ShapingActions, controller):
	
	types = {
		BuilderAction: action_children.builders,
		ReplacerAction: action_children.replacements,
		MakerAction: action_children.makers,
		ResolverAction: action_children.resolvers,
	}
	
	for action_type, actions in types.items():
		for name, shaping_action in actions.items():
			child_action = action_type(controller, name, shaping_action)
			action.Actions.append(child_action)


def setup_action_uni(action, shaping_action):
	if not hasattr(shaping_action, 'actions'):
		return
	
	for child_action in getattr(action, 'actions'):
		action.Actions.append(setup_action(child_action, child_action.actions))
	
