# LAB8
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import unittest
from list_comp import *

# Test point class


class TestCases(unittest.TestCase):
    def test_1(self):
        point1 = Point(2, 3)
        point2 = Point(4, 5)
        point3 = Point(5, 6)
        listPoint = [point1, point2]
        self.assertListEqual(distance_all(listPoint), [
            3.605551275463989, 6.4031242374328485])
        listPoint = [point1, point2, point3]
        self.assertListEqual(distance_all(listPoint), [
            3.605551275463989, 6.4031242374328485, 7.810249675906654])

    def test_2(self):
        point1 = Point(2, 3)
        point2 = Point(3, 4)
        point3 = Point(-5, 2)
        listPoint = [point1, point2]
        self.assertEqual(are_in_first_quadrant(
            listPoint), [Point(2, 3), Point(3, 4)])
        listPoint.append(point3)
        self.assertListEqual(are_in_first_quadrant(
            listPoint), [Point(2, 3), Point(3, 4)])



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
