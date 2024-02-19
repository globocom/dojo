class GameObject(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return unicode(self)
    def __unicode__(self):
        return self.name
    def __gt__(self, other):
        self.ganha_de = other
        return other

pedra = GameObject("pedra")
papel = GameObject("papel")
tesoura = GameObject("tesoura")
pedra > tesoura > papel > pedra


def jokenpo(mao1, mao2):
    if mao1 == mao2:
        return "{0:s} empata com {1:s}".format(mao1, mao2)
    elif mao1.ganha_de == mao2:
        return "{0:s} ganha de {1:s}".format(mao1, mao2)
    else:
        return "{0:s} ganha de {1:s}".format(mao2, mao1)