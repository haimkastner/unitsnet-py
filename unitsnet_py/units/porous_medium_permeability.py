from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class PorousMediumPermeabilityUnits(Enum):
        """
            PorousMediumPermeabilityUnits enumeration
        """
        
        Darcy = 'darcy'
        """
            
        """
        
        SquareMeter = 'square_meter'
        """
            
        """
        
        SquareCentimeter = 'square_centimeter'
        """
            
        """
        
        Microdarcy = 'microdarcy'
        """
            
        """
        
        Millidarcy = 'millidarcy'
        """
            
        """
        

class PorousMediumPermeability(AbstractMeasure):
    """
    None

    Args:
        value (float): The value.
        from_unit (PorousMediumPermeabilityUnits): The PorousMediumPermeability unit to create from, The default unit is SquareMeter
    """
    def __init__(self, value: float, from_unit: PorousMediumPermeabilityUnits = PorousMediumPermeabilityUnits.SquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__darcys = None
        
        self.__square_meters = None
        
        self.__square_centimeters = None
        
        self.__microdarcys = None
        
        self.__millidarcys = None
        

    def convert(self, unit: PorousMediumPermeabilityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: PorousMediumPermeabilityUnits) -> float:
        value = self._value
        
        if from_unit == PorousMediumPermeabilityUnits.Darcy:
            return (value / 9.869233e-13)
        
        if from_unit == PorousMediumPermeabilityUnits.SquareMeter:
            return (value)
        
        if from_unit == PorousMediumPermeabilityUnits.SquareCentimeter:
            return (value / 1e-4)
        
        if from_unit == PorousMediumPermeabilityUnits.Microdarcy:
            return ((value / 9.869233e-13) / 1e-06)
        
        if from_unit == PorousMediumPermeabilityUnits.Millidarcy:
            return ((value / 9.869233e-13) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PorousMediumPermeabilityUnits) -> float:
        
        if to_unit == PorousMediumPermeabilityUnits.Darcy:
            return (value * 9.869233e-13)
        
        if to_unit == PorousMediumPermeabilityUnits.SquareMeter:
            return (value)
        
        if to_unit == PorousMediumPermeabilityUnits.SquareCentimeter:
            return (value * 1e-4)
        
        if to_unit == PorousMediumPermeabilityUnits.Microdarcy:
            return ((value * 9.869233e-13) * 1e-06)
        
        if to_unit == PorousMediumPermeabilityUnits.Millidarcy:
            return ((value * 9.869233e-13) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_darcys(darcys: float):
        """
        Create a new instance of PorousMediumPermeability from a value in darcys.

        

        :param meters: The PorousMediumPermeability value in darcys.
        :type darcys: float
        :return: A new instance of PorousMediumPermeability.
        :rtype: PorousMediumPermeability
        """
        return PorousMediumPermeability(darcys, PorousMediumPermeabilityUnits.Darcy)

    
    @staticmethod
    def from_square_meters(square_meters: float):
        """
        Create a new instance of PorousMediumPermeability from a value in square_meters.

        

        :param meters: The PorousMediumPermeability value in square_meters.
        :type square_meters: float
        :return: A new instance of PorousMediumPermeability.
        :rtype: PorousMediumPermeability
        """
        return PorousMediumPermeability(square_meters, PorousMediumPermeabilityUnits.SquareMeter)

    
    @staticmethod
    def from_square_centimeters(square_centimeters: float):
        """
        Create a new instance of PorousMediumPermeability from a value in square_centimeters.

        

        :param meters: The PorousMediumPermeability value in square_centimeters.
        :type square_centimeters: float
        :return: A new instance of PorousMediumPermeability.
        :rtype: PorousMediumPermeability
        """
        return PorousMediumPermeability(square_centimeters, PorousMediumPermeabilityUnits.SquareCentimeter)

    
    @staticmethod
    def from_microdarcys(microdarcys: float):
        """
        Create a new instance of PorousMediumPermeability from a value in microdarcys.

        

        :param meters: The PorousMediumPermeability value in microdarcys.
        :type microdarcys: float
        :return: A new instance of PorousMediumPermeability.
        :rtype: PorousMediumPermeability
        """
        return PorousMediumPermeability(microdarcys, PorousMediumPermeabilityUnits.Microdarcy)

    
    @staticmethod
    def from_millidarcys(millidarcys: float):
        """
        Create a new instance of PorousMediumPermeability from a value in millidarcys.

        

        :param meters: The PorousMediumPermeability value in millidarcys.
        :type millidarcys: float
        :return: A new instance of PorousMediumPermeability.
        :rtype: PorousMediumPermeability
        """
        return PorousMediumPermeability(millidarcys, PorousMediumPermeabilityUnits.Millidarcy)

    
    @property
    def darcys(self) -> float:
        """
        
        """
        if self.__darcys != None:
            return self.__darcys
        self.__darcys = self.__convert_from_base(PorousMediumPermeabilityUnits.Darcy)
        return self.__darcys

    
    @property
    def square_meters(self) -> float:
        """
        
        """
        if self.__square_meters != None:
            return self.__square_meters
        self.__square_meters = self.__convert_from_base(PorousMediumPermeabilityUnits.SquareMeter)
        return self.__square_meters

    
    @property
    def square_centimeters(self) -> float:
        """
        
        """
        if self.__square_centimeters != None:
            return self.__square_centimeters
        self.__square_centimeters = self.__convert_from_base(PorousMediumPermeabilityUnits.SquareCentimeter)
        return self.__square_centimeters

    
    @property
    def microdarcys(self) -> float:
        """
        
        """
        if self.__microdarcys != None:
            return self.__microdarcys
        self.__microdarcys = self.__convert_from_base(PorousMediumPermeabilityUnits.Microdarcy)
        return self.__microdarcys

    
    @property
    def millidarcys(self) -> float:
        """
        
        """
        if self.__millidarcys != None:
            return self.__millidarcys
        self.__millidarcys = self.__convert_from_base(PorousMediumPermeabilityUnits.Millidarcy)
        return self.__millidarcys

    
    def to_string(self, unit: PorousMediumPermeabilityUnits = PorousMediumPermeabilityUnits.SquareMeter) -> str:
        """
        Format the PorousMediumPermeability to string.
        Note! the default format for PorousMediumPermeability is SquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PorousMediumPermeabilityUnits.Darcy:
            return f"""{self.darcys} D"""
        
        if unit == PorousMediumPermeabilityUnits.SquareMeter:
            return f"""{self.square_meters} m²"""
        
        if unit == PorousMediumPermeabilityUnits.SquareCentimeter:
            return f"""{self.square_centimeters} cm²"""
        
        if unit == PorousMediumPermeabilityUnits.Microdarcy:
            return f"""{self.microdarcys} μD"""
        
        if unit == PorousMediumPermeabilityUnits.Millidarcy:
            return f"""{self.millidarcys} mD"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PorousMediumPermeabilityUnits = PorousMediumPermeabilityUnits.SquareMeter) -> str:
        """
        Get PorousMediumPermeability unit abbreviation.
        Note! the default abbreviation for PorousMediumPermeability is SquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PorousMediumPermeabilityUnits.Darcy:
            return """D"""
        
        if unit_abbreviation == PorousMediumPermeabilityUnits.SquareMeter:
            return """m²"""
        
        if unit_abbreviation == PorousMediumPermeabilityUnits.SquareCentimeter:
            return """cm²"""
        
        if unit_abbreviation == PorousMediumPermeabilityUnits.Microdarcy:
            return """μD"""
        
        if unit_abbreviation == PorousMediumPermeabilityUnits.Millidarcy:
            return """mD"""
        