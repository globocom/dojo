import unittest
from dojo import is_upper, is_lower, is_number, get_upper_list, get_lower_list, apply_filter


class DojoTest(unittest.TestCase):

    def test_is_upper(self):
        self.assertTrue(is_upper('A'))
    
    def test_is_not_upper_1(self):
        self.assertFalse(is_upper('b'))
    
    def test_is_not_upper_2(self):
        self.assertTrue(is_lower('b'))
    
    def test_is_not_lower_1(self):
        self.assertFalse(is_lower('A'))
    
    def test_is_not_lower_2(self):
        self.assertFalse(is_lower('3'))
    
    def test_is_number(self):
        self.assertTrue(is_number('2'))
    
    def test_is_not_number(self):
        self.assertFalse(is_number('p'))
    
    def test_is_not_number(self):
        self.assertFalse(is_number('T'))
    
    def test_apply_filter_upper(self):
        self.assertEqual(apply_filter('AbC1ad87', is_upper), 'AC')
    
    def test_apply_filter_lower(self):
        self.assertEqual(apply_filter('AbC1ad87', is_lower), 'bad')

    def test_apply_filter_number(self):
        self.assertEqual(apply_filter('AbC1ad87', is_number), '187')
    
    # def test_ginortS(self):
    #     self.assertEqual(ginortS('Sorting1234'), 'ginortS1234')



if __name__ == '__main__':
    unittest.main()

#Natalia - Mateus - Sami