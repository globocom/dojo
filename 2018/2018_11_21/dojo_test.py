import unittest
from dojo import start_lampadas, is_divisible, switch_lampada, percorre_corredor, main


class DojoTest(unittest.TestCase):
    def test_init_lampadas(self):
        self.assertEqual(["off", "off", "off"], start_lampadas(3))
        self.assertEqual(["off", "off"], start_lampadas(2))
        self.assertEqual(["off"], start_lampadas(1))

    def test_is_divisible(self):
        self.assertTrue(is_divisible(1, 1))
        self.assertFalse(is_divisible(1, 2))
        self.assertTrue(is_divisible(2, 2))

    def test_switch_lampada(self):
        self.assertEqual("on", switch_lampada("off"))
        self.assertEqual("off", switch_lampada("on"))

    def test_percorre_corredor(self):
        self.assertEqual(["on"], percorre_corredor(["off"], 1))
        self.assertEqual(["on", "on"], percorre_corredor(["off", "off"], 1))
        self.assertEqual(["on", "off"], percorre_corredor(["on", "on"], 2))
        self.assertEqual(["on", "off", "off"],
                         percorre_corredor(["on", "off", "on"], 3))

    def test_main(self):
        self.assertEqual(["on", "off", "off"], main(3))


if __name__ == '__main__':
    unittest.main()
