# LAB8
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import math
from objects import*

# Purpose: takes the distance between two points
# Point,Point->int


def distance(point1, point2):
    return math.sqrt((((point1.x-point2.x)**2)+(point1.y-point2.y)**2))

# Purpose: takes two circles and sees if it overlaps
# Circle,Circle-> bool


def circles_overLap(circle1, circle2):
    overlap = distance(circle1.center, circle2.center)

    return(overlap < (circle1.radius+circle2.radius))
