import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())


if __name__ == '__main__':
    unittest.main()
