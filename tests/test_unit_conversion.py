import unittest
from unitsnet_py import Angle


class TestUnitConversion(unittest.TestCase):
    def test_convert_from_base_to_other_unit(self):
        angle = Angle.from_degrees(180)
        self.assertEqual(angle.radians, 3.141592653589793)

    def test_convert_base_to_prefix_unit(self):
        angle = Angle.from_degrees(180)
        self.assertEqual(angle.microdegrees, 180000000)

    def test_convert_base_to_other_unit_prefix_unit(self):
        angle = Angle.from_degrees(180)
        self.assertEqual(angle.microradians, 3141592.6535897935)

    def test_convert_unit_to_base(self):
        angle = Angle.from_radians(3.141592653589793)
        self.assertAlmostEqual(angle.degrees, 180, delta=0.00001)

    def test_convert_base_prefix_to_base(self):
        angle = Angle.from_microdegrees(180000000)
        self.assertEqual(angle.degrees, 180)

    def test_convert_unit_prefix_to_base(self):
        angle = Angle.from_microradians(3141592.65358979)
        self.assertAlmostEqual(angle.degrees, 180, delta=0.00001)


if __name__ == "__main__":
    unittest.main()
