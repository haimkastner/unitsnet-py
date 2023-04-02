from enum import Enum
import math
import string


class ReactiveEnergyUnits(Enum):
        """
            ReactiveEnergyUnits enumeration
        """
        
        VoltampereReactiveHour = 'voltampere_reactive_hour'
        """
            
        """
        
        KilovoltampereReactiveHour = 'kilovoltampere_reactive_hour'
        """
            
        """
        
        MegavoltampereReactiveHour = 'megavoltampere_reactive_hour'
        """
            
        """
        

class ReactiveEnergy:
    """
    The Volt-ampere reactive hour (expressed as varh) is the reactive power of one Volt-ampere reactive produced in one hour.

    Args:
        value (float): The value.
        from_unit (ReactiveEnergyUnits): The ReactiveEnergy unit to create from, The default unit is VoltampereReactiveHour
    """
    def __init__(self, value: float, from_unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__voltampere_reactive_hours = None
        
        self.__kilovoltampere_reactive_hours = None
        
        self.__megavoltampere_reactive_hours = None
        

    def __convert_from_base(self, from_unit: ReactiveEnergyUnits) -> float:
        value = self.__value
        
        if from_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if from_unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) / 1000.0)
        
        if from_unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReactiveEnergyUnits) -> float:
        
        if to_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if to_unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return ((value) * 1000.0)
        
        if to_unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_voltampere_reactive_hours(voltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in voltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in voltampere_reactive_hours.
        :type voltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(voltampere_reactive_hours, ReactiveEnergyUnits.VoltampereReactiveHour)

    
    @staticmethod
    def from_kilovoltampere_reactive_hours(kilovoltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in kilovoltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in kilovoltampere_reactive_hours.
        :type kilovoltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(kilovoltampere_reactive_hours, ReactiveEnergyUnits.KilovoltampereReactiveHour)

    
    @staticmethod
    def from_megavoltampere_reactive_hours(megavoltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in megavoltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in megavoltampere_reactive_hours.
        :type megavoltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(megavoltampere_reactive_hours, ReactiveEnergyUnits.MegavoltampereReactiveHour)

    
    @property
    def voltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__voltampere_reactive_hours != None:
            return self.__voltampere_reactive_hours
        self.__voltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.VoltampereReactiveHour)
        return self.__voltampere_reactive_hours

    
    @property
    def kilovoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__kilovoltampere_reactive_hours != None:
            return self.__kilovoltampere_reactive_hours
        self.__kilovoltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.KilovoltampereReactiveHour)
        return self.__kilovoltampere_reactive_hours

    
    @property
    def megavoltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__megavoltampere_reactive_hours != None:
            return self.__megavoltampere_reactive_hours
        self.__megavoltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.MegavoltampereReactiveHour)
        return self.__megavoltampere_reactive_hours

    
    def to_string(self, unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> string:
        """
        Format the ReactiveEnergy to string.
        Note! the default format for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return f"""{self.voltampere_reactive_hours} varh"""
        
        if unit == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return f"""{self.kilovoltampere_reactive_hours} """
        
        if unit == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return f"""{self.megavoltampere_reactive_hours} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> string:
        """
        Get ReactiveEnergy unit abbreviation.
        Note! the default abbreviation for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReactiveEnergyUnits.VoltampereReactiveHour:
            return """varh"""
        
        if unit_abbreviation == ReactiveEnergyUnits.KilovoltampereReactiveHour:
            return """"""
        
        if unit_abbreviation == ReactiveEnergyUnits.MegavoltampereReactiveHour:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for +: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return ReactiveEnergy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for *: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return ReactiveEnergy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for -: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return ReactiveEnergy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for /: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return ReactiveEnergy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for %: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return ReactiveEnergy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for **: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return ReactiveEnergy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for ==: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for <: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for >: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for <=: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ReactiveEnergy):
            raise TypeError("unsupported operand type(s) for >=: 'ReactiveEnergy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value