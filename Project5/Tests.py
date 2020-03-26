import unittest
from list_comp import *


class TestCases(unittest.TestCase):
    def test_1(self):
        crime1 = Crime("12345", "ROBBERY")
        crime2 = Crime("12345", "ROBBERY")

        self.assertEqual(crime1 == crime2, True)
