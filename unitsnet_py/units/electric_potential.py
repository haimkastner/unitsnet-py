from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricPotentialUnits(Enum):
        """
            ElectricPotentialUnits enumeration
        """
        
        Volt = 'Volt'
        """
            
        """
        
        Nanovolt = 'Nanovolt'
        """
            
        """
        
        Microvolt = 'Microvolt'
        """
            
        """
        
        Millivolt = 'Millivolt'
        """
            
        """
        
        Kilovolt = 'Kilovolt'
        """
            
        """
        
        Megavolt = 'Megavolt'
        """
            
        """
        

class ElectricPotentialDto:
    """
    A DTO representation of a ElectricPotential

    Attributes:
        value (float): The value of the ElectricPotential.
        unit (ElectricPotentialUnits): The specific unit that the ElectricPotential value is representing.
    """

    def __init__(self, value: float, unit: ElectricPotentialUnits):
        """
        Create a new DTO representation of a ElectricPotential

        Parameters:
            value (float): The value of the ElectricPotential.
            unit (ElectricPotentialUnits): The specific unit that the ElectricPotential value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricPotential
        """
        self.unit: ElectricPotentialUnits = unit
        """
        The specific unit that the ElectricPotential value is representing
        """

    def to_json(self):
        """
        Get a ElectricPotential DTO JSON object representing the current unit.

        :return: JSON object represents ElectricPotential DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Volt"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricPotential DTO from a json representation.

        :param data: The ElectricPotential DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Volt"}
        :return: A new instance of ElectricPotentialDto.
        :rtype: ElectricPotentialDto
        """
        return ElectricPotentialDto(value=data["value"], unit=ElectricPotentialUnits(data["unit"]))


class ElectricPotential(AbstractMeasure):
    """
    In classical electromagnetism, the electric potential (a scalar quantity denoted by Φ, ΦE or V and also called the electric field potential or the electrostatic potential) at a point is the amount of electric potential energy that a unitary point charge would have when located at that point.

    Args:
        value (float): The value.
        from_unit (ElectricPotentialUnits): The ElectricPotential unit to create from, The default unit is Volt
    """
    def __init__(self, value: float, from_unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__volts = None
        
        self.__nanovolts = None
        
        self.__microvolts = None
        
        self.__millivolts = None
        
        self.__kilovolts = None
        
        self.__megavolts = None
        

    def convert(self, unit: ElectricPotentialUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt) -> ElectricPotentialDto:
        """
        Get a new instance of ElectricPotential DTO representing the current unit.

        :param hold_in_unit: The specific ElectricPotential unit to store the ElectricPotential value in the DTO representation.
        :type hold_in_unit: ElectricPotentialUnits
        :return: A new instance of ElectricPotentialDto.
        :rtype: ElectricPotentialDto
        """
        return ElectricPotentialDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt):
        """
        Get a ElectricPotential DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricPotential unit to store the ElectricPotential value in the DTO representation.
        :type hold_in_unit: ElectricPotentialUnits
        :return: JSON object represents ElectricPotential DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Volt"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_potential_dto: ElectricPotentialDto):
        """
        Obtain a new instance of ElectricPotential from a DTO unit object.

        :param electric_potential_dto: The ElectricPotential DTO representation.
        :type electric_potential_dto: ElectricPotentialDto
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(electric_potential_dto.value, electric_potential_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricPotential from a DTO unit json representation.

        :param data: The ElectricPotential DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Volt"}
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential.from_dto(ElectricPotentialDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricPotentialUnits) -> float:
        value = self._value
        
        if from_unit == ElectricPotentialUnits.Volt:
            return (value)
        
        if from_unit == ElectricPotentialUnits.Nanovolt:
            return ((value) / 1e-09)
        
        if from_unit == ElectricPotentialUnits.Microvolt:
            return ((value) / 1e-06)
        
        if from_unit == ElectricPotentialUnits.Millivolt:
            return ((value) / 0.001)
        
        if from_unit == ElectricPotentialUnits.Kilovolt:
            return ((value) / 1000.0)
        
        if from_unit == ElectricPotentialUnits.Megavolt:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricPotentialUnits) -> float:
        
        if to_unit == ElectricPotentialUnits.Volt:
            return (value)
        
        if to_unit == ElectricPotentialUnits.Nanovolt:
            return ((value) * 1e-09)
        
        if to_unit == ElectricPotentialUnits.Microvolt:
            return ((value) * 1e-06)
        
        if to_unit == ElectricPotentialUnits.Millivolt:
            return ((value) * 0.001)
        
        if to_unit == ElectricPotentialUnits.Kilovolt:
            return ((value) * 1000.0)
        
        if to_unit == ElectricPotentialUnits.Megavolt:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_volts(volts: float):
        """
        Create a new instance of ElectricPotential from a value in volts.

        

        :param meters: The ElectricPotential value in volts.
        :type volts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(volts, ElectricPotentialUnits.Volt)

    
    @staticmethod
    def from_nanovolts(nanovolts: float):
        """
        Create a new instance of ElectricPotential from a value in nanovolts.

        

        :param meters: The ElectricPotential value in nanovolts.
        :type nanovolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(nanovolts, ElectricPotentialUnits.Nanovolt)

    
    @staticmethod
    def from_microvolts(microvolts: float):
        """
        Create a new instance of ElectricPotential from a value in microvolts.

        

        :param meters: The ElectricPotential value in microvolts.
        :type microvolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(microvolts, ElectricPotentialUnits.Microvolt)

    
    @staticmethod
    def from_millivolts(millivolts: float):
        """
        Create a new instance of ElectricPotential from a value in millivolts.

        

        :param meters: The ElectricPotential value in millivolts.
        :type millivolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(millivolts, ElectricPotentialUnits.Millivolt)

    
    @staticmethod
    def from_kilovolts(kilovolts: float):
        """
        Create a new instance of ElectricPotential from a value in kilovolts.

        

        :param meters: The ElectricPotential value in kilovolts.
        :type kilovolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(kilovolts, ElectricPotentialUnits.Kilovolt)

    
    @staticmethod
    def from_megavolts(megavolts: float):
        """
        Create a new instance of ElectricPotential from a value in megavolts.

        

        :param meters: The ElectricPotential value in megavolts.
        :type megavolts: float
        :return: A new instance of ElectricPotential.
        :rtype: ElectricPotential
        """
        return ElectricPotential(megavolts, ElectricPotentialUnits.Megavolt)

    
    @property
    def volts(self) -> float:
        """
        
        """
        if self.__volts != None:
            return self.__volts
        self.__volts = self.__convert_from_base(ElectricPotentialUnits.Volt)
        return self.__volts

    
    @property
    def nanovolts(self) -> float:
        """
        
        """
        if self.__nanovolts != None:
            return self.__nanovolts
        self.__nanovolts = self.__convert_from_base(ElectricPotentialUnits.Nanovolt)
        return self.__nanovolts

    
    @property
    def microvolts(self) -> float:
        """
        
        """
        if self.__microvolts != None:
            return self.__microvolts
        self.__microvolts = self.__convert_from_base(ElectricPotentialUnits.Microvolt)
        return self.__microvolts

    
    @property
    def millivolts(self) -> float:
        """
        
        """
        if self.__millivolts != None:
            return self.__millivolts
        self.__millivolts = self.__convert_from_base(ElectricPotentialUnits.Millivolt)
        return self.__millivolts

    
    @property
    def kilovolts(self) -> float:
        """
        
        """
        if self.__kilovolts != None:
            return self.__kilovolts
        self.__kilovolts = self.__convert_from_base(ElectricPotentialUnits.Kilovolt)
        return self.__kilovolts

    
    @property
    def megavolts(self) -> float:
        """
        
        """
        if self.__megavolts != None:
            return self.__megavolts
        self.__megavolts = self.__convert_from_base(ElectricPotentialUnits.Megavolt)
        return self.__megavolts

    
    def to_string(self, unit: ElectricPotentialUnits = ElectricPotentialUnits.Volt, fractional_digits: int = None) -> str:
        """
        Format the ElectricPotential to a string.
        
        Note: the default format for ElectricPotential is Volt.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricPotential. Default is 'Volt'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricPotentialUnits.Volt:
            return f"""{super()._truncate_fraction_digits(self.volts, fractional_digits)} V"""
        
        if unit == ElectricPotentialUnits.Nanovolt:
            return f"""{super()._truncate_fraction_digits(self.nanovolts, fractional_digits)} nV"""
        
        if unit == ElectricPotentialUnits.Microvolt:
            return f"""{super()._truncate_fraction_digits(self.microvolts, fractional_digits)} μV"""
        
        if unit == ElectricPotentialUnits.Millivolt:
            return f"""{super()._truncate_fraction_digits(self.millivolts, fractional_digits)} mV"""
        
        if unit == ElectricPotentialUnits.Kilovolt:
            return f"""{super()._truncate_fraction_digits(self.kilovolts, fractional_digits)} kV"""
        
        if unit == ElectricPotentialUnits.Megavolt:
            return f"""{super()._truncate_fraction_digits(self.megavolts, fractional_digits)} MV"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricPotentialUnits = ElectricPotentialUnits.Volt) -> str:
        """
        Get ElectricPotential unit abbreviation.
        Note! the default abbreviation for ElectricPotential is Volt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricPotentialUnits.Volt:
            return """V"""
        
        if unit_abbreviation == ElectricPotentialUnits.Nanovolt:
            return """nV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Microvolt:
            return """μV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Millivolt:
            return """mV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Kilovolt:
            return """kV"""
        
        if unit_abbreviation == ElectricPotentialUnits.Megavolt:
            return """MV"""
        