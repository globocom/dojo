import unittest
from dojo import main


class DojoTest(unittest.TestCase):
    def test_pe(self):
        self.assertEqual(main(["PE"]), ["PE", "B"])

    def test_2pe(self):
        self.assertEqual(main(["PE", "PE"]), ["PE", "B", "PE", "B"])

    def test_3pe(self):
        self.assertEqual(main(["PE", "PE", "PE"]), [
                         "PE", "B", "PE", "B", "PE", "B"])

    def test_ps(self):
        self.assertEqual(main(["PS"]), ["PS"])

    def test_2ps(self):
        self.assertEqual(main(["PS", "PS"]), ["PS", "PS", "B"])

    def test_3ps(self):
        self.assertEqual(main(["PS", "PS", "PS"]), ["PS", "PS", "B", "PS"])

    def test_4ps(self):
        self.assertEqual(main(["PS", "PS", "PS", "PS"]), [
                         "PS", "PS", "B", "PS", "PS", "B"])

    def test_pe_ps(self):
        self.assertEqual(main(["PE", "PS"]), ["PE", "B", "PS"])

    def test_ps_pe(self):
        self.assertEqual(main(["PS", "PE"]), ["PS", "PE", "B"])

    def test_ps_pe_ps(self):
        self.assertEqual(main(["PS", "PE", "PS"]), ["PS", "PE", "B", "PS"])


if __name__ == '__main__':
    unittest.main()
