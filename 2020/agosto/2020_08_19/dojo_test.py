import unittest
from dojo import get_painted_nodes, get_both_nodes, main


class DojoTest(unittest.TestCase):
    def test_get_painted(self):
        self.assertEqual(get_painted_nodes([1,2,3],2,3), {2})

    def test_get_painted2(self):
        self.assertEqual(get_painted_nodes([1,2,3],1,3), {1})

    def test_get_painted3(self):
        self.assertEqual(get_painted_nodes([1,2,3],3,3), {3})

    def test_get_both_nodes(self):
        self.assertEqual(get_both_nodes([1,2,3], 4, 3, 4, 1), 4)

    def test_get_both_nodes2(self):
        self.assertEqual(get_both_nodes([1,2,3], 3, 3, 4, 1), 4)

    def test_get_both_nodes3(self):
        self.assertEqual(get_both_nodes([1,2,3], 2, 3, 3, 1), 3)

    def test_main(self):
        self.assertEqual(main([1,2,3], 3, 1), 2.875)

    def test_main2(self):
        self.assertEqual(main([1, 1, 3, 4, 4, 3, 4], 2, 3), 2.65625)

    def test_main3(self):
        self.assertEqual(main([1, 1, 1, 1, 1, 1, 1, 1, 1], 3, 4), 1.9000000000000012)

if __name__ == '__main__':
    unittest.main()

# Nós: 1 2 3
# Entradas: 4 3 1

# Nós: 1 1 3 4 4 3 4
# Entradas: 8 2 3

# Nós: 1 1 1 1 1 1 1 1 1
# Entradas: 10 3 4