from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricConductanceUnits(Enum):
        """
            ElectricConductanceUnits enumeration
        """
        
        Siemens = 'Siemens'
        """
            
        """
        
        Nanosiemens = 'Nanosiemens'
        """
            
        """
        
        Microsiemens = 'Microsiemens'
        """
            
        """
        
        Millisiemens = 'Millisiemens'
        """
            
        """
        
        Kilosiemens = 'Kilosiemens'
        """
            
        """
        

class ElectricConductanceDto:
    """
    A DTO representation of a ElectricConductance

    Attributes:
        value (float): The value of the ElectricConductance.
        unit (ElectricConductanceUnits): The specific unit that the ElectricConductance value is representing.
    """

    def __init__(self, value: float, unit: ElectricConductanceUnits):
        """
        Create a new DTO representation of a ElectricConductance

        Parameters:
            value (float): The value of the ElectricConductance.
            unit (ElectricConductanceUnits): The specific unit that the ElectricConductance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricConductance
        """
        self.unit: ElectricConductanceUnits = unit
        """
        The specific unit that the ElectricConductance value is representing
        """

    def to_json(self):
        """
        Get a ElectricConductance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricConductance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricConductance DTO from a json representation.

        :param data: The ElectricConductance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricConductanceDto.
        :rtype: ElectricConductanceDto
        """
        return ElectricConductanceDto(value=data["value"], unit=ElectricConductanceUnits(data["unit"]))


class ElectricConductance(AbstractMeasure):
    """
    The electrical conductance of an electrical conductor is a measure of the easeness to pass an electric current through that conductor.

    Args:
        value (float): The value.
        from_unit (ElectricConductanceUnits): The ElectricConductance unit to create from, The default unit is Siemens
    """
    def __init__(self, value: float, from_unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__siemens = None
        
        self.__nanosiemens = None
        
        self.__microsiemens = None
        
        self.__millisiemens = None
        
        self.__kilosiemens = None
        

    def convert(self, unit: ElectricConductanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> ElectricConductanceDto:
        """
        Get a new instance of ElectricConductance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricConductance unit to store the ElectricConductance value in the DTO representation.
        :type hold_in_unit: ElectricConductanceUnits
        :return: A new instance of ElectricConductanceDto.
        :rtype: ElectricConductanceDto
        """
        return ElectricConductanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens):
        """
        Get a ElectricConductance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricConductance unit to store the ElectricConductance value in the DTO representation.
        :type hold_in_unit: ElectricConductanceUnits
        :return: JSON object represents ElectricConductance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Siemens"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_conductance_dto: ElectricConductanceDto):
        """
        Obtain a new instance of ElectricConductance from a DTO unit object.

        :param electric_conductance_dto: The ElectricConductance DTO representation.
        :type electric_conductance_dto: ElectricConductanceDto
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(electric_conductance_dto.value, electric_conductance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricConductance from a DTO unit json representation.

        :param data: The ElectricConductance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Siemens"}
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance.from_dto(ElectricConductanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricConductanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if from_unit == ElectricConductanceUnits.Nanosiemens:
            return ((value) / 1e-09)
        
        if from_unit == ElectricConductanceUnits.Microsiemens:
            return ((value) / 1e-06)
        
        if from_unit == ElectricConductanceUnits.Millisiemens:
            return ((value) / 0.001)
        
        if from_unit == ElectricConductanceUnits.Kilosiemens:
            return ((value) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricConductanceUnits) -> float:
        
        if to_unit == ElectricConductanceUnits.Siemens:
            return (value)
        
        if to_unit == ElectricConductanceUnits.Nanosiemens:
            return ((value) * 1e-09)
        
        if to_unit == ElectricConductanceUnits.Microsiemens:
            return ((value) * 1e-06)
        
        if to_unit == ElectricConductanceUnits.Millisiemens:
            return ((value) * 0.001)
        
        if to_unit == ElectricConductanceUnits.Kilosiemens:
            return ((value) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_siemens(siemens: float):
        """
        Create a new instance of ElectricConductance from a value in siemens.

        

        :param meters: The ElectricConductance value in siemens.
        :type siemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(siemens, ElectricConductanceUnits.Siemens)

    
    @staticmethod
    def from_nanosiemens(nanosiemens: float):
        """
        Create a new instance of ElectricConductance from a value in nanosiemens.

        

        :param meters: The ElectricConductance value in nanosiemens.
        :type nanosiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(nanosiemens, ElectricConductanceUnits.Nanosiemens)

    
    @staticmethod
    def from_microsiemens(microsiemens: float):
        """
        Create a new instance of ElectricConductance from a value in microsiemens.

        

        :param meters: The ElectricConductance value in microsiemens.
        :type microsiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(microsiemens, ElectricConductanceUnits.Microsiemens)

    
    @staticmethod
    def from_millisiemens(millisiemens: float):
        """
        Create a new instance of ElectricConductance from a value in millisiemens.

        

        :param meters: The ElectricConductance value in millisiemens.
        :type millisiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(millisiemens, ElectricConductanceUnits.Millisiemens)

    
    @staticmethod
    def from_kilosiemens(kilosiemens: float):
        """
        Create a new instance of ElectricConductance from a value in kilosiemens.

        

        :param meters: The ElectricConductance value in kilosiemens.
        :type kilosiemens: float
        :return: A new instance of ElectricConductance.
        :rtype: ElectricConductance
        """
        return ElectricConductance(kilosiemens, ElectricConductanceUnits.Kilosiemens)

    
    @property
    def siemens(self) -> float:
        """
        
        """
        if self.__siemens != None:
            return self.__siemens
        self.__siemens = self.__convert_from_base(ElectricConductanceUnits.Siemens)
        return self.__siemens

    
    @property
    def nanosiemens(self) -> float:
        """
        
        """
        if self.__nanosiemens != None:
            return self.__nanosiemens
        self.__nanosiemens = self.__convert_from_base(ElectricConductanceUnits.Nanosiemens)
        return self.__nanosiemens

    
    @property
    def microsiemens(self) -> float:
        """
        
        """
        if self.__microsiemens != None:
            return self.__microsiemens
        self.__microsiemens = self.__convert_from_base(ElectricConductanceUnits.Microsiemens)
        return self.__microsiemens

    
    @property
    def millisiemens(self) -> float:
        """
        
        """
        if self.__millisiemens != None:
            return self.__millisiemens
        self.__millisiemens = self.__convert_from_base(ElectricConductanceUnits.Millisiemens)
        return self.__millisiemens

    
    @property
    def kilosiemens(self) -> float:
        """
        
        """
        if self.__kilosiemens != None:
            return self.__kilosiemens
        self.__kilosiemens = self.__convert_from_base(ElectricConductanceUnits.Kilosiemens)
        return self.__kilosiemens

    
    def to_string(self, unit: ElectricConductanceUnits = ElectricConductanceUnits.Siemens, fractional_digits: int = None) -> str:
        """
        Format the ElectricConductance to a string.
        
        Note: the default format for ElectricConductance is Siemens.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricConductance. Default is 'Siemens'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricConductanceUnits.Siemens:
            return f"""{super()._truncate_fraction_digits(self.siemens, fractional_digits)} S"""
        
        if unit == ElectricConductanceUnits.Nanosiemens:
            return f"""{super()._truncate_fraction_digits(self.nanosiemens, fractional_digits)} nS"""
        
        if unit == ElectricConductanceUnits.Microsiemens:
            return f"""{super()._truncate_fraction_digits(self.microsiemens, fractional_digits)} μS"""
        
        if unit == ElectricConductanceUnits.Millisiemens:
            return f"""{super()._truncate_fraction_digits(self.millisiemens, fractional_digits)} mS"""
        
        if unit == ElectricConductanceUnits.Kilosiemens:
            return f"""{super()._truncate_fraction_digits(self.kilosiemens, fractional_digits)} kS"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricConductanceUnits = ElectricConductanceUnits.Siemens) -> str:
        """
        Get ElectricConductance unit abbreviation.
        Note! the default abbreviation for ElectricConductance is Siemens.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricConductanceUnits.Siemens:
            return """S"""
        
        if unit_abbreviation == ElectricConductanceUnits.Nanosiemens:
            return """nS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Microsiemens:
            return """μS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Millisiemens:
            return """mS"""
        
        if unit_abbreviation == ElectricConductanceUnits.Kilosiemens:
            return """kS"""
        