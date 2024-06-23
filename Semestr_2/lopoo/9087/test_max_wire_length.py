import unittest
from max_wire_length import *


class MaxWireLength(unittest.TestCase):
    def test_1(self):
        result = read_file('max_wire_length1.txt')
        self.assertEqual(result, 5.66)

    def test_2(self):
        result = read_file('max_wire_length2.txt')
        self.assertEqual(result, 300.00)

    def test_3(self):
        result = read_file('max_wire_length3.txt')
        self.assertEqual(result, 396.32)

    def test_4(self):
        result = read_file('max_wire_length4.txt')
        self.assertEqual(result, 2738.18)


if __name__ == '__main__':
    unittest.main()
