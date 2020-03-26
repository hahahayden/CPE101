# Name: Hayden Tam
# Teacher: S. Einikan
# CPE101
# Section: 05

# Signature: list, list
# Purpose: groups a list of words into a sublist of three


def groups_of_3(listVal):
    newL = []

    for count2 in range(len(listVal)):
        if count2 % 3 == 0:
            newL.append(listVal[count2:count2+3])

    return newL
