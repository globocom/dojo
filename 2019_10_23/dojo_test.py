import unittest
from dojo import check_token, replace_target, main


class DojoTest(unittest.TestCase):
    def test_check_token(self):
        self.assertTrue(check_token('if a + b > 0 && a - b < 0', '&&'))

    def test_check_token_2(self):
        self.assertFalse(check_token('if a + b > 0 && a - b < 0', '||'))
    
    def test_check_token_3(self):
        self.assertTrue(check_token('if a + b > 0  && a - b < 0', ''))

    def test_check_token_4(self):
        self.assertFalse(check_token('if a + b > 0 &&& a - b < 0', '&&'))

    def test_replace_target(self):
        self.assertEqual(replace_target('if a + b > 0 && a - b < 0', '&&', 'and'), 'if a + b > 0 and a - b < 0')

    def test_replace_target_2(self):
        self.assertEqual(replace_target('if a + b > 0 || a - b < 0', '||', 'or'), 'if a + b > 0 or a - b < 0')

    def test_replace_target_3(self):
        self.assertEqual(replace_target('if a + b > 0', '', ''), 'if a + b > 0')

    def test_replace_target_4(self):
        self.assertEqual(replace_target('if a + b > 0', '19', ''), 'if a + b > 0')
    
    def test_main(self):
        self.assertEqual(main(['if a + b > 0 || a - b < 0']), ['if a + b > 0 or a - b < 0'])

    def test_main_1(self):
        self.assertEqual(main(['if a + b > 0']), ['if a + b > 0'])

    def test_main_2(self):
        self.assertEqual(main(['if a + b > 0 && a - b < 0']), ['if a + b > 0 and a - b < 0'])

if __name__ == '__main__':
    unittest.main()
