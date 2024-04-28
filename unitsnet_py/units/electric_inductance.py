from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricInductanceUnits(Enum):
        """
            ElectricInductanceUnits enumeration
        """
        
        Henry = 'Henry'
        """
            
        """
        
        Picohenry = 'Picohenry'
        """
            
        """
        
        Nanohenry = 'Nanohenry'
        """
            
        """
        
        Microhenry = 'Microhenry'
        """
            
        """
        
        Millihenry = 'Millihenry'
        """
            
        """
        

class ElectricInductanceDto:
    """
    A DTO representation of a ElectricInductance

    Attributes:
        value (float): The value of the ElectricInductance.
        unit (ElectricInductanceUnits): The specific unit that the ElectricInductance value is representing.
    """

    def __init__(self, value: float, unit: ElectricInductanceUnits):
        """
        Create a new DTO representation of a ElectricInductance

        Parameters:
            value (float): The value of the ElectricInductance.
            unit (ElectricInductanceUnits): The specific unit that the ElectricInductance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricInductance
        """
        self.unit: ElectricInductanceUnits = unit
        """
        The specific unit that the ElectricInductance value is representing
        """

    def to_json(self):
        """
        Get a ElectricInductance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricInductance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Henry"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricInductance DTO from a json representation.

        :param data: The ElectricInductance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Henry"}
        :return: A new instance of ElectricInductanceDto.
        :rtype: ElectricInductanceDto
        """
        return ElectricInductanceDto(value=data["value"], unit=ElectricInductanceUnits(data["unit"]))


class ElectricInductance(AbstractMeasure):
    """
    Inductance is a property of an electrical conductor which opposes a change in current.

    Args:
        value (float): The value.
        from_unit (ElectricInductanceUnits): The ElectricInductance unit to create from, The default unit is Henry
    """
    def __init__(self, value: float, from_unit: ElectricInductanceUnits = ElectricInductanceUnits.Henry):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__henries = None
        
        self.__picohenries = None
        
        self.__nanohenries = None
        
        self.__microhenries = None
        
        self.__millihenries = None
        

    def convert(self, unit: ElectricInductanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricInductanceUnits = ElectricInductanceUnits.Henry) -> ElectricInductanceDto:
        """
        Get a new instance of ElectricInductance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricInductance unit to store the ElectricInductance value in the DTO representation.
        :type hold_in_unit: ElectricInductanceUnits
        :return: A new instance of ElectricInductanceDto.
        :rtype: ElectricInductanceDto
        """
        return ElectricInductanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricInductanceUnits = ElectricInductanceUnits.Henry):
        """
        Get a ElectricInductance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricInductance unit to store the ElectricInductance value in the DTO representation.
        :type hold_in_unit: ElectricInductanceUnits
        :return: JSON object represents ElectricInductance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Henry"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_inductance_dto: ElectricInductanceDto):
        """
        Obtain a new instance of ElectricInductance from a DTO unit object.

        :param electric_inductance_dto: The ElectricInductance DTO representation.
        :type electric_inductance_dto: ElectricInductanceDto
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(electric_inductance_dto.value, electric_inductance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricInductance from a DTO unit json representation.

        :param data: The ElectricInductance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Henry"}
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance.from_dto(ElectricInductanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricInductanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricInductanceUnits.Henry:
            return (value)
        
        if from_unit == ElectricInductanceUnits.Picohenry:
            return ((value) / 1e-12)
        
        if from_unit == ElectricInductanceUnits.Nanohenry:
            return ((value) / 1e-09)
        
        if from_unit == ElectricInductanceUnits.Microhenry:
            return ((value) / 1e-06)
        
        if from_unit == ElectricInductanceUnits.Millihenry:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricInductanceUnits) -> float:
        
        if to_unit == ElectricInductanceUnits.Henry:
            return (value)
        
        if to_unit == ElectricInductanceUnits.Picohenry:
            return ((value) * 1e-12)
        
        if to_unit == ElectricInductanceUnits.Nanohenry:
            return ((value) * 1e-09)
        
        if to_unit == ElectricInductanceUnits.Microhenry:
            return ((value) * 1e-06)
        
        if to_unit == ElectricInductanceUnits.Millihenry:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_henries(henries: float):
        """
        Create a new instance of ElectricInductance from a value in henries.

        

        :param meters: The ElectricInductance value in henries.
        :type henries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(henries, ElectricInductanceUnits.Henry)

    
    @staticmethod
    def from_picohenries(picohenries: float):
        """
        Create a new instance of ElectricInductance from a value in picohenries.

        

        :param meters: The ElectricInductance value in picohenries.
        :type picohenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(picohenries, ElectricInductanceUnits.Picohenry)

    
    @staticmethod
    def from_nanohenries(nanohenries: float):
        """
        Create a new instance of ElectricInductance from a value in nanohenries.

        

        :param meters: The ElectricInductance value in nanohenries.
        :type nanohenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(nanohenries, ElectricInductanceUnits.Nanohenry)

    
    @staticmethod
    def from_microhenries(microhenries: float):
        """
        Create a new instance of ElectricInductance from a value in microhenries.

        

        :param meters: The ElectricInductance value in microhenries.
        :type microhenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(microhenries, ElectricInductanceUnits.Microhenry)

    
    @staticmethod
    def from_millihenries(millihenries: float):
        """
        Create a new instance of ElectricInductance from a value in millihenries.

        

        :param meters: The ElectricInductance value in millihenries.
        :type millihenries: float
        :return: A new instance of ElectricInductance.
        :rtype: ElectricInductance
        """
        return ElectricInductance(millihenries, ElectricInductanceUnits.Millihenry)

    
    @property
    def henries(self) -> float:
        """
        
        """
        if self.__henries != None:
            return self.__henries
        self.__henries = self.__convert_from_base(ElectricInductanceUnits.Henry)
        return self.__henries

    
    @property
    def picohenries(self) -> float:
        """
        
        """
        if self.__picohenries != None:
            return self.__picohenries
        self.__picohenries = self.__convert_from_base(ElectricInductanceUnits.Picohenry)
        return self.__picohenries

    
    @property
    def nanohenries(self) -> float:
        """
        
        """
        if self.__nanohenries != None:
            return self.__nanohenries
        self.__nanohenries = self.__convert_from_base(ElectricInductanceUnits.Nanohenry)
        return self.__nanohenries

    
    @property
    def microhenries(self) -> float:
        """
        
        """
        if self.__microhenries != None:
            return self.__microhenries
        self.__microhenries = self.__convert_from_base(ElectricInductanceUnits.Microhenry)
        return self.__microhenries

    
    @property
    def millihenries(self) -> float:
        """
        
        """
        if self.__millihenries != None:
            return self.__millihenries
        self.__millihenries = self.__convert_from_base(ElectricInductanceUnits.Millihenry)
        return self.__millihenries

    
    def to_string(self, unit: ElectricInductanceUnits = ElectricInductanceUnits.Henry, fractional_digits: int = None) -> str:
        """
        Format the ElectricInductance to a string.
        
        Note: the default format for ElectricInductance is Henry.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricInductance. Default is 'Henry'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricInductanceUnits.Henry:
            return f"""{super()._truncate_fraction_digits(self.henries, fractional_digits)} H"""
        
        if unit == ElectricInductanceUnits.Picohenry:
            return f"""{super()._truncate_fraction_digits(self.picohenries, fractional_digits)} pH"""
        
        if unit == ElectricInductanceUnits.Nanohenry:
            return f"""{super()._truncate_fraction_digits(self.nanohenries, fractional_digits)} nH"""
        
        if unit == ElectricInductanceUnits.Microhenry:
            return f"""{super()._truncate_fraction_digits(self.microhenries, fractional_digits)} μH"""
        
        if unit == ElectricInductanceUnits.Millihenry:
            return f"""{super()._truncate_fraction_digits(self.millihenries, fractional_digits)} mH"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricInductanceUnits = ElectricInductanceUnits.Henry) -> str:
        """
        Get ElectricInductance unit abbreviation.
        Note! the default abbreviation for ElectricInductance is Henry.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricInductanceUnits.Henry:
            return """H"""
        
        if unit_abbreviation == ElectricInductanceUnits.Picohenry:
            return """pH"""
        
        if unit_abbreviation == ElectricInductanceUnits.Nanohenry:
            return """nH"""
        
        if unit_abbreviation == ElectricInductanceUnits.Microhenry:
            return """μH"""
        
        if unit_abbreviation == ElectricInductanceUnits.Millihenry:
            return """mH"""
        