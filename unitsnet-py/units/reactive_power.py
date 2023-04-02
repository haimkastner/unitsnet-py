from enum import Enum
import math
import string


class ReactivePowerUnits(Enum):
        """
            ReactivePowerUnits enumeration
        """
        
        VoltampereReactive = 'voltampere_reactive'
        """
            
        """
        
        KiloVoltampereReactive = 'kilo_voltampere_reactive'
        """
            
        """
        
        MegaVoltampereReactive = 'mega_voltampere_reactive'
        """
            
        """
        
        GigaVoltampereReactive = 'giga_voltampere_reactive'
        """
            
        """
        

class ReactivePower:
    """
    Volt-ampere reactive (var) is a unit by which reactive power is expressed in an AC electric power system. Reactive power exists in an AC circuit when the current and voltage are not in phase.

    Args:
        value (float): The value.
        from_unit (ReactivePowerUnits): The ReactivePower unit to create from, The default unit is VoltampereReactive
    """
    def __init__(self, value: float, from_unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__voltamperes_reactive = None
        
        self.__kilo_voltamperes_reactive = None
        
        self.__mega_voltamperes_reactive = None
        
        self.__giga_voltamperes_reactive = None
        

    def __convert_from_base(self, from_unit: ReactivePowerUnits) -> float:
        value = self.__value
        
        if from_unit == ReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if from_unit == ReactivePowerUnits.KiloVoltampereReactive:
            return ((value) / 1000.0)
        
        if from_unit == ReactivePowerUnits.MegaVoltampereReactive:
            return ((value) / 1000000.0)
        
        if from_unit == ReactivePowerUnits.GigaVoltampereReactive:
            return ((value) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ReactivePowerUnits) -> float:
        
        if to_unit == ReactivePowerUnits.VoltampereReactive:
            return (value)
        
        if to_unit == ReactivePowerUnits.KiloVoltampereReactive:
            return ((value) * 1000.0)
        
        if to_unit == ReactivePowerUnits.MegaVoltampereReactive:
            return ((value) * 1000000.0)
        
        if to_unit == ReactivePowerUnits.GigaVoltampereReactive:
            return ((value) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_voltamperes_reactive(voltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in voltamperes_reactive.

        

        :param meters: The ReactivePower value in voltamperes_reactive.
        :type voltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(voltamperes_reactive, ReactivePowerUnits.VoltampereReactive)

    
    @staticmethod
    def from_kilo_voltamperes_reactive(kilo_voltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in kilo_voltamperes_reactive.

        

        :param meters: The ReactivePower value in kilo_voltamperes_reactive.
        :type kilo_voltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(kilo_voltamperes_reactive, ReactivePowerUnits.KiloVoltampereReactive)

    
    @staticmethod
    def from_mega_voltamperes_reactive(mega_voltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in mega_voltamperes_reactive.

        

        :param meters: The ReactivePower value in mega_voltamperes_reactive.
        :type mega_voltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(mega_voltamperes_reactive, ReactivePowerUnits.MegaVoltampereReactive)

    
    @staticmethod
    def from_giga_voltamperes_reactive(giga_voltamperes_reactive: float):
        """
        Create a new instance of ReactivePower from a value in giga_voltamperes_reactive.

        

        :param meters: The ReactivePower value in giga_voltamperes_reactive.
        :type giga_voltamperes_reactive: float
        :return: A new instance of ReactivePower.
        :rtype: ReactivePower
        """
        return ReactivePower(giga_voltamperes_reactive, ReactivePowerUnits.GigaVoltampereReactive)

    
    @property
    def voltamperes_reactive(self) -> float:
        """
        
        """
        if self.__voltamperes_reactive != None:
            return self.__voltamperes_reactive
        self.__voltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.VoltampereReactive)
        return self.__voltamperes_reactive

    
    @property
    def kilo_voltamperes_reactive(self) -> float:
        """
        
        """
        if self.__kilo_voltamperes_reactive != None:
            return self.__kilo_voltamperes_reactive
        self.__kilo_voltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.KiloVoltampereReactive)
        return self.__kilo_voltamperes_reactive

    
    @property
    def mega_voltamperes_reactive(self) -> float:
        """
        
        """
        if self.__mega_voltamperes_reactive != None:
            return self.__mega_voltamperes_reactive
        self.__mega_voltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.MegaVoltampereReactive)
        return self.__mega_voltamperes_reactive

    
    @property
    def giga_voltamperes_reactive(self) -> float:
        """
        
        """
        if self.__giga_voltamperes_reactive != None:
            return self.__giga_voltamperes_reactive
        self.__giga_voltamperes_reactive = self.__convert_from_base(ReactivePowerUnits.GigaVoltampereReactive)
        return self.__giga_voltamperes_reactive

    
    def to_string(self, unit: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive) -> string:
        """
        Format the ReactivePower to string.
        Note! the default format for ReactivePower is VoltampereReactive.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ReactivePowerUnits.VoltampereReactive:
            return f"""{self.voltamperes_reactive} var"""
        
        if unit == ReactivePowerUnits.KiloVoltampereReactive:
            return f"""{self.kilo_voltamperes_reactive} """
        
        if unit == ReactivePowerUnits.MegaVoltampereReactive:
            return f"""{self.mega_voltamperes_reactive} """
        
        if unit == ReactivePowerUnits.GigaVoltampereReactive:
            return f"""{self.giga_voltamperes_reactive} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ReactivePowerUnits = ReactivePowerUnits.VoltampereReactive) -> string:
        """
        Get ReactivePower unit abbreviation.
        Note! the default abbreviation for ReactivePower is VoltampereReactive.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ReactivePowerUnits.VoltampereReactive:
            return """var"""
        
        if unit_abbreviation == ReactivePowerUnits.KiloVoltampereReactive:
            return """"""
        
        if unit_abbreviation == ReactivePowerUnits.MegaVoltampereReactive:
            return """"""
        
        if unit_abbreviation == ReactivePowerUnits.GigaVoltampereReactive:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for +: 'ReactivePower' and '{}'".format(type(other).__name__))
        return ReactivePower(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for *: 'ReactivePower' and '{}'".format(type(other).__name__))
        return ReactivePower(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for -: 'ReactivePower' and '{}'".format(type(other).__name__))
        return ReactivePower(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for /: 'ReactivePower' and '{}'".format(type(other).__name__))
        return ReactivePower(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for %: 'ReactivePower' and '{}'".format(type(other).__name__))
        return ReactivePower(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for **: 'ReactivePower' and '{}'".format(type(other).__name__))
        return ReactivePower(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for ==: 'ReactivePower' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for <: 'ReactivePower' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for >: 'ReactivePower' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for <=: 'ReactivePower' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ReactivePower):
            raise TypeError("unsupported operand type(s) for >=: 'ReactivePower' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value