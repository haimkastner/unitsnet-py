from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RadiationEquivalentDoseRateUnits(Enum):
        """
            RadiationEquivalentDoseRateUnits enumeration
        """
        
        SievertPerHour = 'SievertPerHour'
        """
            
        """
        
        RoentgenEquivalentManPerHour = 'RoentgenEquivalentManPerHour'
        """
            
        """
        
        NanosievertPerHour = 'NanosievertPerHour'
        """
            
        """
        
        MicrosievertPerHour = 'MicrosievertPerHour'
        """
            
        """
        
        MillisievertPerHour = 'MillisievertPerHour'
        """
            
        """
        
        MilliroentgenEquivalentManPerHour = 'MilliroentgenEquivalentManPerHour'
        """
            
        """
        

class RadiationEquivalentDoseRateDto:
    """
    A DTO representation of a RadiationEquivalentDoseRate

    Attributes:
        value (float): The value of the RadiationEquivalentDoseRate.
        unit (RadiationEquivalentDoseRateUnits): The specific unit that the RadiationEquivalentDoseRate value is representing.
    """

    def __init__(self, value: float, unit: RadiationEquivalentDoseRateUnits):
        """
        Create a new DTO representation of a RadiationEquivalentDoseRate

        Parameters:
            value (float): The value of the RadiationEquivalentDoseRate.
            unit (RadiationEquivalentDoseRateUnits): The specific unit that the RadiationEquivalentDoseRate value is representing.
        """
        self.value: float = value
        """
        The value of the RadiationEquivalentDoseRate
        """
        self.unit: RadiationEquivalentDoseRateUnits = unit
        """
        The specific unit that the RadiationEquivalentDoseRate value is representing
        """

    def to_json(self):
        """
        Get a RadiationEquivalentDoseRate DTO JSON object representing the current unit.

        :return: JSON object represents RadiationEquivalentDoseRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SievertPerHour"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of RadiationEquivalentDoseRate DTO from a json representation.

        :param data: The RadiationEquivalentDoseRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SievertPerHour"}
        :return: A new instance of RadiationEquivalentDoseRateDto.
        :rtype: RadiationEquivalentDoseRateDto
        """
        return RadiationEquivalentDoseRateDto(value=data["value"], unit=RadiationEquivalentDoseRateUnits(data["unit"]))


class RadiationEquivalentDoseRate(AbstractMeasure):
    """
    A dose rate is quantity of radiation absorbed or delivered per unit time.

    Args:
        value (float): The value.
        from_unit (RadiationEquivalentDoseRateUnits): The RadiationEquivalentDoseRate unit to create from, The default unit is SievertPerHour
    """
    def __init__(self, value: float, from_unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerHour):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__sieverts_per_hour = None
        
        self.__roentgens_equivalent_man_per_hour = None
        
        self.__nanosieverts_per_hour = None
        
        self.__microsieverts_per_hour = None
        
        self.__millisieverts_per_hour = None
        
        self.__milliroentgens_equivalent_man_per_hour = None
        

    def convert(self, unit: RadiationEquivalentDoseRateUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerHour) -> RadiationEquivalentDoseRateDto:
        """
        Get a new instance of RadiationEquivalentDoseRate DTO representing the current unit.

        :param hold_in_unit: The specific RadiationEquivalentDoseRate unit to store the RadiationEquivalentDoseRate value in the DTO representation.
        :type hold_in_unit: RadiationEquivalentDoseRateUnits
        :return: A new instance of RadiationEquivalentDoseRateDto.
        :rtype: RadiationEquivalentDoseRateDto
        """
        return RadiationEquivalentDoseRateDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerHour):
        """
        Get a RadiationEquivalentDoseRate DTO JSON object representing the current unit.

        :param hold_in_unit: The specific RadiationEquivalentDoseRate unit to store the RadiationEquivalentDoseRate value in the DTO representation.
        :type hold_in_unit: RadiationEquivalentDoseRateUnits
        :return: JSON object represents RadiationEquivalentDoseRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SievertPerHour"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(radiation_equivalent_dose_rate_dto: RadiationEquivalentDoseRateDto):
        """
        Obtain a new instance of RadiationEquivalentDoseRate from a DTO unit object.

        :param radiation_equivalent_dose_rate_dto: The RadiationEquivalentDoseRate DTO representation.
        :type radiation_equivalent_dose_rate_dto: RadiationEquivalentDoseRateDto
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(radiation_equivalent_dose_rate_dto.value, radiation_equivalent_dose_rate_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of RadiationEquivalentDoseRate from a DTO unit json representation.

        :param data: The RadiationEquivalentDoseRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SievertPerHour"}
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate.from_dto(RadiationEquivalentDoseRateDto.from_json(data))

    def __convert_from_base(self, from_unit: RadiationEquivalentDoseRateUnits) -> float:
        value = self._value
        
        if from_unit == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return (value)
        
        if from_unit == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return (value * 100)
        
        if from_unit == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return ((value) / 1e-09)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return ((value) / 1e-06)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return ((value) / 0.001)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return ((value * 100) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RadiationEquivalentDoseRateUnits) -> float:
        
        if to_unit == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return (value)
        
        if to_unit == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return (value / 100)
        
        if to_unit == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return ((value) * 1e-09)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return ((value) * 1e-06)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return ((value) * 0.001)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return ((value / 100) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_sieverts_per_hour(sieverts_per_hour: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in sieverts_per_hour.

        

        :param meters: The RadiationEquivalentDoseRate value in sieverts_per_hour.
        :type sieverts_per_hour: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(sieverts_per_hour, RadiationEquivalentDoseRateUnits.SievertPerHour)

    
    @staticmethod
    def from_roentgens_equivalent_man_per_hour(roentgens_equivalent_man_per_hour: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in roentgens_equivalent_man_per_hour.

        

        :param meters: The RadiationEquivalentDoseRate value in roentgens_equivalent_man_per_hour.
        :type roentgens_equivalent_man_per_hour: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(roentgens_equivalent_man_per_hour, RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour)

    
    @staticmethod
    def from_nanosieverts_per_hour(nanosieverts_per_hour: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in nanosieverts_per_hour.

        

        :param meters: The RadiationEquivalentDoseRate value in nanosieverts_per_hour.
        :type nanosieverts_per_hour: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(nanosieverts_per_hour, RadiationEquivalentDoseRateUnits.NanosievertPerHour)

    
    @staticmethod
    def from_microsieverts_per_hour(microsieverts_per_hour: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in microsieverts_per_hour.

        

        :param meters: The RadiationEquivalentDoseRate value in microsieverts_per_hour.
        :type microsieverts_per_hour: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(microsieverts_per_hour, RadiationEquivalentDoseRateUnits.MicrosievertPerHour)

    
    @staticmethod
    def from_millisieverts_per_hour(millisieverts_per_hour: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in millisieverts_per_hour.

        

        :param meters: The RadiationEquivalentDoseRate value in millisieverts_per_hour.
        :type millisieverts_per_hour: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(millisieverts_per_hour, RadiationEquivalentDoseRateUnits.MillisievertPerHour)

    
    @staticmethod
    def from_milliroentgens_equivalent_man_per_hour(milliroentgens_equivalent_man_per_hour: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in milliroentgens_equivalent_man_per_hour.

        

        :param meters: The RadiationEquivalentDoseRate value in milliroentgens_equivalent_man_per_hour.
        :type milliroentgens_equivalent_man_per_hour: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(milliroentgens_equivalent_man_per_hour, RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour)

    
    @property
    def sieverts_per_hour(self) -> float:
        """
        
        """
        if self.__sieverts_per_hour != None:
            return self.__sieverts_per_hour
        self.__sieverts_per_hour = self.__convert_from_base(RadiationEquivalentDoseRateUnits.SievertPerHour)
        return self.__sieverts_per_hour

    
    @property
    def roentgens_equivalent_man_per_hour(self) -> float:
        """
        
        """
        if self.__roentgens_equivalent_man_per_hour != None:
            return self.__roentgens_equivalent_man_per_hour
        self.__roentgens_equivalent_man_per_hour = self.__convert_from_base(RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour)
        return self.__roentgens_equivalent_man_per_hour

    
    @property
    def nanosieverts_per_hour(self) -> float:
        """
        
        """
        if self.__nanosieverts_per_hour != None:
            return self.__nanosieverts_per_hour
        self.__nanosieverts_per_hour = self.__convert_from_base(RadiationEquivalentDoseRateUnits.NanosievertPerHour)
        return self.__nanosieverts_per_hour

    
    @property
    def microsieverts_per_hour(self) -> float:
        """
        
        """
        if self.__microsieverts_per_hour != None:
            return self.__microsieverts_per_hour
        self.__microsieverts_per_hour = self.__convert_from_base(RadiationEquivalentDoseRateUnits.MicrosievertPerHour)
        return self.__microsieverts_per_hour

    
    @property
    def millisieverts_per_hour(self) -> float:
        """
        
        """
        if self.__millisieverts_per_hour != None:
            return self.__millisieverts_per_hour
        self.__millisieverts_per_hour = self.__convert_from_base(RadiationEquivalentDoseRateUnits.MillisievertPerHour)
        return self.__millisieverts_per_hour

    
    @property
    def milliroentgens_equivalent_man_per_hour(self) -> float:
        """
        
        """
        if self.__milliroentgens_equivalent_man_per_hour != None:
            return self.__milliroentgens_equivalent_man_per_hour
        self.__milliroentgens_equivalent_man_per_hour = self.__convert_from_base(RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour)
        return self.__milliroentgens_equivalent_man_per_hour

    
    def to_string(self, unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerHour, fractional_digits: int = None) -> str:
        """
        Format the RadiationEquivalentDoseRate to a string.
        
        Note: the default format for RadiationEquivalentDoseRate is SievertPerHour.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the RadiationEquivalentDoseRate. Default is 'SievertPerHour'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.sieverts_per_hour, fractional_digits)} Sv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return f"""{super()._truncate_fraction_digits(self.roentgens_equivalent_man_per_hour, fractional_digits)} rem/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.nanosieverts_per_hour, fractional_digits)} nSv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.microsieverts_per_hour, fractional_digits)} μSv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.millisieverts_per_hour, fractional_digits)} mSv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return f"""{super()._truncate_fraction_digits(self.milliroentgens_equivalent_man_per_hour, fractional_digits)} mrem/h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerHour) -> str:
        """
        Get RadiationEquivalentDoseRate unit abbreviation.
        Note! the default abbreviation for RadiationEquivalentDoseRate is SievertPerHour.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return """Sv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return """rem/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return """nSv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return """μSv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return """mSv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return """mrem/h"""
        