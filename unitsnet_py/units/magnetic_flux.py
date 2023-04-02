from enum import Enum
import math
import string


class MagneticFluxUnits(Enum):
        """
            MagneticFluxUnits enumeration
        """
        
        Weber = 'weber'
        """
            
        """
        

class MagneticFlux:
    """
    In physics, specifically electromagnetism, the magnetic flux through a surface is the surface integral of the normal component of the magnetic field B passing through that surface.

    Args:
        value (float): The value.
        from_unit (MagneticFluxUnits): The MagneticFlux unit to create from, The default unit is Weber
    """
    def __init__(self, value: float, from_unit: MagneticFluxUnits = MagneticFluxUnits.Weber):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__webers = None
        

    def __convert_from_base(self, from_unit: MagneticFluxUnits) -> float:
        value = self.__value
        
        if from_unit == MagneticFluxUnits.Weber:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagneticFluxUnits) -> float:
        
        if to_unit == MagneticFluxUnits.Weber:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_webers(webers: float):
        """
        Create a new instance of MagneticFlux from a value in webers.

        

        :param meters: The MagneticFlux value in webers.
        :type webers: float
        :return: A new instance of MagneticFlux.
        :rtype: MagneticFlux
        """
        return MagneticFlux(webers, MagneticFluxUnits.Weber)

    
    @property
    def webers(self) -> float:
        """
        
        """
        if self.__webers != None:
            return self.__webers
        self.__webers = self.__convert_from_base(MagneticFluxUnits.Weber)
        return self.__webers

    
    def to_string(self, unit: MagneticFluxUnits = MagneticFluxUnits.Weber) -> string:
        """
        Format the MagneticFlux to string.
        Note! the default format for MagneticFlux is Weber.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MagneticFluxUnits.Weber:
            return f"""{self.webers} Wb"""
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagneticFluxUnits = MagneticFluxUnits.Weber) -> string:
        """
        Get MagneticFlux unit abbreviation.
        Note! the default abbreviation for MagneticFlux is Weber.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagneticFluxUnits.Weber:
            return """Wb"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for +: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return MagneticFlux(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for *: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return MagneticFlux(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for -: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return MagneticFlux(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for /: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return MagneticFlux(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for %: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return MagneticFlux(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for **: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return MagneticFlux(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for ==: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for <: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for >: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for <=: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MagneticFlux):
            raise TypeError("unsupported operand type(s) for >=: 'MagneticFlux' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value