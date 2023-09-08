from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class IlluminanceUnits(Enum):
        """
            IlluminanceUnits enumeration
        """
        
        Lux = 'lux'
        """
            
        """
        
        Millilux = 'millilux'
        """
            
        """
        
        Kilolux = 'kilolux'
        """
            
        """
        
        Megalux = 'megalux'
        """
            
        """
        

class Illuminance(AbstractMeasure):
    """
    In photometry, illuminance is the total luminous flux incident on a surface, per unit area.

    Args:
        value (float): The value.
        from_unit (IlluminanceUnits): The Illuminance unit to create from, The default unit is Lux
    """
    def __init__(self, value: float, from_unit: IlluminanceUnits = IlluminanceUnits.Lux):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__lux = None
        
        self.__millilux = None
        
        self.__kilolux = None
        
        self.__megalux = None
        

    def convert(self, unit: IlluminanceUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: IlluminanceUnits) -> float:
        value = self._value
        
        if from_unit == IlluminanceUnits.Lux:
            return (value)
        
        if from_unit == IlluminanceUnits.Millilux:
            return ((value) / 0.001)
        
        if from_unit == IlluminanceUnits.Kilolux:
            return ((value) / 1000.0)
        
        if from_unit == IlluminanceUnits.Megalux:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IlluminanceUnits) -> float:
        
        if to_unit == IlluminanceUnits.Lux:
            return (value)
        
        if to_unit == IlluminanceUnits.Millilux:
            return ((value) * 0.001)
        
        if to_unit == IlluminanceUnits.Kilolux:
            return ((value) * 1000.0)
        
        if to_unit == IlluminanceUnits.Megalux:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_lux(lux: float):
        """
        Create a new instance of Illuminance from a value in lux.

        

        :param meters: The Illuminance value in lux.
        :type lux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(lux, IlluminanceUnits.Lux)

    
    @staticmethod
    def from_millilux(millilux: float):
        """
        Create a new instance of Illuminance from a value in millilux.

        

        :param meters: The Illuminance value in millilux.
        :type millilux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(millilux, IlluminanceUnits.Millilux)

    
    @staticmethod
    def from_kilolux(kilolux: float):
        """
        Create a new instance of Illuminance from a value in kilolux.

        

        :param meters: The Illuminance value in kilolux.
        :type kilolux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(kilolux, IlluminanceUnits.Kilolux)

    
    @staticmethod
    def from_megalux(megalux: float):
        """
        Create a new instance of Illuminance from a value in megalux.

        

        :param meters: The Illuminance value in megalux.
        :type megalux: float
        :return: A new instance of Illuminance.
        :rtype: Illuminance
        """
        return Illuminance(megalux, IlluminanceUnits.Megalux)

    
    @property
    def lux(self) -> float:
        """
        
        """
        if self.__lux != None:
            return self.__lux
        self.__lux = self.__convert_from_base(IlluminanceUnits.Lux)
        return self.__lux

    
    @property
    def millilux(self) -> float:
        """
        
        """
        if self.__millilux != None:
            return self.__millilux
        self.__millilux = self.__convert_from_base(IlluminanceUnits.Millilux)
        return self.__millilux

    
    @property
    def kilolux(self) -> float:
        """
        
        """
        if self.__kilolux != None:
            return self.__kilolux
        self.__kilolux = self.__convert_from_base(IlluminanceUnits.Kilolux)
        return self.__kilolux

    
    @property
    def megalux(self) -> float:
        """
        
        """
        if self.__megalux != None:
            return self.__megalux
        self.__megalux = self.__convert_from_base(IlluminanceUnits.Megalux)
        return self.__megalux

    
    def to_string(self, unit: IlluminanceUnits = IlluminanceUnits.Lux) -> str:
        """
        Format the Illuminance to string.
        Note! the default format for Illuminance is Lux.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == IlluminanceUnits.Lux:
            return f"""{self.lux} lx"""
        
        if unit == IlluminanceUnits.Millilux:
            return f"""{self.millilux} mlx"""
        
        if unit == IlluminanceUnits.Kilolux:
            return f"""{self.kilolux} klx"""
        
        if unit == IlluminanceUnits.Megalux:
            return f"""{self.megalux} Mlx"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: IlluminanceUnits = IlluminanceUnits.Lux) -> str:
        """
        Get Illuminance unit abbreviation.
        Note! the default abbreviation for Illuminance is Lux.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IlluminanceUnits.Lux:
            return """lx"""
        
        if unit_abbreviation == IlluminanceUnits.Millilux:
            return """mlx"""
        
        if unit_abbreviation == IlluminanceUnits.Kilolux:
            return """klx"""
        
        if unit_abbreviation == IlluminanceUnits.Megalux:
            return """Mlx"""
        