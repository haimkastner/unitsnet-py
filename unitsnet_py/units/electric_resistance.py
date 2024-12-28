from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricResistanceUnits(Enum):
        """
            ElectricResistanceUnits enumeration
        """
        
        Ohm = 'Ohm'
        """
            
        """
        
        Nanoohm = 'Nanoohm'
        """
            
        """
        
        Microohm = 'Microohm'
        """
            
        """
        
        Milliohm = 'Milliohm'
        """
            
        """
        
        Kiloohm = 'Kiloohm'
        """
            
        """
        
        Megaohm = 'Megaohm'
        """
            
        """
        
        Gigaohm = 'Gigaohm'
        """
            
        """
        
        Teraohm = 'Teraohm'
        """
            
        """
        

class ElectricResistanceDto:
    """
    A DTO representation of a ElectricResistance

    Attributes:
        value (float): The value of the ElectricResistance.
        unit (ElectricResistanceUnits): The specific unit that the ElectricResistance value is representing.
    """

    def __init__(self, value: float, unit: ElectricResistanceUnits):
        """
        Create a new DTO representation of a ElectricResistance

        Parameters:
            value (float): The value of the ElectricResistance.
            unit (ElectricResistanceUnits): The specific unit that the ElectricResistance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricResistance
        """
        self.unit: ElectricResistanceUnits = unit
        """
        The specific unit that the ElectricResistance value is representing
        """

    def to_json(self):
        """
        Get a ElectricResistance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Ohm"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricResistance DTO from a json representation.

        :param data: The ElectricResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Ohm"}
        :return: A new instance of ElectricResistanceDto.
        :rtype: ElectricResistanceDto
        """
        return ElectricResistanceDto(value=data["value"], unit=ElectricResistanceUnits(data["unit"]))


class ElectricResistance(AbstractMeasure):
    """
    The electrical resistance of an object is a measure of its opposition to the flow of electric current. Along with reactance, it is one of two elements of impedance. Its reciprocal quantity is electrical conductance.

    Args:
        value (float): The value.
        from_unit (ElectricResistanceUnits): The ElectricResistance unit to create from, The default unit is Ohm
    """
    def __init__(self, value: float, from_unit: ElectricResistanceUnits = ElectricResistanceUnits.Ohm):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__ohms = None
        
        self.__nanoohms = None
        
        self.__microohms = None
        
        self.__milliohms = None
        
        self.__kiloohms = None
        
        self.__megaohms = None
        
        self.__gigaohms = None
        
        self.__teraohms = None
        

    def convert(self, unit: ElectricResistanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricResistanceUnits = ElectricResistanceUnits.Ohm) -> ElectricResistanceDto:
        """
        Get a new instance of ElectricResistance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricResistance unit to store the ElectricResistance value in the DTO representation.
        :type hold_in_unit: ElectricResistanceUnits
        :return: A new instance of ElectricResistanceDto.
        :rtype: ElectricResistanceDto
        """
        return ElectricResistanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricResistanceUnits = ElectricResistanceUnits.Ohm):
        """
        Get a ElectricResistance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricResistance unit to store the ElectricResistance value in the DTO representation.
        :type hold_in_unit: ElectricResistanceUnits
        :return: JSON object represents ElectricResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Ohm"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_resistance_dto: ElectricResistanceDto):
        """
        Obtain a new instance of ElectricResistance from a DTO unit object.

        :param electric_resistance_dto: The ElectricResistance DTO representation.
        :type electric_resistance_dto: ElectricResistanceDto
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(electric_resistance_dto.value, electric_resistance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricResistance from a DTO unit json representation.

        :param data: The ElectricResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Ohm"}
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance.from_dto(ElectricResistanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricResistanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricResistanceUnits.Ohm:
            return (value)
        
        if from_unit == ElectricResistanceUnits.Nanoohm:
            return ((value) / 1e-09)
        
        if from_unit == ElectricResistanceUnits.Microohm:
            return ((value) / 1e-06)
        
        if from_unit == ElectricResistanceUnits.Milliohm:
            return ((value) / 0.001)
        
        if from_unit == ElectricResistanceUnits.Kiloohm:
            return ((value) / 1000.0)
        
        if from_unit == ElectricResistanceUnits.Megaohm:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricResistanceUnits.Gigaohm:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricResistanceUnits.Teraohm:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricResistanceUnits) -> float:
        
        if to_unit == ElectricResistanceUnits.Ohm:
            return (value)
        
        if to_unit == ElectricResistanceUnits.Nanoohm:
            return ((value) * 1e-09)
        
        if to_unit == ElectricResistanceUnits.Microohm:
            return ((value) * 1e-06)
        
        if to_unit == ElectricResistanceUnits.Milliohm:
            return ((value) * 0.001)
        
        if to_unit == ElectricResistanceUnits.Kiloohm:
            return ((value) * 1000.0)
        
        if to_unit == ElectricResistanceUnits.Megaohm:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricResistanceUnits.Gigaohm:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricResistanceUnits.Teraohm:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_ohms(ohms: float):
        """
        Create a new instance of ElectricResistance from a value in ohms.

        

        :param meters: The ElectricResistance value in ohms.
        :type ohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(ohms, ElectricResistanceUnits.Ohm)

    
    @staticmethod
    def from_nanoohms(nanoohms: float):
        """
        Create a new instance of ElectricResistance from a value in nanoohms.

        

        :param meters: The ElectricResistance value in nanoohms.
        :type nanoohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(nanoohms, ElectricResistanceUnits.Nanoohm)

    
    @staticmethod
    def from_microohms(microohms: float):
        """
        Create a new instance of ElectricResistance from a value in microohms.

        

        :param meters: The ElectricResistance value in microohms.
        :type microohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(microohms, ElectricResistanceUnits.Microohm)

    
    @staticmethod
    def from_milliohms(milliohms: float):
        """
        Create a new instance of ElectricResistance from a value in milliohms.

        

        :param meters: The ElectricResistance value in milliohms.
        :type milliohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(milliohms, ElectricResistanceUnits.Milliohm)

    
    @staticmethod
    def from_kiloohms(kiloohms: float):
        """
        Create a new instance of ElectricResistance from a value in kiloohms.

        

        :param meters: The ElectricResistance value in kiloohms.
        :type kiloohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(kiloohms, ElectricResistanceUnits.Kiloohm)

    
    @staticmethod
    def from_megaohms(megaohms: float):
        """
        Create a new instance of ElectricResistance from a value in megaohms.

        

        :param meters: The ElectricResistance value in megaohms.
        :type megaohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(megaohms, ElectricResistanceUnits.Megaohm)

    
    @staticmethod
    def from_gigaohms(gigaohms: float):
        """
        Create a new instance of ElectricResistance from a value in gigaohms.

        

        :param meters: The ElectricResistance value in gigaohms.
        :type gigaohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(gigaohms, ElectricResistanceUnits.Gigaohm)

    
    @staticmethod
    def from_teraohms(teraohms: float):
        """
        Create a new instance of ElectricResistance from a value in teraohms.

        

        :param meters: The ElectricResistance value in teraohms.
        :type teraohms: float
        :return: A new instance of ElectricResistance.
        :rtype: ElectricResistance
        """
        return ElectricResistance(teraohms, ElectricResistanceUnits.Teraohm)

    
    @property
    def ohms(self) -> float:
        """
        
        """
        if self.__ohms != None:
            return self.__ohms
        self.__ohms = self.__convert_from_base(ElectricResistanceUnits.Ohm)
        return self.__ohms

    
    @property
    def nanoohms(self) -> float:
        """
        
        """
        if self.__nanoohms != None:
            return self.__nanoohms
        self.__nanoohms = self.__convert_from_base(ElectricResistanceUnits.Nanoohm)
        return self.__nanoohms

    
    @property
    def microohms(self) -> float:
        """
        
        """
        if self.__microohms != None:
            return self.__microohms
        self.__microohms = self.__convert_from_base(ElectricResistanceUnits.Microohm)
        return self.__microohms

    
    @property
    def milliohms(self) -> float:
        """
        
        """
        if self.__milliohms != None:
            return self.__milliohms
        self.__milliohms = self.__convert_from_base(ElectricResistanceUnits.Milliohm)
        return self.__milliohms

    
    @property
    def kiloohms(self) -> float:
        """
        
        """
        if self.__kiloohms != None:
            return self.__kiloohms
        self.__kiloohms = self.__convert_from_base(ElectricResistanceUnits.Kiloohm)
        return self.__kiloohms

    
    @property
    def megaohms(self) -> float:
        """
        
        """
        if self.__megaohms != None:
            return self.__megaohms
        self.__megaohms = self.__convert_from_base(ElectricResistanceUnits.Megaohm)
        return self.__megaohms

    
    @property
    def gigaohms(self) -> float:
        """
        
        """
        if self.__gigaohms != None:
            return self.__gigaohms
        self.__gigaohms = self.__convert_from_base(ElectricResistanceUnits.Gigaohm)
        return self.__gigaohms

    
    @property
    def teraohms(self) -> float:
        """
        
        """
        if self.__teraohms != None:
            return self.__teraohms
        self.__teraohms = self.__convert_from_base(ElectricResistanceUnits.Teraohm)
        return self.__teraohms

    
    def to_string(self, unit: ElectricResistanceUnits = ElectricResistanceUnits.Ohm, fractional_digits: int = None) -> str:
        """
        Format the ElectricResistance to a string.
        
        Note: the default format for ElectricResistance is Ohm.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricResistance. Default is 'Ohm'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricResistanceUnits.Ohm:
            return f"""{super()._truncate_fraction_digits(self.ohms, fractional_digits)} Ω"""
        
        if unit == ElectricResistanceUnits.Nanoohm:
            return f"""{super()._truncate_fraction_digits(self.nanoohms, fractional_digits)} nΩ"""
        
        if unit == ElectricResistanceUnits.Microohm:
            return f"""{super()._truncate_fraction_digits(self.microohms, fractional_digits)} μΩ"""
        
        if unit == ElectricResistanceUnits.Milliohm:
            return f"""{super()._truncate_fraction_digits(self.milliohms, fractional_digits)} mΩ"""
        
        if unit == ElectricResistanceUnits.Kiloohm:
            return f"""{super()._truncate_fraction_digits(self.kiloohms, fractional_digits)} kΩ"""
        
        if unit == ElectricResistanceUnits.Megaohm:
            return f"""{super()._truncate_fraction_digits(self.megaohms, fractional_digits)} MΩ"""
        
        if unit == ElectricResistanceUnits.Gigaohm:
            return f"""{super()._truncate_fraction_digits(self.gigaohms, fractional_digits)} GΩ"""
        
        if unit == ElectricResistanceUnits.Teraohm:
            return f"""{super()._truncate_fraction_digits(self.teraohms, fractional_digits)} TΩ"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricResistanceUnits = ElectricResistanceUnits.Ohm) -> str:
        """
        Get ElectricResistance unit abbreviation.
        Note! the default abbreviation for ElectricResistance is Ohm.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricResistanceUnits.Ohm:
            return """Ω"""
        
        if unit_abbreviation == ElectricResistanceUnits.Nanoohm:
            return """nΩ"""
        
        if unit_abbreviation == ElectricResistanceUnits.Microohm:
            return """μΩ"""
        
        if unit_abbreviation == ElectricResistanceUnits.Milliohm:
            return """mΩ"""
        
        if unit_abbreviation == ElectricResistanceUnits.Kiloohm:
            return """kΩ"""
        
        if unit_abbreviation == ElectricResistanceUnits.Megaohm:
            return """MΩ"""
        
        if unit_abbreviation == ElectricResistanceUnits.Gigaohm:
            return """GΩ"""
        
        if unit_abbreviation == ElectricResistanceUnits.Teraohm:
            return """TΩ"""
        