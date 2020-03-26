# LAB8
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import unittest
from objects import *

from funcs_objects import*

# Test cases for objects


class TestCases(unittest.TestCase):
    def test_point(self):
        # Add code here.
        point1 = Point(2, 3)
        self.assertEqual(point1.x, 2)
        self.assertEqual(point1.y, 3)

    def test_circle(self):
        # Add code here.
        circle1 = Circle(Point(2, 3), 6)
        circle2 = Circle(Point(4, 5), 9)
        self.assertEqual(circle1.radius, 6)
        self.assertEqual(circle1.center.x, 2)
        self.assertEqual(circle2.center.x, 4)
        self.assertEqual(circle2.radius, 9)
    # Add other testing functions

    def testDistance(self):
        point1 = Point(2, 3)
        point2 = Point(5, 6)
        point3 = Point(4, 0)
        point4 = Point(5, 0)
        self.assertAlmostEqual(distance(point1, point2), 4.24264068711)
        self.assertEqual(distance(point3, point4), 1)

    def testOverlap(self):
        point1 = Point(2, 3)
        point2 = Point(5, 6)
        circle1 = Circle(point1, 8)
        circle2 = Circle(point2, 9)
        circle3 = Circle(point2, 10)
        circle4 = Circle(point2, 11)
        self.assertEqual(circles_overLap(circle1, circle2), True)
        self.assertEqual(circles_overLap(circle1, circle2), True)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
