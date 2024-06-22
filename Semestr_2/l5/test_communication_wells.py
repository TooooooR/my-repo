import unittest
from communication_wells import *


class CommunicationWellsTest(unittest.TestCase):
    def test_1(self):
        result = read_file('communication_wells_1.csv')
        self.assertEqual(result, 2000)

    def test_2(self):
        result = read_file('communication_wells_2.csv')
        self.assertEqual(result, 2600)

    def test_3(self):
        result = read_file('communication_wells_3.csv')
        self.assertEqual(result, -1)

    def test_4(self):
        result = read_file('communication_wells_4.csv')
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
