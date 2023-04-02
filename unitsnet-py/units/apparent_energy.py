from enum import Enum
import math
import string


class ApparentEnergyUnits(Enum):
        """
            ApparentEnergyUnits enumeration
        """
        
        VoltampereHour = 'voltampere_hour'
        """
            
        """
        
        KilovoltampereHour = 'kilovoltampere_hour'
        """
            
        """
        
        MegavoltampereHour = 'megavoltampere_hour'
        """
            
        """
        

class ApparentEnergy:
    """
    A unit for expressing the integral of apparent power over time, equal to the product of 1 volt-ampere and 1 hour, or to 3600 joules.

    Args:
        value (float): The value.
        from_unit (ApparentEnergyUnits): The ApparentEnergy unit to create from, The default unit is VoltampereHour
    """
    def __init__(self, value: float, from_unit: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__voltampere_hours = None
        
        self.__kilovoltampere_hours = None
        
        self.__megavoltampere_hours = None
        

    def __convert_from_base(self, from_unit: ApparentEnergyUnits) -> float:
        value = self.__value
        
        if from_unit == ApparentEnergyUnits.VoltampereHour:
            return (value)
        
        if from_unit == ApparentEnergyUnits.KilovoltampereHour:
            return ((value) / 1000.0)
        
        if from_unit == ApparentEnergyUnits.MegavoltampereHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ApparentEnergyUnits) -> float:
        
        if to_unit == ApparentEnergyUnits.VoltampereHour:
            return (value)
        
        if to_unit == ApparentEnergyUnits.KilovoltampereHour:
            return ((value) * 1000.0)
        
        if to_unit == ApparentEnergyUnits.MegavoltampereHour:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_voltampere_hours(voltampere_hours: float):
        """
        Create a new instance of ApparentEnergy from a value in voltampere_hours.

        

        :param meters: The ApparentEnergy value in voltampere_hours.
        :type voltampere_hours: float
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy(voltampere_hours, ApparentEnergyUnits.VoltampereHour)

    
    @staticmethod
    def from_kilovoltampere_hours(kilovoltampere_hours: float):
        """
        Create a new instance of ApparentEnergy from a value in kilovoltampere_hours.

        

        :param meters: The ApparentEnergy value in kilovoltampere_hours.
        :type kilovoltampere_hours: float
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy(kilovoltampere_hours, ApparentEnergyUnits.KilovoltampereHour)

    
    @staticmethod
    def from_megavoltampere_hours(megavoltampere_hours: float):
        """
        Create a new instance of ApparentEnergy from a value in megavoltampere_hours.

        

        :param meters: The ApparentEnergy value in megavoltampere_hours.
        :type megavoltampere_hours: float
        :return: A new instance of ApparentEnergy.
        :rtype: ApparentEnergy
        """
        return ApparentEnergy(megavoltampere_hours, ApparentEnergyUnits.MegavoltampereHour)

    
    @property
    def voltampere_hours(self) -> float:
        """
        
        """
        if self.__voltampere_hours != None:
            return self.__voltampere_hours
        self.__voltampere_hours = self.__convert_from_base(ApparentEnergyUnits.VoltampereHour)
        return self.__voltampere_hours

    
    @property
    def kilovoltampere_hours(self) -> float:
        """
        
        """
        if self.__kilovoltampere_hours != None:
            return self.__kilovoltampere_hours
        self.__kilovoltampere_hours = self.__convert_from_base(ApparentEnergyUnits.KilovoltampereHour)
        return self.__kilovoltampere_hours

    
    @property
    def megavoltampere_hours(self) -> float:
        """
        
        """
        if self.__megavoltampere_hours != None:
            return self.__megavoltampere_hours
        self.__megavoltampere_hours = self.__convert_from_base(ApparentEnergyUnits.MegavoltampereHour)
        return self.__megavoltampere_hours

    
    def to_string(self, unit: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour) -> string:
        """
        Format the ApparentEnergy to string.
        Note! the default format for ApparentEnergy is VoltampereHour.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ApparentEnergyUnits.VoltampereHour:
            return f"""{self.voltampere_hours} VAh"""
        
        if unit == ApparentEnergyUnits.KilovoltampereHour:
            return f"""{self.kilovoltampere_hours} """
        
        if unit == ApparentEnergyUnits.MegavoltampereHour:
            return f"""{self.megavoltampere_hours} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ApparentEnergyUnits = ApparentEnergyUnits.VoltampereHour) -> string:
        """
        Get ApparentEnergy unit abbreviation.
        Note! the default abbreviation for ApparentEnergy is VoltampereHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ApparentEnergyUnits.VoltampereHour:
            return """VAh"""
        
        if unit_abbreviation == ApparentEnergyUnits.KilovoltampereHour:
            return """"""
        
        if unit_abbreviation == ApparentEnergyUnits.MegavoltampereHour:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for +: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return ApparentEnergy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for *: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return ApparentEnergy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for -: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return ApparentEnergy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for /: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return ApparentEnergy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for %: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return ApparentEnergy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for **: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return ApparentEnergy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for ==: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for <: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for >: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for <=: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ApparentEnergy):
            raise TypeError("unsupported operand type(s) for >=: 'ApparentEnergy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value