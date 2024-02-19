import unittest
from dojo import ana_eat, bill_person, main


class DojoTest(unittest.TestCase):
    def test_ana_eat(self):
        self.assertEqual(ana_eat([3,4,5,6], 1), [3,5,6])

    def test_ana_eat_2(self):
        self.assertEqual(ana_eat([3,4,5,6], 0), [4,5,6])

    def test_ana_eat_3(self):
        self.assertEqual(ana_eat([3,4,5,6], 2), [3,4,6])

    def test_bill_person(self):
        self.assertEqual(bill_person([3,4,5,6]), 9)

    def test_bill_person_2(self):
        self.assertEqual(bill_person([3,4,5]), 6)

    def test_main(self):
        self.assertEqual(main([3,4,5,6],1,9), 2)

    def test_main_2(self):
        self.assertEqual(main([3,4,5,6],2,9), 3)
    
    def test_main_3(self):
        self.assertEqual(main([3,10,2,9],1,12), 5)

    def test_main_4(self):
        self.assertEqual(main([3,10,2,9],1,7), "Bon Appetit")

    def test_main_5(self):
        self.assertEqual(main([3,10,4,9],1,8), "Bon Appetit")






if __name__ == '__main__':
    unittest.main()
