import unittest
from dojo import remove_word, main


class DojoTest(unittest.TestCase):
    def test_remove_word_1(self):
        self.assertEqual(remove_word("bananauva", "banana"), "uva")

    def test_remove_word_2(self):
        self.assertEqual(remove_word("catdog", "dog"), "catdog")

    def test_remove_word_3(self):
        self.assertEqual(remove_word("pão", "pão"), "")
    
    def test_main_1(self):
        words = [
            "leet",
            "code"
        ]
        self.assertEqual(main("leetcode", words), True)

    def test_main_2(self):
        words = [
            "leet",
            "code",
            "apple",
        ]
        self.assertEqual(main("leetcodeapple", words), True)
    

if __name__ == '__main__':
    unittest.main()



# Sami - Elen - Allan - Tiago - Mateus - Juan


# s = "leetcode", wordDict = ["leet", "code"]
# FncOne(s,oneWord)
# "bananaaçaimaça" = ["banana", "açai", "maça"]
# "maçabanana"

# {
#     banana
#     acai
#     maca
# }

# bananaaçaimaça

# naaçaimaça { - - - } , açaimaça { - - - }

# solbabanana / [uva,sol, solba, banana]
# 
# sol_babanana
