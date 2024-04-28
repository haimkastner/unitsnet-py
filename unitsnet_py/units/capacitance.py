from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class CapacitanceUnits(Enum):
        """
            CapacitanceUnits enumeration
        """
        
        Farad = 'Farad'
        """
            
        """
        
        Picofarad = 'Picofarad'
        """
            
        """
        
        Nanofarad = 'Nanofarad'
        """
            
        """
        
        Microfarad = 'Microfarad'
        """
            
        """
        
        Millifarad = 'Millifarad'
        """
            
        """
        
        Kilofarad = 'Kilofarad'
        """
            
        """
        
        Megafarad = 'Megafarad'
        """
            
        """
        

class CapacitanceDto:
    """
    A DTO representation of a Capacitance

    Attributes:
        value (float): The value of the Capacitance.
        unit (CapacitanceUnits): The specific unit that the Capacitance value is representing.
    """

    def __init__(self, value: float, unit: CapacitanceUnits):
        """
        Create a new DTO representation of a Capacitance

        Parameters:
            value (float): The value of the Capacitance.
            unit (CapacitanceUnits): The specific unit that the Capacitance value is representing.
        """
        self.value: float = value
        """
        The value of the Capacitance
        """
        self.unit: CapacitanceUnits = unit
        """
        The specific unit that the Capacitance value is representing
        """

    def to_json(self):
        """
        Get a Capacitance DTO JSON object representing the current unit.

        :return: JSON object represents Capacitance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Farad"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Capacitance DTO from a json representation.

        :param data: The Capacitance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Farad"}
        :return: A new instance of CapacitanceDto.
        :rtype: CapacitanceDto
        """
        return CapacitanceDto(value=data["value"], unit=CapacitanceUnits(data["unit"]))


class Capacitance(AbstractMeasure):
    """
    Capacitance is the ability of a body to store an electric charge.

    Args:
        value (float): The value.
        from_unit (CapacitanceUnits): The Capacitance unit to create from, The default unit is Farad
    """
    def __init__(self, value: float, from_unit: CapacitanceUnits = CapacitanceUnits.Farad):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__farads = None
        
        self.__picofarads = None
        
        self.__nanofarads = None
        
        self.__microfarads = None
        
        self.__millifarads = None
        
        self.__kilofarads = None
        
        self.__megafarads = None
        

    def convert(self, unit: CapacitanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: CapacitanceUnits = CapacitanceUnits.Farad) -> CapacitanceDto:
        """
        Get a new instance of Capacitance DTO representing the current unit.

        :param hold_in_unit: The specific Capacitance unit to store the Capacitance value in the DTO representation.
        :type hold_in_unit: CapacitanceUnits
        :return: A new instance of CapacitanceDto.
        :rtype: CapacitanceDto
        """
        return CapacitanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: CapacitanceUnits = CapacitanceUnits.Farad):
        """
        Get a Capacitance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Capacitance unit to store the Capacitance value in the DTO representation.
        :type hold_in_unit: CapacitanceUnits
        :return: JSON object represents Capacitance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Farad"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(capacitance_dto: CapacitanceDto):
        """
        Obtain a new instance of Capacitance from a DTO unit object.

        :param capacitance_dto: The Capacitance DTO representation.
        :type capacitance_dto: CapacitanceDto
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(capacitance_dto.value, capacitance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Capacitance from a DTO unit json representation.

        :param data: The Capacitance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Farad"}
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance.from_dto(CapacitanceDto.from_json(data))

    def __convert_from_base(self, from_unit: CapacitanceUnits) -> float:
        value = self._value
        
        if from_unit == CapacitanceUnits.Farad:
            return (value)
        
        if from_unit == CapacitanceUnits.Picofarad:
            return ((value) / 1e-12)
        
        if from_unit == CapacitanceUnits.Nanofarad:
            return ((value) / 1e-09)
        
        if from_unit == CapacitanceUnits.Microfarad:
            return ((value) / 1e-06)
        
        if from_unit == CapacitanceUnits.Millifarad:
            return ((value) / 0.001)
        
        if from_unit == CapacitanceUnits.Kilofarad:
            return ((value) / 1000.0)
        
        if from_unit == CapacitanceUnits.Megafarad:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: CapacitanceUnits) -> float:
        
        if to_unit == CapacitanceUnits.Farad:
            return (value)
        
        if to_unit == CapacitanceUnits.Picofarad:
            return ((value) * 1e-12)
        
        if to_unit == CapacitanceUnits.Nanofarad:
            return ((value) * 1e-09)
        
        if to_unit == CapacitanceUnits.Microfarad:
            return ((value) * 1e-06)
        
        if to_unit == CapacitanceUnits.Millifarad:
            return ((value) * 0.001)
        
        if to_unit == CapacitanceUnits.Kilofarad:
            return ((value) * 1000.0)
        
        if to_unit == CapacitanceUnits.Megafarad:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_farads(farads: float):
        """
        Create a new instance of Capacitance from a value in farads.

        

        :param meters: The Capacitance value in farads.
        :type farads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(farads, CapacitanceUnits.Farad)

    
    @staticmethod
    def from_picofarads(picofarads: float):
        """
        Create a new instance of Capacitance from a value in picofarads.

        

        :param meters: The Capacitance value in picofarads.
        :type picofarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(picofarads, CapacitanceUnits.Picofarad)

    
    @staticmethod
    def from_nanofarads(nanofarads: float):
        """
        Create a new instance of Capacitance from a value in nanofarads.

        

        :param meters: The Capacitance value in nanofarads.
        :type nanofarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(nanofarads, CapacitanceUnits.Nanofarad)

    
    @staticmethod
    def from_microfarads(microfarads: float):
        """
        Create a new instance of Capacitance from a value in microfarads.

        

        :param meters: The Capacitance value in microfarads.
        :type microfarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(microfarads, CapacitanceUnits.Microfarad)

    
    @staticmethod
    def from_millifarads(millifarads: float):
        """
        Create a new instance of Capacitance from a value in millifarads.

        

        :param meters: The Capacitance value in millifarads.
        :type millifarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(millifarads, CapacitanceUnits.Millifarad)

    
    @staticmethod
    def from_kilofarads(kilofarads: float):
        """
        Create a new instance of Capacitance from a value in kilofarads.

        

        :param meters: The Capacitance value in kilofarads.
        :type kilofarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(kilofarads, CapacitanceUnits.Kilofarad)

    
    @staticmethod
    def from_megafarads(megafarads: float):
        """
        Create a new instance of Capacitance from a value in megafarads.

        

        :param meters: The Capacitance value in megafarads.
        :type megafarads: float
        :return: A new instance of Capacitance.
        :rtype: Capacitance
        """
        return Capacitance(megafarads, CapacitanceUnits.Megafarad)

    
    @property
    def farads(self) -> float:
        """
        
        """
        if self.__farads != None:
            return self.__farads
        self.__farads = self.__convert_from_base(CapacitanceUnits.Farad)
        return self.__farads

    
    @property
    def picofarads(self) -> float:
        """
        
        """
        if self.__picofarads != None:
            return self.__picofarads
        self.__picofarads = self.__convert_from_base(CapacitanceUnits.Picofarad)
        return self.__picofarads

    
    @property
    def nanofarads(self) -> float:
        """
        
        """
        if self.__nanofarads != None:
            return self.__nanofarads
        self.__nanofarads = self.__convert_from_base(CapacitanceUnits.Nanofarad)
        return self.__nanofarads

    
    @property
    def microfarads(self) -> float:
        """
        
        """
        if self.__microfarads != None:
            return self.__microfarads
        self.__microfarads = self.__convert_from_base(CapacitanceUnits.Microfarad)
        return self.__microfarads

    
    @property
    def millifarads(self) -> float:
        """
        
        """
        if self.__millifarads != None:
            return self.__millifarads
        self.__millifarads = self.__convert_from_base(CapacitanceUnits.Millifarad)
        return self.__millifarads

    
    @property
    def kilofarads(self) -> float:
        """
        
        """
        if self.__kilofarads != None:
            return self.__kilofarads
        self.__kilofarads = self.__convert_from_base(CapacitanceUnits.Kilofarad)
        return self.__kilofarads

    
    @property
    def megafarads(self) -> float:
        """
        
        """
        if self.__megafarads != None:
            return self.__megafarads
        self.__megafarads = self.__convert_from_base(CapacitanceUnits.Megafarad)
        return self.__megafarads

    
    def to_string(self, unit: CapacitanceUnits = CapacitanceUnits.Farad, fractional_digits: int = None) -> str:
        """
        Format the Capacitance to a string.
        
        Note: the default format for Capacitance is Farad.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Capacitance. Default is 'Farad'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == CapacitanceUnits.Farad:
            return f"""{super()._truncate_fraction_digits(self.farads, fractional_digits)} F"""
        
        if unit == CapacitanceUnits.Picofarad:
            return f"""{super()._truncate_fraction_digits(self.picofarads, fractional_digits)} pF"""
        
        if unit == CapacitanceUnits.Nanofarad:
            return f"""{super()._truncate_fraction_digits(self.nanofarads, fractional_digits)} nF"""
        
        if unit == CapacitanceUnits.Microfarad:
            return f"""{super()._truncate_fraction_digits(self.microfarads, fractional_digits)} μF"""
        
        if unit == CapacitanceUnits.Millifarad:
            return f"""{super()._truncate_fraction_digits(self.millifarads, fractional_digits)} mF"""
        
        if unit == CapacitanceUnits.Kilofarad:
            return f"""{super()._truncate_fraction_digits(self.kilofarads, fractional_digits)} kF"""
        
        if unit == CapacitanceUnits.Megafarad:
            return f"""{super()._truncate_fraction_digits(self.megafarads, fractional_digits)} MF"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: CapacitanceUnits = CapacitanceUnits.Farad) -> str:
        """
        Get Capacitance unit abbreviation.
        Note! the default abbreviation for Capacitance is Farad.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == CapacitanceUnits.Farad:
            return """F"""
        
        if unit_abbreviation == CapacitanceUnits.Picofarad:
            return """pF"""
        
        if unit_abbreviation == CapacitanceUnits.Nanofarad:
            return """nF"""
        
        if unit_abbreviation == CapacitanceUnits.Microfarad:
            return """μF"""
        
        if unit_abbreviation == CapacitanceUnits.Millifarad:
            return """mF"""
        
        if unit_abbreviation == CapacitanceUnits.Kilofarad:
            return """kF"""
        
        if unit_abbreviation == CapacitanceUnits.Megafarad:
            return """MF"""
        