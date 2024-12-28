from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricReactanceUnits(Enum):
        """
            ElectricReactanceUnits enumeration
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
        

class ElectricReactanceDto:
    """
    A DTO representation of a ElectricReactance

    Attributes:
        value (float): The value of the ElectricReactance.
        unit (ElectricReactanceUnits): The specific unit that the ElectricReactance value is representing.
    """

    def __init__(self, value: float, unit: ElectricReactanceUnits):
        """
        Create a new DTO representation of a ElectricReactance

        Parameters:
            value (float): The value of the ElectricReactance.
            unit (ElectricReactanceUnits): The specific unit that the ElectricReactance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricReactance
        """
        self.unit: ElectricReactanceUnits = unit
        """
        The specific unit that the ElectricReactance value is representing
        """

    def to_json(self):
        """
        Get a ElectricReactance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricReactance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Ohm"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricReactance DTO from a json representation.

        :param data: The ElectricReactance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Ohm"}
        :return: A new instance of ElectricReactanceDto.
        :rtype: ElectricReactanceDto
        """
        return ElectricReactanceDto(value=data["value"], unit=ElectricReactanceUnits(data["unit"]))


class ElectricReactance(AbstractMeasure):
    """
    In electrical circuits, reactance is the opposition presented to alternating current by inductance and capacitance. Along with resistance, it is one of two elements of impedance.

    Args:
        value (float): The value.
        from_unit (ElectricReactanceUnits): The ElectricReactance unit to create from, The default unit is Ohm
    """
    def __init__(self, value: float, from_unit: ElectricReactanceUnits = ElectricReactanceUnits.Ohm):
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
        

    def convert(self, unit: ElectricReactanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricReactanceUnits = ElectricReactanceUnits.Ohm) -> ElectricReactanceDto:
        """
        Get a new instance of ElectricReactance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricReactance unit to store the ElectricReactance value in the DTO representation.
        :type hold_in_unit: ElectricReactanceUnits
        :return: A new instance of ElectricReactanceDto.
        :rtype: ElectricReactanceDto
        """
        return ElectricReactanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricReactanceUnits = ElectricReactanceUnits.Ohm):
        """
        Get a ElectricReactance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricReactance unit to store the ElectricReactance value in the DTO representation.
        :type hold_in_unit: ElectricReactanceUnits
        :return: JSON object represents ElectricReactance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Ohm"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_reactance_dto: ElectricReactanceDto):
        """
        Obtain a new instance of ElectricReactance from a DTO unit object.

        :param electric_reactance_dto: The ElectricReactance DTO representation.
        :type electric_reactance_dto: ElectricReactanceDto
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(electric_reactance_dto.value, electric_reactance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricReactance from a DTO unit json representation.

        :param data: The ElectricReactance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Ohm"}
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance.from_dto(ElectricReactanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricReactanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricReactanceUnits.Ohm:
            return (value)
        
        if from_unit == ElectricReactanceUnits.Nanoohm:
            return ((value) / 1e-09)
        
        if from_unit == ElectricReactanceUnits.Microohm:
            return ((value) / 1e-06)
        
        if from_unit == ElectricReactanceUnits.Milliohm:
            return ((value) / 0.001)
        
        if from_unit == ElectricReactanceUnits.Kiloohm:
            return ((value) / 1000.0)
        
        if from_unit == ElectricReactanceUnits.Megaohm:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricReactanceUnits.Gigaohm:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricReactanceUnits.Teraohm:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricReactanceUnits) -> float:
        
        if to_unit == ElectricReactanceUnits.Ohm:
            return (value)
        
        if to_unit == ElectricReactanceUnits.Nanoohm:
            return ((value) * 1e-09)
        
        if to_unit == ElectricReactanceUnits.Microohm:
            return ((value) * 1e-06)
        
        if to_unit == ElectricReactanceUnits.Milliohm:
            return ((value) * 0.001)
        
        if to_unit == ElectricReactanceUnits.Kiloohm:
            return ((value) * 1000.0)
        
        if to_unit == ElectricReactanceUnits.Megaohm:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricReactanceUnits.Gigaohm:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricReactanceUnits.Teraohm:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_ohms(ohms: float):
        """
        Create a new instance of ElectricReactance from a value in ohms.

        

        :param meters: The ElectricReactance value in ohms.
        :type ohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(ohms, ElectricReactanceUnits.Ohm)

    
    @staticmethod
    def from_nanoohms(nanoohms: float):
        """
        Create a new instance of ElectricReactance from a value in nanoohms.

        

        :param meters: The ElectricReactance value in nanoohms.
        :type nanoohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(nanoohms, ElectricReactanceUnits.Nanoohm)

    
    @staticmethod
    def from_microohms(microohms: float):
        """
        Create a new instance of ElectricReactance from a value in microohms.

        

        :param meters: The ElectricReactance value in microohms.
        :type microohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(microohms, ElectricReactanceUnits.Microohm)

    
    @staticmethod
    def from_milliohms(milliohms: float):
        """
        Create a new instance of ElectricReactance from a value in milliohms.

        

        :param meters: The ElectricReactance value in milliohms.
        :type milliohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(milliohms, ElectricReactanceUnits.Milliohm)

    
    @staticmethod
    def from_kiloohms(kiloohms: float):
        """
        Create a new instance of ElectricReactance from a value in kiloohms.

        

        :param meters: The ElectricReactance value in kiloohms.
        :type kiloohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(kiloohms, ElectricReactanceUnits.Kiloohm)

    
    @staticmethod
    def from_megaohms(megaohms: float):
        """
        Create a new instance of ElectricReactance from a value in megaohms.

        

        :param meters: The ElectricReactance value in megaohms.
        :type megaohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(megaohms, ElectricReactanceUnits.Megaohm)

    
    @staticmethod
    def from_gigaohms(gigaohms: float):
        """
        Create a new instance of ElectricReactance from a value in gigaohms.

        

        :param meters: The ElectricReactance value in gigaohms.
        :type gigaohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(gigaohms, ElectricReactanceUnits.Gigaohm)

    
    @staticmethod
    def from_teraohms(teraohms: float):
        """
        Create a new instance of ElectricReactance from a value in teraohms.

        

        :param meters: The ElectricReactance value in teraohms.
        :type teraohms: float
        :return: A new instance of ElectricReactance.
        :rtype: ElectricReactance
        """
        return ElectricReactance(teraohms, ElectricReactanceUnits.Teraohm)

    
    @property
    def ohms(self) -> float:
        """
        
        """
        if self.__ohms != None:
            return self.__ohms
        self.__ohms = self.__convert_from_base(ElectricReactanceUnits.Ohm)
        return self.__ohms

    
    @property
    def nanoohms(self) -> float:
        """
        
        """
        if self.__nanoohms != None:
            return self.__nanoohms
        self.__nanoohms = self.__convert_from_base(ElectricReactanceUnits.Nanoohm)
        return self.__nanoohms

    
    @property
    def microohms(self) -> float:
        """
        
        """
        if self.__microohms != None:
            return self.__microohms
        self.__microohms = self.__convert_from_base(ElectricReactanceUnits.Microohm)
        return self.__microohms

    
    @property
    def milliohms(self) -> float:
        """
        
        """
        if self.__milliohms != None:
            return self.__milliohms
        self.__milliohms = self.__convert_from_base(ElectricReactanceUnits.Milliohm)
        return self.__milliohms

    
    @property
    def kiloohms(self) -> float:
        """
        
        """
        if self.__kiloohms != None:
            return self.__kiloohms
        self.__kiloohms = self.__convert_from_base(ElectricReactanceUnits.Kiloohm)
        return self.__kiloohms

    
    @property
    def megaohms(self) -> float:
        """
        
        """
        if self.__megaohms != None:
            return self.__megaohms
        self.__megaohms = self.__convert_from_base(ElectricReactanceUnits.Megaohm)
        return self.__megaohms

    
    @property
    def gigaohms(self) -> float:
        """
        
        """
        if self.__gigaohms != None:
            return self.__gigaohms
        self.__gigaohms = self.__convert_from_base(ElectricReactanceUnits.Gigaohm)
        return self.__gigaohms

    
    @property
    def teraohms(self) -> float:
        """
        
        """
        if self.__teraohms != None:
            return self.__teraohms
        self.__teraohms = self.__convert_from_base(ElectricReactanceUnits.Teraohm)
        return self.__teraohms

    
    def to_string(self, unit: ElectricReactanceUnits = ElectricReactanceUnits.Ohm, fractional_digits: int = None) -> str:
        """
        Format the ElectricReactance to a string.
        
        Note: the default format for ElectricReactance is Ohm.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricReactance. Default is 'Ohm'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricReactanceUnits.Ohm:
            return f"""{super()._truncate_fraction_digits(self.ohms, fractional_digits)} Ω"""
        
        if unit == ElectricReactanceUnits.Nanoohm:
            return f"""{super()._truncate_fraction_digits(self.nanoohms, fractional_digits)} nΩ"""
        
        if unit == ElectricReactanceUnits.Microohm:
            return f"""{super()._truncate_fraction_digits(self.microohms, fractional_digits)} μΩ"""
        
        if unit == ElectricReactanceUnits.Milliohm:
            return f"""{super()._truncate_fraction_digits(self.milliohms, fractional_digits)} mΩ"""
        
        if unit == ElectricReactanceUnits.Kiloohm:
            return f"""{super()._truncate_fraction_digits(self.kiloohms, fractional_digits)} kΩ"""
        
        if unit == ElectricReactanceUnits.Megaohm:
            return f"""{super()._truncate_fraction_digits(self.megaohms, fractional_digits)} MΩ"""
        
        if unit == ElectricReactanceUnits.Gigaohm:
            return f"""{super()._truncate_fraction_digits(self.gigaohms, fractional_digits)} GΩ"""
        
        if unit == ElectricReactanceUnits.Teraohm:
            return f"""{super()._truncate_fraction_digits(self.teraohms, fractional_digits)} TΩ"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricReactanceUnits = ElectricReactanceUnits.Ohm) -> str:
        """
        Get ElectricReactance unit abbreviation.
        Note! the default abbreviation for ElectricReactance is Ohm.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricReactanceUnits.Ohm:
            return """Ω"""
        
        if unit_abbreviation == ElectricReactanceUnits.Nanoohm:
            return """nΩ"""
        
        if unit_abbreviation == ElectricReactanceUnits.Microohm:
            return """μΩ"""
        
        if unit_abbreviation == ElectricReactanceUnits.Milliohm:
            return """mΩ"""
        
        if unit_abbreviation == ElectricReactanceUnits.Kiloohm:
            return """kΩ"""
        
        if unit_abbreviation == ElectricReactanceUnits.Megaohm:
            return """MΩ"""
        
        if unit_abbreviation == ElectricReactanceUnits.Gigaohm:
            return """GΩ"""
        
        if unit_abbreviation == ElectricReactanceUnits.Teraohm:
            return """TΩ"""
        