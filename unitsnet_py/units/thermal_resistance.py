from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ThermalResistanceUnits(Enum):
        """
            ThermalResistanceUnits enumeration
        """
        
        SquareMeterKelvinPerKilowatt = 'SquareMeterKelvinPerKilowatt'
        """
            
        """
        
        SquareMeterKelvinPerWatt = 'SquareMeterKelvinPerWatt'
        """
            
        """
        
        SquareMeterDegreeCelsiusPerWatt = 'SquareMeterDegreeCelsiusPerWatt'
        """
            
        """
        
        SquareCentimeterKelvinPerWatt = 'SquareCentimeterKelvinPerWatt'
        """
            
        """
        
        SquareCentimeterHourDegreeCelsiusPerKilocalorie = 'SquareCentimeterHourDegreeCelsiusPerKilocalorie'
        """
            
        """
        
        HourSquareFeetDegreeFahrenheitPerBtu = 'HourSquareFeetDegreeFahrenheitPerBtu'
        """
            
        """
        

class ThermalResistanceDto:
    """
    A DTO representation of a ThermalResistance

    Attributes:
        value (float): The value of the ThermalResistance.
        unit (ThermalResistanceUnits): The specific unit that the ThermalResistance value is representing.
    """

    def __init__(self, value: float, unit: ThermalResistanceUnits):
        """
        Create a new DTO representation of a ThermalResistance

        Parameters:
            value (float): The value of the ThermalResistance.
            unit (ThermalResistanceUnits): The specific unit that the ThermalResistance value is representing.
        """
        self.value: float = value
        """
        The value of the ThermalResistance
        """
        self.unit: ThermalResistanceUnits = unit
        """
        The specific unit that the ThermalResistance value is representing
        """

    def to_json(self):
        """
        Get a ThermalResistance DTO JSON object representing the current unit.

        :return: JSON object represents ThermalResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ThermalResistance DTO from a json representation.

        :param data: The ThermalResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        :return: A new instance of ThermalResistanceDto.
        :rtype: ThermalResistanceDto
        """
        return ThermalResistanceDto(value=data["value"], unit=ThermalResistanceUnits(data["unit"]))


class ThermalResistance(AbstractMeasure):
    """
    Heat Transfer Coefficient or Thermal conductivity - indicates a materials ability to conduct heat.

    Args:
        value (float): The value.
        from_unit (ThermalResistanceUnits): The ThermalResistance unit to create from, The default unit is SquareMeterKelvinPerKilowatt
    """
    def __init__(self, value: float, from_unit: ThermalResistanceUnits = ThermalResistanceUnits.SquareMeterKelvinPerKilowatt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__square_meter_kelvins_per_kilowatt = None
        
        self.__square_meter_kelvins_per_watt = None
        
        self.__square_meter_degrees_celsius_per_watt = None
        
        self.__square_centimeter_kelvins_per_watt = None
        
        self.__square_centimeter_hour_degrees_celsius_per_kilocalorie = None
        
        self.__hour_square_feet_degrees_fahrenheit_per_btu = None
        

    def convert(self, unit: ThermalResistanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ThermalResistanceUnits = ThermalResistanceUnits.SquareMeterKelvinPerKilowatt) -> ThermalResistanceDto:
        """
        Get a new instance of ThermalResistance DTO representing the current unit.

        :param hold_in_unit: The specific ThermalResistance unit to store the ThermalResistance value in the DTO representation.
        :type hold_in_unit: ThermalResistanceUnits
        :return: A new instance of ThermalResistanceDto.
        :rtype: ThermalResistanceDto
        """
        return ThermalResistanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ThermalResistanceUnits = ThermalResistanceUnits.SquareMeterKelvinPerKilowatt):
        """
        Get a ThermalResistance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ThermalResistance unit to store the ThermalResistance value in the DTO representation.
        :type hold_in_unit: ThermalResistanceUnits
        :return: JSON object represents ThermalResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(thermal_resistance_dto: ThermalResistanceDto):
        """
        Obtain a new instance of ThermalResistance from a DTO unit object.

        :param thermal_resistance_dto: The ThermalResistance DTO representation.
        :type thermal_resistance_dto: ThermalResistanceDto
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(thermal_resistance_dto.value, thermal_resistance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ThermalResistance from a DTO unit json representation.

        :param data: The ThermalResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterKelvinPerKilowatt"}
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance.from_dto(ThermalResistanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ThermalResistanceUnits) -> float:
        value = self._value
        
        if from_unit == ThermalResistanceUnits.SquareMeterKelvinPerKilowatt:
            return (value)
        
        if from_unit == ThermalResistanceUnits.SquareMeterKelvinPerWatt:
            return (value / 1000)
        
        if from_unit == ThermalResistanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return (value / 1000.0)
        
        if from_unit == ThermalResistanceUnits.SquareCentimeterKelvinPerWatt:
            return (value / 0.1)
        
        if from_unit == ThermalResistanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return (value / 0.0859779507590433)
        
        if from_unit == ThermalResistanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return (value / 176.1121482159839)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ThermalResistanceUnits) -> float:
        
        if to_unit == ThermalResistanceUnits.SquareMeterKelvinPerKilowatt:
            return (value)
        
        if to_unit == ThermalResistanceUnits.SquareMeterKelvinPerWatt:
            return (value * 1000)
        
        if to_unit == ThermalResistanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return (value * 1000.0)
        
        if to_unit == ThermalResistanceUnits.SquareCentimeterKelvinPerWatt:
            return (value * 0.1)
        
        if to_unit == ThermalResistanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return (value * 0.0859779507590433)
        
        if to_unit == ThermalResistanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return (value * 176.1121482159839)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_square_meter_kelvins_per_kilowatt(square_meter_kelvins_per_kilowatt: float):
        """
        Create a new instance of ThermalResistance from a value in square_meter_kelvins_per_kilowatt.

        

        :param meters: The ThermalResistance value in square_meter_kelvins_per_kilowatt.
        :type square_meter_kelvins_per_kilowatt: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(square_meter_kelvins_per_kilowatt, ThermalResistanceUnits.SquareMeterKelvinPerKilowatt)

    
    @staticmethod
    def from_square_meter_kelvins_per_watt(square_meter_kelvins_per_watt: float):
        """
        Create a new instance of ThermalResistance from a value in square_meter_kelvins_per_watt.

        

        :param meters: The ThermalResistance value in square_meter_kelvins_per_watt.
        :type square_meter_kelvins_per_watt: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(square_meter_kelvins_per_watt, ThermalResistanceUnits.SquareMeterKelvinPerWatt)

    
    @staticmethod
    def from_square_meter_degrees_celsius_per_watt(square_meter_degrees_celsius_per_watt: float):
        """
        Create a new instance of ThermalResistance from a value in square_meter_degrees_celsius_per_watt.

        

        :param meters: The ThermalResistance value in square_meter_degrees_celsius_per_watt.
        :type square_meter_degrees_celsius_per_watt: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(square_meter_degrees_celsius_per_watt, ThermalResistanceUnits.SquareMeterDegreeCelsiusPerWatt)

    
    @staticmethod
    def from_square_centimeter_kelvins_per_watt(square_centimeter_kelvins_per_watt: float):
        """
        Create a new instance of ThermalResistance from a value in square_centimeter_kelvins_per_watt.

        

        :param meters: The ThermalResistance value in square_centimeter_kelvins_per_watt.
        :type square_centimeter_kelvins_per_watt: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(square_centimeter_kelvins_per_watt, ThermalResistanceUnits.SquareCentimeterKelvinPerWatt)

    
    @staticmethod
    def from_square_centimeter_hour_degrees_celsius_per_kilocalorie(square_centimeter_hour_degrees_celsius_per_kilocalorie: float):
        """
        Create a new instance of ThermalResistance from a value in square_centimeter_hour_degrees_celsius_per_kilocalorie.

        

        :param meters: The ThermalResistance value in square_centimeter_hour_degrees_celsius_per_kilocalorie.
        :type square_centimeter_hour_degrees_celsius_per_kilocalorie: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(square_centimeter_hour_degrees_celsius_per_kilocalorie, ThermalResistanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie)

    
    @staticmethod
    def from_hour_square_feet_degrees_fahrenheit_per_btu(hour_square_feet_degrees_fahrenheit_per_btu: float):
        """
        Create a new instance of ThermalResistance from a value in hour_square_feet_degrees_fahrenheit_per_btu.

        

        :param meters: The ThermalResistance value in hour_square_feet_degrees_fahrenheit_per_btu.
        :type hour_square_feet_degrees_fahrenheit_per_btu: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(hour_square_feet_degrees_fahrenheit_per_btu, ThermalResistanceUnits.HourSquareFeetDegreeFahrenheitPerBtu)

    
    @property
    def square_meter_kelvins_per_kilowatt(self) -> float:
        """
        
        """
        if self.__square_meter_kelvins_per_kilowatt != None:
            return self.__square_meter_kelvins_per_kilowatt
        self.__square_meter_kelvins_per_kilowatt = self.__convert_from_base(ThermalResistanceUnits.SquareMeterKelvinPerKilowatt)
        return self.__square_meter_kelvins_per_kilowatt

    
    @property
    def square_meter_kelvins_per_watt(self) -> float:
        """
        
        """
        if self.__square_meter_kelvins_per_watt != None:
            return self.__square_meter_kelvins_per_watt
        self.__square_meter_kelvins_per_watt = self.__convert_from_base(ThermalResistanceUnits.SquareMeterKelvinPerWatt)
        return self.__square_meter_kelvins_per_watt

    
    @property
    def square_meter_degrees_celsius_per_watt(self) -> float:
        """
        
        """
        if self.__square_meter_degrees_celsius_per_watt != None:
            return self.__square_meter_degrees_celsius_per_watt
        self.__square_meter_degrees_celsius_per_watt = self.__convert_from_base(ThermalResistanceUnits.SquareMeterDegreeCelsiusPerWatt)
        return self.__square_meter_degrees_celsius_per_watt

    
    @property
    def square_centimeter_kelvins_per_watt(self) -> float:
        """
        
        """
        if self.__square_centimeter_kelvins_per_watt != None:
            return self.__square_centimeter_kelvins_per_watt
        self.__square_centimeter_kelvins_per_watt = self.__convert_from_base(ThermalResistanceUnits.SquareCentimeterKelvinPerWatt)
        return self.__square_centimeter_kelvins_per_watt

    
    @property
    def square_centimeter_hour_degrees_celsius_per_kilocalorie(self) -> float:
        """
        
        """
        if self.__square_centimeter_hour_degrees_celsius_per_kilocalorie != None:
            return self.__square_centimeter_hour_degrees_celsius_per_kilocalorie
        self.__square_centimeter_hour_degrees_celsius_per_kilocalorie = self.__convert_from_base(ThermalResistanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie)
        return self.__square_centimeter_hour_degrees_celsius_per_kilocalorie

    
    @property
    def hour_square_feet_degrees_fahrenheit_per_btu(self) -> float:
        """
        
        """
        if self.__hour_square_feet_degrees_fahrenheit_per_btu != None:
            return self.__hour_square_feet_degrees_fahrenheit_per_btu
        self.__hour_square_feet_degrees_fahrenheit_per_btu = self.__convert_from_base(ThermalResistanceUnits.HourSquareFeetDegreeFahrenheitPerBtu)
        return self.__hour_square_feet_degrees_fahrenheit_per_btu

    
    def to_string(self, unit: ThermalResistanceUnits = ThermalResistanceUnits.SquareMeterKelvinPerKilowatt, fractional_digits: int = None) -> str:
        """
        Format the ThermalResistance to a string.
        
        Note: the default format for ThermalResistance is SquareMeterKelvinPerKilowatt.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ThermalResistance. Default is 'SquareMeterKelvinPerKilowatt'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ThermalResistanceUnits.SquareMeterKelvinPerKilowatt:
            return f"""{super()._truncate_fraction_digits(self.square_meter_kelvins_per_kilowatt, fractional_digits)} m²K/kW"""
        
        if unit == ThermalResistanceUnits.SquareMeterKelvinPerWatt:
            return f"""{super()._truncate_fraction_digits(self.square_meter_kelvins_per_watt, fractional_digits)} m²K/W"""
        
        if unit == ThermalResistanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return f"""{super()._truncate_fraction_digits(self.square_meter_degrees_celsius_per_watt, fractional_digits)} m²°C/W"""
        
        if unit == ThermalResistanceUnits.SquareCentimeterKelvinPerWatt:
            return f"""{super()._truncate_fraction_digits(self.square_centimeter_kelvins_per_watt, fractional_digits)} cm²K/W"""
        
        if unit == ThermalResistanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return f"""{super()._truncate_fraction_digits(self.square_centimeter_hour_degrees_celsius_per_kilocalorie, fractional_digits)} cm²Hr°C/kcal"""
        
        if unit == ThermalResistanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return f"""{super()._truncate_fraction_digits(self.hour_square_feet_degrees_fahrenheit_per_btu, fractional_digits)} Hrft²°F/Btu"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ThermalResistanceUnits = ThermalResistanceUnits.SquareMeterKelvinPerKilowatt) -> str:
        """
        Get ThermalResistance unit abbreviation.
        Note! the default abbreviation for ThermalResistance is SquareMeterKelvinPerKilowatt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ThermalResistanceUnits.SquareMeterKelvinPerKilowatt:
            return """m²K/kW"""
        
        if unit_abbreviation == ThermalResistanceUnits.SquareMeterKelvinPerWatt:
            return """m²K/W"""
        
        if unit_abbreviation == ThermalResistanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return """m²°C/W"""
        
        if unit_abbreviation == ThermalResistanceUnits.SquareCentimeterKelvinPerWatt:
            return """cm²K/W"""
        
        if unit_abbreviation == ThermalResistanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return """cm²Hr°C/kcal"""
        
        if unit_abbreviation == ThermalResistanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return """Hrft²°F/Btu"""
        