from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ThermalResistanceUnits(Enum):
        """
            ThermalResistanceUnits enumeration
        """
        
        SquareMeterKelvinPerKilowatt = 'square_meter_kelvin_per_kilowatt'
        """
            
        """
        
        SquareMeterKelvinPerWatt = 'square_meter_kelvin_per_watt'
        """
            
        """
        
        SquareMeterDegreeCelsiusPerWatt = 'square_meter_degree_celsius_per_watt'
        """
            
        """
        
        SquareCentimeterKelvinPerWatt = 'square_centimeter_kelvin_per_watt'
        """
            
        """
        
        SquareCentimeterHourDegreeCelsiusPerKilocalorie = 'square_centimeter_hour_degree_celsius_per_kilocalorie'
        """
            
        """
        
        HourSquareFeetDegreeFahrenheitPerBtu = 'hour_square_feet_degree_fahrenheit_per_btu'
        """
            
        """
        

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

    
    def to_string(self, unit: ThermalResistanceUnits = ThermalResistanceUnits.SquareMeterKelvinPerKilowatt) -> str:
        """
        Format the ThermalResistance to string.
        Note! the default format for ThermalResistance is SquareMeterKelvinPerKilowatt.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ThermalResistanceUnits.SquareMeterKelvinPerKilowatt:
            return f"""{self.square_meter_kelvins_per_kilowatt} m²K/kW"""
        
        if unit == ThermalResistanceUnits.SquareMeterKelvinPerWatt:
            return f"""{self.square_meter_kelvins_per_watt} m²K/W"""
        
        if unit == ThermalResistanceUnits.SquareMeterDegreeCelsiusPerWatt:
            return f"""{self.square_meter_degrees_celsius_per_watt} m²°C/W"""
        
        if unit == ThermalResistanceUnits.SquareCentimeterKelvinPerWatt:
            return f"""{self.square_centimeter_kelvins_per_watt} cm²K/W"""
        
        if unit == ThermalResistanceUnits.SquareCentimeterHourDegreeCelsiusPerKilocalorie:
            return f"""{self.square_centimeter_hour_degrees_celsius_per_kilocalorie} cm²Hr°C/kcal"""
        
        if unit == ThermalResistanceUnits.HourSquareFeetDegreeFahrenheitPerBtu:
            return f"""{self.hour_square_feet_degrees_fahrenheit_per_btu} Hrft²°F/Btu"""
        
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
        