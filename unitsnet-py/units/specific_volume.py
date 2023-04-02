from enum import Enum
import math
import string


class SpecificVolumeUnits(Enum):
        """
            SpecificVolumeUnits enumeration
        """
        
        CubicMeterPerKilogram = 'cubic_meter_per_kilogram'
        """
            
        """
        
        CubicFootPerPound = 'cubic_foot_per_pound'
        """
            
        """
        
        MillicubicMeterPerKilogram = 'millicubic_meter_per_kilogram'
        """
            
        """
        

class SpecificVolume:
    """
    In thermodynamics, the specific volume of a substance is the ratio of the substance's volume to its mass. It is the reciprocal of density and an intrinsic property of matter as well.

    Args:
        value (float): The value.
        from_unit (SpecificVolumeUnits): The SpecificVolume unit to create from, The default unit is CubicMeterPerKilogram
    """
    def __init__(self, value: float, from_unit: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__cubic_meters_per_kilogram = None
        
        self.__cubic_feet_per_pound = None
        
        self.__millicubic_meters_per_kilogram = None
        

    def __convert_from_base(self, from_unit: SpecificVolumeUnits) -> float:
        value = self.__value
        
        if from_unit == SpecificVolumeUnits.CubicMeterPerKilogram:
            return (value)
        
        if from_unit == SpecificVolumeUnits.CubicFootPerPound:
            return (value * 16.01846353)
        
        if from_unit == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: SpecificVolumeUnits) -> float:
        
        if to_unit == SpecificVolumeUnits.CubicMeterPerKilogram:
            return (value)
        
        if to_unit == SpecificVolumeUnits.CubicFootPerPound:
            return (value / 16.01846353)
        
        if to_unit == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_cubic_meters_per_kilogram(cubic_meters_per_kilogram: float):
        """
        Create a new instance of SpecificVolume from a value in cubic_meters_per_kilogram.

        

        :param meters: The SpecificVolume value in cubic_meters_per_kilogram.
        :type cubic_meters_per_kilogram: float
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume(cubic_meters_per_kilogram, SpecificVolumeUnits.CubicMeterPerKilogram)

    
    @staticmethod
    def from_cubic_feet_per_pound(cubic_feet_per_pound: float):
        """
        Create a new instance of SpecificVolume from a value in cubic_feet_per_pound.

        

        :param meters: The SpecificVolume value in cubic_feet_per_pound.
        :type cubic_feet_per_pound: float
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume(cubic_feet_per_pound, SpecificVolumeUnits.CubicFootPerPound)

    
    @staticmethod
    def from_millicubic_meters_per_kilogram(millicubic_meters_per_kilogram: float):
        """
        Create a new instance of SpecificVolume from a value in millicubic_meters_per_kilogram.

        

        :param meters: The SpecificVolume value in millicubic_meters_per_kilogram.
        :type millicubic_meters_per_kilogram: float
        :return: A new instance of SpecificVolume.
        :rtype: SpecificVolume
        """
        return SpecificVolume(millicubic_meters_per_kilogram, SpecificVolumeUnits.MillicubicMeterPerKilogram)

    
    @property
    def cubic_meters_per_kilogram(self) -> float:
        """
        
        """
        if self.__cubic_meters_per_kilogram != None:
            return self.__cubic_meters_per_kilogram
        self.__cubic_meters_per_kilogram = self.__convert_from_base(SpecificVolumeUnits.CubicMeterPerKilogram)
        return self.__cubic_meters_per_kilogram

    
    @property
    def cubic_feet_per_pound(self) -> float:
        """
        
        """
        if self.__cubic_feet_per_pound != None:
            return self.__cubic_feet_per_pound
        self.__cubic_feet_per_pound = self.__convert_from_base(SpecificVolumeUnits.CubicFootPerPound)
        return self.__cubic_feet_per_pound

    
    @property
    def millicubic_meters_per_kilogram(self) -> float:
        """
        
        """
        if self.__millicubic_meters_per_kilogram != None:
            return self.__millicubic_meters_per_kilogram
        self.__millicubic_meters_per_kilogram = self.__convert_from_base(SpecificVolumeUnits.MillicubicMeterPerKilogram)
        return self.__millicubic_meters_per_kilogram

    
    def to_string(self, unit: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram) -> string:
        """
        Format the SpecificVolume to string.
        Note! the default format for SpecificVolume is CubicMeterPerKilogram.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == SpecificVolumeUnits.CubicMeterPerKilogram:
            return f"""{self.cubic_meters_per_kilogram} m³/kg"""
        
        if unit == SpecificVolumeUnits.CubicFootPerPound:
            return f"""{self.cubic_feet_per_pound} ft³/lb"""
        
        if unit == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return f"""{self.millicubic_meters_per_kilogram} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: SpecificVolumeUnits = SpecificVolumeUnits.CubicMeterPerKilogram) -> string:
        """
        Get SpecificVolume unit abbreviation.
        Note! the default abbreviation for SpecificVolume is CubicMeterPerKilogram.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == SpecificVolumeUnits.CubicMeterPerKilogram:
            return """m³/kg"""
        
        if unit_abbreviation == SpecificVolumeUnits.CubicFootPerPound:
            return """ft³/lb"""
        
        if unit_abbreviation == SpecificVolumeUnits.MillicubicMeterPerKilogram:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for +: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return SpecificVolume(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for *: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return SpecificVolume(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for -: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return SpecificVolume(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for /: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return SpecificVolume(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for %: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return SpecificVolume(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for **: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return SpecificVolume(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for ==: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for <: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for >: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for <=: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, SpecificVolume):
            raise TypeError("unsupported operand type(s) for >=: 'SpecificVolume' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value