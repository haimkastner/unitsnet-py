from enum import Enum
import math
import string


class MagneticFieldUnits(Enum):
        """
            MagneticFieldUnits enumeration
        """
        
        Tesla = 'tesla'
        """
            
        """
        
        Gauss = 'gauss'
        """
            
        """
        
        Nanotesla = 'nanotesla'
        """
            
        """
        
        Microtesla = 'microtesla'
        """
            
        """
        
        Millitesla = 'millitesla'
        """
            
        """
        
        Milligauss = 'milligauss'
        """
            
        """
        

class MagneticField:
    """
    A magnetic field is a force field that is created by moving electric charges (electric currents) and magnetic dipoles, and exerts a force on other nearby moving charges and magnetic dipoles.

    Args:
        value (float): The value.
        from_unit (MagneticFieldUnits): The MagneticField unit to create from, The default unit is Tesla
    """
    def __init__(self, value: float, from_unit: MagneticFieldUnits = MagneticFieldUnits.Tesla):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__teslas = None
        
        self.__gausses = None
        
        self.__nanoteslas = None
        
        self.__microteslas = None
        
        self.__milliteslas = None
        
        self.__milligausses = None
        

    def __convert_from_base(self, from_unit: MagneticFieldUnits) -> float:
        value = self.__value
        
        if from_unit == MagneticFieldUnits.Tesla:
            return (value)
        
        if from_unit == MagneticFieldUnits.Gauss:
            return (value * 1e4)
        
        if from_unit == MagneticFieldUnits.Nanotesla:
            return ((value) / 1e-09)
        
        if from_unit == MagneticFieldUnits.Microtesla:
            return ((value) / 1e-06)
        
        if from_unit == MagneticFieldUnits.Millitesla:
            return ((value) / 0.001)
        
        if from_unit == MagneticFieldUnits.Milligauss:
            return ((value * 1e4) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagneticFieldUnits) -> float:
        
        if to_unit == MagneticFieldUnits.Tesla:
            return (value)
        
        if to_unit == MagneticFieldUnits.Gauss:
            return (value / 1e4)
        
        if to_unit == MagneticFieldUnits.Nanotesla:
            return ((value) * 1e-09)
        
        if to_unit == MagneticFieldUnits.Microtesla:
            return ((value) * 1e-06)
        
        if to_unit == MagneticFieldUnits.Millitesla:
            return ((value) * 0.001)
        
        if to_unit == MagneticFieldUnits.Milligauss:
            return ((value / 1e4) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_teslas(teslas: float):
        """
        Create a new instance of MagneticField from a value in teslas.

        

        :param meters: The MagneticField value in teslas.
        :type teslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(teslas, MagneticFieldUnits.Tesla)

    
    @staticmethod
    def from_gausses(gausses: float):
        """
        Create a new instance of MagneticField from a value in gausses.

        

        :param meters: The MagneticField value in gausses.
        :type gausses: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(gausses, MagneticFieldUnits.Gauss)

    
    @staticmethod
    def from_nanoteslas(nanoteslas: float):
        """
        Create a new instance of MagneticField from a value in nanoteslas.

        

        :param meters: The MagneticField value in nanoteslas.
        :type nanoteslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(nanoteslas, MagneticFieldUnits.Nanotesla)

    
    @staticmethod
    def from_microteslas(microteslas: float):
        """
        Create a new instance of MagneticField from a value in microteslas.

        

        :param meters: The MagneticField value in microteslas.
        :type microteslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(microteslas, MagneticFieldUnits.Microtesla)

    
    @staticmethod
    def from_milliteslas(milliteslas: float):
        """
        Create a new instance of MagneticField from a value in milliteslas.

        

        :param meters: The MagneticField value in milliteslas.
        :type milliteslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(milliteslas, MagneticFieldUnits.Millitesla)

    
    @staticmethod
    def from_milligausses(milligausses: float):
        """
        Create a new instance of MagneticField from a value in milligausses.

        

        :param meters: The MagneticField value in milligausses.
        :type milligausses: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(milligausses, MagneticFieldUnits.Milligauss)

    
    @property
    def teslas(self) -> float:
        """
        
        """
        if self.__teslas != None:
            return self.__teslas
        self.__teslas = self.__convert_from_base(MagneticFieldUnits.Tesla)
        return self.__teslas

    
    @property
    def gausses(self) -> float:
        """
        
        """
        if self.__gausses != None:
            return self.__gausses
        self.__gausses = self.__convert_from_base(MagneticFieldUnits.Gauss)
        return self.__gausses

    
    @property
    def nanoteslas(self) -> float:
        """
        
        """
        if self.__nanoteslas != None:
            return self.__nanoteslas
        self.__nanoteslas = self.__convert_from_base(MagneticFieldUnits.Nanotesla)
        return self.__nanoteslas

    
    @property
    def microteslas(self) -> float:
        """
        
        """
        if self.__microteslas != None:
            return self.__microteslas
        self.__microteslas = self.__convert_from_base(MagneticFieldUnits.Microtesla)
        return self.__microteslas

    
    @property
    def milliteslas(self) -> float:
        """
        
        """
        if self.__milliteslas != None:
            return self.__milliteslas
        self.__milliteslas = self.__convert_from_base(MagneticFieldUnits.Millitesla)
        return self.__milliteslas

    
    @property
    def milligausses(self) -> float:
        """
        
        """
        if self.__milligausses != None:
            return self.__milligausses
        self.__milligausses = self.__convert_from_base(MagneticFieldUnits.Milligauss)
        return self.__milligausses

    
    def to_string(self, unit: MagneticFieldUnits = MagneticFieldUnits.Tesla) -> string:
        """
        Format the MagneticField to string.
        Note! the default format for MagneticField is Tesla.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MagneticFieldUnits.Tesla:
            return f"""{self.teslas} T"""
        
        if unit == MagneticFieldUnits.Gauss:
            return f"""{self.gausses} G"""
        
        if unit == MagneticFieldUnits.Nanotesla:
            return f"""{self.nanoteslas} """
        
        if unit == MagneticFieldUnits.Microtesla:
            return f"""{self.microteslas} """
        
        if unit == MagneticFieldUnits.Millitesla:
            return f"""{self.milliteslas} """
        
        if unit == MagneticFieldUnits.Milligauss:
            return f"""{self.milligausses} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagneticFieldUnits = MagneticFieldUnits.Tesla) -> string:
        """
        Get MagneticField unit abbreviation.
        Note! the default abbreviation for MagneticField is Tesla.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagneticFieldUnits.Tesla:
            return """T"""
        
        if unit_abbreviation == MagneticFieldUnits.Gauss:
            return """G"""
        
        if unit_abbreviation == MagneticFieldUnits.Nanotesla:
            return """"""
        
        if unit_abbreviation == MagneticFieldUnits.Microtesla:
            return """"""
        
        if unit_abbreviation == MagneticFieldUnits.Millitesla:
            return """"""
        
        if unit_abbreviation == MagneticFieldUnits.Milligauss:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for +: 'MagneticField' and '{}'".format(type(other).__name__))
        return MagneticField(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for *: 'MagneticField' and '{}'".format(type(other).__name__))
        return MagneticField(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for -: 'MagneticField' and '{}'".format(type(other).__name__))
        return MagneticField(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for /: 'MagneticField' and '{}'".format(type(other).__name__))
        return MagneticField(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for %: 'MagneticField' and '{}'".format(type(other).__name__))
        return MagneticField(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for **: 'MagneticField' and '{}'".format(type(other).__name__))
        return MagneticField(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for ==: 'MagneticField' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for <: 'MagneticField' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for >: 'MagneticField' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for <=: 'MagneticField' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MagneticField):
            raise TypeError("unsupported operand type(s) for >=: 'MagneticField' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value