from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ThermalResistanceUnits(Enum):
        """
            ThermalResistanceUnits enumeration
        """
        
        KelvinPerWatt = 'KelvinPerWatt'
        """
            
        """
        
        DegreeCelsiusPerWatt = 'DegreeCelsiusPerWatt'
        """
            
        """
        

class ThermalResistanceDto:
    """
    A DTO representation of a ThermalResistance

    Attributes:
        value (float): The value of the ThermalResistance.
        unit (ThermalResistanceUnits): The specific unit that the ThermalResistance value is representing.
    """

    def __init__(self, value: float, unit: ThermalResistanceUnits):
        """
        Create a new DTO representation of a ThermalResistance

        Parameters:
            value (float): The value of the ThermalResistance.
            unit (ThermalResistanceUnits): The specific unit that the ThermalResistance value is representing.
        """
        self.value: float = value
        """
        The value of the ThermalResistance
        """
        self.unit: ThermalResistanceUnits = unit
        """
        The specific unit that the ThermalResistance value is representing
        """

    def to_json(self):
        """
        Get a ThermalResistance DTO JSON object representing the current unit.

        :return: JSON object represents ThermalResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KelvinPerWatt"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ThermalResistance DTO from a json representation.

        :param data: The ThermalResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KelvinPerWatt"}
        :return: A new instance of ThermalResistanceDto.
        :rtype: ThermalResistanceDto
        """
        return ThermalResistanceDto(value=data["value"], unit=ThermalResistanceUnits(data["unit"]))


class ThermalResistance(AbstractMeasure):
    """
    Thermal resistance (R) measures the opposition to the heat current in a material or system. It is measured in units of kelvins per watt (K/W) and indicates how much temperature difference (in kelvins) is required to transfer a unit of heat current (in watts) through the material or object. It is essential to optimize the building insulation, evaluate the efficiency of electronic devices, and enhance the performance of heat sinks in various applications.

    Args:
        value (float): The value.
        from_unit (ThermalResistanceUnits): The ThermalResistance unit to create from, The default unit is KelvinPerWatt
    """
    def __init__(self, value: float, from_unit: ThermalResistanceUnits = ThermalResistanceUnits.KelvinPerWatt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__kelvins_per_watt = None
        
        self.__degrees_celsius_per_watt = None
        

    def convert(self, unit: ThermalResistanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ThermalResistanceUnits = ThermalResistanceUnits.KelvinPerWatt) -> ThermalResistanceDto:
        """
        Get a new instance of ThermalResistance DTO representing the current unit.

        :param hold_in_unit: The specific ThermalResistance unit to store the ThermalResistance value in the DTO representation.
        :type hold_in_unit: ThermalResistanceUnits
        :return: A new instance of ThermalResistanceDto.
        :rtype: ThermalResistanceDto
        """
        return ThermalResistanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ThermalResistanceUnits = ThermalResistanceUnits.KelvinPerWatt):
        """
        Get a ThermalResistance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ThermalResistance unit to store the ThermalResistance value in the DTO representation.
        :type hold_in_unit: ThermalResistanceUnits
        :return: JSON object represents ThermalResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KelvinPerWatt"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(thermal_resistance_dto: ThermalResistanceDto):
        """
        Obtain a new instance of ThermalResistance from a DTO unit object.

        :param thermal_resistance_dto: The ThermalResistance DTO representation.
        :type thermal_resistance_dto: ThermalResistanceDto
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(thermal_resistance_dto.value, thermal_resistance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ThermalResistance from a DTO unit json representation.

        :param data: The ThermalResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KelvinPerWatt"}
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance.from_dto(ThermalResistanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ThermalResistanceUnits) -> float:
        value = self._value
        
        if from_unit == ThermalResistanceUnits.KelvinPerWatt:
            return (value)
        
        if from_unit == ThermalResistanceUnits.DegreeCelsiusPerWatt:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ThermalResistanceUnits) -> float:
        
        if to_unit == ThermalResistanceUnits.KelvinPerWatt:
            return (value)
        
        if to_unit == ThermalResistanceUnits.DegreeCelsiusPerWatt:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_kelvins_per_watt(kelvins_per_watt: float):
        """
        Create a new instance of ThermalResistance from a value in kelvins_per_watt.

        

        :param meters: The ThermalResistance value in kelvins_per_watt.
        :type kelvins_per_watt: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(kelvins_per_watt, ThermalResistanceUnits.KelvinPerWatt)

    
    @staticmethod
    def from_degrees_celsius_per_watt(degrees_celsius_per_watt: float):
        """
        Create a new instance of ThermalResistance from a value in degrees_celsius_per_watt.

        

        :param meters: The ThermalResistance value in degrees_celsius_per_watt.
        :type degrees_celsius_per_watt: float
        :return: A new instance of ThermalResistance.
        :rtype: ThermalResistance
        """
        return ThermalResistance(degrees_celsius_per_watt, ThermalResistanceUnits.DegreeCelsiusPerWatt)

    
    @property
    def kelvins_per_watt(self) -> float:
        """
        
        """
        if self.__kelvins_per_watt != None:
            return self.__kelvins_per_watt
        self.__kelvins_per_watt = self.__convert_from_base(ThermalResistanceUnits.KelvinPerWatt)
        return self.__kelvins_per_watt

    
    @property
    def degrees_celsius_per_watt(self) -> float:
        """
        
        """
        if self.__degrees_celsius_per_watt != None:
            return self.__degrees_celsius_per_watt
        self.__degrees_celsius_per_watt = self.__convert_from_base(ThermalResistanceUnits.DegreeCelsiusPerWatt)
        return self.__degrees_celsius_per_watt

    
    def to_string(self, unit: ThermalResistanceUnits = ThermalResistanceUnits.KelvinPerWatt, fractional_digits: int = None) -> str:
        """
        Format the ThermalResistance to a string.
        
        Note: the default format for ThermalResistance is KelvinPerWatt.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ThermalResistance. Default is 'KelvinPerWatt'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ThermalResistanceUnits.KelvinPerWatt:
            return f"""{super()._truncate_fraction_digits(self.kelvins_per_watt, fractional_digits)} K/W"""
        
        if unit == ThermalResistanceUnits.DegreeCelsiusPerWatt:
            return f"""{super()._truncate_fraction_digits(self.degrees_celsius_per_watt, fractional_digits)} °C/W"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ThermalResistanceUnits = ThermalResistanceUnits.KelvinPerWatt) -> str:
        """
        Get ThermalResistance unit abbreviation.
        Note! the default abbreviation for ThermalResistance is KelvinPerWatt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ThermalResistanceUnits.KelvinPerWatt:
            return """K/W"""
        
        if unit_abbreviation == ThermalResistanceUnits.DegreeCelsiusPerWatt:
            return """°C/W"""
        