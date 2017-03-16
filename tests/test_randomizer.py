from unittest import TestCase
from randomizer.randomizer import Randomizer


class TestRandomizer(TestCase):
    def test_get_random_city(self):
        city = Randomizer.get_random_city()
        self.assertIsNotNone(city)

    def test_get_random_first_name(self):
        name = Randomizer.get_random_first_name()
        self.assertIsNotNone(name)

    def test_get_random_last_name(self):
        name = Randomizer.get_random_last_name()
        self.assertIsNotNone(name)

    def test_get_random_email(self):
        fname = Randomizer.get_random_first_name()
        lname = Randomizer.get_random_last_name()
        email = Randomizer.get_random_email(fname, lname)
        self.assertIsNotNone(email)

    def test_get_random_string(self):
        str = Randomizer.get_random_string(20)
        self.assertIsNotNone(str)

    def test_get_random_phrase(self):
        str = Randomizer.get_random_phrase(12)
        self.assertIsNotNone(str)

    def test_get_random_int(self):
        min = 1
        max = 100
        num = Randomizer.get_random_int(min, max)
        self.assertIsNotNone(num)
        self.assertTrue(num >= min)
        self.assertTrue(num <= max)

    def test_get_random_float(self):
        min = 1.25
        max = 87.0124
        num = Randomizer.get_random_float(min, max)
        self.assertIsNotNone(num)
        self.assertTrue(num >= min)
        self.assertTrue(num <= max)
