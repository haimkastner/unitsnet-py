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
        
        NanoTesla = 'nano_tesla'
        """
            
        """
        
        MicroTesla = 'micro_tesla'
        """
            
        """
        
        MilliTesla = 'milli_tesla'
        """
            
        """
        
        MilliGauss = 'milli_gauss'
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
        
        self.__nano_teslas = None
        
        self.__micro_teslas = None
        
        self.__milli_teslas = None
        
        self.__milli_gausses = None
        

    def __convert_from_base(self, from_unit: MagneticFieldUnits) -> float:
        value = self.__value
        
        if from_unit == MagneticFieldUnits.Tesla:
            return (value)
        
        if from_unit == MagneticFieldUnits.Gauss:
            return (value * 1e4)
        
        if from_unit == MagneticFieldUnits.NanoTesla:
            return ((value) / 1e-09)
        
        if from_unit == MagneticFieldUnits.MicroTesla:
            return ((value) / 1e-06)
        
        if from_unit == MagneticFieldUnits.MilliTesla:
            return ((value) / 0.001)
        
        if from_unit == MagneticFieldUnits.MilliGauss:
            return ((value * 1e4) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagneticFieldUnits) -> float:
        
        if to_unit == MagneticFieldUnits.Tesla:
            return (value)
        
        if to_unit == MagneticFieldUnits.Gauss:
            return (value / 1e4)
        
        if to_unit == MagneticFieldUnits.NanoTesla:
            return ((value) * 1e-09)
        
        if to_unit == MagneticFieldUnits.MicroTesla:
            return ((value) * 1e-06)
        
        if to_unit == MagneticFieldUnits.MilliTesla:
            return ((value) * 0.001)
        
        if to_unit == MagneticFieldUnits.MilliGauss:
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
    def from_nano_teslas(nano_teslas: float):
        """
        Create a new instance of MagneticField from a value in nano_teslas.

        

        :param meters: The MagneticField value in nano_teslas.
        :type nano_teslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(nano_teslas, MagneticFieldUnits.NanoTesla)

    
    @staticmethod
    def from_micro_teslas(micro_teslas: float):
        """
        Create a new instance of MagneticField from a value in micro_teslas.

        

        :param meters: The MagneticField value in micro_teslas.
        :type micro_teslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(micro_teslas, MagneticFieldUnits.MicroTesla)

    
    @staticmethod
    def from_milli_teslas(milli_teslas: float):
        """
        Create a new instance of MagneticField from a value in milli_teslas.

        

        :param meters: The MagneticField value in milli_teslas.
        :type milli_teslas: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(milli_teslas, MagneticFieldUnits.MilliTesla)

    
    @staticmethod
    def from_milli_gausses(milli_gausses: float):
        """
        Create a new instance of MagneticField from a value in milli_gausses.

        

        :param meters: The MagneticField value in milli_gausses.
        :type milli_gausses: float
        :return: A new instance of MagneticField.
        :rtype: MagneticField
        """
        return MagneticField(milli_gausses, MagneticFieldUnits.MilliGauss)

    
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
    def nano_teslas(self) -> float:
        """
        
        """
        if self.__nano_teslas != None:
            return self.__nano_teslas
        self.__nano_teslas = self.__convert_from_base(MagneticFieldUnits.NanoTesla)
        return self.__nano_teslas

    
    @property
    def micro_teslas(self) -> float:
        """
        
        """
        if self.__micro_teslas != None:
            return self.__micro_teslas
        self.__micro_teslas = self.__convert_from_base(MagneticFieldUnits.MicroTesla)
        return self.__micro_teslas

    
    @property
    def milli_teslas(self) -> float:
        """
        
        """
        if self.__milli_teslas != None:
            return self.__milli_teslas
        self.__milli_teslas = self.__convert_from_base(MagneticFieldUnits.MilliTesla)
        return self.__milli_teslas

    
    @property
    def milli_gausses(self) -> float:
        """
        
        """
        if self.__milli_gausses != None:
            return self.__milli_gausses
        self.__milli_gausses = self.__convert_from_base(MagneticFieldUnits.MilliGauss)
        return self.__milli_gausses

    
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
        
        if unit == MagneticFieldUnits.NanoTesla:
            return f"""{self.nano_teslas} """
        
        if unit == MagneticFieldUnits.MicroTesla:
            return f"""{self.micro_teslas} """
        
        if unit == MagneticFieldUnits.MilliTesla:
            return f"""{self.milli_teslas} """
        
        if unit == MagneticFieldUnits.MilliGauss:
            return f"""{self.milli_gausses} """
        
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
        
        if unit_abbreviation == MagneticFieldUnits.NanoTesla:
            return """"""
        
        if unit_abbreviation == MagneticFieldUnits.MicroTesla:
            return """"""
        
        if unit_abbreviation == MagneticFieldUnits.MilliTesla:
            return """"""
        
        if unit_abbreviation == MagneticFieldUnits.MilliGauss:
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