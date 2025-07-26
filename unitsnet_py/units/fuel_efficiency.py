from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class FuelEfficiencyUnits(Enum):
        """
            FuelEfficiencyUnits enumeration
        """
        
        LiterPer100Kilometers = 'LiterPer100Kilometers'
        """
            
        """
        
        MilePerUsGallon = 'MilePerUsGallon'
        """
            
        """
        
        MilePerUkGallon = 'MilePerUkGallon'
        """
            
        """
        
        KilometerPerLiter = 'KilometerPerLiter'
        """
            
        """
        

class FuelEfficiencyDto:
    """
    A DTO representation of a FuelEfficiency

    Attributes:
        value (float): The value of the FuelEfficiency.
        unit (FuelEfficiencyUnits): The specific unit that the FuelEfficiency value is representing.
    """

    def __init__(self, value: float, unit: FuelEfficiencyUnits):
        """
        Create a new DTO representation of a FuelEfficiency

        Parameters:
            value (float): The value of the FuelEfficiency.
            unit (FuelEfficiencyUnits): The specific unit that the FuelEfficiency value is representing.
        """
        self.value: float = value
        """
        The value of the FuelEfficiency
        """
        self.unit: FuelEfficiencyUnits = unit
        """
        The specific unit that the FuelEfficiency value is representing
        """

    def to_json(self):
        """
        Get a FuelEfficiency DTO JSON object representing the current unit.

        :return: JSON object represents FuelEfficiency DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilometerPerLiter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of FuelEfficiency DTO from a json representation.

        :param data: The FuelEfficiency DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilometerPerLiter"}
        :return: A new instance of FuelEfficiencyDto.
        :rtype: FuelEfficiencyDto
        """
        return FuelEfficiencyDto(value=data["value"], unit=FuelEfficiencyUnits(data["unit"]))


class FuelEfficiency(AbstractMeasure):
    """
    In the context of transport, fuel economy is the energy efficiency of a particular vehicle, given as a ratio of distance traveled per unit of fuel consumed. In most countries, using the metric system, fuel economy is stated as "fuel consumption" in liters per 100 kilometers (L/100 km) or kilometers per liter (km/L or kmpl). In countries using non-metric system, fuel economy is expressed in miles per gallon (mpg) (imperial galon or US galon).

    Args:
        value (float): The value.
        from_unit (FuelEfficiencyUnits): The FuelEfficiency unit to create from, The default unit is KilometerPerLiter
    """
    def __init__(self, value: float, from_unit: FuelEfficiencyUnits = FuelEfficiencyUnits.KilometerPerLiter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__liters_per100_kilometers = None
        
        self.__miles_per_us_gallon = None
        
        self.__miles_per_uk_gallon = None
        
        self.__kilometers_per_liter = None
        

    def convert(self, unit: FuelEfficiencyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: FuelEfficiencyUnits = FuelEfficiencyUnits.KilometerPerLiter) -> FuelEfficiencyDto:
        """
        Get a new instance of FuelEfficiency DTO representing the current unit.

        :param hold_in_unit: The specific FuelEfficiency unit to store the FuelEfficiency value in the DTO representation.
        :type hold_in_unit: FuelEfficiencyUnits
        :return: A new instance of FuelEfficiencyDto.
        :rtype: FuelEfficiencyDto
        """
        return FuelEfficiencyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: FuelEfficiencyUnits = FuelEfficiencyUnits.KilometerPerLiter):
        """
        Get a FuelEfficiency DTO JSON object representing the current unit.

        :param hold_in_unit: The specific FuelEfficiency unit to store the FuelEfficiency value in the DTO representation.
        :type hold_in_unit: FuelEfficiencyUnits
        :return: JSON object represents FuelEfficiency DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilometerPerLiter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(fuel_efficiency_dto: FuelEfficiencyDto):
        """
        Obtain a new instance of FuelEfficiency from a DTO unit object.

        :param fuel_efficiency_dto: The FuelEfficiency DTO representation.
        :type fuel_efficiency_dto: FuelEfficiencyDto
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(fuel_efficiency_dto.value, fuel_efficiency_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of FuelEfficiency from a DTO unit json representation.

        :param data: The FuelEfficiency DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilometerPerLiter"}
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency.from_dto(FuelEfficiencyDto.from_json(data))

    def __convert_from_base(self, from_unit: FuelEfficiencyUnits) -> float:
        value = self._value
        
        if from_unit == FuelEfficiencyUnits.LiterPer100Kilometers:
            return (100 / value)
        
        if from_unit == FuelEfficiencyUnits.MilePerUsGallon:
            return (value * 3.785411784 / 1.609344)
        
        if from_unit == FuelEfficiencyUnits.MilePerUkGallon:
            return (value * 4.54609 / 1.609344)
        
        if from_unit == FuelEfficiencyUnits.KilometerPerLiter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: FuelEfficiencyUnits) -> float:
        
        if to_unit == FuelEfficiencyUnits.LiterPer100Kilometers:
            return (100 / value)
        
        if to_unit == FuelEfficiencyUnits.MilePerUsGallon:
            return (value * 1.609344 / 3.785411784)
        
        if to_unit == FuelEfficiencyUnits.MilePerUkGallon:
            return (value * 1.609344 / 4.54609)
        
        if to_unit == FuelEfficiencyUnits.KilometerPerLiter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_liters_per100_kilometers(liters_per100_kilometers: float):
        """
        Create a new instance of FuelEfficiency from a value in liters_per100_kilometers.

        

        :param meters: The FuelEfficiency value in liters_per100_kilometers.
        :type liters_per100_kilometers: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(liters_per100_kilometers, FuelEfficiencyUnits.LiterPer100Kilometers)

    
    @staticmethod
    def from_miles_per_us_gallon(miles_per_us_gallon: float):
        """
        Create a new instance of FuelEfficiency from a value in miles_per_us_gallon.

        

        :param meters: The FuelEfficiency value in miles_per_us_gallon.
        :type miles_per_us_gallon: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(miles_per_us_gallon, FuelEfficiencyUnits.MilePerUsGallon)

    
    @staticmethod
    def from_miles_per_uk_gallon(miles_per_uk_gallon: float):
        """
        Create a new instance of FuelEfficiency from a value in miles_per_uk_gallon.

        

        :param meters: The FuelEfficiency value in miles_per_uk_gallon.
        :type miles_per_uk_gallon: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(miles_per_uk_gallon, FuelEfficiencyUnits.MilePerUkGallon)

    
    @staticmethod
    def from_kilometers_per_liter(kilometers_per_liter: float):
        """
        Create a new instance of FuelEfficiency from a value in kilometers_per_liter.

        

        :param meters: The FuelEfficiency value in kilometers_per_liter.
        :type kilometers_per_liter: float
        :return: A new instance of FuelEfficiency.
        :rtype: FuelEfficiency
        """
        return FuelEfficiency(kilometers_per_liter, FuelEfficiencyUnits.KilometerPerLiter)

    
    @property
    def liters_per100_kilometers(self) -> float:
        """
        
        """
        if self.__liters_per100_kilometers != None:
            return self.__liters_per100_kilometers
        self.__liters_per100_kilometers = self.__convert_from_base(FuelEfficiencyUnits.LiterPer100Kilometers)
        return self.__liters_per100_kilometers

    
    @property
    def miles_per_us_gallon(self) -> float:
        """
        
        """
        if self.__miles_per_us_gallon != None:
            return self.__miles_per_us_gallon
        self.__miles_per_us_gallon = self.__convert_from_base(FuelEfficiencyUnits.MilePerUsGallon)
        return self.__miles_per_us_gallon

    
    @property
    def miles_per_uk_gallon(self) -> float:
        """
        
        """
        if self.__miles_per_uk_gallon != None:
            return self.__miles_per_uk_gallon
        self.__miles_per_uk_gallon = self.__convert_from_base(FuelEfficiencyUnits.MilePerUkGallon)
        return self.__miles_per_uk_gallon

    
    @property
    def kilometers_per_liter(self) -> float:
        """
        
        """
        if self.__kilometers_per_liter != None:
            return self.__kilometers_per_liter
        self.__kilometers_per_liter = self.__convert_from_base(FuelEfficiencyUnits.KilometerPerLiter)
        return self.__kilometers_per_liter

    
    def to_string(self, unit: FuelEfficiencyUnits = FuelEfficiencyUnits.KilometerPerLiter, fractional_digits: int = None) -> str:
        """
        Format the FuelEfficiency to a string.
        
        Note: the default format for FuelEfficiency is KilometerPerLiter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the FuelEfficiency. Default is 'KilometerPerLiter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == FuelEfficiencyUnits.LiterPer100Kilometers:
            return f"""{super()._truncate_fraction_digits(self.liters_per100_kilometers, fractional_digits)} l/100km"""
        
        if unit == FuelEfficiencyUnits.MilePerUsGallon:
            return f"""{super()._truncate_fraction_digits(self.miles_per_us_gallon, fractional_digits)} mpg (U.S.)"""
        
        if unit == FuelEfficiencyUnits.MilePerUkGallon:
            return f"""{super()._truncate_fraction_digits(self.miles_per_uk_gallon, fractional_digits)} mpg (imp.)"""
        
        if unit == FuelEfficiencyUnits.KilometerPerLiter:
            return f"""{super()._truncate_fraction_digits(self.kilometers_per_liter, fractional_digits)} km/l"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: FuelEfficiencyUnits = FuelEfficiencyUnits.KilometerPerLiter) -> str:
        """
        Get FuelEfficiency unit abbreviation.
        Note! the default abbreviation for FuelEfficiency is KilometerPerLiter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == FuelEfficiencyUnits.LiterPer100Kilometers:
            return """l/100km"""
        
        if unit_abbreviation == FuelEfficiencyUnits.MilePerUsGallon:
            return """mpg (U.S.)"""
        
        if unit_abbreviation == FuelEfficiencyUnits.MilePerUkGallon:
            return """mpg (imp.)"""
        
        if unit_abbreviation == FuelEfficiencyUnits.KilometerPerLiter:
            return """km/l"""
        