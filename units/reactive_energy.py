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
        
        KiloVoltampereReactiveHour = 'kilo_voltampere_reactive_hour'
        """
            
        """
        
        MegaVoltampereReactiveHour = 'mega_voltampere_reactive_hour'
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
        
        self.__kilo_voltampere_reactive_hours = None
        
        self.__mega_voltampere_reactive_hours = None
        

    def __convert_from_base(self, from_unit: ReactiveEnergyUnits) -> float:
        value = self.__value
        
        if from_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if from_unit == ReactiveEnergyUnits.KiloVoltampereReactiveHour:
            return ((value) / 1000.0)
        
        if from_unit == ReactiveEnergyUnits.MegaVoltampereReactiveHour:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReactiveEnergyUnits) -> float:
        
        if to_unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return (value)
        
        if to_unit == ReactiveEnergyUnits.KiloVoltampereReactiveHour:
            return ((value) * 1000.0)
        
        if to_unit == ReactiveEnergyUnits.MegaVoltampereReactiveHour:
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
    def from_kilo_voltampere_reactive_hours(kilo_voltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in kilo_voltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in kilo_voltampere_reactive_hours.
        :type kilo_voltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(kilo_voltampere_reactive_hours, ReactiveEnergyUnits.KiloVoltampereReactiveHour)

    
    @staticmethod
    def from_mega_voltampere_reactive_hours(mega_voltampere_reactive_hours: float):
        """
        Create a new instance of ReactiveEnergy from a value in mega_voltampere_reactive_hours.

        

        :param meters: The ReactiveEnergy value in mega_voltampere_reactive_hours.
        :type mega_voltampere_reactive_hours: float
        :return: A new instance of ReactiveEnergy.
        :rtype: ReactiveEnergy
        """
        return ReactiveEnergy(mega_voltampere_reactive_hours, ReactiveEnergyUnits.MegaVoltampereReactiveHour)

    
    @property
    def voltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__voltampere_reactive_hours != None:
            return self.__voltampere_reactive_hours
        self.__voltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.VoltampereReactiveHour)
        return self.__voltampere_reactive_hours

    
    @property
    def kilo_voltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__kilo_voltampere_reactive_hours != None:
            return self.__kilo_voltampere_reactive_hours
        self.__kilo_voltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.KiloVoltampereReactiveHour)
        return self.__kilo_voltampere_reactive_hours

    
    @property
    def mega_voltampere_reactive_hours(self) -> float:
        """
        
        """
        if self.__mega_voltampere_reactive_hours != None:
            return self.__mega_voltampere_reactive_hours
        self.__mega_voltampere_reactive_hours = self.__convert_from_base(ReactiveEnergyUnits.MegaVoltampereReactiveHour)
        return self.__mega_voltampere_reactive_hours

    
    def to_string(self, unit: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> string:
        """
        Format the ReactiveEnergy to string.
        Note! the default format for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ReactiveEnergyUnits.VoltampereReactiveHour:
            return f"""{self.voltampere_reactive_hours} varh"""
        
        if unit == ReactiveEnergyUnits.KiloVoltampereReactiveHour:
            return f"""{self.kilo_voltampere_reactive_hours} """
        
        if unit == ReactiveEnergyUnits.MegaVoltampereReactiveHour:
            return f"""{self.mega_voltampere_reactive_hours} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReactiveEnergyUnits = ReactiveEnergyUnits.VoltampereReactiveHour) -> string:
        """
        Get ReactiveEnergy unit abbreviation.
        Note! the default abbreviation for ReactiveEnergy is VoltampereReactiveHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReactiveEnergyUnits.VoltampereReactiveHour:
            return """varh"""
        
        if unit_abbreviation == ReactiveEnergyUnits.KiloVoltampereReactiveHour:
            return """"""
        
        if unit_abbreviation == ReactiveEnergyUnits.MegaVoltampereReactiveHour:
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