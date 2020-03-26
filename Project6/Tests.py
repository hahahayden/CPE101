# Project6-Test functions
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import unittest
from crimetime import *


class TestCases(unittest.TestCase):

    def test_creation(self):
        crime1 = Crime(12345, "ROBBERY")
        crime2 = Crime(12345, "ROBBERY")
        crime3 = Crime(72108, "ROBBERY")
        crime4 = Crime(72108, "ROBBERY")
        crime5 = Crime(999110, "ROBBERY")
        self.assertEqual(crime1, Crime(12345, "ROBBERY")
                         )  # Test object creation

        self.assertEqual(crime3, Crime(72108, "ROBBERY"))
        self.assertEqual(crime4, Crime(72108, "ROBBERY"))

    def test_equality(self):
        crime1 = Crime(12345, "ROBBERY")
        crime2 = Crime(12345, "ROBBERY")
        crime3 = Crime(72108, "ROBBERY")
        crime4 = Crime(72108, "ROBBERY")
        crime5 = Crime(999110, "ROBBERY")
        self.assertEqual((crime1.iD == crime2.iD), True)  # Test Obj Eq
        self.assertEqual((crime2.iD == crime3.iD), False)  # Test Obj Eq
        self.assertEqual((crime1 == crime2), True)  # Test Object Equality

    def test_repr(self):
        crime1 = Crime(12345, "ROBBERY")
        crime2 = Crime(12345, "ROBBERY")
        crime3 = Crime(72108, "ROBBERY")
        crime4 = Crime(72108, "ROBBERY")
        crime5 = Crime(999110, "ROBBERY")
        self.assertEqual((str(crime1)), ("12345,ROBBERY"))  # Test repr
        self.assertEqual((str(crime2)), ("12345,ROBBERY"))  # test repr
        self.assertEqual((str(crime4)), ("72108,ROBBERY"))

    def test_set_time(self):
        crime1 = Crime(12345, "ROBBERY")
        crime2 = Crime(12345, "ROBBERY")
        crime3 = Crime(72108, "ROBBERY")
        crime4 = Crime(72108, "ROBBERY")
        crime5 = Crime(999110, "ROBBERY")
        crime2.set_time(5, 7)
        crime1.set_time(2, 10)
        self.assertEqual(crime1.month, "February")  # Test set_time
        self.assertEqual(crime1.hour, "10AM")
        self.assertEqual(crime2.month, "May")

    def test_create_crimes(self):  # Three tests to check if Crime object is made
        crime1 = ['150027877', 'ROBBERY', 'ROBBERY ON THE STREET WITH A DANGEROUS WEAPON'], [
            '150042160', 'WEAPON LAWS', 'POSS OF FIREARM BY CONVICTED FELON/ADDICT/ALIEN']

        crimeList = ['150027877', 'ROBBERY', 'ROBBERY ON THE STREET WITH A DANGEROUS WEAPON'], [
            '150042160', 'ROBBERY', 'POSS OF FIREARM BY CONVICTED FELON/ADDICT/ALIEN']

        crimeList2 = ['150027877', 'ROBBERY', 'ROBBERY ON THE STREET WITH A DANGEROUS WEAPON'], [
            '150042160', 'ROBBERY', 'POSS OF FIREARM BY CONVICTED FELON/ADDICT/ALIEN'], ['150042160', 'WEAPON LAWS', 'POSS OF FIREARM BY CONVICTED FELON/ADDICT/ALIEN']
        self.assertEqual(create_crimes(crime1),
                         [Crime('150027877', 'ROBBERY')])
        self.assertEqual(create_crimes(crimeList),
                         [Crime('150027877', 'ROBBERY'), Crime('150042160', 'ROBBERY')])
        self.assertEqual(create_crimes(crimeList2),
                         [Crime('150027877', 'ROBBERY'), Crime('150042160', 'ROBBERY')])

    def test_sort_crimes(self):  # Three tests to check if sort_crimes sorts
        crime1 = Crime('12345', 'ROBBERY')
        crime2 = Crime('34567', 'ROBBERY')
        crime3 = Crime('45512', 'ROBBERY')

        crimeList = [crime1, crime2]
        self.assertListEqual(sort_crimes(crimeList), [Crime(
            '12345', 'ROBBERY'), Crime('34567', 'ROBBERY')])
        crimeList = [crime2, crime1]
        crimeList2 = [crime2, crime1, crime3]
        self.assertListEqual(sort_crimes(crimeList), [Crime('12345', 'ROBBERY'), Crime(
            '34567', 'ROBBERY')])
        self.assertListEqual(sort_crimes(crimeList2), [Crime('12345', 'ROBBERY'), Crime(
            '34567', 'ROBBERY'), Crime('45512', 'ROBBERY')])

    # Three tests to check if the crime is updated by reading the times.tsv file
    def test_update_crimes(self):
        crime1 = Crime('150017276', 'ROBBERY')
        lines = ["150017276\tTuesday\t01/06/2015\t16: 53\n",
                 '150144562\tMonday\t02/16/2015\t18:15\n']

        crime2 = Crime('150144562', 'ROBBERY')
        crime3 = Crime('150144565', 'ROBBERY')
        crimeList1 = [crime1]
        crimeList2 = [crime1, crime2]
        crimeList3 = [crime1, crime2, crime3]
        c = update_crimes(crimeList1, lines)

        self.assertEqual(c[0].month, "January")
        d = update_crimes(crimeList2, lines)
        e = update_crimes(crimeList3, lines)
        self.assertEqual(d[1].month, "February")
        self.assertEqual(e[1].month, "February")

    def test_find_crime(self):  # Three tests to check if crime is found
        crime1 = Crime('150017276', 'ROBBERY')
        lines = ["150017276\tTuesday\t01/06/2015\t16: 53\n",
                 '150144562\tMonday\t02/16/2015\t18:15\n',
                 '150144564\tMonday\t02/16/2015\t18:15\n']

        crime2 = Crime('150144562', 'ROBBERY')
        crimeList1 = [crime1]
        crimeList2 = [crime1, crime2]
        self.assertEqual(find_crime(crimeList1, '150017276'), (True, 0))
        self.assertEqual(find_crime(crimeList2, '150144562'), (True, 1))

        self.assertEqual(find_crime(crimeList2, '150144563'), (False, 1))

    def test_stats(self):  # Three tests to check if stat returns the right stats
        crime1 = Crime('1500017276', "Robbery")
        crime1.day_of_week = ("Monday")
        crime1.month = ("January")
        crime1.hour = "11AM"
        crimeList = [crime1]

        self.assertEqual(stats(crimeList), ("Monday", "January", "11AM"))

        crime2 = Crime('1500017276', "Robbery")
        crime2.day_of_week = ("Tuesday")
        crime2.month = ("February")
        crime2.hour = "12AM"
        crimeList = [crime2]

        self.assertEqual(stats(crimeList), ("Tuesday", "February", "12AM"))

        crime3 = Crime('1500017276', "Robbery")
        crime3.day_of_week = ("Tuesday")
        crime3.month = ("February")
        crime3.hour = "1AM"
        crimeList = [crime3]

        self.assertEqual(stats(crimeList), ("Tuesday", "February", "1AM"))


if __name__ == '__main__':
    unittest.main()
