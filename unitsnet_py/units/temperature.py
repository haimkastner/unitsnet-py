from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TemperatureUnits(Enum):
        """
            TemperatureUnits enumeration
        """
        
        Kelvin = 'kelvin'
        """
            
        """
        
        DegreeCelsius = 'degree_celsius'
        """
            
        """
        
        MillidegreeCelsius = 'millidegree_celsius'
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
        
        SolarTemperature = 'solar_temperature'
        """
            
        """
        

class Temperature(AbstractMeasure):
    """
    A temperature is a numerical measure of hot or cold. Its measurement is by detection of heat radiation or particle velocity or kinetic energy, or by the bulk behavior of a thermometric material. It may be calibrated in any of various temperature scales, Celsius, Fahrenheit, Kelvin, etc. The fundamental physical definition of temperature is provided by thermodynamics.

    Args:
        value (float): The value.
        from_unit (TemperatureUnits): The Temperature unit to create from, The default unit is Kelvin
    """
    def __init__(self, value: float, from_unit: TemperatureUnits = TemperatureUnits.Kelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__kelvins = None
        
        self.__degrees_celsius = None
        
        self.__millidegrees_celsius = None
        
        self.__degrees_delisle = None
        
        self.__degrees_fahrenheit = None
        
        self.__degrees_newton = None
        
        self.__degrees_rankine = None
        
        self.__degrees_reaumur = None
        
        self.__degrees_roemer = None
        
        self.__solar_temperatures = None
        

    def convert(self, unit: TemperatureUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: TemperatureUnits) -> float:
        value = self._value
        
        if from_unit == TemperatureUnits.Kelvin:
            return (value)
        
        if from_unit == TemperatureUnits.DegreeCelsius:
            return (value - 273.15)
        
        if from_unit == TemperatureUnits.MillidegreeCelsius:
            return ((value - 273.15) * 1000)
        
        if from_unit == TemperatureUnits.DegreeDelisle:
            return ((value - 373.15) * -3 / 2)
        
        if from_unit == TemperatureUnits.DegreeFahrenheit:
            return ((value - 459.67 * 5 / 9) * 9 / 5)
        
        if from_unit == TemperatureUnits.DegreeNewton:
            return ((value - 273.15) * 33 / 100)
        
        if from_unit == TemperatureUnits.DegreeRankine:
            return (value * 9 / 5)
        
        if from_unit == TemperatureUnits.DegreeReaumur:
            return ((value - 273.15) * 4 / 5)
        
        if from_unit == TemperatureUnits.DegreeRoemer:
            return ((value - (273.15 - 7.5 * 40 / 21)) * 21 / 40)
        
        if from_unit == TemperatureUnits.SolarTemperature:
            return (value / 5778)
        
        return None


    def __convert_to_base(self, value: float, to_unit: TemperatureUnits) -> float:
        
        if to_unit == TemperatureUnits.Kelvin:
            return (value)
        
        if to_unit == TemperatureUnits.DegreeCelsius:
            return (value + 273.15)
        
        if to_unit == TemperatureUnits.MillidegreeCelsius:
            return (value / 1000 + 273.15)
        
        if to_unit == TemperatureUnits.DegreeDelisle:
            return (value * -2 / 3 + 373.15)
        
        if to_unit == TemperatureUnits.DegreeFahrenheit:
            return (value * 5 / 9 + 459.67 * 5 / 9)
        
        if to_unit == TemperatureUnits.DegreeNewton:
            return (value * 100 / 33 + 273.15)
        
        if to_unit == TemperatureUnits.DegreeRankine:
            return (value * 5 / 9)
        
        if to_unit == TemperatureUnits.DegreeReaumur:
            return (value * 5 / 4 + 273.15)
        
        if to_unit == TemperatureUnits.DegreeRoemer:
            return (value * 40 / 21 + 273.15 - 7.5 * 40 / 21)
        
        if to_unit == TemperatureUnits.SolarTemperature:
            return (value * 5778)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_kelvins(kelvins: float):
        """
        Create a new instance of Temperature from a value in kelvins.

        

        :param meters: The Temperature value in kelvins.
        :type kelvins: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(kelvins, TemperatureUnits.Kelvin)

    
    @staticmethod
    def from_degrees_celsius(degrees_celsius: float):
        """
        Create a new instance of Temperature from a value in degrees_celsius.

        

        :param meters: The Temperature value in degrees_celsius.
        :type degrees_celsius: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(degrees_celsius, TemperatureUnits.DegreeCelsius)

    
    @staticmethod
    def from_millidegrees_celsius(millidegrees_celsius: float):
        """
        Create a new instance of Temperature from a value in millidegrees_celsius.

        

        :param meters: The Temperature value in millidegrees_celsius.
        :type millidegrees_celsius: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(millidegrees_celsius, TemperatureUnits.MillidegreeCelsius)

    
    @staticmethod
    def from_degrees_delisle(degrees_delisle: float):
        """
        Create a new instance of Temperature from a value in degrees_delisle.

        

        :param meters: The Temperature value in degrees_delisle.
        :type degrees_delisle: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(degrees_delisle, TemperatureUnits.DegreeDelisle)

    
    @staticmethod
    def from_degrees_fahrenheit(degrees_fahrenheit: float):
        """
        Create a new instance of Temperature from a value in degrees_fahrenheit.

        

        :param meters: The Temperature value in degrees_fahrenheit.
        :type degrees_fahrenheit: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(degrees_fahrenheit, TemperatureUnits.DegreeFahrenheit)

    
    @staticmethod
    def from_degrees_newton(degrees_newton: float):
        """
        Create a new instance of Temperature from a value in degrees_newton.

        

        :param meters: The Temperature value in degrees_newton.
        :type degrees_newton: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(degrees_newton, TemperatureUnits.DegreeNewton)

    
    @staticmethod
    def from_degrees_rankine(degrees_rankine: float):
        """
        Create a new instance of Temperature from a value in degrees_rankine.

        

        :param meters: The Temperature value in degrees_rankine.
        :type degrees_rankine: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(degrees_rankine, TemperatureUnits.DegreeRankine)

    
    @staticmethod
    def from_degrees_reaumur(degrees_reaumur: float):
        """
        Create a new instance of Temperature from a value in degrees_reaumur.

        

        :param meters: The Temperature value in degrees_reaumur.
        :type degrees_reaumur: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(degrees_reaumur, TemperatureUnits.DegreeReaumur)

    
    @staticmethod
    def from_degrees_roemer(degrees_roemer: float):
        """
        Create a new instance of Temperature from a value in degrees_roemer.

        

        :param meters: The Temperature value in degrees_roemer.
        :type degrees_roemer: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(degrees_roemer, TemperatureUnits.DegreeRoemer)

    
    @staticmethod
    def from_solar_temperatures(solar_temperatures: float):
        """
        Create a new instance of Temperature from a value in solar_temperatures.

        

        :param meters: The Temperature value in solar_temperatures.
        :type solar_temperatures: float
        :return: A new instance of Temperature.
        :rtype: Temperature
        """
        return Temperature(solar_temperatures, TemperatureUnits.SolarTemperature)

    
    @property
    def kelvins(self) -> float:
        """
        
        """
        if self.__kelvins != None:
            return self.__kelvins
        self.__kelvins = self.__convert_from_base(TemperatureUnits.Kelvin)
        return self.__kelvins

    
    @property
    def degrees_celsius(self) -> float:
        """
        
        """
        if self.__degrees_celsius != None:
            return self.__degrees_celsius
        self.__degrees_celsius = self.__convert_from_base(TemperatureUnits.DegreeCelsius)
        return self.__degrees_celsius

    
    @property
    def millidegrees_celsius(self) -> float:
        """
        
        """
        if self.__millidegrees_celsius != None:
            return self.__millidegrees_celsius
        self.__millidegrees_celsius = self.__convert_from_base(TemperatureUnits.MillidegreeCelsius)
        return self.__millidegrees_celsius

    
    @property
    def degrees_delisle(self) -> float:
        """
        
        """
        if self.__degrees_delisle != None:
            return self.__degrees_delisle
        self.__degrees_delisle = self.__convert_from_base(TemperatureUnits.DegreeDelisle)
        return self.__degrees_delisle

    
    @property
    def degrees_fahrenheit(self) -> float:
        """
        
        """
        if self.__degrees_fahrenheit != None:
            return self.__degrees_fahrenheit
        self.__degrees_fahrenheit = self.__convert_from_base(TemperatureUnits.DegreeFahrenheit)
        return self.__degrees_fahrenheit

    
    @property
    def degrees_newton(self) -> float:
        """
        
        """
        if self.__degrees_newton != None:
            return self.__degrees_newton
        self.__degrees_newton = self.__convert_from_base(TemperatureUnits.DegreeNewton)
        return self.__degrees_newton

    
    @property
    def degrees_rankine(self) -> float:
        """
        
        """
        if self.__degrees_rankine != None:
            return self.__degrees_rankine
        self.__degrees_rankine = self.__convert_from_base(TemperatureUnits.DegreeRankine)
        return self.__degrees_rankine

    
    @property
    def degrees_reaumur(self) -> float:
        """
        
        """
        if self.__degrees_reaumur != None:
            return self.__degrees_reaumur
        self.__degrees_reaumur = self.__convert_from_base(TemperatureUnits.DegreeReaumur)
        return self.__degrees_reaumur

    
    @property
    def degrees_roemer(self) -> float:
        """
        
        """
        if self.__degrees_roemer != None:
            return self.__degrees_roemer
        self.__degrees_roemer = self.__convert_from_base(TemperatureUnits.DegreeRoemer)
        return self.__degrees_roemer

    
    @property
    def solar_temperatures(self) -> float:
        """
        
        """
        if self.__solar_temperatures != None:
            return self.__solar_temperatures
        self.__solar_temperatures = self.__convert_from_base(TemperatureUnits.SolarTemperature)
        return self.__solar_temperatures

    
    def to_string(self, unit: TemperatureUnits = TemperatureUnits.Kelvin) -> str:
        """
        Format the Temperature to string.
        Note! the default format for Temperature is Kelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == TemperatureUnits.Kelvin:
            return f"""{self.kelvins} K"""
        
        if unit == TemperatureUnits.DegreeCelsius:
            return f"""{self.degrees_celsius} °C"""
        
        if unit == TemperatureUnits.MillidegreeCelsius:
            return f"""{self.millidegrees_celsius} m°C"""
        
        if unit == TemperatureUnits.DegreeDelisle:
            return f"""{self.degrees_delisle} °De"""
        
        if unit == TemperatureUnits.DegreeFahrenheit:
            return f"""{self.degrees_fahrenheit} °F"""
        
        if unit == TemperatureUnits.DegreeNewton:
            return f"""{self.degrees_newton} °N"""
        
        if unit == TemperatureUnits.DegreeRankine:
            return f"""{self.degrees_rankine} °R"""
        
        if unit == TemperatureUnits.DegreeReaumur:
            return f"""{self.degrees_reaumur} °Ré"""
        
        if unit == TemperatureUnits.DegreeRoemer:
            return f"""{self.degrees_roemer} °Rø"""
        
        if unit == TemperatureUnits.SolarTemperature:
            return f"""{self.solar_temperatures} T⊙"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: TemperatureUnits = TemperatureUnits.Kelvin) -> str:
        """
        Get Temperature unit abbreviation.
        Note! the default abbreviation for Temperature is Kelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == TemperatureUnits.Kelvin:
            return """K"""
        
        if unit_abbreviation == TemperatureUnits.DegreeCelsius:
            return """°C"""
        
        if unit_abbreviation == TemperatureUnits.MillidegreeCelsius:
            return """m°C"""
        
        if unit_abbreviation == TemperatureUnits.DegreeDelisle:
            return """°De"""
        
        if unit_abbreviation == TemperatureUnits.DegreeFahrenheit:
            return """°F"""
        
        if unit_abbreviation == TemperatureUnits.DegreeNewton:
            return """°N"""
        
        if unit_abbreviation == TemperatureUnits.DegreeRankine:
            return """°R"""
        
        if unit_abbreviation == TemperatureUnits.DegreeReaumur:
            return """°Ré"""
        
        if unit_abbreviation == TemperatureUnits.DegreeRoemer:
            return """°Rø"""
        
        if unit_abbreviation == TemperatureUnits.SolarTemperature:
            return """T⊙"""
        