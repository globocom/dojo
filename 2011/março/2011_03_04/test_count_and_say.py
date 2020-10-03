import unittest
from count_and_say import count_and_say

class CountAndSayTestCase(unittest.TestCase):

    def test_asa_tem_2_a_1_s(self):
        self.assertEqual(count_and_say('asa'), '2 a 1 s')

    def test_aba_tem_2_a_1_b(self):
        self.assertEqual(count_and_say('aba'), '2 a 1 b')

    def test_bebe_tem_2_b_2_e(self):
        self.assertEqual(count_and_say('bebe'), '2 b 2 e')

    def test_baba_tem_2_a_2_b(self):
        self.assertEqual(count_and_say('baba'), '2 a 2 b')
    
    def test_look_and_say(self):
        self.assertEqual(count_and_say('look and say'), '2 a 1 d 1 k 1 l 1 n 2 o 1 s 1 y')
unittest.main()