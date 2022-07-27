## System Imports
from re import RegexFlag


## Application Imports


## Library Imports
import regex


Pattern: str = r'#\{(.*?)\}'
Flag: RegexFlag | int = 0

WithArgumentsPattern: str = r'#\{(.*?)\}\((.*?)\)'
WithArgumentsFlag: RegexFlag | int = 0

ArgumentsPattern: str = r'[^,]+(?=,)?'
ArgumentsFlag: RegexFlag | int = 0


def has_expressions(expression: str) -> bool:
	return regex.match(Pattern, expression, Flag) is not None


def get_expression_names(expression: str) -> list[str]:
	names = []
	
	for find in regex.findall(Pattern, expression, Flag):
		if isinstance(find, tuple):
			names.append(find[0])
			continue
		
		names.append(find)
	
	return names


def get_expression_arguments(expression: str) -> list[str]:
	arguments = []
	
	for find in regex.findall(WithArgumentsPattern, expression, WithArgumentsFlag):
		if isinstance(find, tuple):
			arguments.append(find[1])
			continue
		
		arguments.append(find)
	
	return arguments


def parse_expression_arguments(arguments_expression: str) -> list[str]:
	return regex.findall(ArgumentsPattern, arguments_expression, ArgumentsFlag)

