import unittest
from unitsnet_py import Length, LengthUnits, LengthDto

length1 = Length.from_meters(100.01)

class TestUnitDto(unittest.TestCase):
    def test_create_json_from_default_unit(self):
        self.assertDictEqual(length1.to_dto().to_json(), {
            "value":100.01,
            "unit":"Meter"
        })
   

    def test_create_json_from_specific_unit(self):
        self.assertDictEqual(length1.to_dto(LengthUnits.Centimeter).to_json(), {
            "value":10001,
            "unit":"Centimeter"
        })


    def test_create_dto_from_default_unit(self):
        dto = length1.to_dto()
        self.assertEqual(dto.value, 100.01)
        self.assertEqual(dto.unit, LengthUnits.Meter)


    def test_create_dto_from_specific_unit(self):
        dto = length1.to_dto(LengthUnits.Centimeter)
        self.assertEqual(dto.value, 10001)
        self.assertEqual(dto.unit, LengthUnits.Centimeter)


    def test_load_from_default_unit_json(self):
        json_dto = length1.to_dto().to_json()
        new_length = Length.from_dto(LengthDto.from_json(json_dto))
        self.assertEqual(new_length.meters, 100.01) 


    def test_load_from_specific_unit_json(self):
        json_dto = length1.to_dto(LengthUnits.Centimeter).to_json()
        new_length = Length.from_dto(LengthDto.from_json(json_dto))
        self.assertEqual(new_length.decimeters, 1000.1) 


    def test_load_from_default_unit_dto(self):
        dto = length1.to_dto()
        new_length = Length.from_dto(dto)
        self.assertEqual(new_length.meters, 100.01) 


    def test_load_from_specific_unit_dto(self):
        dto = length1.to_dto(LengthUnits.Centimeter)
        new_length = Length.from_dto(dto)
        self.assertEqual(new_length.decimeters, 1000.1)


if __name__ == "__main__":
    unittest.main()
