import unittest

from count_numbers import count_letters_in_numbers

class TestCountNumber(unittest.TestCase):
    def test_1_should_have_3_letters(self):
        self.assertEquals(count_letters_in_numbers(1), 3)
        
    def test_2_should_have_3_letters(self):
        self.assertEquals(count_letters_in_numbers(2), 3)
        
    def test_3_should_have_5_letters(self):
        self.assertEquals(count_letters_in_numbers(3), 5)
        
    def test_9_should_have_4_letters(self):
        self.assertEquals(count_letters_in_numbers(9), 4)
        
    def test_11_should_have_6_letters(self):
        self.assertEquals(count_letters_in_numbers(11), 6)
        
    def test_20_should_have_6_letters(self):
        self.assertEquals(count_letters_in_numbers(20), 6)
        
    def test_22_should_have_9_letters(self):
        self.assertEquals(count_letters_in_numbers(22), 9)
        
    def test_99_should_have_10_letters(self):
        self.assertEquals(count_letters_in_numbers(99), 10)
        
    def test_100_should_have_10_letters(self):
        self.assertEquals(count_letters_in_numbers(100), 10)
        
    def test_200_should_have_10_letters(self):
        self.assertEquals(count_letters_in_numbers(200), 10)
        
    def test_101_should_have_16_letters(self):
        self.assertEquals(count_letters_in_numbers(101), 16)
    
    def test_102_should_have_16_letters(self):
        self.assertEquals(count_letters_in_numbers(102), 16)
    

unittest.main()