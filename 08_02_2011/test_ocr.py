import unittest
from ocr import ocr


class OCRTest(unittest.TestCase):
    
    def test_numero_um(self):
        numero_um = """
   
   |
   |
"""
        
        self.assertEquals(1, ocr(numero_um))
    
    def test_numero_dois(self):
        numero_dois = """
 __
 __|
|__
"""
        
        self.assertEquals(2, ocr(numero_dois))
    
    def test_numero_tres(self):
        numero_tres="""
 __
 __|
 __|
"""
        self.assertEquals(3, ocr(numero_tres))
    
    def test_numero_quatro(self):
        numero_quatro="""

|__|
   |
"""
        
        self.assertEquals(4, ocr(numero_quatro))
        
    def test_numero_cinco(self):
        numero_cinco = """
 __
|__
 __|
"""
        self.assertEquals(5, ocr(numero_cinco))
    
    def test_numero_seis(self):
        numero_seis = """
 __
|__  
|__|
"""
        self.assertEquals(6, ocr(numero_seis))

    def test_numero_sete(self):
        numero_sete = """
 __
   |
   |
"""
        self.assertEquals(7, ocr(numero_sete))

    def test_numero_oito(self):
        numero_oito = """
 __
|__|
|__|
"""
        self.assertEquals(8, ocr(numero_oito))

    def test_numero_nove(self):
        numero_nove = """
 __
|__|
 __|
"""
        self.assertEquals(9, ocr(numero_nove))

    def test_numero_zero(self):
        numero_zero = """
 __
|  |
|__|
"""        
        self.assertEquals(0, ocr(numero_zero))

    def test_numero_dez(self):
        numero_dez = """
      __
   | |  |
   | |__|
"""
        print repr(numero_dez)
        self.assertEquals(10, ocr(numero_dez))
    
if __name__ == '__main__':
    unittest.main()