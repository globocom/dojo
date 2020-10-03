import unittest
from dojo import most_visited_page, most_visited_pages


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertEquals(most_visited_page(['A','B','A']), 'A')
 
    def test_true_2(self):
        self.assertEquals(most_visited_page(['B','B','A']), 'B') 

    def test_true_3(self):
        self.assertEquals(most_visited_page(['C','B','A']), 'C') 
        
    def test_true_4(self):
        self.assertEquals(most_visited_pages([['A','B','A'],['B','C','D']]), ['B','C','A'])

    def test_true_5(self):
        self.assertEquals(most_visited_pages([['C','B','A'],['B','C','D']]), ['C','B','A'])
    
    def test_true_6(self):
        self.assertEquals(most_visited_pages([['B','B','A'],['B','C','D']]), ['B','A','C'])

if __name__ == '__main__':
    unittest.main()
