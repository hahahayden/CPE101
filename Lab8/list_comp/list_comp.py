# LAB8-List-comprehension
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import math
from utility import *

# Initiate a point class and define equality using the epsiolon function


class Point:
    def __init__(self, x, y):
        self. x = x
        self. y = y

    def __eq__(self, other):
        return (type(self) == type(other) and(epsilon_equal(self.x, other.x)) and (epsilon_equal(self.y, other.y)))

# initiate a circle class


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# Purpose: Takes in a list and calculates the distance between it and origin for each item
# Sig: list->list


def distance_all(list1):
    list2 = []

    newL = list(map(distance, list1))

    return newL

# Purpose: Takes in a point and calculates the distance between it and the origin
# Sig: Point->int


def distance(point1):
    return math.sqrt((((point1.x)**2)+(point1.y)**2))

# Purpose: checks if the point is in the first quadrant
# Sig: list(Point object)->list (Point obj)


def are_in_first_quadrant(pointList):

    newList = list(filter(lambda x: x.x > 0 and x.y > 0, pointList))

    return newList
