import unittest
from dojo import brainfuck


class DojoTest(unittest.TestCase):
    def test_should_return_a(self):
        instructions = "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
        stdout = brainfuck(instructions)
        self.assertEqual(stdout, "A")

    def test_should_return_b(self):
        instructions = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
        stdout = brainfuck(instructions)
        self.assertEqual(stdout, "B")

    def test_should_return_c(self):
        instructions = "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
        stdout = brainfuck(instructions)
        self.assertEqual(stdout, "C")

    def test_should_return_b_when_decrement(self):
        instructions = "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-++++++++."
        stdout = brainfuck(instructions)
        self.assertEqual(stdout, "B")

    def test_should_return_a_when_decrement(self):
        instructions = "+++++++++++++++-++++++++++++++++++++++++++++++++++++++++++++-++++++++."
        stdout = brainfuck(instructions)
        self.assertEqual(stdout, "A")

    def test_should_print_a_and_b(self):
        instructions = (
            "+++++++++++++++-++++++++++++++++++++++++++++++++++++++++++++-++++++++."
            ">++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
        )
        stdout = brainfuck(instructions)
        self.assertEqual(stdout, "AB")

    def test_should_print_c_and_a(self):
        instructions = (
            "+++++++++++++++++-++++++++++++++++++++++++++++++++++++++++++++-++++++++."
            ">++++++++++++++-++++++++++++++++++++++++++++++++++++++++++++++++++++."
        )
        stdout = brainfuck(instructions)
        self.assertEqual(stdout, "CA")

if __name__ == '__main__':
    unittest.main()
