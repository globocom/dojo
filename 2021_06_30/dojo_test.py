import unittest
from dojo import main, LinkedList


class DojoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(main())

    def test_LinkedList_1(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.root.val, 1)

    def test_LinkedList_2(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.root.val, 1)

    def test_LinkedList_3(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.root.next.next.val, 3)

    def test_LinkedList_print(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(5)
        self.assertEqual(str(ll), "1 -> 2 -> 3 -> 5")





if __name__ == '__main__':
    unittest.main()

