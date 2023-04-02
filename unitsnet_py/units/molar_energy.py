from enum import Enum
import math
import string


class MolarEnergyUnits(Enum):
        """
            MolarEnergyUnits enumeration
        """
        
        JoulePerMole = 'joule_per_mole'
        """
            
        """
        
        KilojoulePerMole = 'kilojoule_per_mole'
        """
            
        """
        
        MegajoulePerMole = 'megajoule_per_mole'
        """
            
        """
        

class MolarEnergy:
    """
    Molar energy is the amount of energy stored in 1 mole of a substance.

    Args:
        value (float): The value.
        from_unit (MolarEnergyUnits): The MolarEnergy unit to create from, The default unit is JoulePerMole
    """
    def __init__(self, value: float, from_unit: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_mole = None
        
        self.__kilojoules_per_mole = None
        
        self.__megajoules_per_mole = None
        

    def __convert_from_base(self, from_unit: MolarEnergyUnits) -> float:
        value = self.__value
        
        if from_unit == MolarEnergyUnits.JoulePerMole:
            return (value)
        
        if from_unit == MolarEnergyUnits.KilojoulePerMole:
            return ((value) / 1000.0)
        
        if from_unit == MolarEnergyUnits.MegajoulePerMole:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarEnergyUnits) -> float:
        
        if to_unit == MolarEnergyUnits.JoulePerMole:
            return (value)
        
        if to_unit == MolarEnergyUnits.KilojoulePerMole:
            return ((value) * 1000.0)
        
        if to_unit == MolarEnergyUnits.MegajoulePerMole:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_joules_per_mole(joules_per_mole: float):
        """
        Create a new instance of MolarEnergy from a value in joules_per_mole.

        

        :param meters: The MolarEnergy value in joules_per_mole.
        :type joules_per_mole: float
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy(joules_per_mole, MolarEnergyUnits.JoulePerMole)

    
    @staticmethod
    def from_kilojoules_per_mole(kilojoules_per_mole: float):
        """
        Create a new instance of MolarEnergy from a value in kilojoules_per_mole.

        

        :param meters: The MolarEnergy value in kilojoules_per_mole.
        :type kilojoules_per_mole: float
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy(kilojoules_per_mole, MolarEnergyUnits.KilojoulePerMole)

    
    @staticmethod
    def from_megajoules_per_mole(megajoules_per_mole: float):
        """
        Create a new instance of MolarEnergy from a value in megajoules_per_mole.

        

        :param meters: The MolarEnergy value in megajoules_per_mole.
        :type megajoules_per_mole: float
        :return: A new instance of MolarEnergy.
        :rtype: MolarEnergy
        """
        return MolarEnergy(megajoules_per_mole, MolarEnergyUnits.MegajoulePerMole)

    
    @property
    def joules_per_mole(self) -> float:
        """
        
        """
        if self.__joules_per_mole != None:
            return self.__joules_per_mole
        self.__joules_per_mole = self.__convert_from_base(MolarEnergyUnits.JoulePerMole)
        return self.__joules_per_mole

    
    @property
    def kilojoules_per_mole(self) -> float:
        """
        
        """
        if self.__kilojoules_per_mole != None:
            return self.__kilojoules_per_mole
        self.__kilojoules_per_mole = self.__convert_from_base(MolarEnergyUnits.KilojoulePerMole)
        return self.__kilojoules_per_mole

    
    @property
    def megajoules_per_mole(self) -> float:
        """
        
        """
        if self.__megajoules_per_mole != None:
            return self.__megajoules_per_mole
        self.__megajoules_per_mole = self.__convert_from_base(MolarEnergyUnits.MegajoulePerMole)
        return self.__megajoules_per_mole

    
    def to_string(self, unit: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole) -> string:
        """
        Format the MolarEnergy to string.
        Note! the default format for MolarEnergy is JoulePerMole.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolarEnergyUnits.JoulePerMole:
            return f"""{self.joules_per_mole} J/mol"""
        
        if unit == MolarEnergyUnits.KilojoulePerMole:
            return f"""{self.kilojoules_per_mole} """
        
        if unit == MolarEnergyUnits.MegajoulePerMole:
            return f"""{self.megajoules_per_mole} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarEnergyUnits = MolarEnergyUnits.JoulePerMole) -> string:
        """
        Get MolarEnergy unit abbreviation.
        Note! the default abbreviation for MolarEnergy is JoulePerMole.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarEnergyUnits.JoulePerMole:
            return """J/mol"""
        
        if unit_abbreviation == MolarEnergyUnits.KilojoulePerMole:
            return """"""
        
        if unit_abbreviation == MolarEnergyUnits.MegajoulePerMole:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for +: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return MolarEnergy(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for *: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return MolarEnergy(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for -: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return MolarEnergy(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for /: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return MolarEnergy(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for %: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return MolarEnergy(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for **: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return MolarEnergy(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for ==: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for <: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for >: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for <=: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MolarEnergy):
            raise TypeError("unsupported operand type(s) for >=: 'MolarEnergy' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value