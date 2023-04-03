import unittest
from unitsnet_py import Angle, AngleUnits


class TestUnitFormatting(unittest.TestCase):
    def test_format_base(self):
        angle = Angle.from_degrees(180)
        self.assertEqual(angle.to_string(), "180 °")

    def test_format_other_unit(self):
        angle = Angle.from_degrees(180)
        self.assertEqual(angle.to_string(AngleUnits.Degree), "180 °")
        self.assertEqual(angle.to_string(AngleUnits.Radian), "3.141592653589793 rad")


if __name__ == "__main__":
    unittest.main()
