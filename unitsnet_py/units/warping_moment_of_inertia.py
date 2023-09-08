from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class WarpingMomentOfInertiaUnits(Enum):
        """
            WarpingMomentOfInertiaUnits enumeration
        """
        
        MeterToTheSixth = 'meter_to_the_sixth'
        """
            
        """
        
        DecimeterToTheSixth = 'decimeter_to_the_sixth'
        """
            
        """
        
        CentimeterToTheSixth = 'centimeter_to_the_sixth'
        """
            
        """
        
        MillimeterToTheSixth = 'millimeter_to_the_sixth'
        """
            
        """
        
        FootToTheSixth = 'foot_to_the_sixth'
        """
            
        """
        
        InchToTheSixth = 'inch_to_the_sixth'
        """
            
        """
        

class WarpingMomentOfInertia(AbstractMeasure):
    """
    A geometric property of an area that is used to determine the warping stress.

    Args:
        value (float): The value.
        from_unit (WarpingMomentOfInertiaUnits): The WarpingMomentOfInertia unit to create from, The default unit is MeterToTheSixth
    """
    def __init__(self, value: float, from_unit: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__meters_to_the_sixth = None
        
        self.__decimeters_to_the_sixth = None
        
        self.__centimeters_to_the_sixth = None
        
        self.__millimeters_to_the_sixth = None
        
        self.__feet_to_the_sixth = None
        
        self.__inches_to_the_sixth = None
        

    def convert(self, unit: WarpingMomentOfInertiaUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: WarpingMomentOfInertiaUnits) -> float:
        value = self._value
        
        if from_unit == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return (value)
        
        if from_unit == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return (value * 1e6)
        
        if from_unit == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return (value * 1e12)
        
        if from_unit == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return (value * 1e18)
        
        if from_unit == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return (value / math.pow(0.3048, 6))
        
        if from_unit == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return (value / math.pow(2.54e-2, 6))
        
        return None


    def __convert_to_base(self, value: float, to_unit: WarpingMomentOfInertiaUnits) -> float:
        
        if to_unit == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return (value)
        
        if to_unit == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return (value / 1e6)
        
        if to_unit == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return (value / 1e12)
        
        if to_unit == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return (value / 1e18)
        
        if to_unit == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return (value * math.pow(0.3048, 6))
        
        if to_unit == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return (value * math.pow(2.54e-2, 6))
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_meters_to_the_sixth(meters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in meters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in meters_to_the_sixth.
        :type meters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(meters_to_the_sixth, WarpingMomentOfInertiaUnits.MeterToTheSixth)

    
    @staticmethod
    def from_decimeters_to_the_sixth(decimeters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in decimeters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in decimeters_to_the_sixth.
        :type decimeters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(decimeters_to_the_sixth, WarpingMomentOfInertiaUnits.DecimeterToTheSixth)

    
    @staticmethod
    def from_centimeters_to_the_sixth(centimeters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in centimeters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in centimeters_to_the_sixth.
        :type centimeters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(centimeters_to_the_sixth, WarpingMomentOfInertiaUnits.CentimeterToTheSixth)

    
    @staticmethod
    def from_millimeters_to_the_sixth(millimeters_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in millimeters_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in millimeters_to_the_sixth.
        :type millimeters_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(millimeters_to_the_sixth, WarpingMomentOfInertiaUnits.MillimeterToTheSixth)

    
    @staticmethod
    def from_feet_to_the_sixth(feet_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in feet_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in feet_to_the_sixth.
        :type feet_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(feet_to_the_sixth, WarpingMomentOfInertiaUnits.FootToTheSixth)

    
    @staticmethod
    def from_inches_to_the_sixth(inches_to_the_sixth: float):
        """
        Create a new instance of WarpingMomentOfInertia from a value in inches_to_the_sixth.

        

        :param meters: The WarpingMomentOfInertia value in inches_to_the_sixth.
        :type inches_to_the_sixth: float
        :return: A new instance of WarpingMomentOfInertia.
        :rtype: WarpingMomentOfInertia
        """
        return WarpingMomentOfInertia(inches_to_the_sixth, WarpingMomentOfInertiaUnits.InchToTheSixth)

    
    @property
    def meters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__meters_to_the_sixth != None:
            return self.__meters_to_the_sixth
        self.__meters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.MeterToTheSixth)
        return self.__meters_to_the_sixth

    
    @property
    def decimeters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__decimeters_to_the_sixth != None:
            return self.__decimeters_to_the_sixth
        self.__decimeters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.DecimeterToTheSixth)
        return self.__decimeters_to_the_sixth

    
    @property
    def centimeters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__centimeters_to_the_sixth != None:
            return self.__centimeters_to_the_sixth
        self.__centimeters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.CentimeterToTheSixth)
        return self.__centimeters_to_the_sixth

    
    @property
    def millimeters_to_the_sixth(self) -> float:
        """
        
        """
        if self.__millimeters_to_the_sixth != None:
            return self.__millimeters_to_the_sixth
        self.__millimeters_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.MillimeterToTheSixth)
        return self.__millimeters_to_the_sixth

    
    @property
    def feet_to_the_sixth(self) -> float:
        """
        
        """
        if self.__feet_to_the_sixth != None:
            return self.__feet_to_the_sixth
        self.__feet_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.FootToTheSixth)
        return self.__feet_to_the_sixth

    
    @property
    def inches_to_the_sixth(self) -> float:
        """
        
        """
        if self.__inches_to_the_sixth != None:
            return self.__inches_to_the_sixth
        self.__inches_to_the_sixth = self.__convert_from_base(WarpingMomentOfInertiaUnits.InchToTheSixth)
        return self.__inches_to_the_sixth

    
    def to_string(self, unit: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth) -> str:
        """
        Format the WarpingMomentOfInertia to string.
        Note! the default format for WarpingMomentOfInertia is MeterToTheSixth.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return f"""{self.meters_to_the_sixth} m⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return f"""{self.decimeters_to_the_sixth} dm⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return f"""{self.centimeters_to_the_sixth} cm⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return f"""{self.millimeters_to_the_sixth} mm⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return f"""{self.feet_to_the_sixth} ft⁶"""
        
        if unit == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return f"""{self.inches_to_the_sixth} in⁶"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: WarpingMomentOfInertiaUnits = WarpingMomentOfInertiaUnits.MeterToTheSixth) -> str:
        """
        Get WarpingMomentOfInertia unit abbreviation.
        Note! the default abbreviation for WarpingMomentOfInertia is MeterToTheSixth.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.MeterToTheSixth:
            return """m⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.DecimeterToTheSixth:
            return """dm⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.CentimeterToTheSixth:
            return """cm⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.MillimeterToTheSixth:
            return """mm⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.FootToTheSixth:
            return """ft⁶"""
        
        if unit_abbreviation == WarpingMomentOfInertiaUnits.InchToTheSixth:
            return """in⁶"""
        