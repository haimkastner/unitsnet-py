from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LeakRateUnits(Enum):
        """
            LeakRateUnits enumeration
        """
        
        PascalCubicMeterPerSecond = 'pascal_cubic_meter_per_second'
        """
            
        """
        
        MillibarLiterPerSecond = 'millibar_liter_per_second'
        """
            
        """
        
        TorrLiterPerSecond = 'torr_liter_per_second'
        """
            
        """
        

class LeakRate(AbstractMeasure):
    """
    A leakage rate of QL = 1 Pa-m³/s is given when the pressure in a closed, evacuated container with a volume of 1 m³ rises by 1 Pa per second or when the pressure in the container drops by 1 Pa in the event of overpressure.

    Args:
        value (float): The value.
        from_unit (LeakRateUnits): The LeakRate unit to create from, The default unit is PascalCubicMeterPerSecond
    """
    def __init__(self, value: float, from_unit: LeakRateUnits = LeakRateUnits.PascalCubicMeterPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__pascal_cubic_meters_per_second = None
        
        self.__millibar_liters_per_second = None
        
        self.__torr_liters_per_second = None
        

    def convert(self, unit: LeakRateUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: LeakRateUnits) -> float:
        value = self._value
        
        if from_unit == LeakRateUnits.PascalCubicMeterPerSecond:
            return (value)
        
        if from_unit == LeakRateUnits.MillibarLiterPerSecond:
            return (value * 10)
        
        if from_unit == LeakRateUnits.TorrLiterPerSecond:
            return (value * 7.5)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LeakRateUnits) -> float:
        
        if to_unit == LeakRateUnits.PascalCubicMeterPerSecond:
            return (value)
        
        if to_unit == LeakRateUnits.MillibarLiterPerSecond:
            return (value / 10)
        
        if to_unit == LeakRateUnits.TorrLiterPerSecond:
            return (value / 7.5)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_pascal_cubic_meters_per_second(pascal_cubic_meters_per_second: float):
        """
        Create a new instance of LeakRate from a value in pascal_cubic_meters_per_second.

        

        :param meters: The LeakRate value in pascal_cubic_meters_per_second.
        :type pascal_cubic_meters_per_second: float
        :return: A new instance of LeakRate.
        :rtype: LeakRate
        """
        return LeakRate(pascal_cubic_meters_per_second, LeakRateUnits.PascalCubicMeterPerSecond)

    
    @staticmethod
    def from_millibar_liters_per_second(millibar_liters_per_second: float):
        """
        Create a new instance of LeakRate from a value in millibar_liters_per_second.

        

        :param meters: The LeakRate value in millibar_liters_per_second.
        :type millibar_liters_per_second: float
        :return: A new instance of LeakRate.
        :rtype: LeakRate
        """
        return LeakRate(millibar_liters_per_second, LeakRateUnits.MillibarLiterPerSecond)

    
    @staticmethod
    def from_torr_liters_per_second(torr_liters_per_second: float):
        """
        Create a new instance of LeakRate from a value in torr_liters_per_second.

        

        :param meters: The LeakRate value in torr_liters_per_second.
        :type torr_liters_per_second: float
        :return: A new instance of LeakRate.
        :rtype: LeakRate
        """
        return LeakRate(torr_liters_per_second, LeakRateUnits.TorrLiterPerSecond)

    
    @property
    def pascal_cubic_meters_per_second(self) -> float:
        """
        
        """
        if self.__pascal_cubic_meters_per_second != None:
            return self.__pascal_cubic_meters_per_second
        self.__pascal_cubic_meters_per_second = self.__convert_from_base(LeakRateUnits.PascalCubicMeterPerSecond)
        return self.__pascal_cubic_meters_per_second

    
    @property
    def millibar_liters_per_second(self) -> float:
        """
        
        """
        if self.__millibar_liters_per_second != None:
            return self.__millibar_liters_per_second
        self.__millibar_liters_per_second = self.__convert_from_base(LeakRateUnits.MillibarLiterPerSecond)
        return self.__millibar_liters_per_second

    
    @property
    def torr_liters_per_second(self) -> float:
        """
        
        """
        if self.__torr_liters_per_second != None:
            return self.__torr_liters_per_second
        self.__torr_liters_per_second = self.__convert_from_base(LeakRateUnits.TorrLiterPerSecond)
        return self.__torr_liters_per_second

    
    def to_string(self, unit: LeakRateUnits = LeakRateUnits.PascalCubicMeterPerSecond) -> str:
        """
        Format the LeakRate to string.
        Note! the default format for LeakRate is PascalCubicMeterPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LeakRateUnits.PascalCubicMeterPerSecond:
            return f"""{self.pascal_cubic_meters_per_second} Pa·m³/s"""
        
        if unit == LeakRateUnits.MillibarLiterPerSecond:
            return f"""{self.millibar_liters_per_second} mbar·l/s"""
        
        if unit == LeakRateUnits.TorrLiterPerSecond:
            return f"""{self.torr_liters_per_second} Torr·l/s"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LeakRateUnits = LeakRateUnits.PascalCubicMeterPerSecond) -> str:
        """
        Get LeakRate unit abbreviation.
        Note! the default abbreviation for LeakRate is PascalCubicMeterPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LeakRateUnits.PascalCubicMeterPerSecond:
            return """Pa·m³/s"""
        
        if unit_abbreviation == LeakRateUnits.MillibarLiterPerSecond:
            return """mbar·l/s"""
        
        if unit_abbreviation == LeakRateUnits.TorrLiterPerSecond:
            return """Torr·l/s"""
        