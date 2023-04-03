import unittest
from unitsnet_py import Length, AngleUnits


class TestUnitComparing(unittest.TestCase):
    length1 = Length.from_meters(10)
    length2 = Length.from_decimeters(100)
    length3 = Length.from_meters(3)

    def test_equal(self):
        self.assertTrue(self.length1 == self.length2)

    def test_not_equal(self):
        self.assertTrue(self.length1 != self.length3)

    def test_bigger(self):
        self.assertTrue(self.length1 > self.length3)

    def test_smaller(self):
        self.assertTrue(self.length3 < self.length1)

    def test_smaller_or_equal(self):
        self.assertTrue(self.length1 <= self.length2)

    def test_bigger_or_equal(self):
        self.assertTrue(self.length1 >= self.length2)


if __name__ == "__main__":
    unittest.main()
