from enum import Enum
import math
import string


class ThermalConductivityUnits(Enum):
        """
            ThermalConductivityUnits enumeration
        """
        
        WattPerMeterKelvin = 'watt_per_meter_kelvin'
        """
            
        """
        
        BtuPerHourFootFahrenheit = 'btu_per_hour_foot_fahrenheit'
        """
            
        """
        

class ThermalConductivity:
    """
    Thermal conductivity is the property of a material to conduct heat.

    Args:
        value (float): The value.
        from_unit (ThermalConductivityUnits): The ThermalConductivity unit to create from, The default unit is WattPerMeterKelvin
    """
    def __init__(self, value: float, from_unit: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_meter_kelvin = None
        
        self.__btus_per_hour_foot_fahrenheit = None
        

    def __convert_from_base(self, from_unit: ThermalConductivityUnits) -> float:
        value = self.__value
        
        if from_unit == ThermalConductivityUnits.WattPerMeterKelvin:
            return (value)
        
        if from_unit == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return (value / 1.73073467)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ThermalConductivityUnits) -> float:
        
        if to_unit == ThermalConductivityUnits.WattPerMeterKelvin:
            return (value)
        
        if to_unit == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return (value * 1.73073467)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_watts_per_meter_kelvin(watts_per_meter_kelvin: float):
        """
        Create a new instance of ThermalConductivity from a value in watts_per_meter_kelvin.

        

        :param meters: The ThermalConductivity value in watts_per_meter_kelvin.
        :type watts_per_meter_kelvin: float
        :return: A new instance of ThermalConductivity.
        :rtype: ThermalConductivity
        """
        return ThermalConductivity(watts_per_meter_kelvin, ThermalConductivityUnits.WattPerMeterKelvin)

    
    @staticmethod
    def from_btus_per_hour_foot_fahrenheit(btus_per_hour_foot_fahrenheit: float):
        """
        Create a new instance of ThermalConductivity from a value in btus_per_hour_foot_fahrenheit.

        

        :param meters: The ThermalConductivity value in btus_per_hour_foot_fahrenheit.
        :type btus_per_hour_foot_fahrenheit: float
        :return: A new instance of ThermalConductivity.
        :rtype: ThermalConductivity
        """
        return ThermalConductivity(btus_per_hour_foot_fahrenheit, ThermalConductivityUnits.BtuPerHourFootFahrenheit)

    
    @property
    def watts_per_meter_kelvin(self) -> float:
        """
        
        """
        if self.__watts_per_meter_kelvin != None:
            return self.__watts_per_meter_kelvin
        self.__watts_per_meter_kelvin = self.__convert_from_base(ThermalConductivityUnits.WattPerMeterKelvin)
        return self.__watts_per_meter_kelvin

    
    @property
    def btus_per_hour_foot_fahrenheit(self) -> float:
        """
        
        """
        if self.__btus_per_hour_foot_fahrenheit != None:
            return self.__btus_per_hour_foot_fahrenheit
        self.__btus_per_hour_foot_fahrenheit = self.__convert_from_base(ThermalConductivityUnits.BtuPerHourFootFahrenheit)
        return self.__btus_per_hour_foot_fahrenheit

    
    def to_string(self, unit: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin) -> string:
        """
        Format the ThermalConductivity to string.
        Note! the default format for ThermalConductivity is WattPerMeterKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ThermalConductivityUnits.WattPerMeterKelvin:
            return f"""{self.watts_per_meter_kelvin} W/m·K"""
        
        if unit == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return f"""{self.btus_per_hour_foot_fahrenheit} BTU/h·ft·°F"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin) -> string:
        """
        Get ThermalConductivity unit abbreviation.
        Note! the default abbreviation for ThermalConductivity is WattPerMeterKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ThermalConductivityUnits.WattPerMeterKelvin:
            return """W/m·K"""
        
        if unit_abbreviation == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return """BTU/h·ft·°F"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for +: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return ThermalConductivity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for *: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return ThermalConductivity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for -: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return ThermalConductivity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for /: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return ThermalConductivity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for %: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return ThermalConductivity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for **: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return ThermalConductivity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for ==: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for <: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for >: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for <=: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ThermalConductivity):
            raise TypeError("unsupported operand type(s) for >=: 'ThermalConductivity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value