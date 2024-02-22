from main.pumpkins import find_robot_way
import unittest


class TestOfRobotsWays(unittest.TestCase):

    def test_1(self):
        """
        Поле розміром m==n==5
        """
        field_with_pumpkins_1 = [[1, 2, 3, 4, 5],
                                 [6, 7, 8, 9, 10],
                                 [11, 12, 13, 14, 15],
                                 [16, 17, 18, 19, 20]]

        assert find_robot_way(field_with_pumpkins_1) == [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18,
                                                         17,
                                                         16]

    def test_2(self):
        """
        Поле розміром m = 2, n = 4
        """
        field_with_pumpkins_1 = [[1, 2, 3, 4],
                                 [5, 6, 7, 8]]

        assert find_robot_way(field_with_pumpkins_1) == [1, 2, 3, 4, 8, 7, 6, 5]

    def test_3(self):
        """
        Поле розміром n = 1, m = 6
        """
        field_with_pumpkins_1 = [[1],
                                 [7],
                                 [11],
                                 [16],
                                 [1],
                                 [12]]

        assert find_robot_way(field_with_pumpkins_1) == [1, 7, 11, 16, 1, 12]
