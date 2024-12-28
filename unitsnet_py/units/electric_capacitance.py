from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricCapacitanceUnits(Enum):
        """
            ElectricCapacitanceUnits enumeration
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
        

class ElectricCapacitanceDto:
    """
    A DTO representation of a ElectricCapacitance

    Attributes:
        value (float): The value of the ElectricCapacitance.
        unit (ElectricCapacitanceUnits): The specific unit that the ElectricCapacitance value is representing.
    """

    def __init__(self, value: float, unit: ElectricCapacitanceUnits):
        """
        Create a new DTO representation of a ElectricCapacitance

        Parameters:
            value (float): The value of the ElectricCapacitance.
            unit (ElectricCapacitanceUnits): The specific unit that the ElectricCapacitance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricCapacitance
        """
        self.unit: ElectricCapacitanceUnits = unit
        """
        The specific unit that the ElectricCapacitance value is representing
        """

    def to_json(self):
        """
        Get a ElectricCapacitance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricCapacitance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Farad"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricCapacitance DTO from a json representation.

        :param data: The ElectricCapacitance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Farad"}
        :return: A new instance of ElectricCapacitanceDto.
        :rtype: ElectricCapacitanceDto
        """
        return ElectricCapacitanceDto(value=data["value"], unit=ElectricCapacitanceUnits(data["unit"]))


class ElectricCapacitance(AbstractMeasure):
    """
    Capacitance is the capacity of a material object or device to store electric charge.

    Args:
        value (float): The value.
        from_unit (ElectricCapacitanceUnits): The ElectricCapacitance unit to create from, The default unit is Farad
    """
    def __init__(self, value: float, from_unit: ElectricCapacitanceUnits = ElectricCapacitanceUnits.Farad):
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
        

    def convert(self, unit: ElectricCapacitanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricCapacitanceUnits = ElectricCapacitanceUnits.Farad) -> ElectricCapacitanceDto:
        """
        Get a new instance of ElectricCapacitance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricCapacitance unit to store the ElectricCapacitance value in the DTO representation.
        :type hold_in_unit: ElectricCapacitanceUnits
        :return: A new instance of ElectricCapacitanceDto.
        :rtype: ElectricCapacitanceDto
        """
        return ElectricCapacitanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricCapacitanceUnits = ElectricCapacitanceUnits.Farad):
        """
        Get a ElectricCapacitance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricCapacitance unit to store the ElectricCapacitance value in the DTO representation.
        :type hold_in_unit: ElectricCapacitanceUnits
        :return: JSON object represents ElectricCapacitance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Farad"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_capacitance_dto: ElectricCapacitanceDto):
        """
        Obtain a new instance of ElectricCapacitance from a DTO unit object.

        :param electric_capacitance_dto: The ElectricCapacitance DTO representation.
        :type electric_capacitance_dto: ElectricCapacitanceDto
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(electric_capacitance_dto.value, electric_capacitance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricCapacitance from a DTO unit json representation.

        :param data: The ElectricCapacitance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Farad"}
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance.from_dto(ElectricCapacitanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricCapacitanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricCapacitanceUnits.Farad:
            return (value)
        
        if from_unit == ElectricCapacitanceUnits.Picofarad:
            return ((value) / 1e-12)
        
        if from_unit == ElectricCapacitanceUnits.Nanofarad:
            return ((value) / 1e-09)
        
        if from_unit == ElectricCapacitanceUnits.Microfarad:
            return ((value) / 1e-06)
        
        if from_unit == ElectricCapacitanceUnits.Millifarad:
            return ((value) / 0.001)
        
        if from_unit == ElectricCapacitanceUnits.Kilofarad:
            return ((value) / 1000.0)
        
        if from_unit == ElectricCapacitanceUnits.Megafarad:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricCapacitanceUnits) -> float:
        
        if to_unit == ElectricCapacitanceUnits.Farad:
            return (value)
        
        if to_unit == ElectricCapacitanceUnits.Picofarad:
            return ((value) * 1e-12)
        
        if to_unit == ElectricCapacitanceUnits.Nanofarad:
            return ((value) * 1e-09)
        
        if to_unit == ElectricCapacitanceUnits.Microfarad:
            return ((value) * 1e-06)
        
        if to_unit == ElectricCapacitanceUnits.Millifarad:
            return ((value) * 0.001)
        
        if to_unit == ElectricCapacitanceUnits.Kilofarad:
            return ((value) * 1000.0)
        
        if to_unit == ElectricCapacitanceUnits.Megafarad:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_farads(farads: float):
        """
        Create a new instance of ElectricCapacitance from a value in farads.

        

        :param meters: The ElectricCapacitance value in farads.
        :type farads: float
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(farads, ElectricCapacitanceUnits.Farad)

    
    @staticmethod
    def from_picofarads(picofarads: float):
        """
        Create a new instance of ElectricCapacitance from a value in picofarads.

        

        :param meters: The ElectricCapacitance value in picofarads.
        :type picofarads: float
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(picofarads, ElectricCapacitanceUnits.Picofarad)

    
    @staticmethod
    def from_nanofarads(nanofarads: float):
        """
        Create a new instance of ElectricCapacitance from a value in nanofarads.

        

        :param meters: The ElectricCapacitance value in nanofarads.
        :type nanofarads: float
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(nanofarads, ElectricCapacitanceUnits.Nanofarad)

    
    @staticmethod
    def from_microfarads(microfarads: float):
        """
        Create a new instance of ElectricCapacitance from a value in microfarads.

        

        :param meters: The ElectricCapacitance value in microfarads.
        :type microfarads: float
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(microfarads, ElectricCapacitanceUnits.Microfarad)

    
    @staticmethod
    def from_millifarads(millifarads: float):
        """
        Create a new instance of ElectricCapacitance from a value in millifarads.

        

        :param meters: The ElectricCapacitance value in millifarads.
        :type millifarads: float
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(millifarads, ElectricCapacitanceUnits.Millifarad)

    
    @staticmethod
    def from_kilofarads(kilofarads: float):
        """
        Create a new instance of ElectricCapacitance from a value in kilofarads.

        

        :param meters: The ElectricCapacitance value in kilofarads.
        :type kilofarads: float
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(kilofarads, ElectricCapacitanceUnits.Kilofarad)

    
    @staticmethod
    def from_megafarads(megafarads: float):
        """
        Create a new instance of ElectricCapacitance from a value in megafarads.

        

        :param meters: The ElectricCapacitance value in megafarads.
        :type megafarads: float
        :return: A new instance of ElectricCapacitance.
        :rtype: ElectricCapacitance
        """
        return ElectricCapacitance(megafarads, ElectricCapacitanceUnits.Megafarad)

    
    @property
    def farads(self) -> float:
        """
        
        """
        if self.__farads != None:
            return self.__farads
        self.__farads = self.__convert_from_base(ElectricCapacitanceUnits.Farad)
        return self.__farads

    
    @property
    def picofarads(self) -> float:
        """
        
        """
        if self.__picofarads != None:
            return self.__picofarads
        self.__picofarads = self.__convert_from_base(ElectricCapacitanceUnits.Picofarad)
        return self.__picofarads

    
    @property
    def nanofarads(self) -> float:
        """
        
        """
        if self.__nanofarads != None:
            return self.__nanofarads
        self.__nanofarads = self.__convert_from_base(ElectricCapacitanceUnits.Nanofarad)
        return self.__nanofarads

    
    @property
    def microfarads(self) -> float:
        """
        
        """
        if self.__microfarads != None:
            return self.__microfarads
        self.__microfarads = self.__convert_from_base(ElectricCapacitanceUnits.Microfarad)
        return self.__microfarads

    
    @property
    def millifarads(self) -> float:
        """
        
        """
        if self.__millifarads != None:
            return self.__millifarads
        self.__millifarads = self.__convert_from_base(ElectricCapacitanceUnits.Millifarad)
        return self.__millifarads

    
    @property
    def kilofarads(self) -> float:
        """
        
        """
        if self.__kilofarads != None:
            return self.__kilofarads
        self.__kilofarads = self.__convert_from_base(ElectricCapacitanceUnits.Kilofarad)
        return self.__kilofarads

    
    @property
    def megafarads(self) -> float:
        """
        
        """
        if self.__megafarads != None:
            return self.__megafarads
        self.__megafarads = self.__convert_from_base(ElectricCapacitanceUnits.Megafarad)
        return self.__megafarads

    
    def to_string(self, unit: ElectricCapacitanceUnits = ElectricCapacitanceUnits.Farad, fractional_digits: int = None) -> str:
        """
        Format the ElectricCapacitance to a string.
        
        Note: the default format for ElectricCapacitance is Farad.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricCapacitance. Default is 'Farad'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricCapacitanceUnits.Farad:
            return f"""{super()._truncate_fraction_digits(self.farads, fractional_digits)} F"""
        
        if unit == ElectricCapacitanceUnits.Picofarad:
            return f"""{super()._truncate_fraction_digits(self.picofarads, fractional_digits)} pF"""
        
        if unit == ElectricCapacitanceUnits.Nanofarad:
            return f"""{super()._truncate_fraction_digits(self.nanofarads, fractional_digits)} nF"""
        
        if unit == ElectricCapacitanceUnits.Microfarad:
            return f"""{super()._truncate_fraction_digits(self.microfarads, fractional_digits)} μF"""
        
        if unit == ElectricCapacitanceUnits.Millifarad:
            return f"""{super()._truncate_fraction_digits(self.millifarads, fractional_digits)} mF"""
        
        if unit == ElectricCapacitanceUnits.Kilofarad:
            return f"""{super()._truncate_fraction_digits(self.kilofarads, fractional_digits)} kF"""
        
        if unit == ElectricCapacitanceUnits.Megafarad:
            return f"""{super()._truncate_fraction_digits(self.megafarads, fractional_digits)} MF"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricCapacitanceUnits = ElectricCapacitanceUnits.Farad) -> str:
        """
        Get ElectricCapacitance unit abbreviation.
        Note! the default abbreviation for ElectricCapacitance is Farad.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricCapacitanceUnits.Farad:
            return """F"""
        
        if unit_abbreviation == ElectricCapacitanceUnits.Picofarad:
            return """pF"""
        
        if unit_abbreviation == ElectricCapacitanceUnits.Nanofarad:
            return """nF"""
        
        if unit_abbreviation == ElectricCapacitanceUnits.Microfarad:
            return """μF"""
        
        if unit_abbreviation == ElectricCapacitanceUnits.Millifarad:
            return """mF"""
        
        if unit_abbreviation == ElectricCapacitanceUnits.Kilofarad:
            return """kF"""
        
        if unit_abbreviation == ElectricCapacitanceUnits.Megafarad:
            return """MF"""
        