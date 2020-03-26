# LAB8
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import unittest
from objects import *


class TestCases(unittest.TestCase):
    def test_equality(self):
        # Add test here
        point1 = Point(2, 3)
        point2 = Point(2, 3)
        point3 = Point(3, 4)
        point4 = Point(3, 4)
        circle1 = Circle(5, 6)
        circle2 = Circle(5, 6)
        circle3 = Circle(6, 7)
        circle4 = Circle(6, 8)
        self.assertEqual(point1 == point2, True)
        self.assertEqual(point3 == point4, True)
        self.assertEqual(circle1 == circle2, True)
        self.assertEqual(circle3 == circle4, False)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
