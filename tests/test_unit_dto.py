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

    def test_directly_create_json_from_unit(self):
        self.assertDictEqual(length1.to_dto_json(), {
            "value":100.01,
            "unit":"Meter"
        })

    def test_directly_create_json_from_specific_unit(self):
        self.assertDictEqual(length1.to_dto_json(LengthUnits.Centimeter), {
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

    def test_load_from_json(self):
        json = {
            "value":100.01,
            "unit":"Meter"
        }
        new_length = Length.from_dto(LengthDto.from_json(json))
        self.assertEqual(new_length.meters, 100.01) 

    def test_load_directly_from_json(self):
        json = {
            "value":100.01,
            "unit":"Meter"
        }
        new_length = Length.from_dto_json(json)
        self.assertEqual(new_length.meters, 100.01) 
    
    def test_load_directly_from_specific_unit_json(self):
        json = {
            "value":10001,
            "unit":"Centimeter"
        }
        new_length = Length.from_dto_json(json)
        self.assertEqual(new_length.meters, 100.01) 

    def test_should_be_similar_values_from_two_dto_representations(self):
        # Create a Length unit object
        length = Length.from_meters(100.01)

        # Obtain the DTO object as json, represented by the default unit - meter
        length_dto_json = length.to_dto_json() # {"value":100.01,"unit":"Meter"}

        # Obtain the same value but represent DTO in KM 
        length_dto_represents_in_km_json = length.to_dto_json(LengthUnits.Kilometer) # {'value': 0.10001, 'unit': 'Kilometer'}

        # Load JSON to DTO, and load
        length_from_meters_dto = Length.from_dto_json(length_dto_json)
        # The exact same value as
        length_from_km_dto = Length.from_dto_json(length_dto_represents_in_km_json)

        self.assertEqual(length_from_meters_dto.meters, length_from_km_dto.meters)

        # Get a DTO instance from a Length instance
        length_dto: LengthDto = length.to_dto()
        # Get the json representation of the DTO
        length_json = length_dto.to_json() # {"value":100.01,"unit":"Meter"}
        # Obtain DTO instance from a json representation
        length_dto: LengthDto = LengthDto.from_json(length_json)
        # Obtain Length unit from a DTO instance
        length = Length.from_dto(length_dto)

        self.assertEqual(length.meters, length_from_meters_dto.meters)


if __name__ == "__main__":
    unittest.main()
