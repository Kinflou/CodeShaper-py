## System Imports
from re import RegexFlag


## Application Imports


## Library Imports
import regex


Pattern: str = r'#\{(.*?)\}'
Flags: RegexFlag | int = 0

ArgumentsPattern: str = r'[^,]+(?=,)?'
ArgumentFlags: RegexFlag | int = 0


def has_expressions(expression: str):
	return regex.match(Pattern, expression, Flags)


def get_expression_names(expression: str) -> list[str]:
	names = []
	
	for find in regex.findall(Pattern, expression, Flags):
		if isinstance(find, tuple):
			names.append(find[0])
			continue
		
		names.append(find)
	
	return names


def parse_arguments(arguments_expression: str):
	return regex.findall(ArgumentsPattern, arguments_expression, ArgumentFlags)
