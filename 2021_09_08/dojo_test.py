import unittest
from dojo import *


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def teste_hash_1(self):
        self.assertEqual(MyHashMap._hash(53), 5)

    def teste_hash_2(self):
        self.assertEqual(MyHashMap._hash(56), 0)

    def test_get_1(self):
        my_hmap = MyHashMap()
        my_hmap.set(53, "Olá")
        self.assertEqual(my_hmap.get(53), "Olá")

    def teste_get_2(self):
        my_hmap = MyHashMap()
        my_hmap.set(53, "Olá")
        my_hmap.set(54, "Tudo bem")
        self.assertEqual(my_hmap.get(54), "Tudo bem")

    def teste_get_3(self):
        my_hmap = MyHashMap()
        my_hmap.set(53, "Olá")
        my_hmap.set(54, "Tudo bem")
        self.assertEqual(my_hmap.get(5), None)

    # def teste_len_1(self):
    #     my_hmap = MyHashMap()
    #     my_hmap.set(53, "Olá")
    #     my_hmap.set(54, "Tudo bem")
    #     self.assertEqual(my_hmap.len(), 2)
    def teste_len_1(self):
        my_hmap = MyHashMap()
        my_hmap.set(53, "Olá")
        my_hmap.set(54, "Tudo bem")
        self.assertEqual(len(my_hmap), 2)

    def teste_repeated_1(self):
        my_hmap = MyHashMap()
        my_hmap.set(53, "Olá")
        my_hmap.set(53, "Tudo bem")
        self.assertEqual(len(my_hmap), 1)
        self.assertEqual(my_hmap.get(53), "Tudo bem")

    def test_delete_1(self):
        my_hmap = MyHashMap()
        my_hmap.set(53, "Olá")
        my_hmap.set(5, "Tudo bem")
        self.assertEqual(len(my_hmap), 2)
        self.assertEqual(my_hmap.get(53), "Olá")
        print(my_hmap.arr)
        my_hmap.delete(5)
        self.assertEqual(len(my_hmap), 1)
        self.assertEqual(my_hmap.get(5), None)
        print(my_hmap.arr)


if __name__ == "__main__":
    unittest.main()
