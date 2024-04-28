from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AmplitudeRatioUnits(Enum):
        """
            AmplitudeRatioUnits enumeration
        """
        
        DecibelVolt = 'DecibelVolt'
        """
            
        """
        
        DecibelMicrovolt = 'DecibelMicrovolt'
        """
            
        """
        
        DecibelMillivolt = 'DecibelMillivolt'
        """
            
        """
        
        DecibelUnloaded = 'DecibelUnloaded'
        """
            
        """
        

class AmplitudeRatioDto:
    """
    A DTO representation of a AmplitudeRatio

    Attributes:
        value (float): The value of the AmplitudeRatio.
        unit (AmplitudeRatioUnits): The specific unit that the AmplitudeRatio value is representing.
    """

    def __init__(self, value: float, unit: AmplitudeRatioUnits):
        """
        Create a new DTO representation of a AmplitudeRatio

        Parameters:
            value (float): The value of the AmplitudeRatio.
            unit (AmplitudeRatioUnits): The specific unit that the AmplitudeRatio value is representing.
        """
        self.value: float = value
        """
        The value of the AmplitudeRatio
        """
        self.unit: AmplitudeRatioUnits = unit
        """
        The specific unit that the AmplitudeRatio value is representing
        """

    def to_json(self):
        """
        Get a AmplitudeRatio DTO JSON object representing the current unit.

        :return: JSON object represents AmplitudeRatio DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecibelVolt"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of AmplitudeRatio DTO from a json representation.

        :param data: The AmplitudeRatio DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecibelVolt"}
        :return: A new instance of AmplitudeRatioDto.
        :rtype: AmplitudeRatioDto
        """
        return AmplitudeRatioDto(value=data["value"], unit=AmplitudeRatioUnits(data["unit"]))


class AmplitudeRatio(AbstractMeasure):
    """
    The strength of a signal expressed in decibels (dB) relative to one volt RMS.

    Args:
        value (float): The value.
        from_unit (AmplitudeRatioUnits): The AmplitudeRatio unit to create from, The default unit is DecibelVolt
    """
    def __init__(self, value: float, from_unit: AmplitudeRatioUnits = AmplitudeRatioUnits.DecibelVolt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decibel_volts = None
        
        self.__decibel_microvolts = None
        
        self.__decibel_millivolts = None
        
        self.__decibels_unloaded = None
        

    def convert(self, unit: AmplitudeRatioUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: AmplitudeRatioUnits = AmplitudeRatioUnits.DecibelVolt) -> AmplitudeRatioDto:
        """
        Get a new instance of AmplitudeRatio DTO representing the current unit.

        :param hold_in_unit: The specific AmplitudeRatio unit to store the AmplitudeRatio value in the DTO representation.
        :type hold_in_unit: AmplitudeRatioUnits
        :return: A new instance of AmplitudeRatioDto.
        :rtype: AmplitudeRatioDto
        """
        return AmplitudeRatioDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: AmplitudeRatioUnits = AmplitudeRatioUnits.DecibelVolt):
        """
        Get a AmplitudeRatio DTO JSON object representing the current unit.

        :param hold_in_unit: The specific AmplitudeRatio unit to store the AmplitudeRatio value in the DTO representation.
        :type hold_in_unit: AmplitudeRatioUnits
        :return: JSON object represents AmplitudeRatio DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "DecibelVolt"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(amplitude_ratio_dto: AmplitudeRatioDto):
        """
        Obtain a new instance of AmplitudeRatio from a DTO unit object.

        :param amplitude_ratio_dto: The AmplitudeRatio DTO representation.
        :type amplitude_ratio_dto: AmplitudeRatioDto
        :return: A new instance of AmplitudeRatio.
        :rtype: AmplitudeRatio
        """
        return AmplitudeRatio(amplitude_ratio_dto.value, amplitude_ratio_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of AmplitudeRatio from a DTO unit json representation.

        :param data: The AmplitudeRatio DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "DecibelVolt"}
        :return: A new instance of AmplitudeRatio.
        :rtype: AmplitudeRatio
        """
        return AmplitudeRatio.from_dto(AmplitudeRatioDto.from_json(data))

    def __convert_from_base(self, from_unit: AmplitudeRatioUnits) -> float:
        value = self._value
        
        if from_unit == AmplitudeRatioUnits.DecibelVolt:
            return (value)
        
        if from_unit == AmplitudeRatioUnits.DecibelMicrovolt:
            return (value + 120)
        
        if from_unit == AmplitudeRatioUnits.DecibelMillivolt:
            return (value + 60)
        
        if from_unit == AmplitudeRatioUnits.DecibelUnloaded:
            return (value + 2.218487499)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AmplitudeRatioUnits) -> float:
        
        if to_unit == AmplitudeRatioUnits.DecibelVolt:
            return (value)
        
        if to_unit == AmplitudeRatioUnits.DecibelMicrovolt:
            return (value - 120)
        
        if to_unit == AmplitudeRatioUnits.DecibelMillivolt:
            return (value - 60)
        
        if to_unit == AmplitudeRatioUnits.DecibelUnloaded:
            return (value - 2.218487499)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_decibel_volts(decibel_volts: float):
        """
        Create a new instance of AmplitudeRatio from a value in decibel_volts.

        

        :param meters: The AmplitudeRatio value in decibel_volts.
        :type decibel_volts: float
        :return: A new instance of AmplitudeRatio.
        :rtype: AmplitudeRatio
        """
        return AmplitudeRatio(decibel_volts, AmplitudeRatioUnits.DecibelVolt)

    
    @staticmethod
    def from_decibel_microvolts(decibel_microvolts: float):
        """
        Create a new instance of AmplitudeRatio from a value in decibel_microvolts.

        

        :param meters: The AmplitudeRatio value in decibel_microvolts.
        :type decibel_microvolts: float
        :return: A new instance of AmplitudeRatio.
        :rtype: AmplitudeRatio
        """
        return AmplitudeRatio(decibel_microvolts, AmplitudeRatioUnits.DecibelMicrovolt)

    
    @staticmethod
    def from_decibel_millivolts(decibel_millivolts: float):
        """
        Create a new instance of AmplitudeRatio from a value in decibel_millivolts.

        

        :param meters: The AmplitudeRatio value in decibel_millivolts.
        :type decibel_millivolts: float
        :return: A new instance of AmplitudeRatio.
        :rtype: AmplitudeRatio
        """
        return AmplitudeRatio(decibel_millivolts, AmplitudeRatioUnits.DecibelMillivolt)

    
    @staticmethod
    def from_decibels_unloaded(decibels_unloaded: float):
        """
        Create a new instance of AmplitudeRatio from a value in decibels_unloaded.

        

        :param meters: The AmplitudeRatio value in decibels_unloaded.
        :type decibels_unloaded: float
        :return: A new instance of AmplitudeRatio.
        :rtype: AmplitudeRatio
        """
        return AmplitudeRatio(decibels_unloaded, AmplitudeRatioUnits.DecibelUnloaded)

    
    @property
    def decibel_volts(self) -> float:
        """
        
        """
        if self.__decibel_volts != None:
            return self.__decibel_volts
        self.__decibel_volts = self.__convert_from_base(AmplitudeRatioUnits.DecibelVolt)
        return self.__decibel_volts

    
    @property
    def decibel_microvolts(self) -> float:
        """
        
        """
        if self.__decibel_microvolts != None:
            return self.__decibel_microvolts
        self.__decibel_microvolts = self.__convert_from_base(AmplitudeRatioUnits.DecibelMicrovolt)
        return self.__decibel_microvolts

    
    @property
    def decibel_millivolts(self) -> float:
        """
        
        """
        if self.__decibel_millivolts != None:
            return self.__decibel_millivolts
        self.__decibel_millivolts = self.__convert_from_base(AmplitudeRatioUnits.DecibelMillivolt)
        return self.__decibel_millivolts

    
    @property
    def decibels_unloaded(self) -> float:
        """
        
        """
        if self.__decibels_unloaded != None:
            return self.__decibels_unloaded
        self.__decibels_unloaded = self.__convert_from_base(AmplitudeRatioUnits.DecibelUnloaded)
        return self.__decibels_unloaded

    
    def to_string(self, unit: AmplitudeRatioUnits = AmplitudeRatioUnits.DecibelVolt, fractional_digits: int = None) -> str:
        """
        Format the AmplitudeRatio to a string.
        
        Note: the default format for AmplitudeRatio is DecibelVolt.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the AmplitudeRatio. Default is 'DecibelVolt'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == AmplitudeRatioUnits.DecibelVolt:
            return f"""{super()._truncate_fraction_digits(self.decibel_volts, fractional_digits)} dBV"""
        
        if unit == AmplitudeRatioUnits.DecibelMicrovolt:
            return f"""{super()._truncate_fraction_digits(self.decibel_microvolts, fractional_digits)} dBµV"""
        
        if unit == AmplitudeRatioUnits.DecibelMillivolt:
            return f"""{super()._truncate_fraction_digits(self.decibel_millivolts, fractional_digits)} dBmV"""
        
        if unit == AmplitudeRatioUnits.DecibelUnloaded:
            return f"""{super()._truncate_fraction_digits(self.decibels_unloaded, fractional_digits)} dBu"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AmplitudeRatioUnits = AmplitudeRatioUnits.DecibelVolt) -> str:
        """
        Get AmplitudeRatio unit abbreviation.
        Note! the default abbreviation for AmplitudeRatio is DecibelVolt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AmplitudeRatioUnits.DecibelVolt:
            return """dBV"""
        
        if unit_abbreviation == AmplitudeRatioUnits.DecibelMicrovolt:
            return """dBµV"""
        
        if unit_abbreviation == AmplitudeRatioUnits.DecibelMillivolt:
            return """dBmV"""
        
        if unit_abbreviation == AmplitudeRatioUnits.DecibelUnloaded:
            return """dBu"""
        