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
        
        SievertPerSecond = 'SievertPerSecond'
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
        
        NanosievertPerSecond = 'NanosievertPerSecond'
        """
            
        """
        
        MicrosievertPerSecond = 'MicrosievertPerSecond'
        """
            
        """
        
        MillisievertPerSecond = 'MillisievertPerSecond'
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
        :example return: {"value": 100, "unit": "SievertPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of RadiationEquivalentDoseRate DTO from a json representation.

        :param data: The RadiationEquivalentDoseRate DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SievertPerSecond"}
        :return: A new instance of RadiationEquivalentDoseRateDto.
        :rtype: RadiationEquivalentDoseRateDto
        """
        return RadiationEquivalentDoseRateDto(value=data["value"], unit=RadiationEquivalentDoseRateUnits(data["unit"]))


class RadiationEquivalentDoseRate(AbstractMeasure):
    """
    A dose rate is quantity of radiation absorbed or delivered per unit time.

    Args:
        value (float): The value.
        from_unit (RadiationEquivalentDoseRateUnits): The RadiationEquivalentDoseRate unit to create from, The default unit is SievertPerSecond
    """
    def __init__(self, value: float, from_unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__sieverts_per_hour = None
        
        self.__sieverts_per_second = None
        
        self.__roentgens_equivalent_man_per_hour = None
        
        self.__nanosieverts_per_hour = None
        
        self.__microsieverts_per_hour = None
        
        self.__millisieverts_per_hour = None
        
        self.__nanosieverts_per_second = None
        
        self.__microsieverts_per_second = None
        
        self.__millisieverts_per_second = None
        
        self.__milliroentgens_equivalent_man_per_hour = None
        

    def convert(self, unit: RadiationEquivalentDoseRateUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerSecond) -> RadiationEquivalentDoseRateDto:
        """
        Get a new instance of RadiationEquivalentDoseRate DTO representing the current unit.

        :param hold_in_unit: The specific RadiationEquivalentDoseRate unit to store the RadiationEquivalentDoseRate value in the DTO representation.
        :type hold_in_unit: RadiationEquivalentDoseRateUnits
        :return: A new instance of RadiationEquivalentDoseRateDto.
        :rtype: RadiationEquivalentDoseRateDto
        """
        return RadiationEquivalentDoseRateDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerSecond):
        """
        Get a RadiationEquivalentDoseRate DTO JSON object representing the current unit.

        :param hold_in_unit: The specific RadiationEquivalentDoseRate unit to store the RadiationEquivalentDoseRate value in the DTO representation.
        :type hold_in_unit: RadiationEquivalentDoseRateUnits
        :return: JSON object represents RadiationEquivalentDoseRate DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SievertPerSecond"}
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
        :example data: {"value": 100, "unit": "SievertPerSecond"}
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate.from_dto(RadiationEquivalentDoseRateDto.from_json(data))

    def __convert_from_base(self, from_unit: RadiationEquivalentDoseRateUnits) -> float:
        value = self._value
        
        if from_unit == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return (value*3600)
        
        if from_unit == RadiationEquivalentDoseRateUnits.SievertPerSecond:
            return (value)
        
        if from_unit == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return (value * 100 * 3600)
        
        if from_unit == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return ((value*3600) / 1e-09)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return ((value*3600) / 1e-06)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return ((value*3600) / 0.001)
        
        if from_unit == RadiationEquivalentDoseRateUnits.NanosievertPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MicrosievertPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MillisievertPerSecond:
            return ((value) / 0.001)
        
        if from_unit == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return ((value * 100 * 3600) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RadiationEquivalentDoseRateUnits) -> float:
        
        if to_unit == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return (value/3600)
        
        if to_unit == RadiationEquivalentDoseRateUnits.SievertPerSecond:
            return (value)
        
        if to_unit == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return (value / 100 / 3600)
        
        if to_unit == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return ((value/3600) * 1e-09)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return ((value/3600) * 1e-06)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return ((value/3600) * 0.001)
        
        if to_unit == RadiationEquivalentDoseRateUnits.NanosievertPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MicrosievertPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MillisievertPerSecond:
            return ((value) * 0.001)
        
        if to_unit == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return ((value / 100 / 3600) * 0.001)
        
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
    def from_sieverts_per_second(sieverts_per_second: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in sieverts_per_second.

        

        :param meters: The RadiationEquivalentDoseRate value in sieverts_per_second.
        :type sieverts_per_second: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(sieverts_per_second, RadiationEquivalentDoseRateUnits.SievertPerSecond)

    
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
    def from_nanosieverts_per_second(nanosieverts_per_second: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in nanosieverts_per_second.

        

        :param meters: The RadiationEquivalentDoseRate value in nanosieverts_per_second.
        :type nanosieverts_per_second: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(nanosieverts_per_second, RadiationEquivalentDoseRateUnits.NanosievertPerSecond)

    
    @staticmethod
    def from_microsieverts_per_second(microsieverts_per_second: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in microsieverts_per_second.

        

        :param meters: The RadiationEquivalentDoseRate value in microsieverts_per_second.
        :type microsieverts_per_second: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(microsieverts_per_second, RadiationEquivalentDoseRateUnits.MicrosievertPerSecond)

    
    @staticmethod
    def from_millisieverts_per_second(millisieverts_per_second: float):
        """
        Create a new instance of RadiationEquivalentDoseRate from a value in millisieverts_per_second.

        

        :param meters: The RadiationEquivalentDoseRate value in millisieverts_per_second.
        :type millisieverts_per_second: float
        :return: A new instance of RadiationEquivalentDoseRate.
        :rtype: RadiationEquivalentDoseRate
        """
        return RadiationEquivalentDoseRate(millisieverts_per_second, RadiationEquivalentDoseRateUnits.MillisievertPerSecond)

    
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
    def sieverts_per_second(self) -> float:
        """
        
        """
        if self.__sieverts_per_second != None:
            return self.__sieverts_per_second
        self.__sieverts_per_second = self.__convert_from_base(RadiationEquivalentDoseRateUnits.SievertPerSecond)
        return self.__sieverts_per_second

    
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
    def nanosieverts_per_second(self) -> float:
        """
        
        """
        if self.__nanosieverts_per_second != None:
            return self.__nanosieverts_per_second
        self.__nanosieverts_per_second = self.__convert_from_base(RadiationEquivalentDoseRateUnits.NanosievertPerSecond)
        return self.__nanosieverts_per_second

    
    @property
    def microsieverts_per_second(self) -> float:
        """
        
        """
        if self.__microsieverts_per_second != None:
            return self.__microsieverts_per_second
        self.__microsieverts_per_second = self.__convert_from_base(RadiationEquivalentDoseRateUnits.MicrosievertPerSecond)
        return self.__microsieverts_per_second

    
    @property
    def millisieverts_per_second(self) -> float:
        """
        
        """
        if self.__millisieverts_per_second != None:
            return self.__millisieverts_per_second
        self.__millisieverts_per_second = self.__convert_from_base(RadiationEquivalentDoseRateUnits.MillisievertPerSecond)
        return self.__millisieverts_per_second

    
    @property
    def milliroentgens_equivalent_man_per_hour(self) -> float:
        """
        
        """
        if self.__milliroentgens_equivalent_man_per_hour != None:
            return self.__milliroentgens_equivalent_man_per_hour
        self.__milliroentgens_equivalent_man_per_hour = self.__convert_from_base(RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour)
        return self.__milliroentgens_equivalent_man_per_hour

    
    def to_string(self, unit: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerSecond, fractional_digits: int = None) -> str:
        """
        Format the RadiationEquivalentDoseRate to a string.
        
        Note: the default format for RadiationEquivalentDoseRate is SievertPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the RadiationEquivalentDoseRate. Default is 'SievertPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.sieverts_per_hour, fractional_digits)} Sv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.SievertPerSecond:
            return f"""{super()._truncate_fraction_digits(self.sieverts_per_second, fractional_digits)} Sv/s"""
        
        if unit == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return f"""{super()._truncate_fraction_digits(self.roentgens_equivalent_man_per_hour, fractional_digits)} rem/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.nanosieverts_per_hour, fractional_digits)} nSv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.microsieverts_per_hour, fractional_digits)} μSv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return f"""{super()._truncate_fraction_digits(self.millisieverts_per_hour, fractional_digits)} mSv/h"""
        
        if unit == RadiationEquivalentDoseRateUnits.NanosievertPerSecond:
            return f"""{super()._truncate_fraction_digits(self.nanosieverts_per_second, fractional_digits)} nSv/s"""
        
        if unit == RadiationEquivalentDoseRateUnits.MicrosievertPerSecond:
            return f"""{super()._truncate_fraction_digits(self.microsieverts_per_second, fractional_digits)} μSv/s"""
        
        if unit == RadiationEquivalentDoseRateUnits.MillisievertPerSecond:
            return f"""{super()._truncate_fraction_digits(self.millisieverts_per_second, fractional_digits)} mSv/s"""
        
        if unit == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return f"""{super()._truncate_fraction_digits(self.milliroentgens_equivalent_man_per_hour, fractional_digits)} mrem/h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RadiationEquivalentDoseRateUnits = RadiationEquivalentDoseRateUnits.SievertPerSecond) -> str:
        """
        Get RadiationEquivalentDoseRate unit abbreviation.
        Note! the default abbreviation for RadiationEquivalentDoseRate is SievertPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.SievertPerHour:
            return """Sv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.SievertPerSecond:
            return """Sv/s"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.RoentgenEquivalentManPerHour:
            return """rem/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.NanosievertPerHour:
            return """nSv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MicrosievertPerHour:
            return """μSv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MillisievertPerHour:
            return """mSv/h"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.NanosievertPerSecond:
            return """nSv/s"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MicrosievertPerSecond:
            return """μSv/s"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MillisievertPerSecond:
            return """mSv/s"""
        
        if unit_abbreviation == RadiationEquivalentDoseRateUnits.MilliroentgenEquivalentManPerHour:
            return """mrem/h"""
        