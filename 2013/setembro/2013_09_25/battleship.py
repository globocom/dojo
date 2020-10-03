from random import random

resposta = None


class Jogo:

    def __init__(self):
        self.tab = self.cria_tabuleiro()

    def cria_tabuleiro(self):
        self.resposta = self.coloca_navio()
        return [['O'] * 5]*5

    def coloca_navio(self):
        return (int(random()*5), int(random()*5))

    def joga(self, x, y):
        if self.resposta != (x, y):
            self.tab[x][y] = 'x'
