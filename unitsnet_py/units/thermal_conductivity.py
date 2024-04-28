from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ThermalConductivityUnits(Enum):
        """
            ThermalConductivityUnits enumeration
        """
        
        WattPerMeterKelvin = 'WattPerMeterKelvin'
        """
            
        """
        
        BtuPerHourFootFahrenheit = 'BtuPerHourFootFahrenheit'
        """
            
        """
        

class ThermalConductivityDto:
    """
    A DTO representation of a ThermalConductivity

    Attributes:
        value (float): The value of the ThermalConductivity.
        unit (ThermalConductivityUnits): The specific unit that the ThermalConductivity value is representing.
    """

    def __init__(self, value: float, unit: ThermalConductivityUnits):
        """
        Create a new DTO representation of a ThermalConductivity

        Parameters:
            value (float): The value of the ThermalConductivity.
            unit (ThermalConductivityUnits): The specific unit that the ThermalConductivity value is representing.
        """
        self.value: float = value
        """
        The value of the ThermalConductivity
        """
        self.unit: ThermalConductivityUnits = unit
        """
        The specific unit that the ThermalConductivity value is representing
        """

    def to_json(self):
        """
        Get a ThermalConductivity DTO JSON object representing the current unit.

        :return: JSON object represents ThermalConductivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerMeterKelvin"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ThermalConductivity DTO from a json representation.

        :param data: The ThermalConductivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerMeterKelvin"}
        :return: A new instance of ThermalConductivityDto.
        :rtype: ThermalConductivityDto
        """
        return ThermalConductivityDto(value=data["value"], unit=ThermalConductivityUnits(data["unit"]))


class ThermalConductivity(AbstractMeasure):
    """
    Thermal conductivity is the property of a material to conduct heat.

    Args:
        value (float): The value.
        from_unit (ThermalConductivityUnits): The ThermalConductivity unit to create from, The default unit is WattPerMeterKelvin
    """
    def __init__(self, value: float, from_unit: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_meter_kelvin = None
        
        self.__btus_per_hour_foot_fahrenheit = None
        

    def convert(self, unit: ThermalConductivityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin) -> ThermalConductivityDto:
        """
        Get a new instance of ThermalConductivity DTO representing the current unit.

        :param hold_in_unit: The specific ThermalConductivity unit to store the ThermalConductivity value in the DTO representation.
        :type hold_in_unit: ThermalConductivityUnits
        :return: A new instance of ThermalConductivityDto.
        :rtype: ThermalConductivityDto
        """
        return ThermalConductivityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin):
        """
        Get a ThermalConductivity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ThermalConductivity unit to store the ThermalConductivity value in the DTO representation.
        :type hold_in_unit: ThermalConductivityUnits
        :return: JSON object represents ThermalConductivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "WattPerMeterKelvin"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(thermal_conductivity_dto: ThermalConductivityDto):
        """
        Obtain a new instance of ThermalConductivity from a DTO unit object.

        :param thermal_conductivity_dto: The ThermalConductivity DTO representation.
        :type thermal_conductivity_dto: ThermalConductivityDto
        :return: A new instance of ThermalConductivity.
        :rtype: ThermalConductivity
        """
        return ThermalConductivity(thermal_conductivity_dto.value, thermal_conductivity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ThermalConductivity from a DTO unit json representation.

        :param data: The ThermalConductivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "WattPerMeterKelvin"}
        :return: A new instance of ThermalConductivity.
        :rtype: ThermalConductivity
        """
        return ThermalConductivity.from_dto(ThermalConductivityDto.from_json(data))

    def __convert_from_base(self, from_unit: ThermalConductivityUnits) -> float:
        value = self._value
        
        if from_unit == ThermalConductivityUnits.WattPerMeterKelvin:
            return (value)
        
        if from_unit == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return (value / 1.73073467)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ThermalConductivityUnits) -> float:
        
        if to_unit == ThermalConductivityUnits.WattPerMeterKelvin:
            return (value)
        
        if to_unit == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return (value * 1.73073467)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts_per_meter_kelvin(watts_per_meter_kelvin: float):
        """
        Create a new instance of ThermalConductivity from a value in watts_per_meter_kelvin.

        

        :param meters: The ThermalConductivity value in watts_per_meter_kelvin.
        :type watts_per_meter_kelvin: float
        :return: A new instance of ThermalConductivity.
        :rtype: ThermalConductivity
        """
        return ThermalConductivity(watts_per_meter_kelvin, ThermalConductivityUnits.WattPerMeterKelvin)

    
    @staticmethod
    def from_btus_per_hour_foot_fahrenheit(btus_per_hour_foot_fahrenheit: float):
        """
        Create a new instance of ThermalConductivity from a value in btus_per_hour_foot_fahrenheit.

        

        :param meters: The ThermalConductivity value in btus_per_hour_foot_fahrenheit.
        :type btus_per_hour_foot_fahrenheit: float
        :return: A new instance of ThermalConductivity.
        :rtype: ThermalConductivity
        """
        return ThermalConductivity(btus_per_hour_foot_fahrenheit, ThermalConductivityUnits.BtuPerHourFootFahrenheit)

    
    @property
    def watts_per_meter_kelvin(self) -> float:
        """
        
        """
        if self.__watts_per_meter_kelvin != None:
            return self.__watts_per_meter_kelvin
        self.__watts_per_meter_kelvin = self.__convert_from_base(ThermalConductivityUnits.WattPerMeterKelvin)
        return self.__watts_per_meter_kelvin

    
    @property
    def btus_per_hour_foot_fahrenheit(self) -> float:
        """
        
        """
        if self.__btus_per_hour_foot_fahrenheit != None:
            return self.__btus_per_hour_foot_fahrenheit
        self.__btus_per_hour_foot_fahrenheit = self.__convert_from_base(ThermalConductivityUnits.BtuPerHourFootFahrenheit)
        return self.__btus_per_hour_foot_fahrenheit

    
    def to_string(self, unit: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin, fractional_digits: int = None) -> str:
        """
        Format the ThermalConductivity to a string.
        
        Note: the default format for ThermalConductivity is WattPerMeterKelvin.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ThermalConductivity. Default is 'WattPerMeterKelvin'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ThermalConductivityUnits.WattPerMeterKelvin:
            return f"""{super()._truncate_fraction_digits(self.watts_per_meter_kelvin, fractional_digits)} W/m·K"""
        
        if unit == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return f"""{super()._truncate_fraction_digits(self.btus_per_hour_foot_fahrenheit, fractional_digits)} BTU/h·ft·°F"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ThermalConductivityUnits = ThermalConductivityUnits.WattPerMeterKelvin) -> str:
        """
        Get ThermalConductivity unit abbreviation.
        Note! the default abbreviation for ThermalConductivity is WattPerMeterKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ThermalConductivityUnits.WattPerMeterKelvin:
            return """W/m·K"""
        
        if unit_abbreviation == ThermalConductivityUnits.BtuPerHourFootFahrenheit:
            return """BTU/h·ft·°F"""
        