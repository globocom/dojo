import unittest

from fizzbuzz import fizzbuzz, fizzbuzz_lista


class FizzBuzzTestCase(unittest.TestCase):

    def test_1_retorna_1(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_7_retorna_7(self):
        self.assertEqual(fizzbuzz(7), 7)

    def test_3_retorna_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_5_retorna_buzz(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_15_retorna_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15),'FizzBuzz')

    def test_45_retorna_fizzbuzz(self):
        self.assertEqual(fizzbuzz(45), 'FizzBuzz')

    def test_deve_imprimir_uma_lista_com_100_numeros(self):
        self.assertEqual(100, len(fizzbuzz_lista(range(1, 101))))

    def test_deve_retornar_fizz(self):
        lista = fizzbuzz_lista(range(1, 101))
        self.assertEqual('Fizz', lista[2])

    def test_deve_retornar_buzz(self):
        lista = fizzbuzz_lista()

if __name__ == "__main__":
    unittest.main()


# FizzBuzz
# divisivel por 3? -> Fizz
# divisivel por 5? -> Buzz
# pelos dois -> FizzBuzz
# por nenhum -> numero