from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricImpedanceUnits(Enum):
        """
            ElectricImpedanceUnits enumeration
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
        

class ElectricImpedanceDto:
    """
    A DTO representation of a ElectricImpedance

    Attributes:
        value (float): The value of the ElectricImpedance.
        unit (ElectricImpedanceUnits): The specific unit that the ElectricImpedance value is representing.
    """

    def __init__(self, value: float, unit: ElectricImpedanceUnits):
        """
        Create a new DTO representation of a ElectricImpedance

        Parameters:
            value (float): The value of the ElectricImpedance.
            unit (ElectricImpedanceUnits): The specific unit that the ElectricImpedance value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricImpedance
        """
        self.unit: ElectricImpedanceUnits = unit
        """
        The specific unit that the ElectricImpedance value is representing
        """

    def to_json(self):
        """
        Get a ElectricImpedance DTO JSON object representing the current unit.

        :return: JSON object represents ElectricImpedance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Ohm"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricImpedance DTO from a json representation.

        :param data: The ElectricImpedance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Ohm"}
        :return: A new instance of ElectricImpedanceDto.
        :rtype: ElectricImpedanceDto
        """
        return ElectricImpedanceDto(value=data["value"], unit=ElectricImpedanceUnits(data["unit"]))


class ElectricImpedance(AbstractMeasure):
    """
    Electric impedance is the opposition to alternating current presented by the combined effect of resistance and reactance in a circuit. It is defined as the inverse of admittance. The SI unit of impedance is the ohm (symbol Ω).

    Args:
        value (float): The value.
        from_unit (ElectricImpedanceUnits): The ElectricImpedance unit to create from, The default unit is Ohm
    """
    def __init__(self, value: float, from_unit: ElectricImpedanceUnits = ElectricImpedanceUnits.Ohm):
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
        

    def convert(self, unit: ElectricImpedanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricImpedanceUnits = ElectricImpedanceUnits.Ohm) -> ElectricImpedanceDto:
        """
        Get a new instance of ElectricImpedance DTO representing the current unit.

        :param hold_in_unit: The specific ElectricImpedance unit to store the ElectricImpedance value in the DTO representation.
        :type hold_in_unit: ElectricImpedanceUnits
        :return: A new instance of ElectricImpedanceDto.
        :rtype: ElectricImpedanceDto
        """
        return ElectricImpedanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricImpedanceUnits = ElectricImpedanceUnits.Ohm):
        """
        Get a ElectricImpedance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricImpedance unit to store the ElectricImpedance value in the DTO representation.
        :type hold_in_unit: ElectricImpedanceUnits
        :return: JSON object represents ElectricImpedance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Ohm"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_impedance_dto: ElectricImpedanceDto):
        """
        Obtain a new instance of ElectricImpedance from a DTO unit object.

        :param electric_impedance_dto: The ElectricImpedance DTO representation.
        :type electric_impedance_dto: ElectricImpedanceDto
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(electric_impedance_dto.value, electric_impedance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricImpedance from a DTO unit json representation.

        :param data: The ElectricImpedance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Ohm"}
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance.from_dto(ElectricImpedanceDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricImpedanceUnits) -> float:
        value = self._value
        
        if from_unit == ElectricImpedanceUnits.Ohm:
            return (value)
        
        if from_unit == ElectricImpedanceUnits.Nanoohm:
            return ((value) / 1e-09)
        
        if from_unit == ElectricImpedanceUnits.Microohm:
            return ((value) / 1e-06)
        
        if from_unit == ElectricImpedanceUnits.Milliohm:
            return ((value) / 0.001)
        
        if from_unit == ElectricImpedanceUnits.Kiloohm:
            return ((value) / 1000.0)
        
        if from_unit == ElectricImpedanceUnits.Megaohm:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricImpedanceUnits.Gigaohm:
            return ((value) / 1000000000.0)
        
        if from_unit == ElectricImpedanceUnits.Teraohm:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricImpedanceUnits) -> float:
        
        if to_unit == ElectricImpedanceUnits.Ohm:
            return (value)
        
        if to_unit == ElectricImpedanceUnits.Nanoohm:
            return ((value) * 1e-09)
        
        if to_unit == ElectricImpedanceUnits.Microohm:
            return ((value) * 1e-06)
        
        if to_unit == ElectricImpedanceUnits.Milliohm:
            return ((value) * 0.001)
        
        if to_unit == ElectricImpedanceUnits.Kiloohm:
            return ((value) * 1000.0)
        
        if to_unit == ElectricImpedanceUnits.Megaohm:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricImpedanceUnits.Gigaohm:
            return ((value) * 1000000000.0)
        
        if to_unit == ElectricImpedanceUnits.Teraohm:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_ohms(ohms: float):
        """
        Create a new instance of ElectricImpedance from a value in ohms.

        

        :param meters: The ElectricImpedance value in ohms.
        :type ohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(ohms, ElectricImpedanceUnits.Ohm)

    
    @staticmethod
    def from_nanoohms(nanoohms: float):
        """
        Create a new instance of ElectricImpedance from a value in nanoohms.

        

        :param meters: The ElectricImpedance value in nanoohms.
        :type nanoohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(nanoohms, ElectricImpedanceUnits.Nanoohm)

    
    @staticmethod
    def from_microohms(microohms: float):
        """
        Create a new instance of ElectricImpedance from a value in microohms.

        

        :param meters: The ElectricImpedance value in microohms.
        :type microohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(microohms, ElectricImpedanceUnits.Microohm)

    
    @staticmethod
    def from_milliohms(milliohms: float):
        """
        Create a new instance of ElectricImpedance from a value in milliohms.

        

        :param meters: The ElectricImpedance value in milliohms.
        :type milliohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(milliohms, ElectricImpedanceUnits.Milliohm)

    
    @staticmethod
    def from_kiloohms(kiloohms: float):
        """
        Create a new instance of ElectricImpedance from a value in kiloohms.

        

        :param meters: The ElectricImpedance value in kiloohms.
        :type kiloohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(kiloohms, ElectricImpedanceUnits.Kiloohm)

    
    @staticmethod
    def from_megaohms(megaohms: float):
        """
        Create a new instance of ElectricImpedance from a value in megaohms.

        

        :param meters: The ElectricImpedance value in megaohms.
        :type megaohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(megaohms, ElectricImpedanceUnits.Megaohm)

    
    @staticmethod
    def from_gigaohms(gigaohms: float):
        """
        Create a new instance of ElectricImpedance from a value in gigaohms.

        

        :param meters: The ElectricImpedance value in gigaohms.
        :type gigaohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(gigaohms, ElectricImpedanceUnits.Gigaohm)

    
    @staticmethod
    def from_teraohms(teraohms: float):
        """
        Create a new instance of ElectricImpedance from a value in teraohms.

        

        :param meters: The ElectricImpedance value in teraohms.
        :type teraohms: float
        :return: A new instance of ElectricImpedance.
        :rtype: ElectricImpedance
        """
        return ElectricImpedance(teraohms, ElectricImpedanceUnits.Teraohm)

    
    @property
    def ohms(self) -> float:
        """
        
        """
        if self.__ohms != None:
            return self.__ohms
        self.__ohms = self.__convert_from_base(ElectricImpedanceUnits.Ohm)
        return self.__ohms

    
    @property
    def nanoohms(self) -> float:
        """
        
        """
        if self.__nanoohms != None:
            return self.__nanoohms
        self.__nanoohms = self.__convert_from_base(ElectricImpedanceUnits.Nanoohm)
        return self.__nanoohms

    
    @property
    def microohms(self) -> float:
        """
        
        """
        if self.__microohms != None:
            return self.__microohms
        self.__microohms = self.__convert_from_base(ElectricImpedanceUnits.Microohm)
        return self.__microohms

    
    @property
    def milliohms(self) -> float:
        """
        
        """
        if self.__milliohms != None:
            return self.__milliohms
        self.__milliohms = self.__convert_from_base(ElectricImpedanceUnits.Milliohm)
        return self.__milliohms

    
    @property
    def kiloohms(self) -> float:
        """
        
        """
        if self.__kiloohms != None:
            return self.__kiloohms
        self.__kiloohms = self.__convert_from_base(ElectricImpedanceUnits.Kiloohm)
        return self.__kiloohms

    
    @property
    def megaohms(self) -> float:
        """
        
        """
        if self.__megaohms != None:
            return self.__megaohms
        self.__megaohms = self.__convert_from_base(ElectricImpedanceUnits.Megaohm)
        return self.__megaohms

    
    @property
    def gigaohms(self) -> float:
        """
        
        """
        if self.__gigaohms != None:
            return self.__gigaohms
        self.__gigaohms = self.__convert_from_base(ElectricImpedanceUnits.Gigaohm)
        return self.__gigaohms

    
    @property
    def teraohms(self) -> float:
        """
        
        """
        if self.__teraohms != None:
            return self.__teraohms
        self.__teraohms = self.__convert_from_base(ElectricImpedanceUnits.Teraohm)
        return self.__teraohms

    
    def to_string(self, unit: ElectricImpedanceUnits = ElectricImpedanceUnits.Ohm, fractional_digits: int = None) -> str:
        """
        Format the ElectricImpedance to a string.
        
        Note: the default format for ElectricImpedance is Ohm.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricImpedance. Default is 'Ohm'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricImpedanceUnits.Ohm:
            return f"""{super()._truncate_fraction_digits(self.ohms, fractional_digits)} Ω"""
        
        if unit == ElectricImpedanceUnits.Nanoohm:
            return f"""{super()._truncate_fraction_digits(self.nanoohms, fractional_digits)} nΩ"""
        
        if unit == ElectricImpedanceUnits.Microohm:
            return f"""{super()._truncate_fraction_digits(self.microohms, fractional_digits)} μΩ"""
        
        if unit == ElectricImpedanceUnits.Milliohm:
            return f"""{super()._truncate_fraction_digits(self.milliohms, fractional_digits)} mΩ"""
        
        if unit == ElectricImpedanceUnits.Kiloohm:
            return f"""{super()._truncate_fraction_digits(self.kiloohms, fractional_digits)} kΩ"""
        
        if unit == ElectricImpedanceUnits.Megaohm:
            return f"""{super()._truncate_fraction_digits(self.megaohms, fractional_digits)} MΩ"""
        
        if unit == ElectricImpedanceUnits.Gigaohm:
            return f"""{super()._truncate_fraction_digits(self.gigaohms, fractional_digits)} GΩ"""
        
        if unit == ElectricImpedanceUnits.Teraohm:
            return f"""{super()._truncate_fraction_digits(self.teraohms, fractional_digits)} TΩ"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricImpedanceUnits = ElectricImpedanceUnits.Ohm) -> str:
        """
        Get ElectricImpedance unit abbreviation.
        Note! the default abbreviation for ElectricImpedance is Ohm.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricImpedanceUnits.Ohm:
            return """Ω"""
        
        if unit_abbreviation == ElectricImpedanceUnits.Nanoohm:
            return """nΩ"""
        
        if unit_abbreviation == ElectricImpedanceUnits.Microohm:
            return """μΩ"""
        
        if unit_abbreviation == ElectricImpedanceUnits.Milliohm:
            return """mΩ"""
        
        if unit_abbreviation == ElectricImpedanceUnits.Kiloohm:
            return """kΩ"""
        
        if unit_abbreviation == ElectricImpedanceUnits.Megaohm:
            return """MΩ"""
        
        if unit_abbreviation == ElectricImpedanceUnits.Gigaohm:
            return """GΩ"""
        
        if unit_abbreviation == ElectricImpedanceUnits.Teraohm:
            return """TΩ"""
        