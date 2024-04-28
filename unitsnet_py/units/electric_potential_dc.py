from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricPotentialDcUnits(Enum):
        """
            ElectricPotentialDcUnits enumeration
        """
        
        VoltDc = 'VoltDc'
        """
            
        """
        
        MicrovoltDc = 'MicrovoltDc'
        """
            
        """
        
        MillivoltDc = 'MillivoltDc'
        """
            
        """
        
        KilovoltDc = 'KilovoltDc'
        """
            
        """
        
        MegavoltDc = 'MegavoltDc'
        """
            
        """
        

class ElectricPotentialDcDto:
    """
    A DTO representation of a ElectricPotentialDc

    Attributes:
        value (float): The value of the ElectricPotentialDc.
        unit (ElectricPotentialDcUnits): The specific unit that the ElectricPotentialDc value is representing.
    """

    def __init__(self, value: float, unit: ElectricPotentialDcUnits):
        """
        Create a new DTO representation of a ElectricPotentialDc

        Parameters:
            value (float): The value of the ElectricPotentialDc.
            unit (ElectricPotentialDcUnits): The specific unit that the ElectricPotentialDc value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricPotentialDc
        """
        self.unit: ElectricPotentialDcUnits = unit
        """
        The specific unit that the ElectricPotentialDc value is representing
        """

    def to_json(self):
        """
        Get a ElectricPotentialDc DTO JSON object representing the current unit.

        :return: JSON object represents ElectricPotentialDc DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltDc"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricPotentialDc DTO from a json representation.

        :param data: The ElectricPotentialDc DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltDc"}
        :return: A new instance of ElectricPotentialDcDto.
        :rtype: ElectricPotentialDcDto
        """
        return ElectricPotentialDcDto(value=data["value"], unit=ElectricPotentialDcUnits(data["unit"]))


class ElectricPotentialDc(AbstractMeasure):
    """
    The Electric Potential of a system known to use Direct Current.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialDcUnits): The ElectricPotentialDc unit to create from, The default unit is VoltDc
    """
    def __init__(self, value: float, from_unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts_dc = None
        
        self.__microvolts_dc = None
        
        self.__millivolts_dc = None
        
        self.__kilovolts_dc = None
        
        self.__megavolts_dc = None
        

    def convert(self, unit: ElectricPotentialDcUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc) -> ElectricPotentialDcDto:
        """
        Get a new instance of ElectricPotentialDc DTO representing the current unit.

        :param hold_in_unit: The specific ElectricPotentialDc unit to store the ElectricPotentialDc value in the DTO representation.
        :type hold_in_unit: ElectricPotentialDcUnits
        :return: A new instance of ElectricPotentialDcDto.
        :rtype: ElectricPotentialDcDto
        """
        return ElectricPotentialDcDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc):
        """
        Get a ElectricPotentialDc DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricPotentialDc unit to store the ElectricPotentialDc value in the DTO representation.
        :type hold_in_unit: ElectricPotentialDcUnits
        :return: JSON object represents ElectricPotentialDc DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "VoltDc"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_potential_dc_dto: ElectricPotentialDcDto):
        """
        Obtain a new instance of ElectricPotentialDc from a DTO unit object.

        :param electric_potential_dc_dto: The ElectricPotentialDc DTO representation.
        :type electric_potential_dc_dto: ElectricPotentialDcDto
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(electric_potential_dc_dto.value, electric_potential_dc_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricPotentialDc from a DTO unit json representation.

        :param data: The ElectricPotentialDc DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "VoltDc"}
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc.from_dto(ElectricPotentialDcDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricPotentialDcUnits) -> float:
        value = self._value
        
        if from_unit == ElectricPotentialDcUnits.VoltDc:
            return (value)
        
        if from_unit == ElectricPotentialDcUnits.MicrovoltDc:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialDcUnits.MillivoltDc:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialDcUnits.KilovoltDc:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialDcUnits.MegavoltDc:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialDcUnits) -> float:
        
        if to_unit == ElectricPotentialDcUnits.VoltDc:
            return (value)
        
        if to_unit == ElectricPotentialDcUnits.MicrovoltDc:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialDcUnits.MillivoltDc:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialDcUnits.KilovoltDc:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialDcUnits.MegavoltDc:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts_dc(volts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in volts_dc.

        

        :param meters: The ElectricPotentialDc value in volts_dc.
        :type volts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(volts_dc, ElectricPotentialDcUnits.VoltDc)

    
    @staticmethod
    def from_microvolts_dc(microvolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in microvolts_dc.

        

        :param meters: The ElectricPotentialDc value in microvolts_dc.
        :type microvolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(microvolts_dc, ElectricPotentialDcUnits.MicrovoltDc)

    
    @staticmethod
    def from_millivolts_dc(millivolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in millivolts_dc.

        

        :param meters: The ElectricPotentialDc value in millivolts_dc.
        :type millivolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(millivolts_dc, ElectricPotentialDcUnits.MillivoltDc)

    
    @staticmethod
    def from_kilovolts_dc(kilovolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in kilovolts_dc.

        

        :param meters: The ElectricPotentialDc value in kilovolts_dc.
        :type kilovolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(kilovolts_dc, ElectricPotentialDcUnits.KilovoltDc)

    
    @staticmethod
    def from_megavolts_dc(megavolts_dc: float):
        """
        Create a new instance of ElectricPotentialDc from a value in megavolts_dc.

        

        :param meters: The ElectricPotentialDc value in megavolts_dc.
        :type megavolts_dc: float
        :return: A new instance of ElectricPotentialDc.
        :rtype: ElectricPotentialDc
        """
        return ElectricPotentialDc(megavolts_dc, ElectricPotentialDcUnits.MegavoltDc)

    
    @property
    def volts_dc(self) -> float:
        """
        
        """
        if self.__volts_dc != None:
            return self.__volts_dc
        self.__volts_dc = self.__convert_from_base(ElectricPotentialDcUnits.VoltDc)
        return self.__volts_dc

    
    @property
    def microvolts_dc(self) -> float:
        """
        
        """
        if self.__microvolts_dc != None:
            return self.__microvolts_dc
        self.__microvolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MicrovoltDc)
        return self.__microvolts_dc

    
    @property
    def millivolts_dc(self) -> float:
        """
        
        """
        if self.__millivolts_dc != None:
            return self.__millivolts_dc
        self.__millivolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MillivoltDc)
        return self.__millivolts_dc

    
    @property
    def kilovolts_dc(self) -> float:
        """
        
        """
        if self.__kilovolts_dc != None:
            return self.__kilovolts_dc
        self.__kilovolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.KilovoltDc)
        return self.__kilovolts_dc

    
    @property
    def megavolts_dc(self) -> float:
        """
        
        """
        if self.__megavolts_dc != None:
            return self.__megavolts_dc
        self.__megavolts_dc = self.__convert_from_base(ElectricPotentialDcUnits.MegavoltDc)
        return self.__megavolts_dc

    
    def to_string(self, unit: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc, fractional_digits: int = None) -> str:
        """
        Format the ElectricPotentialDc to a string.
        
        Note: the default format for ElectricPotentialDc is VoltDc.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricPotentialDc. Default is 'VoltDc'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricPotentialDcUnits.VoltDc:
            return f"""{super()._truncate_fraction_digits(self.volts_dc, fractional_digits)} Vdc"""
        
        if unit == ElectricPotentialDcUnits.MicrovoltDc:
            return f"""{super()._truncate_fraction_digits(self.microvolts_dc, fractional_digits)} μVdc"""
        
        if unit == ElectricPotentialDcUnits.MillivoltDc:
            return f"""{super()._truncate_fraction_digits(self.millivolts_dc, fractional_digits)} mVdc"""
        
        if unit == ElectricPotentialDcUnits.KilovoltDc:
            return f"""{super()._truncate_fraction_digits(self.kilovolts_dc, fractional_digits)} kVdc"""
        
        if unit == ElectricPotentialDcUnits.MegavoltDc:
            return f"""{super()._truncate_fraction_digits(self.megavolts_dc, fractional_digits)} MVdc"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialDcUnits = ElectricPotentialDcUnits.VoltDc) -> str:
        """
        Get ElectricPotentialDc unit abbreviation.
        Note! the default abbreviation for ElectricPotentialDc is VoltDc.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialDcUnits.VoltDc:
            return """Vdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MicrovoltDc:
            return """μVdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MillivoltDc:
            return """mVdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.KilovoltDc:
            return """kVdc"""
        
        if unit_abbreviation == ElectricPotentialDcUnits.MegavoltDc:
            return """MVdc"""
        