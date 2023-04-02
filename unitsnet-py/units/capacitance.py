from enum import Enum
import math
import string


class CapacitanceUnits(Enum):
        """
            CapacitanceUnits enumeration
        """
        
        Farad = 'farad'
        """
            
        """
        
        PicoFarad = 'pico_farad'
        """
            
        """
        
        NanoFarad = 'nano_farad'
        """
            
        """
        
        MicroFarad = 'micro_farad'
        """
            
        """
        
        MilliFarad = 'milli_farad'
        """
            
        """
        
        KiloFarad = 'kilo_farad'
        """
            
        """
        
        MegaFarad = 'mega_farad'
        """
            
        """
        

class Capacitance:
    """
    Capacitance is the ability of a body to store an electric charge.

    Args:
        value (float): The value.
        from_unit (CapacitanceUnits): The Capacitance unit to create from, The default unit is Farad
    """
    def __init__(self, value: float, from_unit: CapacitanceUnits = CapacitanceUnits.Farad):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__farads = None
        
        self.__pico_farads = None
        
        self.__nano_farads = None
        
        self.__micro_farads = None
        
        self.__milli_farads = None
        
        self.__kilo_farads = None
        
        self.__mega_farads = None
        

    def __convert_from_base(self, from_unit: CapacitanceUnits) -> float:
        value = self.__value
        
        if from_unit == CapacitanceUnits.Farad:
            return (value)
        
        if from_unit == CapacitanceUnits.PicoFarad:
            return ((value) / 1e-12)
        
        if from_unit == CapacitanceUnits.NanoFarad:
            return ((value) / 1e-09)
        
        if from_unit == CapacitanceUnits.MicroFarad:
            return ((value) / 1e-06)
        
        if from_unit == CapacitanceUnits.MilliFarad:
            return ((value) / 0.001)
        
        if from_unit == CapacitanceUnits.KiloFarad:
            return ((value) / 1000.0)
        
        if from_unit == CapacitanceUnits.MegaFarad:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: CapacitanceUnits) -> float:
        
        if to_unit == CapacitanceUnits.Farad:
            return (value)
        
        if to_unit == CapacitanceUnits.PicoFarad:
            return ((value) * 1e-12)
        
        if to_unit == CapacitanceUnits.NanoFarad:
            return ((value) * 1e-09)
        
        if to_unit == CapacitanceUnits.MicroFarad:
            return ((value) * 1e-06)
        
        if to_unit == CapacitanceUnits.MilliFarad:
            return ((value) * 0.001)
        
        if to_unit == CapacitanceUnits.KiloFarad:
            return ((value) * 1000.0)
        
        if to_unit == CapacitanceUnits.MegaFarad:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_farads(farads: float):
        """
        Create a new instance of Capacitance from a value in farads.

        

        :param meters: The Capacitance value in farads.
        :type farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(farads, CapacitanceUnits.Farad)

    
    @staticmethod
    def from_pico_farads(pico_farads: float):
        """
        Create a new instance of Capacitance from a value in pico_farads.

        

        :param meters: The Capacitance value in pico_farads.
        :type pico_farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(pico_farads, CapacitanceUnits.PicoFarad)

    
    @staticmethod
    def from_nano_farads(nano_farads: float):
        """
        Create a new instance of Capacitance from a value in nano_farads.

        

        :param meters: The Capacitance value in nano_farads.
        :type nano_farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(nano_farads, CapacitanceUnits.NanoFarad)

    
    @staticmethod
    def from_micro_farads(micro_farads: float):
        """
        Create a new instance of Capacitance from a value in micro_farads.

        

        :param meters: The Capacitance value in micro_farads.
        :type micro_farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(micro_farads, CapacitanceUnits.MicroFarad)

    
    @staticmethod
    def from_milli_farads(milli_farads: float):
        """
        Create a new instance of Capacitance from a value in milli_farads.

        

        :param meters: The Capacitance value in milli_farads.
        :type milli_farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(milli_farads, CapacitanceUnits.MilliFarad)

    
    @staticmethod
    def from_kilo_farads(kilo_farads: float):
        """
        Create a new instance of Capacitance from a value in kilo_farads.

        

        :param meters: The Capacitance value in kilo_farads.
        :type kilo_farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(kilo_farads, CapacitanceUnits.KiloFarad)

    
    @staticmethod
    def from_mega_farads(mega_farads: float):
        """
        Create a new instance of Capacitance from a value in mega_farads.

        

        :param meters: The Capacitance value in mega_farads.
        :type mega_farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(mega_farads, CapacitanceUnits.MegaFarad)

    
    @property
    def farads(self) -> float:
        """
        
        """
        if self.__farads != None:
            return self.__farads
        self.__farads = self.__convert_from_base(CapacitanceUnits.Farad)
        return self.__farads

    
    @property
    def pico_farads(self) -> float:
        """
        
        """
        if self.__pico_farads != None:
            return self.__pico_farads
        self.__pico_farads = self.__convert_from_base(CapacitanceUnits.PicoFarad)
        return self.__pico_farads

    
    @property
    def nano_farads(self) -> float:
        """
        
        """
        if self.__nano_farads != None:
            return self.__nano_farads
        self.__nano_farads = self.__convert_from_base(CapacitanceUnits.NanoFarad)
        return self.__nano_farads

    
    @property
    def micro_farads(self) -> float:
        """
        
        """
        if self.__micro_farads != None:
            return self.__micro_farads
        self.__micro_farads = self.__convert_from_base(CapacitanceUnits.MicroFarad)
        return self.__micro_farads

    
    @property
    def milli_farads(self) -> float:
        """
        
        """
        if self.__milli_farads != None:
            return self.__milli_farads
        self.__milli_farads = self.__convert_from_base(CapacitanceUnits.MilliFarad)
        return self.__milli_farads

    
    @property
    def kilo_farads(self) -> float:
        """
        
        """
        if self.__kilo_farads != None:
            return self.__kilo_farads
        self.__kilo_farads = self.__convert_from_base(CapacitanceUnits.KiloFarad)
        return self.__kilo_farads

    
    @property
    def mega_farads(self) -> float:
        """
        
        """
        if self.__mega_farads != None:
            return self.__mega_farads
        self.__mega_farads = self.__convert_from_base(CapacitanceUnits.MegaFarad)
        return self.__mega_farads

    
    def to_string(self, unit: CapacitanceUnits = CapacitanceUnits.Farad) -> string:
        """
        Format the Capacitance to string.
        Note! the default format for Capacitance is Farad.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == CapacitanceUnits.Farad:
            return f"""{self.farads} F"""
        
        if unit == CapacitanceUnits.PicoFarad:
            return f"""{self.pico_farads} """
        
        if unit == CapacitanceUnits.NanoFarad:
            return f"""{self.nano_farads} """
        
        if unit == CapacitanceUnits.MicroFarad:
            return f"""{self.micro_farads} """
        
        if unit == CapacitanceUnits.MilliFarad:
            return f"""{self.milli_farads} """
        
        if unit == CapacitanceUnits.KiloFarad:
            return f"""{self.kilo_farads} """
        
        if unit == CapacitanceUnits.MegaFarad:
            return f"""{self.mega_farads} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: CapacitanceUnits = CapacitanceUnits.Farad) -> string:
        """
        Get Capacitance unit abbreviation.
        Note! the default abbreviation for Capacitance is Farad.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == CapacitanceUnits.Farad:
            return """F"""
        
        if unit_abbreviation == CapacitanceUnits.PicoFarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.NanoFarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.MicroFarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.MilliFarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.KiloFarad:
            return """"""
        
        if unit_abbreviation == CapacitanceUnits.MegaFarad:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for +: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for *: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for -: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for /: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for %: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for **: 'Capacitance' and '{}'".format(type(other).__name__))
        return Capacitance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for ==: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for <: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for >: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for <=: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Capacitance):
            raise TypeError("unsupported operand type(s) for >=: 'Capacitance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value