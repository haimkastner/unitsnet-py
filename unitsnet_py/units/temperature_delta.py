from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class TemperatureDeltaUnits(Enum):
        """
            TemperatureDeltaUnits enumeration
        """
        
        Kelvin = 'Kelvin'
        """
            
        """
        
        DegreeCelsius = 'DegreeCelsius'
        """
            
        """
        
        DegreeDelisle = 'DegreeDelisle'
        """
            
        """
        
        DegreeFahrenheit = 'DegreeFahrenheit'
        """
            
        """
        
        DegreeNewton = 'DegreeNewton'
        """
            
        """
        
        DegreeRankine = 'DegreeRankine'
        """
            
        """
        
        DegreeReaumur = 'DegreeReaumur'
        """
            
        """
        
        DegreeRoemer = 'DegreeRoemer'
        """
            
        """
        
        MillidegreeCelsius = 'MillidegreeCelsius'
        """
            
        """
        

class TemperatureDeltaDto:
    """
    A DTO representation of a TemperatureDelta

    Attributes:
        value (float): The value of the TemperatureDelta.
        unit (TemperatureDeltaUnits): The specific unit that the TemperatureDelta value is representing.
    """

    def __init__(self, value: float, unit: TemperatureDeltaUnits):
        """
        Create a new DTO representation of a TemperatureDelta

        Parameters:
            value (float): The value of the TemperatureDelta.
            unit (TemperatureDeltaUnits): The specific unit that the TemperatureDelta value is representing.
        """
        self.value: float = value
        """
        The value of the TemperatureDelta
        """
        self.unit: TemperatureDeltaUnits = unit
        """
        The specific unit that the TemperatureDelta value is representing
        """

    def to_json(self):
        """
        Get a TemperatureDelta DTO JSON object representing the current unit.

        :return: JSON object represents TemperatureDelta DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Kelvin"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of TemperatureDelta DTO from a json representation.

        :param data: The TemperatureDelta DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Kelvin"}
        :return: A new instance of TemperatureDeltaDto.
        :rtype: TemperatureDeltaDto
        """
        return TemperatureDeltaDto(value=data["value"], unit=TemperatureDeltaUnits(data["unit"]))


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

    def to_dto(self, hold_in_unit: TemperatureDeltaUnits = TemperatureDeltaUnits.Kelvin) -> TemperatureDeltaDto:
        """
        Get a new instance of TemperatureDelta DTO representing the current unit.

        :param hold_in_unit: The specific TemperatureDelta unit to store the TemperatureDelta value in the DTO representation.
        :type hold_in_unit: TemperatureDeltaUnits
        :return: A new instance of TemperatureDeltaDto.
        :rtype: TemperatureDeltaDto
        """
        return TemperatureDeltaDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: TemperatureDeltaUnits = TemperatureDeltaUnits.Kelvin):
        """
        Get a TemperatureDelta DTO JSON object representing the current unit.

        :param hold_in_unit: The specific TemperatureDelta unit to store the TemperatureDelta value in the DTO representation.
        :type hold_in_unit: TemperatureDeltaUnits
        :return: JSON object represents TemperatureDelta DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Kelvin"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(temperature_delta_dto: TemperatureDeltaDto):
        """
        Obtain a new instance of TemperatureDelta from a DTO unit object.

        :param temperature_delta_dto: The TemperatureDelta DTO representation.
        :type temperature_delta_dto: TemperatureDeltaDto
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta(temperature_delta_dto.value, temperature_delta_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of TemperatureDelta from a DTO unit json representation.

        :param data: The TemperatureDelta DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Kelvin"}
        :return: A new instance of TemperatureDelta.
        :rtype: TemperatureDelta
        """
        return TemperatureDelta.from_dto(TemperatureDeltaDto.from_json(data))

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

    
    def to_string(self, unit: TemperatureDeltaUnits = TemperatureDeltaUnits.Kelvin, fractional_digits: int = None) -> str:
        """
        Format the TemperatureDelta to a string.
        
        Note: the default format for TemperatureDelta is Kelvin.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the TemperatureDelta. Default is 'Kelvin'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == TemperatureDeltaUnits.Kelvin:
            return f"""{super()._truncate_fraction_digits(self.kelvins, fractional_digits)} ∆K"""
        
        if unit == TemperatureDeltaUnits.DegreeCelsius:
            return f"""{super()._truncate_fraction_digits(self.degrees_celsius, fractional_digits)} ∆°C"""
        
        if unit == TemperatureDeltaUnits.DegreeDelisle:
            return f"""{super()._truncate_fraction_digits(self.degrees_delisle, fractional_digits)} ∆°De"""
        
        if unit == TemperatureDeltaUnits.DegreeFahrenheit:
            return f"""{super()._truncate_fraction_digits(self.degrees_fahrenheit, fractional_digits)} ∆°F"""
        
        if unit == TemperatureDeltaUnits.DegreeNewton:
            return f"""{super()._truncate_fraction_digits(self.degrees_newton, fractional_digits)} ∆°N"""
        
        if unit == TemperatureDeltaUnits.DegreeRankine:
            return f"""{super()._truncate_fraction_digits(self.degrees_rankine, fractional_digits)} ∆°R"""
        
        if unit == TemperatureDeltaUnits.DegreeReaumur:
            return f"""{super()._truncate_fraction_digits(self.degrees_reaumur, fractional_digits)} ∆°Ré"""
        
        if unit == TemperatureDeltaUnits.DegreeRoemer:
            return f"""{super()._truncate_fraction_digits(self.degrees_roemer, fractional_digits)} ∆°Rø"""
        
        if unit == TemperatureDeltaUnits.MillidegreeCelsius:
            return f"""{super()._truncate_fraction_digits(self.millidegrees_celsius, fractional_digits)} m∆°C"""
        
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
        