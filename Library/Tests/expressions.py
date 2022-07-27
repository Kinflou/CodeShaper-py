## System Imports
import unittest


## Application Imports
from Library.Shaping.Operation.Expressions import composition


## Library Imports


class SingleSimpleExpressionsTestCase(unittest.TestCase):
	
	def test_expression(self):
		expression = '#{expression_name}'
		
		processed = composition.get_expression_names(expression)
		
		expected_result = ['expression_name']
		self.assertEqual(processed, expected_result)
	
	def test_expression_with_one_argument(self):
		expression = '#{expression_name}(Hello)'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name'])
		self.assertEqual(arguments, ['Hello'])
	
	def test_expression_with_two_arguments(self):
		expression = '#{expression_name}(Jhon, Doe)'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name'])
		self.assertEqual(arguments, ['Jhon, Doe'])
	
	def test_expression_with_multiple_arguments(self):
		expression = '#{expression_name}(Jhon, Doe, Mark, Jolly)'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
	
		self.assertEqual(names, ['expression_name'])
		self.assertEqual(arguments, ['Jhon, Doe, Mark, Jolly'])


class SingleComplexExpressionsTestCase(unittest.TestCase):
	
	def test_expression_with_one_expression_argument(self):
		expression = '#{expression_name}(#{argument_expression_name})'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name', 'argument_expression_name'])
		self.assertEqual(arguments, ['#{argument_expression_name}'])
	
	def test_expression_with_two_expression_arguments(self):
		expression = '#{expression_name}(#{argument_expression_name}, #{another_argument_expression_name})'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name'])
		self.assertEqual(arguments, ['#{argument_expression_name}, #{another_argument_expression_name}'])


class MultipleSimpleExpressionsTestCase(unittest.TestCase):
	
	def test_expressions(self):
		expression = '#{expression_name} #{another_expression_name}'
		
		names = composition.get_expression_names(expression)
		
		self.assertEqual(names, ['expression_name', 'another_expression_name'])
	
	def test_expressions_one_with_one_argument(self):
		expression = '#{expression_name}(Hello), #{another_expression_name}'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name', 'another_expression_name'])
		self.assertEqual(arguments, ['Hello'])
	
	def test_expressions_one_with_two_arguments(self):
		expression = '#{expression_name}(Joseph, Joestar), #{another_expression_name}'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name', 'another_expression_name'])
		self.assertEqual(arguments, ['Joseph, Joestar'])
	
	def test_expressions_two_with_one_argument(self):
		expression = '#{expression_name}(Jonathan), #{another_expression_name}(Dio)'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name', 'another_expression_name'])
		self.assertEqual(arguments, ['Jonathan', 'Dio'])
	
	def test_expressions_two_with_two_arguments(self):
		expression = '#{expression_name}(Jonathan, Joestar), #{another_expression_name}(Dio, Brando)'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name', 'another_expression_name'])
		self.assertEqual(arguments, ['Jonathan, Joestar', 'Dio, Brando'])


class MultipleComplexExpressionsTestCase(unittest.TestCase):
	
	def test_expressions_one_with_one_expression_argument(self):
		expression = '#{expression_name}(#{argument_expression_name})'
		
		names = composition.get_expression_names(expression)
		arguments = composition.get_expression_arguments(expression)
		
		self.assertEqual(names, ['expression_name', 'argument_expression_name'])
		self.assertEqual(arguments, ['#{argument_expression_name}'])
		

if __name__ == '__main__':
	unittest.main()
