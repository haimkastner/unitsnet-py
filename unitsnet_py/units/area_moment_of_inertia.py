from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AreaMomentOfInertiaUnits(Enum):
        """
            AreaMomentOfInertiaUnits enumeration
        """
        
        MeterToTheFourth = 'meter_to_the_fourth'
        """
            
        """
        
        DecimeterToTheFourth = 'decimeter_to_the_fourth'
        """
            
        """
        
        CentimeterToTheFourth = 'centimeter_to_the_fourth'
        """
            
        """
        
        MillimeterToTheFourth = 'millimeter_to_the_fourth'
        """
            
        """
        
        FootToTheFourth = 'foot_to_the_fourth'
        """
            
        """
        
        InchToTheFourth = 'inch_to_the_fourth'
        """
            
        """
        

class AreaMomentOfInertia(AbstractMeasure):
    """
    A geometric property of an area that reflects how its points are distributed with regard to an axis.

    Args:
        value (float): The value.
        from_unit (AreaMomentOfInertiaUnits): The AreaMomentOfInertia unit to create from, The default unit is MeterToTheFourth
    """
    def __init__(self, value: float, from_unit: AreaMomentOfInertiaUnits = AreaMomentOfInertiaUnits.MeterToTheFourth):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__meters_to_the_fourth = None
        
        self.__decimeters_to_the_fourth = None
        
        self.__centimeters_to_the_fourth = None
        
        self.__millimeters_to_the_fourth = None
        
        self.__feet_to_the_fourth = None
        
        self.__inches_to_the_fourth = None
        

    def convert(self, unit: AreaMomentOfInertiaUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: AreaMomentOfInertiaUnits) -> float:
        value = self._value
        
        if from_unit == AreaMomentOfInertiaUnits.MeterToTheFourth:
            return (value)
        
        if from_unit == AreaMomentOfInertiaUnits.DecimeterToTheFourth:
            return (value * 1e4)
        
        if from_unit == AreaMomentOfInertiaUnits.CentimeterToTheFourth:
            return (value * 1e8)
        
        if from_unit == AreaMomentOfInertiaUnits.MillimeterToTheFourth:
            return (value * 1e12)
        
        if from_unit == AreaMomentOfInertiaUnits.FootToTheFourth:
            return (value / math.pow(0.3048, 4))
        
        if from_unit == AreaMomentOfInertiaUnits.InchToTheFourth:
            return (value / math.pow(2.54e-2, 4))
        
        return None


    def __convert_to_base(self, value: float, to_unit: AreaMomentOfInertiaUnits) -> float:
        
        if to_unit == AreaMomentOfInertiaUnits.MeterToTheFourth:
            return (value)
        
        if to_unit == AreaMomentOfInertiaUnits.DecimeterToTheFourth:
            return (value / 1e4)
        
        if to_unit == AreaMomentOfInertiaUnits.CentimeterToTheFourth:
            return (value / 1e8)
        
        if to_unit == AreaMomentOfInertiaUnits.MillimeterToTheFourth:
            return (value / 1e12)
        
        if to_unit == AreaMomentOfInertiaUnits.FootToTheFourth:
            return (value * math.pow(0.3048, 4))
        
        if to_unit == AreaMomentOfInertiaUnits.InchToTheFourth:
            return (value * math.pow(2.54e-2, 4))
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_meters_to_the_fourth(meters_to_the_fourth: float):
        """
        Create a new instance of AreaMomentOfInertia from a value in meters_to_the_fourth.

        

        :param meters: The AreaMomentOfInertia value in meters_to_the_fourth.
        :type meters_to_the_fourth: float
        :return: A new instance of AreaMomentOfInertia.
        :rtype: AreaMomentOfInertia
        """
        return AreaMomentOfInertia(meters_to_the_fourth, AreaMomentOfInertiaUnits.MeterToTheFourth)

    
    @staticmethod
    def from_decimeters_to_the_fourth(decimeters_to_the_fourth: float):
        """
        Create a new instance of AreaMomentOfInertia from a value in decimeters_to_the_fourth.

        

        :param meters: The AreaMomentOfInertia value in decimeters_to_the_fourth.
        :type decimeters_to_the_fourth: float
        :return: A new instance of AreaMomentOfInertia.
        :rtype: AreaMomentOfInertia
        """
        return AreaMomentOfInertia(decimeters_to_the_fourth, AreaMomentOfInertiaUnits.DecimeterToTheFourth)

    
    @staticmethod
    def from_centimeters_to_the_fourth(centimeters_to_the_fourth: float):
        """
        Create a new instance of AreaMomentOfInertia from a value in centimeters_to_the_fourth.

        

        :param meters: The AreaMomentOfInertia value in centimeters_to_the_fourth.
        :type centimeters_to_the_fourth: float
        :return: A new instance of AreaMomentOfInertia.
        :rtype: AreaMomentOfInertia
        """
        return AreaMomentOfInertia(centimeters_to_the_fourth, AreaMomentOfInertiaUnits.CentimeterToTheFourth)

    
    @staticmethod
    def from_millimeters_to_the_fourth(millimeters_to_the_fourth: float):
        """
        Create a new instance of AreaMomentOfInertia from a value in millimeters_to_the_fourth.

        

        :param meters: The AreaMomentOfInertia value in millimeters_to_the_fourth.
        :type millimeters_to_the_fourth: float
        :return: A new instance of AreaMomentOfInertia.
        :rtype: AreaMomentOfInertia
        """
        return AreaMomentOfInertia(millimeters_to_the_fourth, AreaMomentOfInertiaUnits.MillimeterToTheFourth)

    
    @staticmethod
    def from_feet_to_the_fourth(feet_to_the_fourth: float):
        """
        Create a new instance of AreaMomentOfInertia from a value in feet_to_the_fourth.

        

        :param meters: The AreaMomentOfInertia value in feet_to_the_fourth.
        :type feet_to_the_fourth: float
        :return: A new instance of AreaMomentOfInertia.
        :rtype: AreaMomentOfInertia
        """
        return AreaMomentOfInertia(feet_to_the_fourth, AreaMomentOfInertiaUnits.FootToTheFourth)

    
    @staticmethod
    def from_inches_to_the_fourth(inches_to_the_fourth: float):
        """
        Create a new instance of AreaMomentOfInertia from a value in inches_to_the_fourth.

        

        :param meters: The AreaMomentOfInertia value in inches_to_the_fourth.
        :type inches_to_the_fourth: float
        :return: A new instance of AreaMomentOfInertia.
        :rtype: AreaMomentOfInertia
        """
        return AreaMomentOfInertia(inches_to_the_fourth, AreaMomentOfInertiaUnits.InchToTheFourth)

    
    @property
    def meters_to_the_fourth(self) -> float:
        """
        
        """
        if self.__meters_to_the_fourth != None:
            return self.__meters_to_the_fourth
        self.__meters_to_the_fourth = self.__convert_from_base(AreaMomentOfInertiaUnits.MeterToTheFourth)
        return self.__meters_to_the_fourth

    
    @property
    def decimeters_to_the_fourth(self) -> float:
        """
        
        """
        if self.__decimeters_to_the_fourth != None:
            return self.__decimeters_to_the_fourth
        self.__decimeters_to_the_fourth = self.__convert_from_base(AreaMomentOfInertiaUnits.DecimeterToTheFourth)
        return self.__decimeters_to_the_fourth

    
    @property
    def centimeters_to_the_fourth(self) -> float:
        """
        
        """
        if self.__centimeters_to_the_fourth != None:
            return self.__centimeters_to_the_fourth
        self.__centimeters_to_the_fourth = self.__convert_from_base(AreaMomentOfInertiaUnits.CentimeterToTheFourth)
        return self.__centimeters_to_the_fourth

    
    @property
    def millimeters_to_the_fourth(self) -> float:
        """
        
        """
        if self.__millimeters_to_the_fourth != None:
            return self.__millimeters_to_the_fourth
        self.__millimeters_to_the_fourth = self.__convert_from_base(AreaMomentOfInertiaUnits.MillimeterToTheFourth)
        return self.__millimeters_to_the_fourth

    
    @property
    def feet_to_the_fourth(self) -> float:
        """
        
        """
        if self.__feet_to_the_fourth != None:
            return self.__feet_to_the_fourth
        self.__feet_to_the_fourth = self.__convert_from_base(AreaMomentOfInertiaUnits.FootToTheFourth)
        return self.__feet_to_the_fourth

    
    @property
    def inches_to_the_fourth(self) -> float:
        """
        
        """
        if self.__inches_to_the_fourth != None:
            return self.__inches_to_the_fourth
        self.__inches_to_the_fourth = self.__convert_from_base(AreaMomentOfInertiaUnits.InchToTheFourth)
        return self.__inches_to_the_fourth

    
    def to_string(self, unit: AreaMomentOfInertiaUnits = AreaMomentOfInertiaUnits.MeterToTheFourth) -> str:
        """
        Format the AreaMomentOfInertia to string.
        Note! the default format for AreaMomentOfInertia is MeterToTheFourth.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AreaMomentOfInertiaUnits.MeterToTheFourth:
            return f"""{self.meters_to_the_fourth} m⁴"""
        
        if unit == AreaMomentOfInertiaUnits.DecimeterToTheFourth:
            return f"""{self.decimeters_to_the_fourth} dm⁴"""
        
        if unit == AreaMomentOfInertiaUnits.CentimeterToTheFourth:
            return f"""{self.centimeters_to_the_fourth} cm⁴"""
        
        if unit == AreaMomentOfInertiaUnits.MillimeterToTheFourth:
            return f"""{self.millimeters_to_the_fourth} mm⁴"""
        
        if unit == AreaMomentOfInertiaUnits.FootToTheFourth:
            return f"""{self.feet_to_the_fourth} ft⁴"""
        
        if unit == AreaMomentOfInertiaUnits.InchToTheFourth:
            return f"""{self.inches_to_the_fourth} in⁴"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AreaMomentOfInertiaUnits = AreaMomentOfInertiaUnits.MeterToTheFourth) -> str:
        """
        Get AreaMomentOfInertia unit abbreviation.
        Note! the default abbreviation for AreaMomentOfInertia is MeterToTheFourth.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AreaMomentOfInertiaUnits.MeterToTheFourth:
            return """m⁴"""
        
        if unit_abbreviation == AreaMomentOfInertiaUnits.DecimeterToTheFourth:
            return """dm⁴"""
        
        if unit_abbreviation == AreaMomentOfInertiaUnits.CentimeterToTheFourth:
            return """cm⁴"""
        
        if unit_abbreviation == AreaMomentOfInertiaUnits.MillimeterToTheFourth:
            return """mm⁴"""
        
        if unit_abbreviation == AreaMomentOfInertiaUnits.FootToTheFourth:
            return """ft⁴"""
        
        if unit_abbreviation == AreaMomentOfInertiaUnits.InchToTheFourth:
            return """in⁴"""
        