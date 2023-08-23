import operator
import unittest
from unitsnet_py import Length, Mass


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


class TestComparingDifferentTypes(unittest.TestCase):
    def test_not_equal(self):
        mass = Mass.from_kilograms(10)
        length = Length.from_meters(10)
        self.assertFalse(mass == length)

    def test_operator_raises_type_error(self):
        mass = Mass.from_kilograms(1)
        length = Length.from_meters(10)
        operators = [
            operator.lt,
            operator.gt,
            operator.le,
            operator.ge,
            operator.mod,
            operator.add,
            operator.sub,
            operator.mul,
            operator.truediv,
            operator.pow,
        ]
        for op in operators:
            with self.subTest(op=op):
                with self.assertRaises(TypeError):
                    op(mass, length)


if __name__ == "__main__":
    unittest.main()
