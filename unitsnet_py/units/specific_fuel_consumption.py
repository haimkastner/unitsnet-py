from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class SpecificFuelConsumptionUnits(Enum):
        """
            SpecificFuelConsumptionUnits enumeration
        """
        
        PoundMassPerPoundForceHour = 'PoundMassPerPoundForceHour'
        """
            
        """
        
        KilogramPerKilogramForceHour = 'KilogramPerKilogramForceHour'
        """
            
        """
        
        GramPerKilonewtonSecond = 'GramPerKilonewtonSecond'
        """
            
        """
        
        KilogramPerKilonewtonSecond = 'KilogramPerKilonewtonSecond'
        """
            
        """
        

class SpecificFuelConsumptionDto:
    """
    A DTO representation of a SpecificFuelConsumption

    Attributes:
        value (float): The value of the SpecificFuelConsumption.
        unit (SpecificFuelConsumptionUnits): The specific unit that the SpecificFuelConsumption value is representing.
    """

    def __init__(self, value: float, unit: SpecificFuelConsumptionUnits):
        """
        Create a new DTO representation of a SpecificFuelConsumption

        Parameters:
            value (float): The value of the SpecificFuelConsumption.
            unit (SpecificFuelConsumptionUnits): The specific unit that the SpecificFuelConsumption value is representing.
        """
        self.value: float = value
        """
        The value of the SpecificFuelConsumption
        """
        self.unit: SpecificFuelConsumptionUnits = unit
        """
        The specific unit that the SpecificFuelConsumption value is representing
        """

    def to_json(self):
        """
        Get a SpecificFuelConsumption DTO JSON object representing the current unit.

        :return: JSON object represents SpecificFuelConsumption DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "GramPerKilonewtonSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of SpecificFuelConsumption DTO from a json representation.

        :param data: The SpecificFuelConsumption DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "GramPerKilonewtonSecond"}
        :return: A new instance of SpecificFuelConsumptionDto.
        :rtype: SpecificFuelConsumptionDto
        """
        return SpecificFuelConsumptionDto(value=data["value"], unit=SpecificFuelConsumptionUnits(data["unit"]))


class SpecificFuelConsumption(AbstractMeasure):
    """
    SFC is the fuel efficiency of an engine design with respect to thrust output

    Args:
        value (float): The value.
        from_unit (SpecificFuelConsumptionUnits): The SpecificFuelConsumption unit to create from, The default unit is GramPerKilonewtonSecond
    """
    def __init__(self, value: float, from_unit: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKilonewtonSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__pounds_mass_per_pound_force_hour = None
        
        self.__kilograms_per_kilogram_force_hour = None
        
        self.__grams_per_kilonewton_second = None
        
        self.__kilograms_per_kilonewton_second = None
        

    def convert(self, unit: SpecificFuelConsumptionUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKilonewtonSecond) -> SpecificFuelConsumptionDto:
        """
        Get a new instance of SpecificFuelConsumption DTO representing the current unit.

        :param hold_in_unit: The specific SpecificFuelConsumption unit to store the SpecificFuelConsumption value in the DTO representation.
        :type hold_in_unit: SpecificFuelConsumptionUnits
        :return: A new instance of SpecificFuelConsumptionDto.
        :rtype: SpecificFuelConsumptionDto
        """
        return SpecificFuelConsumptionDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKilonewtonSecond):
        """
        Get a SpecificFuelConsumption DTO JSON object representing the current unit.

        :param hold_in_unit: The specific SpecificFuelConsumption unit to store the SpecificFuelConsumption value in the DTO representation.
        :type hold_in_unit: SpecificFuelConsumptionUnits
        :return: JSON object represents SpecificFuelConsumption DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "GramPerKilonewtonSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(specific_fuel_consumption_dto: SpecificFuelConsumptionDto):
        """
        Obtain a new instance of SpecificFuelConsumption from a DTO unit object.

        :param specific_fuel_consumption_dto: The SpecificFuelConsumption DTO representation.
        :type specific_fuel_consumption_dto: SpecificFuelConsumptionDto
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(specific_fuel_consumption_dto.value, specific_fuel_consumption_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of SpecificFuelConsumption from a DTO unit json representation.

        :param data: The SpecificFuelConsumption DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "GramPerKilonewtonSecond"}
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption.from_dto(SpecificFuelConsumptionDto.from_json(data))

    def __convert_from_base(self, from_unit: SpecificFuelConsumptionUnits) -> float:
        value = self._value
        
        if from_unit == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return (value * 9.80665e-3 * 3600 / 1000)
        
        if from_unit == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return (value * 9.80665e-3 * 3600 / 1000)
        
        if from_unit == SpecificFuelConsumptionUnits.GramPerKilonewtonSecond:
            return (value)
        
        if from_unit == SpecificFuelConsumptionUnits.KilogramPerKilonewtonSecond:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpecificFuelConsumptionUnits) -> float:
        
        if to_unit == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return (value * 1000 / (9.80665e-3 * 3600))
        
        if to_unit == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return (value * 1000 / (9.80665e-3 * 3600))
        
        if to_unit == SpecificFuelConsumptionUnits.GramPerKilonewtonSecond:
            return (value)
        
        if to_unit == SpecificFuelConsumptionUnits.KilogramPerKilonewtonSecond:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_pounds_mass_per_pound_force_hour(pounds_mass_per_pound_force_hour: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in pounds_mass_per_pound_force_hour.

        

        :param meters: The SpecificFuelConsumption value in pounds_mass_per_pound_force_hour.
        :type pounds_mass_per_pound_force_hour: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(pounds_mass_per_pound_force_hour, SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour)

    
    @staticmethod
    def from_kilograms_per_kilogram_force_hour(kilograms_per_kilogram_force_hour: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in kilograms_per_kilogram_force_hour.

        

        :param meters: The SpecificFuelConsumption value in kilograms_per_kilogram_force_hour.
        :type kilograms_per_kilogram_force_hour: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(kilograms_per_kilogram_force_hour, SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour)

    
    @staticmethod
    def from_grams_per_kilonewton_second(grams_per_kilonewton_second: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in grams_per_kilonewton_second.

        

        :param meters: The SpecificFuelConsumption value in grams_per_kilonewton_second.
        :type grams_per_kilonewton_second: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(grams_per_kilonewton_second, SpecificFuelConsumptionUnits.GramPerKilonewtonSecond)

    
    @staticmethod
    def from_kilograms_per_kilonewton_second(kilograms_per_kilonewton_second: float):
        """
        Create a new instance of SpecificFuelConsumption from a value in kilograms_per_kilonewton_second.

        

        :param meters: The SpecificFuelConsumption value in kilograms_per_kilonewton_second.
        :type kilograms_per_kilonewton_second: float
        :return: A new instance of SpecificFuelConsumption.
        :rtype: SpecificFuelConsumption
        """
        return SpecificFuelConsumption(kilograms_per_kilonewton_second, SpecificFuelConsumptionUnits.KilogramPerKilonewtonSecond)

    
    @property
    def pounds_mass_per_pound_force_hour(self) -> float:
        """
        
        """
        if self.__pounds_mass_per_pound_force_hour != None:
            return self.__pounds_mass_per_pound_force_hour
        self.__pounds_mass_per_pound_force_hour = self.__convert_from_base(SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour)
        return self.__pounds_mass_per_pound_force_hour

    
    @property
    def kilograms_per_kilogram_force_hour(self) -> float:
        """
        
        """
        if self.__kilograms_per_kilogram_force_hour != None:
            return self.__kilograms_per_kilogram_force_hour
        self.__kilograms_per_kilogram_force_hour = self.__convert_from_base(SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour)
        return self.__kilograms_per_kilogram_force_hour

    
    @property
    def grams_per_kilonewton_second(self) -> float:
        """
        
        """
        if self.__grams_per_kilonewton_second != None:
            return self.__grams_per_kilonewton_second
        self.__grams_per_kilonewton_second = self.__convert_from_base(SpecificFuelConsumptionUnits.GramPerKilonewtonSecond)
        return self.__grams_per_kilonewton_second

    
    @property
    def kilograms_per_kilonewton_second(self) -> float:
        """
        
        """
        if self.__kilograms_per_kilonewton_second != None:
            return self.__kilograms_per_kilonewton_second
        self.__kilograms_per_kilonewton_second = self.__convert_from_base(SpecificFuelConsumptionUnits.KilogramPerKilonewtonSecond)
        return self.__kilograms_per_kilonewton_second

    
    def to_string(self, unit: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKilonewtonSecond, fractional_digits: int = None) -> str:
        """
        Format the SpecificFuelConsumption to a string.
        
        Note: the default format for SpecificFuelConsumption is GramPerKilonewtonSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the SpecificFuelConsumption. Default is 'GramPerKilonewtonSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return f"""{super()._truncate_fraction_digits(self.pounds_mass_per_pound_force_hour, fractional_digits)} lb/(lbf·h)"""
        
        if unit == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_kilogram_force_hour, fractional_digits)} kg/(kgf·h)"""
        
        if unit == SpecificFuelConsumptionUnits.GramPerKilonewtonSecond:
            return f"""{super()._truncate_fraction_digits(self.grams_per_kilonewton_second, fractional_digits)} g/(kN·s)"""
        
        if unit == SpecificFuelConsumptionUnits.KilogramPerKilonewtonSecond:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_kilonewton_second, fractional_digits)} kg/(kN·s)"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificFuelConsumptionUnits = SpecificFuelConsumptionUnits.GramPerKilonewtonSecond) -> str:
        """
        Get SpecificFuelConsumption unit abbreviation.
        Note! the default abbreviation for SpecificFuelConsumption is GramPerKilonewtonSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.PoundMassPerPoundForceHour:
            return """lb/(lbf·h)"""
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.KilogramPerKilogramForceHour:
            return """kg/(kgf·h)"""
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.GramPerKilonewtonSecond:
            return """g/(kN·s)"""
        
        if unit_abbreviation == SpecificFuelConsumptionUnits.KilogramPerKilonewtonSecond:
            return """kg/(kN·s)"""
        