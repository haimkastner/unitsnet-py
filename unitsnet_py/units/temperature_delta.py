from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TemperatureDeltaUnits(Enum):
        """
            TemperatureDeltaUnits enumeration
        """
        
        Kelvin = 'kelvin'
        """
            
        """
        
        DegreeCelsius = 'degree_celsius'
        """
            
        """
        
        DegreeDelisle = 'degree_delisle'
        """
            
        """
        
        DegreeFahrenheit = 'degree_fahrenheit'
        """
            
        """
        
        DegreeNewton = 'degree_newton'
        """
            
        """
        
        DegreeRankine = 'degree_rankine'
        """
            
        """
        
        DegreeReaumur = 'degree_reaumur'
        """
            
        """
        
        DegreeRoemer = 'degree_roemer'
        """
            
        """
        
        MillidegreeCelsius = 'millidegree_celsius'
        """
            
        """
        

class TemperatureDelta(AbstractMeasure):
    """
    Difference between two temperatures. The conversions are different than for Temperature.

    Args:
        value (float): The value.
        from_unit (TemperatureDeltaUnits): The TemperatureDelta unit to create from, The default unit is Kelvin
    """
    def __init__(self, value: float, from_unit: TemperatureDeltaUnits = TemperatureDeltaUnits.Kelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__kelvins = None
        
        self.__degrees_celsius = None
        
        self.__degrees_delisle = None
        
        self.__degrees_fahrenheit = None
        
        self.__degrees_newton = None
        
        self.__degrees_rankine = None
        
        self.__degrees_reaumur = None
        
        self.__degrees_roemer = None
        
        self.__millidegrees_celsius = None
        

    def convert(self, unit: TemperatureDeltaUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: TemperatureDeltaUnits) -> float:
        value = self._value
        
        if from_unit == TemperatureDeltaUnits.Kelvin:
            return (value)
        
        if from_unit == TemperatureDeltaUnits.DegreeCelsius:
            return (value)
        
        if from_unit == TemperatureDeltaUnits.DegreeDelisle:
            return (value * -3 / 2)
        
        if from_unit == TemperatureDeltaUnits.DegreeFahrenheit:
            return (value * 9 / 5)
        
        if from_unit == TemperatureDeltaUnits.DegreeNewton:
            return (value * 33 / 100)
        
        if from_unit == TemperatureDeltaUnits.DegreeRankine:
            return (value * 9 / 5)
        
        if from_unit == TemperatureDeltaUnits.DegreeReaumur:
            return (value * 4 / 5)
        
        if from_unit == TemperatureDeltaUnits.DegreeRoemer:
            return (value * 21 / 40)
        
        if from_unit == TemperatureDeltaUnits.MillidegreeCelsius:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TemperatureDeltaUnits) -> float:
        
        if to_unit == TemperatureDeltaUnits.Kelvin:
            return (value)
        
        if to_unit == TemperatureDeltaUnits.DegreeCelsius:
            return (value)
        
        if to_unit == TemperatureDeltaUnits.DegreeDelisle:
            return (value * -2 / 3)
        
        if to_unit == TemperatureDeltaUnits.DegreeFahrenheit:
            return (value * 5 / 9)
        
        if to_unit == TemperatureDeltaUnits.DegreeNewton:
            return (value * 100 / 33)
        
        if to_unit == TemperatureDeltaUnits.DegreeRankine:
            return (value * 5 / 9)
        
        if to_unit == TemperatureDeltaUnits.DegreeReaumur:
            return (value * 5 / 4)
        
        if to_unit == TemperatureDeltaUnits.DegreeRoemer:
            return (value * 40 / 21)
        
        if to_unit == TemperatureDeltaUnits.MillidegreeCelsius:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_kelvins(kelvins: float):
        """
        Create a new instance of TemperatureDelta from a value in kelvins.

        

        :param meters: The TemperatureDelta value in kelvins.
        :type kelvins: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(kelvins, TemperatureDeltaUnits.Kelvin)

    
    @staticmethod
    def from_degrees_celsius(degrees_celsius: float):
        """
        Create a new instance of TemperatureDelta from a value in degrees_celsius.

        

        :param meters: The TemperatureDelta value in degrees_celsius.
        :type degrees_celsius: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(degrees_celsius, TemperatureDeltaUnits.DegreeCelsius)

    
    @staticmethod
    def from_degrees_delisle(degrees_delisle: float):
        """
        Create a new instance of TemperatureDelta from a value in degrees_delisle.

        

        :param meters: The TemperatureDelta value in degrees_delisle.
        :type degrees_delisle: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(degrees_delisle, TemperatureDeltaUnits.DegreeDelisle)

    
    @staticmethod
    def from_degrees_fahrenheit(degrees_fahrenheit: float):
        """
        Create a new instance of TemperatureDelta from a value in degrees_fahrenheit.

        

        :param meters: The TemperatureDelta value in degrees_fahrenheit.
        :type degrees_fahrenheit: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(degrees_fahrenheit, TemperatureDeltaUnits.DegreeFahrenheit)

    
    @staticmethod
    def from_degrees_newton(degrees_newton: float):
        """
        Create a new instance of TemperatureDelta from a value in degrees_newton.

        

        :param meters: The TemperatureDelta value in degrees_newton.
        :type degrees_newton: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(degrees_newton, TemperatureDeltaUnits.DegreeNewton)

    
    @staticmethod
    def from_degrees_rankine(degrees_rankine: float):
        """
        Create a new instance of TemperatureDelta from a value in degrees_rankine.

        

        :param meters: The TemperatureDelta value in degrees_rankine.
        :type degrees_rankine: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(degrees_rankine, TemperatureDeltaUnits.DegreeRankine)

    
    @staticmethod
    def from_degrees_reaumur(degrees_reaumur: float):
        """
        Create a new instance of TemperatureDelta from a value in degrees_reaumur.

        

        :param meters: The TemperatureDelta value in degrees_reaumur.
        :type degrees_reaumur: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(degrees_reaumur, TemperatureDeltaUnits.DegreeReaumur)

    
    @staticmethod
    def from_degrees_roemer(degrees_roemer: float):
        """
        Create a new instance of TemperatureDelta from a value in degrees_roemer.

        

        :param meters: The TemperatureDelta value in degrees_roemer.
        :type degrees_roemer: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(degrees_roemer, TemperatureDeltaUnits.DegreeRoemer)

    
    @staticmethod
    def from_millidegrees_celsius(millidegrees_celsius: float):
        """
        Create a new instance of TemperatureDelta from a value in millidegrees_celsius.

        

        :param meters: The TemperatureDelta value in millidegrees_celsius.
        :type millidegrees_celsius: float
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(millidegrees_celsius, TemperatureDeltaUnits.MillidegreeCelsius)

    
    @property
    def kelvins(self) -> float:
        """
        
        """
        if self.__kelvins != None:
            return self.__kelvins
        self.__kelvins = self.__convert_from_base(TemperatureDeltaUnits.Kelvin)
        return self.__kelvins

    
    @property
    def degrees_celsius(self) -> float:
        """
        
        """
        if self.__degrees_celsius != None:
            return self.__degrees_celsius
        self.__degrees_celsius = self.__convert_from_base(TemperatureDeltaUnits.DegreeCelsius)
        return self.__degrees_celsius

    
    @property
    def degrees_delisle(self) -> float:
        """
        
        """
        if self.__degrees_delisle != None:
            return self.__degrees_delisle
        self.__degrees_delisle = self.__convert_from_base(TemperatureDeltaUnits.DegreeDelisle)
        return self.__degrees_delisle

    
    @property
    def degrees_fahrenheit(self) -> float:
        """
        
        """
        if self.__degrees_fahrenheit != None:
            return self.__degrees_fahrenheit
        self.__degrees_fahrenheit = self.__convert_from_base(TemperatureDeltaUnits.DegreeFahrenheit)
        return self.__degrees_fahrenheit

    
    @property
    def degrees_newton(self) -> float:
        """
        
        """
        if self.__degrees_newton != None:
            return self.__degrees_newton
        self.__degrees_newton = self.__convert_from_base(TemperatureDeltaUnits.DegreeNewton)
        return self.__degrees_newton

    
    @property
    def degrees_rankine(self) -> float:
        """
        
        """
        if self.__degrees_rankine != None:
            return self.__degrees_rankine
        self.__degrees_rankine = self.__convert_from_base(TemperatureDeltaUnits.DegreeRankine)
        return self.__degrees_rankine

    
    @property
    def degrees_reaumur(self) -> float:
        """
        
        """
        if self.__degrees_reaumur != None:
            return self.__degrees_reaumur
        self.__degrees_reaumur = self.__convert_from_base(TemperatureDeltaUnits.DegreeReaumur)
        return self.__degrees_reaumur

    
    @property
    def degrees_roemer(self) -> float:
        """
        
        """
        if self.__degrees_roemer != None:
            return self.__degrees_roemer
        self.__degrees_roemer = self.__convert_from_base(TemperatureDeltaUnits.DegreeRoemer)
        return self.__degrees_roemer

    
    @property
    def millidegrees_celsius(self) -> float:
        """
        
        """
        if self.__millidegrees_celsius != None:
            return self.__millidegrees_celsius
        self.__millidegrees_celsius = self.__convert_from_base(TemperatureDeltaUnits.MillidegreeCelsius)
        return self.__millidegrees_celsius

    
    def to_string(self, unit: TemperatureDeltaUnits = TemperatureDeltaUnits.Kelvin) -> str:
        """
        Format the TemperatureDelta to string.
        Note! the default format for TemperatureDelta is Kelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TemperatureDeltaUnits.Kelvin:
            return f"""{self.kelvins} ∆K"""
        
        if unit == TemperatureDeltaUnits.DegreeCelsius:
            return f"""{self.degrees_celsius} ∆°C"""
        
        if unit == TemperatureDeltaUnits.DegreeDelisle:
            return f"""{self.degrees_delisle} ∆°De"""
        
        if unit == TemperatureDeltaUnits.DegreeFahrenheit:
            return f"""{self.degrees_fahrenheit} ∆°F"""
        
        if unit == TemperatureDeltaUnits.DegreeNewton:
            return f"""{self.degrees_newton} ∆°N"""
        
        if unit == TemperatureDeltaUnits.DegreeRankine:
            return f"""{self.degrees_rankine} ∆°R"""
        
        if unit == TemperatureDeltaUnits.DegreeReaumur:
            return f"""{self.degrees_reaumur} ∆°Ré"""
        
        if unit == TemperatureDeltaUnits.DegreeRoemer:
            return f"""{self.degrees_roemer} ∆°Rø"""
        
        if unit == TemperatureDeltaUnits.MillidegreeCelsius:
            return f"""{self.millidegrees_celsius} m∆°C"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: TemperatureDeltaUnits = TemperatureDeltaUnits.Kelvin) -> str:
        """
        Get TemperatureDelta unit abbreviation.
        Note! the default abbreviation for TemperatureDelta is Kelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TemperatureDeltaUnits.Kelvin:
            return """∆K"""
        
        if unit_abbreviation == TemperatureDeltaUnits.DegreeCelsius:
            return """∆°C"""
        
        if unit_abbreviation == TemperatureDeltaUnits.DegreeDelisle:
            return """∆°De"""
        
        if unit_abbreviation == TemperatureDeltaUnits.DegreeFahrenheit:
            return """∆°F"""
        
        if unit_abbreviation == TemperatureDeltaUnits.DegreeNewton:
            return """∆°N"""
        
        if unit_abbreviation == TemperatureDeltaUnits.DegreeRankine:
            return """∆°R"""
        
        if unit_abbreviation == TemperatureDeltaUnits.DegreeReaumur:
            return """∆°Ré"""
        
        if unit_abbreviation == TemperatureDeltaUnits.DegreeRoemer:
            return """∆°Rø"""
        
        if unit_abbreviation == TemperatureDeltaUnits.MillidegreeCelsius:
            return """m∆°C"""
        