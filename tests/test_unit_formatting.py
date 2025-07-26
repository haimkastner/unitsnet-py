import unittest
from unitsnet_py import Angle, AngleUnits


class TestUnitFormatting(unittest.TestCase):
    def test_format_base(self):
        angle = Angle.from_degrees(180)
        self.assertEqual(angle.to_string(), "3.141592653589793 rad")

    def test_format_other_unit(self):
        angle = Angle.from_degrees(180)
        self.assertEqual(angle.to_string(AngleUnits.Degree, 0), "180 °")
        self.assertEqual(angle.to_string(AngleUnits.Radian), "3.141592653589793 rad")
        self.assertEqual(angle.to_string(AngleUnits.Milliradian), "3141.592653589793 mrad")

    def test_format_with_digits_limit(self):
        angle = Angle.from_degrees(180)
        # without limit
        self.assertEqual(angle.to_string(AngleUnits.Radian), "3.141592653589793 rad")
        # with limit no zero
        self.assertEqual(angle.to_string(AngleUnits.Radian, 0), "3 rad")
        # with limit to one
        self.assertEqual(angle.to_string(AngleUnits.Radian, 1), "3.1 rad")
        # with limit to 2
        self.assertEqual(angle.to_string(AngleUnits.Radian, 2), "3.14 rad")
        # do nothing if nothing to truncate
        self.assertEqual(angle.to_string(AngleUnits.Degree, 2), "180 °")
        # do nothing if it's longer than the fraction digits
        self.assertEqual(angle.to_string(AngleUnits.Radian, 20), "3.141592653589793 rad")

if __name__ == "__main__":
    unittest.main()
