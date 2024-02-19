import unittest
from dojo import class_extract


class ScrapperTest(unittest.TestCase):
    def test_get_class(self):
        response = '<strong>oi</strong>'
        response += '<h1 class="content-head__title" itemprop="headline">Relator da Previdência vai excluir estados e municípios do texto que vai à votação na comissão</h1>'
        response += '<h3 class="content-head__subtitle" itemprop="headline">heyyyyy</h3>'

        self.assertEqual(class_extract(response, 'content-head__title'),
                         ['<h1 class="content-head__title" itemprop="headline">Relator da Previdência vai excluir estados e municípios do texto que vai à votação na comissão</h1>'])

    def test_get_class2(self):
        response = '<strong>oi</strong>'
        response += '<h1 class="content-head__title" itemprop="headline">oiTitle</h1>'
        response += '<h3 class="content-head__subtitle" itemprop="headline">heyyyyy</h3>'

        self.assertEqual(class_extract(response, 'content-head__title'),
                         ['<h1 class="content-head__title" itemprop="headline">oiTitle</h1>'])

    # def test_get_class3(self):
    #     response = '<strong>oi</strong>'
    #     response += '<h1 class="content-head__title" itemprop="headline">oiDojo</h1>'
    #     response += '<h3 class="content-head__subtitle" itemprop="headline">heyyyyy</h3>'

    #     self.assertEqual(class_extract(response, 'content-head__title'),
    #                      ['<h1 class="content-head__title" itemprop="headline">oiDojo</h1>'])


if __name__ == '__main__':
    unittest.main()
