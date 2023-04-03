import unittest
from unitsnet_py import Length


class TestUnitArithmetics(unittest.TestCase):
    length1 = Length.from_meters(10)
    length2 = Length.from_meters(3)

    def test_add(self):
        result = self.length1 + self.length2
        self.assertEqual(result.meters, 13)

    def test_subtract(self):
        result = self.length1 - self.length2
        self.assertEqual(result.meters, 7)

    def test_multiply(self):
        result = self.length1 * self.length2
        self.assertEqual(result.meters, 30)

    def test_divide(self):
        result = self.length1 / self.length2
        self.assertAlmostEqual(result.meters, 3.33333333333333, delta=0.000000001)

    def test_modulo(self):
        result = self.length1 % self.length2
        self.assertEqual(result.meters, 1)

    def test_power(self):
        result = self.length1**self.length2
        self.assertEqual(result.meters, 1000)


if __name__ == "__main__":
    unittest.main()
