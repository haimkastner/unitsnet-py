from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MagneticFluxUnits(Enum):
        """
            MagneticFluxUnits enumeration
        """
        
        Weber = 'weber'
        """
            
        """
        

class MagneticFlux(AbstractMeasure):
    """
    In physics, specifically electromagnetism, the magnetic flux through a surface is the surface integral of the normal component of the magnetic field B passing through that surface.

    Args:
        value (float): The value.
        from_unit (MagneticFluxUnits): The MagneticFlux unit to create from, The default unit is Weber
    """
    def __init__(self, value: float, from_unit: MagneticFluxUnits = MagneticFluxUnits.Weber):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__webers = None
        

    def convert(self, unit: MagneticFluxUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: MagneticFluxUnits) -> float:
        value = self._value
        
        if from_unit == MagneticFluxUnits.Weber:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MagneticFluxUnits) -> float:
        
        if to_unit == MagneticFluxUnits.Weber:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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

    
    def to_string(self, unit: MagneticFluxUnits = MagneticFluxUnits.Weber) -> str:
        """
        Format the MagneticFlux to string.
        Note! the default format for MagneticFlux is Weber.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MagneticFluxUnits.Weber:
            return f"""{self.webers} Wb"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MagneticFluxUnits = MagneticFluxUnits.Weber) -> str:
        """
        Get MagneticFlux unit abbreviation.
        Note! the default abbreviation for MagneticFlux is Weber.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MagneticFluxUnits.Weber:
            return """Wb"""
        