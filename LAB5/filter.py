# Name: Hayden Tam
# Instructor: S. Einakian
# Class: CPE 101-05

# Signature: list-> list
# Purpose: takes in a list and squares all the numbers within the list


def square_all(list):
    c = [x**2 for x in list]
    return c

# Signature: int, list-> list
# Purpose: takes in a list and adds all the numbers within list by designated number


def add_n_all(n, list):
    for count in range(len(list)):

        list[count] = list[count]+n
    return list

# signature: list-> list
# Purpose: takes in a list and checks each number if it is even and odd; true for even false for odd; returns the list


def even_or_odd_all(list):
    count = 0
    while (count < (len(list))):

        if (list[count] % 2 == 0):
            list[count] = True
        else:
            list[count] = False
        count += 1
    return list while (count < (len(list))):

        if (list[count] % 2 == 0):
            list[count] = True
        else:
            list[count] = False
        count += 1
    return list
