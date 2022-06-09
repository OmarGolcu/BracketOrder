from operator import is_
from bracket_order import is_valid_input,bracket_order_control
import unittest

class InputValidation(unittest.TestCase):

    def test_with_empty_string(self):
        self.assertEqual(is_valid_input(''),False)
    
    def test_with_invalid_values(self):
        self.assertEqual(is_valid_input('123421'),False)
        self.assertEqual(is_valid_input('asdeasd'),False)
        self.assertEqual(is_valid_input('{2313.asda'),False)
        self.assertEqual(is_valid_input('{}(.)'),False)
        self.assertEqual(is_valid_input('{}({1].)'),False)
    
    def test_with_valid_values(self):
        self.assertEqual(is_valid_input('{}'),True)
        self.assertEqual(is_valid_input('{'),True)
        self.assertEqual(is_valid_input(')'),True)
        self.assertEqual(is_valid_input('({{]]][]}}))'),True)
        self.assertEqual(is_valid_input('({{]}}))'),True)

    
    
    


class OrderControl(unittest.TestCase):

    def test_with_one_bracket(self):
        for bracket in ['{','}','(',')','[',']']  :
            self.assertEqual(bracket_order_control(bracket),False)
        
    def test_with_unbalanced_string(self):
          self.assertEqual(bracket_order_control('{]'),False)
          self.assertEqual(bracket_order_control('{}(}'),False)
          self.assertEqual(bracket_order_control('{}(()}'),False)
          self.assertEqual(bracket_order_control('{(([{)}]))}()'),False) 

    def test_with_balanced_string(self):
         self.assertEqual(bracket_order_control('{}'),True)
         self.assertEqual(bracket_order_control('{}()'),True)
         self.assertEqual(bracket_order_control('{()}[(())]'),True)
         self.assertEqual(bracket_order_control('{(([]))}'),True)  


if __name__ == '__main__':
    unittest.main()