import unittest
from unitsnet_py import (
    Angle,
    Length,
    LengthUnits,
    Information
)


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

    def test_convert_bits_prefix_to_base(self):
        data = Information.from_kibibits(1)
        self.assertAlmostEqual(data.bits, 1024)

    def test_convert_base_to_bits_prefix(self):
        data = Information.from_bits(1024)
        self.assertAlmostEqual(data.kibibits, 1)

    def test_convert_to_specific_unit_enum(self):
        param_list = [
            (LengthUnits.Meter, LengthUnits.Centimeter, 'centimeters'),
            (LengthUnits.Meter, LengthUnits.Kilometer, 'kilometers'),
            (LengthUnits.Centimeter, LengthUnits.Kilofoot, 'kilofeet'),
        ]
        for item in param_list:
            with self.subTest(item=item):
                source, target, property_name = item
                length = Length(1, source)
                self.assertEqual(
                    length.convert(target),
                    getattr(length, property_name),
                )


if __name__ == "__main__":
    unittest.main()
