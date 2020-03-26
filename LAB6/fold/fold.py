from functools import reduce

# Signature:list->float/int
# Purpose: return the sum of a list of numbers, including nested lists


def sum(list2):
    newL = []
    for count in list2:

        if(type(count) == list):
            for count2 in count:

                newL.append(count2)

        else:
            newL.append(count)
    print(newL)
    sum = (reduce(lambda x, y: x+y, newL))
    return sum

# Signature: list->int
# Purpose:find the position of smallest index in list


def index_of_smallest(list1):
    newL = []
    for count in list1:

        if(type(count) == list):
            for count2 in count:

                newL.append(count2)

        else:
            newL.append(count)

    count = 0
    if len(list1) <= 0:
        return -1
    else:

        small = (reduce(lambda x, y: x if x < y else y, newL))

        for index in range(len(list1)):

            if type(list1[index]) == list:
                for j in range(len(list1[index])):
                    if list1[index][j] == small:
                        return index
            else:
                if list1[index] == small:
                    return index
