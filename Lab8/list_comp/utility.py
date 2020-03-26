# LAB8
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

# Purpose: to check to the 5th place after decimal for equality
# float,float->bool


def epsilon_equal(n, m, epsilon=0.00001):
    return (n - epsilon) < m and (n + epsilon > m)
