from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricPotentialAcUnits(Enum):
        """
            ElectricPotentialAcUnits enumeration
        """
        
        VoltAc = 'VoltAc'
        """
            
        """
        
        MicrovoltAc = 'MicrovoltAc'
        """
            
        """
        
        MillivoltAc = 'MillivoltAc'
        """
            
        """
        
        KilovoltAc = 'KilovoltAc'
        """
            
        """
        
        MegavoltAc = 'MegavoltAc'
        """
            
        """
        

class ElectricPotentialAcDto:
    """
    A DTO representation of a ElectricPotentialAc

    Attributes:
        value (float): The value of the ElectricPotentialAc.
        unit (ElectricPotentialAcUnits): The specific unit that the ElectricPotentialAc value is representing.
    """

    def __init__(self, value: float, unit: ElectricPotentialAcUnits):
        """
        Create a new DTO representation of a ElectricPotentialAc

        Parameters:
            value (float): The value of the ElectricPotentialAc.
            unit (ElectricPotentialAcUnits): The specific unit that the ElectricPotentialAc value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricPotentialAc
        """
        self.unit: ElectricPotentialAcUnits = unit
        """
        The specific unit that the ElectricPotentialAc value is representing
        """

    def to_json(self):
        """
        Get a ElectricPotentialAc DTO JSON object representing the current unit.

        :return: JSON object represents ElectricPotentialAc DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltAc"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricPotentialAc DTO from a json representation.

        :param data: The ElectricPotentialAc DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltAc"}
        :return: A new instance of ElectricPotentialAcDto.
        :rtype: ElectricPotentialAcDto
        """
        return ElectricPotentialAcDto(value=data["value"], unit=ElectricPotentialAcUnits(data["unit"]))


class ElectricPotentialAc(AbstractMeasure):
    """
    The Electric Potential of a system known to use Alternating Current.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialAcUnits): The ElectricPotentialAc unit to create from, The default unit is VoltAc
    """
    def __init__(self, value: float, from_unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts_ac = None
        
        self.__microvolts_ac = None
        
        self.__millivolts_ac = None
        
        self.__kilovolts_ac = None
        
        self.__megavolts_ac = None
        

    def convert(self, unit: ElectricPotentialAcUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc) -> ElectricPotentialAcDto:
        """
        Get a new instance of ElectricPotentialAc DTO representing the current unit.

        :param hold_in_unit: The specific ElectricPotentialAc unit to store the ElectricPotentialAc value in the DTO representation.
        :type hold_in_unit: ElectricPotentialAcUnits
        :return: A new instance of ElectricPotentialAcDto.
        :rtype: ElectricPotentialAcDto
        """
        return ElectricPotentialAcDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc):
        """
        Get a ElectricPotentialAc DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricPotentialAc unit to store the ElectricPotentialAc value in the DTO representation.
        :type hold_in_unit: ElectricPotentialAcUnits
        :return: JSON object represents ElectricPotentialAc DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltAc"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_potential_ac_dto: ElectricPotentialAcDto):
        """
        Obtain a new instance of ElectricPotentialAc from a DTO unit object.

        :param electric_potential_ac_dto: The ElectricPotentialAc DTO representation.
        :type electric_potential_ac_dto: ElectricPotentialAcDto
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(electric_potential_ac_dto.value, electric_potential_ac_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricPotentialAc from a DTO unit json representation.

        :param data: The ElectricPotentialAc DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltAc"}
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc.from_dto(ElectricPotentialAcDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricPotentialAcUnits) -> float:
        value = self._value
        
        if from_unit == ElectricPotentialAcUnits.VoltAc:
            return (value)
        
        if from_unit == ElectricPotentialAcUnits.MicrovoltAc:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialAcUnits.MillivoltAc:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialAcUnits.KilovoltAc:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialAcUnits.MegavoltAc:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialAcUnits) -> float:
        
        if to_unit == ElectricPotentialAcUnits.VoltAc:
            return (value)
        
        if to_unit == ElectricPotentialAcUnits.MicrovoltAc:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialAcUnits.MillivoltAc:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialAcUnits.KilovoltAc:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialAcUnits.MegavoltAc:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts_ac(volts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in volts_ac.

        

        :param meters: The ElectricPotentialAc value in volts_ac.
        :type volts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(volts_ac, ElectricPotentialAcUnits.VoltAc)

    
    @staticmethod
    def from_microvolts_ac(microvolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in microvolts_ac.

        

        :param meters: The ElectricPotentialAc value in microvolts_ac.
        :type microvolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(microvolts_ac, ElectricPotentialAcUnits.MicrovoltAc)

    
    @staticmethod
    def from_millivolts_ac(millivolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in millivolts_ac.

        

        :param meters: The ElectricPotentialAc value in millivolts_ac.
        :type millivolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(millivolts_ac, ElectricPotentialAcUnits.MillivoltAc)

    
    @staticmethod
    def from_kilovolts_ac(kilovolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in kilovolts_ac.

        

        :param meters: The ElectricPotentialAc value in kilovolts_ac.
        :type kilovolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(kilovolts_ac, ElectricPotentialAcUnits.KilovoltAc)

    
    @staticmethod
    def from_megavolts_ac(megavolts_ac: float):
        """
        Create a new instance of ElectricPotentialAc from a value in megavolts_ac.

        

        :param meters: The ElectricPotentialAc value in megavolts_ac.
        :type megavolts_ac: float
        :return: A new instance of ElectricPotentialAc.
        :rtype: ElectricPotentialAc
        """
        return ElectricPotentialAc(megavolts_ac, ElectricPotentialAcUnits.MegavoltAc)

    
    @property
    def volts_ac(self) -> float:
        """
        
        """
        if self.__volts_ac != None:
            return self.__volts_ac
        self.__volts_ac = self.__convert_from_base(ElectricPotentialAcUnits.VoltAc)
        return self.__volts_ac

    
    @property
    def microvolts_ac(self) -> float:
        """
        
        """
        if self.__microvolts_ac != None:
            return self.__microvolts_ac
        self.__microvolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MicrovoltAc)
        return self.__microvolts_ac

    
    @property
    def millivolts_ac(self) -> float:
        """
        
        """
        if self.__millivolts_ac != None:
            return self.__millivolts_ac
        self.__millivolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MillivoltAc)
        return self.__millivolts_ac

    
    @property
    def kilovolts_ac(self) -> float:
        """
        
        """
        if self.__kilovolts_ac != None:
            return self.__kilovolts_ac
        self.__kilovolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.KilovoltAc)
        return self.__kilovolts_ac

    
    @property
    def megavolts_ac(self) -> float:
        """
        
        """
        if self.__megavolts_ac != None:
            return self.__megavolts_ac
        self.__megavolts_ac = self.__convert_from_base(ElectricPotentialAcUnits.MegavoltAc)
        return self.__megavolts_ac

    
    def to_string(self, unit: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc, fractional_digits: int = None) -> str:
        """
        Format the ElectricPotentialAc to a string.
        
        Note: the default format for ElectricPotentialAc is VoltAc.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricPotentialAc. Default is 'VoltAc'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricPotentialAcUnits.VoltAc:
            return f"""{super()._truncate_fraction_digits(self.volts_ac, fractional_digits)} Vac"""
        
        if unit == ElectricPotentialAcUnits.MicrovoltAc:
            return f"""{super()._truncate_fraction_digits(self.microvolts_ac, fractional_digits)} μVac"""
        
        if unit == ElectricPotentialAcUnits.MillivoltAc:
            return f"""{super()._truncate_fraction_digits(self.millivolts_ac, fractional_digits)} mVac"""
        
        if unit == ElectricPotentialAcUnits.KilovoltAc:
            return f"""{super()._truncate_fraction_digits(self.kilovolts_ac, fractional_digits)} kVac"""
        
        if unit == ElectricPotentialAcUnits.MegavoltAc:
            return f"""{super()._truncate_fraction_digits(self.megavolts_ac, fractional_digits)} MVac"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialAcUnits = ElectricPotentialAcUnits.VoltAc) -> str:
        """
        Get ElectricPotentialAc unit abbreviation.
        Note! the default abbreviation for ElectricPotentialAc is VoltAc.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialAcUnits.VoltAc:
            return """Vac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MicrovoltAc:
            return """μVac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MillivoltAc:
            return """mVac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.KilovoltAc:
            return """kVac"""
        
        if unit_abbreviation == ElectricPotentialAcUnits.MegavoltAc:
            return """MVac"""
        