import unittest

from primas import valor_da_letra, valor_da_palavra, eh_primo, palavra_eh_prima

class ValorDaLetraTestCase(unittest.TestCase):

    def teste_valor_da_letra_a(self):
        self.assertEquals(valor_da_letra('a'), 1)

    def teste_valor_da_letra_b(self):
        self.assertEquals(valor_da_letra('b'), 2)

    def teste_valor_da_letra_A(self):
        self.assertEquals(valor_da_letra('A'), 27)

    def teste_valor_da_letra_B(self):
        self.assertEquals(valor_da_letra('B'), 28)


class ValorDaPalavraTestCase(unittest.TestCase):

    def teste_valor_da_palavra_ba(self):
        self.assertEquals(valor_da_palavra('ba'), 3)

    def teste_valor_da_palavra_ave(self):
        self.assertEquals(valor_da_palavra('ave'), 28)

    def teste_valor_da_palavra_AA(self):
        self.assertEquals(valor_da_palavra('AA'), 54)


class NumeroEhPrimoTestCase(unittest.TestCase):

    def teste_eh_primo_7(self):
        self.assertTrue(eh_primo(7))

    def teste_eh_primo_4(self):
        self.assertFalse(eh_primo(4))

    def teste_eh_primo_1(self):
        self.assertFalse(eh_primo(1))

    def teste_eh_primo_2(self):
        self.assertTrue(eh_primo(2))

    def teste_eh_primo_1000000000(self):
        self.assertFalse(eh_primo(1000000000))

    def teste_eh_primo_3571(self):
        self.assertTrue(eh_primo(3571))

    def test_eh_big_prime_16769023(self):
        self.assertTrue(eh_primo(16769023))

class PalavraEhPrimaTestCase(unittest.TestCase):

    def test_eh_prima_ab(self):
        self.assertTrue(palavra_eh_prima('ab'))

    def test_nao_eh_prima_aba(self):
        self.assertFalse(palavra_eh_prima('aba'))

    def test_nao_eh_primo_alchueyr(self):
        self.assertFalse(palavra_eh_prima('alchueyr'))

unittest.main()
