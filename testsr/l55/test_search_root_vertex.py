import unittest
from search_root_vertex import *


class SearchRootVertex(unittest.TestCase):
    def test_1(self):
        search_root_vertex('root_vertex_in1.txt', 'root_vertex_out1.txt')
        with open('root_vertex_out1.txt', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, 4)

    def test_2(self):
        search_root_vertex('root_vertex_in2.txt', 'root_vertex_out2.txt')
        with open('root_vertex_out2.txt', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, 0)

    def test_3(self):
        search_root_vertex('root_vertex_in3.txt', 'root_vertex_out3.txt')
        with open('root_vertex_out3.txt', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, -1)

    def test_4(self):
        search_root_vertex('root_vertex_in4.txt', 'root_vertex_out4.txt')
        with open('root_vertex_out4.txt', 'r') as file:
            result = file.readline()
        self.assertEqual(result, 'None')


if __name__ == '__main__':
    unittest.main()
