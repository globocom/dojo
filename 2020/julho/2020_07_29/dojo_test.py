import unittest
from dojo import get_dependencies, remove_repeted_letters, get_dict_dependencies


class DojoTest(unittest.TestCase):
    def test_return_necessary_letter(self):
        self.assertEquals(get_dependencies([["a","a"],["a", "b"]], "a"), {"b"})

    def test_return_necessary_letter_2(self):
        self.assertEquals(get_dependencies([["a","a"],["a", "a"]], "a"), None)
    
    def test_return_necessary_letter_3(self):
        self.assertEquals(get_dependencies([["a","a"],["a", "b"]], "b"), None)

    def test_return_necessary_letter_4(self):
        self.assertEquals(get_dependencies([['a', 'a', 'a'], ['b','a','c']], "a"), {'b','c'})

    def test_removing_repeted_letters(self):
        self.assertEquals(remove_repeted_letters([["a","a"],["a","b"]]), {"a","b"})

    def test_removing_repeted_letters2(self):
        self.assertEquals(remove_repeted_letters([["a","b"],["c","d"]]), {"a","b","c","d"})
        
    def test_removing_repeted_letters3(self):
        self.assertEquals(remove_repeted_letters([["a","a"],["a","a"]]), {"a"})
    
    def test_dict_dependencies(self):
        self.assertEquals(get_dict_dependencies([["a","a"],["a","a"]]), {"a" : None})
    
    def test_dict_dependencies2(self):
        self.assertEquals(get_dict_dependencies([["a","a"],["a","b"]]), {"a": {"b"}, "b": None})

    def test_dict_dependencies3(self):
        self.assertEquals(get_dict_dependencies([["a","b"],["c","d"]]), {"a": {"c"}, "b": {"d"}, "c": None, "d": None})

if __name__ == '__main__':
    unittest.main()

# Allan - Sami - Mateus - Ingrid