from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class HeatTransferCoefficientUnits(Enum):
        """
            HeatTransferCoefficientUnits enumeration
        """
        
        WattPerSquareMeterKelvin = 'WattPerSquareMeterKelvin'
        """
            
        """
        
        WattPerSquareMeterCelsius = 'WattPerSquareMeterCelsius'
        """
            
        """
        
        BtuPerHourSquareFootDegreeFahrenheit = 'BtuPerHourSquareFootDegreeFahrenheit'
        """
            
        """
        
        CaloriePerHourSquareMeterDegreeCelsius = 'CaloriePerHourSquareMeterDegreeCelsius'
        """
            
        """
        
        KilocaloriePerHourSquareMeterDegreeCelsius = 'KilocaloriePerHourSquareMeterDegreeCelsius'
        """
            
        """
        

class HeatTransferCoefficientDto:
    """
    A DTO representation of a HeatTransferCoefficient

    Attributes:
        value (float): The value of the HeatTransferCoefficient.
        unit (HeatTransferCoefficientUnits): The specific unit that the HeatTransferCoefficient value is representing.
    """

    def __init__(self, value: float, unit: HeatTransferCoefficientUnits):
        """
        Create a new DTO representation of a HeatTransferCoefficient

        Parameters:
            value (float): The value of the HeatTransferCoefficient.
            unit (HeatTransferCoefficientUnits): The specific unit that the HeatTransferCoefficient value is representing.
        """
        self.value: float = value
        """
        The value of the HeatTransferCoefficient
        """
        self.unit: HeatTransferCoefficientUnits = unit
        """
        The specific unit that the HeatTransferCoefficient value is representing
        """

    def to_json(self):
        """
        Get a HeatTransferCoefficient DTO JSON object representing the current unit.

        :return: JSON object represents HeatTransferCoefficient DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerSquareMeterKelvin"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of HeatTransferCoefficient DTO from a json representation.

        :param data: The HeatTransferCoefficient DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerSquareMeterKelvin"}
        :return: A new instance of HeatTransferCoefficientDto.
        :rtype: HeatTransferCoefficientDto
        """
        return HeatTransferCoefficientDto(value=data["value"], unit=HeatTransferCoefficientUnits(data["unit"]))


class HeatTransferCoefficient(AbstractMeasure):
    """
    The heat transfer coefficient or film coefficient, or film effectiveness, in thermodynamics and in mechanics is the proportionality constant between the heat flux and the thermodynamic driving force for the flow of heat (i.e., the temperature difference, ΔT)

    Args:
        value (float): The value.
        from_unit (HeatTransferCoefficientUnits): The HeatTransferCoefficient unit to create from, The default unit is WattPerSquareMeterKelvin
    """
    def __init__(self, value: float, from_unit: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_square_meter_kelvin = None
        
        self.__watts_per_square_meter_celsius = None
        
        self.__btus_per_hour_square_foot_degree_fahrenheit = None
        
        self.__calories_per_hour_square_meter_degree_celsius = None
        
        self.__kilocalories_per_hour_square_meter_degree_celsius = None
        

    def convert(self, unit: HeatTransferCoefficientUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin) -> HeatTransferCoefficientDto:
        """
        Get a new instance of HeatTransferCoefficient DTO representing the current unit.

        :param hold_in_unit: The specific HeatTransferCoefficient unit to store the HeatTransferCoefficient value in the DTO representation.
        :type hold_in_unit: HeatTransferCoefficientUnits
        :return: A new instance of HeatTransferCoefficientDto.
        :rtype: HeatTransferCoefficientDto
        """
        return HeatTransferCoefficientDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin):
        """
        Get a HeatTransferCoefficient DTO JSON object representing the current unit.

        :param hold_in_unit: The specific HeatTransferCoefficient unit to store the HeatTransferCoefficient value in the DTO representation.
        :type hold_in_unit: HeatTransferCoefficientUnits
        :return: JSON object represents HeatTransferCoefficient DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerSquareMeterKelvin"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(heat_transfer_coefficient_dto: HeatTransferCoefficientDto):
        """
        Obtain a new instance of HeatTransferCoefficient from a DTO unit object.

        :param heat_transfer_coefficient_dto: The HeatTransferCoefficient DTO representation.
        :type heat_transfer_coefficient_dto: HeatTransferCoefficientDto
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(heat_transfer_coefficient_dto.value, heat_transfer_coefficient_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of HeatTransferCoefficient from a DTO unit json representation.

        :param data: The HeatTransferCoefficient DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerSquareMeterKelvin"}
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient.from_dto(HeatTransferCoefficientDto.from_json(data))

    def __convert_from_base(self, from_unit: HeatTransferCoefficientUnits) -> float:
        value = self._value
        
        if from_unit == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return (value)
        
        if from_unit == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return (value)
        
        if from_unit == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return (value / 5.6782633411134878)
        
        if from_unit == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return ((value / 4.1868) * 3600)
        
        if from_unit == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return (((value / 4.1868) * 3600) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: HeatTransferCoefficientUnits) -> float:
        
        if to_unit == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return (value)
        
        if to_unit == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return (value)
        
        if to_unit == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return (value * 5.6782633411134878)
        
        if to_unit == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return ((value * 4.1868) / 3600)
        
        if to_unit == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return (((value * 4.1868) / 3600) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts_per_square_meter_kelvin(watts_per_square_meter_kelvin: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in watts_per_square_meter_kelvin.

        

        :param meters: The HeatTransferCoefficient value in watts_per_square_meter_kelvin.
        :type watts_per_square_meter_kelvin: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(watts_per_square_meter_kelvin, HeatTransferCoefficientUnits.WattPerSquareMeterKelvin)

    
    @staticmethod
    def from_watts_per_square_meter_celsius(watts_per_square_meter_celsius: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in watts_per_square_meter_celsius.

        

        :param meters: The HeatTransferCoefficient value in watts_per_square_meter_celsius.
        :type watts_per_square_meter_celsius: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(watts_per_square_meter_celsius, HeatTransferCoefficientUnits.WattPerSquareMeterCelsius)

    
    @staticmethod
    def from_btus_per_hour_square_foot_degree_fahrenheit(btus_per_hour_square_foot_degree_fahrenheit: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in btus_per_hour_square_foot_degree_fahrenheit.

        

        :param meters: The HeatTransferCoefficient value in btus_per_hour_square_foot_degree_fahrenheit.
        :type btus_per_hour_square_foot_degree_fahrenheit: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(btus_per_hour_square_foot_degree_fahrenheit, HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit)

    
    @staticmethod
    def from_calories_per_hour_square_meter_degree_celsius(calories_per_hour_square_meter_degree_celsius: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in calories_per_hour_square_meter_degree_celsius.

        

        :param meters: The HeatTransferCoefficient value in calories_per_hour_square_meter_degree_celsius.
        :type calories_per_hour_square_meter_degree_celsius: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(calories_per_hour_square_meter_degree_celsius, HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius)

    
    @staticmethod
    def from_kilocalories_per_hour_square_meter_degree_celsius(kilocalories_per_hour_square_meter_degree_celsius: float):
        """
        Create a new instance of HeatTransferCoefficient from a value in kilocalories_per_hour_square_meter_degree_celsius.

        

        :param meters: The HeatTransferCoefficient value in kilocalories_per_hour_square_meter_degree_celsius.
        :type kilocalories_per_hour_square_meter_degree_celsius: float
        :return: A new instance of HeatTransferCoefficient.
        :rtype: HeatTransferCoefficient
        """
        return HeatTransferCoefficient(kilocalories_per_hour_square_meter_degree_celsius, HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius)

    
    @property
    def watts_per_square_meter_kelvin(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter_kelvin != None:
            return self.__watts_per_square_meter_kelvin
        self.__watts_per_square_meter_kelvin = self.__convert_from_base(HeatTransferCoefficientUnits.WattPerSquareMeterKelvin)
        return self.__watts_per_square_meter_kelvin

    
    @property
    def watts_per_square_meter_celsius(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter_celsius != None:
            return self.__watts_per_square_meter_celsius
        self.__watts_per_square_meter_celsius = self.__convert_from_base(HeatTransferCoefficientUnits.WattPerSquareMeterCelsius)
        return self.__watts_per_square_meter_celsius

    
    @property
    def btus_per_hour_square_foot_degree_fahrenheit(self) -> float:
        """
        
        """
        if self.__btus_per_hour_square_foot_degree_fahrenheit != None:
            return self.__btus_per_hour_square_foot_degree_fahrenheit
        self.__btus_per_hour_square_foot_degree_fahrenheit = self.__convert_from_base(HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit)
        return self.__btus_per_hour_square_foot_degree_fahrenheit

    
    @property
    def calories_per_hour_square_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__calories_per_hour_square_meter_degree_celsius != None:
            return self.__calories_per_hour_square_meter_degree_celsius
        self.__calories_per_hour_square_meter_degree_celsius = self.__convert_from_base(HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius)
        return self.__calories_per_hour_square_meter_degree_celsius

    
    @property
    def kilocalories_per_hour_square_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilocalories_per_hour_square_meter_degree_celsius != None:
            return self.__kilocalories_per_hour_square_meter_degree_celsius
        self.__kilocalories_per_hour_square_meter_degree_celsius = self.__convert_from_base(HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius)
        return self.__kilocalories_per_hour_square_meter_degree_celsius

    
    def to_string(self, unit: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin, fractional_digits: int = None) -> str:
        """
        Format the HeatTransferCoefficient to a string.
        
        Note: the default format for HeatTransferCoefficient is WattPerSquareMeterKelvin.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the HeatTransferCoefficient. Default is 'WattPerSquareMeterKelvin'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return f"""{super()._truncate_fraction_digits(self.watts_per_square_meter_kelvin, fractional_digits)} W/m²·K"""
        
        if unit == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return f"""{super()._truncate_fraction_digits(self.watts_per_square_meter_celsius, fractional_digits)} W/m²·°C"""
        
        if unit == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return f"""{super()._truncate_fraction_digits(self.btus_per_hour_square_foot_degree_fahrenheit, fractional_digits)} Btu/h·ft²·°F"""
        
        if unit == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return f"""{super()._truncate_fraction_digits(self.calories_per_hour_square_meter_degree_celsius, fractional_digits)} kcal/h·m²·°C"""
        
        if unit == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return f"""{super()._truncate_fraction_digits(self.kilocalories_per_hour_square_meter_degree_celsius, fractional_digits)} kkcal/h·m²·°C"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: HeatTransferCoefficientUnits = HeatTransferCoefficientUnits.WattPerSquareMeterKelvin) -> str:
        """
        Get HeatTransferCoefficient unit abbreviation.
        Note! the default abbreviation for HeatTransferCoefficient is WattPerSquareMeterKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == HeatTransferCoefficientUnits.WattPerSquareMeterKelvin:
            return """W/m²·K"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.WattPerSquareMeterCelsius:
            return """W/m²·°C"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.BtuPerHourSquareFootDegreeFahrenheit:
            return """Btu/h·ft²·°F"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.CaloriePerHourSquareMeterDegreeCelsius:
            return """kcal/h·m²·°C"""
        
        if unit_abbreviation == HeatTransferCoefficientUnits.KilocaloriePerHourSquareMeterDegreeCelsius:
            return """kkcal/h·m²·°C"""
        