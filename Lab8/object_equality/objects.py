# LAB8
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

from utility import *

# Add equality into the class Point


class Point:
    def __init__(self, x, y):
        self. x = x
        self. y = y

    def __eq__(self, other):
        return (type(self) == type(other) and (epsilon_equal(self.x, other.x)) and (epsilon_equal(self.y, other.y)))

# Add equality into the Circle class


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        return (epsilon_equal(self.center, other.center)) and (epsilon_equal(self.radius, other.radius))
