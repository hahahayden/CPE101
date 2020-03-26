# Name: Giselle Dougan, Hayden Tam
# Teacher: S. Einikan
# CPE101
# Section: 05

from sys import *
from math import *


class Pixel:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return (self.r == other.r and
                self.g == other.g and
                self.b == other.b)

    def __repr__(self):
        return (str(self.r) + ' ' + str(self.g) + ' ' + str(self.b))

    def __str__(self):
        return ('red: , green: , blue: ' + int(self.r), int(self.g), int(self.b))

# Purpose:takes each array and splits the lines up
# Signature: str->list


def split_it_up(filename):

    list = []
    for line in filename:
        l = line.strip()
        list.append(l.split())
    return list

# Purpose:turns lists of strings into ints
# Signature: str->int


def make_a_line(lst):

    list = []
    list.append(lst[0][0])
    for val in range(1, len(lst)):
        for value in range(len(lst[val])):
            list.append(int(lst[val][value]))
    return list

# Purpose:group of three from LAB7
# Signature: list-> list


def groups_of_3(values):
    new_list = []
    for x in range(0, len(values), 3):
        new_list.append(values[x:x + 3])
    return new_list

# Purpose: makes a Pixel for Pixel class
# Signature: list-> list of Pixels


def create_pixels(lst):
    pixels = []
    for vals in range(len(lst)):
        red = lst[vals][0]
        green = lst[vals][1]
        blue = lst[vals][2]
        pixels.append(Pixel(red, green, blue))
    return pixels

# Purpose:to get rows and colums
# Signature: list, int-> list


def make_row(pixel_list, width):
    coord_pixel_list = []
    for lst in range(0, len(pixel_list), width):
        coord_pixel_list.append(pixel_list[lst:lst+width])
    return coord_pixel_list

# Purpose:to rename the file to blurred
# Signature: str-> str


def rename_file_blurred(file):
    rename = []
    for c in range(0, len(file)-4):
        rename.append(file[c])
    name = ''.join(rename) + '_blurred.ppm'
    return name

# Purpose:get the location of the pixel in the groupof3
# Signature: list int int-> list


def get_pixel_at_location(pixel_list, row, col):
    return pixel_list[row][col]

# Purpose: make table of values that go out to the reach to create a square
# Signature: list int int int int -> list


def reach_table(original_list, row, col, reach, width, length):
    reach_table = []
    start_row = row - reach
    end_row = row + reach
    start_col = col - reach
    end_col = col + reach

    if start_row < 0:
        start_row = 0
    if end_row >= length:
        end_row = length - 1
    if start_col < 0:
        start_col = 0
    if end_col >= width:
        end_col = width - 1

    for r in range(start_row, end_row + 1, 1):
        for c in range(start_col, end_col + 1, 1):
            reach_table.append(original_list[r][c])
    return reach_table

# Purpose:takes the average of one pixel and returns it
# Signature: list-> Pixel


def blur_one_pixel(reach_table):
    reach_r = 0
    reach_g = 0
    reach_b = 0
    for p in reach_table:
        reach_r += p.r
        reach_g += p.g
        reach_b += p.b
    average_r = int(reach_r / len(reach_table))
    average_g = int(reach_g / len(reach_table))
    average_b = int(reach_b / len(reach_table))
    return Pixel(average_r, average_g, average_b)

# Purpose: appends the blurred pixels together
# Signature: list int int int int int int -> list


def blur(original_list, given_row, given_col, radius, reach, width, length):
    blurred = []
    for row in range(len(original_list)):
        blur = []
        for col in range(len(original_list[row])):
            distance = distance_from_point(given_row, given_col, row, col)
            if distance <= 2*radius:
                if distance <= radius:
                    reach_table1 = reach_table(
                        original_list, row, col, reach, width, length)
                    blur_pix = blur_one_pixel(reach_table1)
                    blur.append(blur_pix)
                else:
                    new_reach = get_percent_reach(distance, radius, reach)
                    reach_table1 = reach_table(
                        original_list, row, col, new_reach, width, length)
                    blur_pix = blur_one_pixel(reach_table1)
                    blur.append(blur_pix)
            else:
                blur.append(original_list[row][col])
        blurred.append(blur)
    return blurred

# Purpose: gets the percent reach
# Signature: int int int-> int


def get_percent_reach(distance, radius, reach):
    return int((1-((distance-radius)/radius))*reach)

# Purpose:distance formula for between two points
# Signature: int int int int -> float


def distance_from_point(given_row, given_col, pix_row, pix_col):
    return sqrt(((pix_row-given_row)**2)+((pix_col-given_col)**2))

# Purpose: main function to blur an image
# str, list-> None


def blurMain(f, argv):

    row = 0
    radius = int(argv[2]) * 100
    reach = 4

    lst = split_it_up(f)

    big_list = make_a_line(lst)

    width = big_list[1]

    length = big_list[2]

    col = length

    list_pixels = groups_of_3(big_list[4:])

    pixels = create_pixels(list_pixels)

    array_2D = make_row(pixels, width)

    blurred = blur(array_2D, row, col, radius, reach, width, length)

    w = open(rename_file_blurred(argv[1]), 'w')
    w.write(str(big_list[0]) + '\n')
    w.write(str(width) + ' ' + str(length) + '\n')
    w.write(str(big_list[3]) + '\n')
    for row in range(len(blurred)):
        for pix in range(len(blurred[row])):
            w.write(str(blurred[row][pix].r) + ' ' + str(blurred[row]
                                                         [pix].g) + ' ' + str(blurred[row][pix].b) + '\n')
    w.close()
