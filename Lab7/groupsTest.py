# Name: Hayden Tam
# Teacher: S. Einikan
# CPE101
# Section: 05

import unittest
from groups import *


class TestCases(unittest.TestCase):
    def test_group_of_3(self):
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]), [
                         [1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(groups_of_3([3, 1, 2, 5, 7, 2, 1, 8, 9, 0, 2, 1, 6, 14]), [
                         [3, 1, 2], [5, 7, 2], [1, 8, 9], [0, 2, 1], [6, 14]])

        self.assertEqual(groups_of_3([3, 1, 2, 5, 7, 2, 1, 8, 9, 0, 2, 1, 6]), [
                         [3, 1, 2], [5, 7, 2], [1, 8, 9], [0, 2, 1], [6]])


if __name__ == '__main__':
    unittest.main()
