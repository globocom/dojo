from unittest import TestCase
from fizz_buzz import fizz_buzz, fizz_ou_buzz
import unittest

class FizzBuzzTest(TestCase):

    def test_3_deve_ser_fizz(self):
        self.assertEqual(fizz_ou_buzz(3), "fizz")

    def test_5_deve_ser_buzz(self):
        self.assertEqual(fizz_ou_buzz(5), "buzz")

    def test_15_deve_ser_fizzbuzz(self):
        self.assertEqual(fizz_ou_buzz(15), "fizzbuzz")

    def test_2_deve_retornar_2(self):
        self.assertEqual(fizz_ou_buzz(2), '2')
        
    def test_lista_com_1_2_3_retorna_1_2_fizz(self):
        self.assertEqual(fizz_buzz([1, 2, 3]), '1\n2\nfizz')

    def test_lista_com_1_2_5_retorna_1_2_buzz(self):
        self.assertEqual(fizz_buzz([1, 2, 5]),'1\n2\nbuzz')
        
    def test_lista_1_ate_100_pra_validar_problema(self):
        self.assertEqual(fizz_buzz(range(1, 101)), '1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n16\n17\nfizz\n19\nbuzz\nfizz\n22\n23\nfizz\nbuzz\n26\nfizz\n28\n29\nfizzbuzz\n31\n32\nfizz\n34\nbuzz\nfizz\n37\n38\nfizz\nbuzz\n41\nfizz\n43\n44\nfizzbuzz\n46\n47\nfizz\n49\nbuzz\nfizz\n52\n53\nfizz\nbuzz\n56\nfizz\n58\n59\nfizzbuzz\n61\n62\nfizz\n64\nbuzz\nfizz\n67\n68\nfizz\nbuzz\n71\nfizz\n73\n74\nfizzbuzz\n76\n77\nfizz\n79\nbuzz\nfizz\n82\n83\nfizz\nbuzz\n86\nfizz\n88\n89\nfizzbuzz\n91\n92\nfizz\n94\nbuzz\nfizz\n97\n98\nfizz\nbuzz')
unittest.main()