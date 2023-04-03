import unittest
from unitsnet_py import Angle, AngleUnits


class TestUnitCreation(unittest.TestCase):
    def test_creation(self):
        angle_ctor_driven = Angle(180, AngleUnits.Degree)
        angle_from_driven = Angle.from_degrees(180)
        self.assertEqual(angle_ctor_driven.base_value, angle_from_driven.base_value)


if __name__ == "__main__":
    unittest.main()
