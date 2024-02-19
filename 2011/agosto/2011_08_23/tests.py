import unittest

from amigos import amigos_proximos, distancia_entre_dois_pontos, Amigo

class ProximidadeEntreAmigosTestCase(unittest.TestCase):
    def setUp(self):
        self.amigo = Amigo(id=1, latitude=0, longitude=0)
        self.amigo2 = Amigo(id=2, latitude=1, longitude=1)
        self.amigo3 = Amigo(id=3, latitude=20, longitude=20)

    def test_deve_retornar_os_amigos_mais_proximos_ordenados(self):
        self.assertEquals(amigos_proximos([self.amigo, self.amigo2]), {1: [2], 2: [1]})

    def test_deve_retornar_os_amigos_mais_proximos_entre_tres_amigos(self):
        self.assertEquals(amigos_proximos([self.amigo, self.amigo2, self.amigo3]),
                          {1: [2, 3], 2: [1, 3], 3: [2, 1]})

class DistanciaEntreDoisPontosTestCase(unittest.TestCase):

    def test_distancia_entre_dois_pontos(self):
        self.assertEquals(distancia_entre_dois_pontos((0, 0), (3, 4)), 5)

class AmigoTestCase(unittest.TestCase):

    def setUp(self):
        self.amigo = Amigo(id=1, latitude=0.4, longitude=0.12)

    def test_cria_instancia_de_amigo(self):
        self.assertTrue(isinstance(self.amigo, Amigo))

    def test_amigo_deve_ter_id(self):
        self.assertEqual(self.amigo.id, 1)

    def test_amigo_deve_ter_latitude(self):
        self.assertEqual(self.amigo.latitude, 0.4)

    def test_amigo_deve_ter_longitute(self):
        self.assertEqual(self.amigo.longitude, 0.12)

if __name__ == '__main__':
    unittest.main()
