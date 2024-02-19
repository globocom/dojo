#coding: utf-8

# Dado o seguinte teclado numérico:
#
# 0 - e
# 1 - j n q
# 2 - r w x
# 3 - d s y
# 4 - f t
# 5 - a m
# 6 - c i v
# 7 - b k u
# 8 - l o p
# 9 - g h z
#
# uma lista de palavras, e uma lista de números. Precisamos encontrar palavras
# que se encaixem nos números dados.
#
# Por exemplo, dada a lista de palavras:
#
# good
# test
# go
# od
#
# Podemos transformar o número
#
# 9883-4034
#
# em
#
# good test
# go od test
#
# Isso pode ser utilizado para tentar advinhar que palavra o usuario está
# digitando num teclado numérico. Também pode ser utilizado para criar palavras
# que vão ajudar as pessoas a decorarem números telefonicos.

import string

class T8l(object):

    def __init__(self, words):
        intab = 'abcdefghijklmnopqrstuvwxyz'
        outab = '57630499617851881234762239'

        self.translator = string.maketrans(intab, outab)
        self.words = words
        self.translated_words = [self.to_numbers(word) for word in words]

    def to_numbers(self, word):
        return word.translate(self.translator)

    def to_words(self, number):
        acc = []
        for n in self.translated_words:
            if number.startswith(n):
                acc.append(self.words[self.translated_words.index(n)])
                acc.extend(self.to_words(number[len(n):]))
        return acc



        return self.words[index]
