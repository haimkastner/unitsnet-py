from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricResistivityUnits(Enum):
        """
            ElectricResistivityUnits enumeration
        """
        
        OhmMeter = 'OhmMeter'
        """
            
        """
        
        OhmCentimeter = 'OhmCentimeter'
        """
            
        """
        
        PicoohmMeter = 'PicoohmMeter'
        """
            
        """
        
        NanoohmMeter = 'NanoohmMeter'
        """
            
        """
        
        MicroohmMeter = 'MicroohmMeter'
        """
            
        """
        
        MilliohmMeter = 'MilliohmMeter'
        """
            
        """
        
        KiloohmMeter = 'KiloohmMeter'
        """
            
        """
        
        MegaohmMeter = 'MegaohmMeter'
        """
            
        """
        
        PicoohmCentimeter = 'PicoohmCentimeter'
        """
            
        """
        
        NanoohmCentimeter = 'NanoohmCentimeter'
        """
            
        """
        
        MicroohmCentimeter = 'MicroohmCentimeter'
        """
            
        """
        
        MilliohmCentimeter = 'MilliohmCentimeter'
        """
            
        """
        
        KiloohmCentimeter = 'KiloohmCentimeter'
        """
            
        """
        
        MegaohmCentimeter = 'MegaohmCentimeter'
        """
            
        """
        

class ElectricResistivityDto:
    """
    A DTO representation of a ElectricResistivity

    Attributes:
        value (float): The value of the ElectricResistivity.
        unit (ElectricResistivityUnits): The specific unit that the ElectricResistivity value is representing.
    """

    def __init__(self, value: float, unit: ElectricResistivityUnits):
        """
        Create a new DTO representation of a ElectricResistivity

        Parameters:
            value (float): The value of the ElectricResistivity.
            unit (ElectricResistivityUnits): The specific unit that the ElectricResistivity value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricResistivity
        """
        self.unit: ElectricResistivityUnits = unit
        """
        The specific unit that the ElectricResistivity value is representing
        """

    def to_json(self):
        """
        Get a ElectricResistivity DTO JSON object representing the current unit.

        :return: JSON object represents ElectricResistivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "OhmMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricResistivity DTO from a json representation.

        :param data: The ElectricResistivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "OhmMeter"}
        :return: A new instance of ElectricResistivityDto.
        :rtype: ElectricResistivityDto
        """
        return ElectricResistivityDto(value=data["value"], unit=ElectricResistivityUnits(data["unit"]))


class ElectricResistivity(AbstractMeasure):
    """
    Electrical resistivity (also known as resistivity, specific electrical resistance, or volume resistivity) is a fundamental property that quantifies how strongly a given material opposes the flow of electric current.

    Args:
        value (float): The value.
        from_unit (ElectricResistivityUnits): The ElectricResistivity unit to create from, The default unit is OhmMeter
    """
    def __init__(self, value: float, from_unit: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__ohm_meters = None
        
        self.__ohms_centimeter = None
        
        self.__picoohm_meters = None
        
        self.__nanoohm_meters = None
        
        self.__microohm_meters = None
        
        self.__milliohm_meters = None
        
        self.__kiloohm_meters = None
        
        self.__megaohm_meters = None
        
        self.__picoohms_centimeter = None
        
        self.__nanoohms_centimeter = None
        
        self.__microohms_centimeter = None
        
        self.__milliohms_centimeter = None
        
        self.__kiloohms_centimeter = None
        
        self.__megaohms_centimeter = None
        

    def convert(self, unit: ElectricResistivityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter) -> ElectricResistivityDto:
        """
        Get a new instance of ElectricResistivity DTO representing the current unit.

        :param hold_in_unit: The specific ElectricResistivity unit to store the ElectricResistivity value in the DTO representation.
        :type hold_in_unit: ElectricResistivityUnits
        :return: A new instance of ElectricResistivityDto.
        :rtype: ElectricResistivityDto
        """
        return ElectricResistivityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter):
        """
        Get a ElectricResistivity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricResistivity unit to store the ElectricResistivity value in the DTO representation.
        :type hold_in_unit: ElectricResistivityUnits
        :return: JSON object represents ElectricResistivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "OhmMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_resistivity_dto: ElectricResistivityDto):
        """
        Obtain a new instance of ElectricResistivity from a DTO unit object.

        :param electric_resistivity_dto: The ElectricResistivity DTO representation.
        :type electric_resistivity_dto: ElectricResistivityDto
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(electric_resistivity_dto.value, electric_resistivity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricResistivity from a DTO unit json representation.

        :param data: The ElectricResistivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "OhmMeter"}
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity.from_dto(ElectricResistivityDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricResistivityUnits) -> float:
        value = self._value
        
        if from_unit == ElectricResistivityUnits.OhmMeter:
            return (value)
        
        if from_unit == ElectricResistivityUnits.OhmCentimeter:
            return (value * 100)
        
        if from_unit == ElectricResistivityUnits.PicoohmMeter:
            return ((value) / 1e-12)
        
        if from_unit == ElectricResistivityUnits.NanoohmMeter:
            return ((value) / 1e-09)
        
        if from_unit == ElectricResistivityUnits.MicroohmMeter:
            return ((value) / 1e-06)
        
        if from_unit == ElectricResistivityUnits.MilliohmMeter:
            return ((value) / 0.001)
        
        if from_unit == ElectricResistivityUnits.KiloohmMeter:
            return ((value) / 1000.0)
        
        if from_unit == ElectricResistivityUnits.MegaohmMeter:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricResistivityUnits.PicoohmCentimeter:
            return ((value * 100) / 1e-12)
        
        if from_unit == ElectricResistivityUnits.NanoohmCentimeter:
            return ((value * 100) / 1e-09)
        
        if from_unit == ElectricResistivityUnits.MicroohmCentimeter:
            return ((value * 100) / 1e-06)
        
        if from_unit == ElectricResistivityUnits.MilliohmCentimeter:
            return ((value * 100) / 0.001)
        
        if from_unit == ElectricResistivityUnits.KiloohmCentimeter:
            return ((value * 100) / 1000.0)
        
        if from_unit == ElectricResistivityUnits.MegaohmCentimeter:
            return ((value * 100) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricResistivityUnits) -> float:
        
        if to_unit == ElectricResistivityUnits.OhmMeter:
            return (value)
        
        if to_unit == ElectricResistivityUnits.OhmCentimeter:
            return (value / 100)
        
        if to_unit == ElectricResistivityUnits.PicoohmMeter:
            return ((value) * 1e-12)
        
        if to_unit == ElectricResistivityUnits.NanoohmMeter:
            return ((value) * 1e-09)
        
        if to_unit == ElectricResistivityUnits.MicroohmMeter:
            return ((value) * 1e-06)
        
        if to_unit == ElectricResistivityUnits.MilliohmMeter:
            return ((value) * 0.001)
        
        if to_unit == ElectricResistivityUnits.KiloohmMeter:
            return ((value) * 1000.0)
        
        if to_unit == ElectricResistivityUnits.MegaohmMeter:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricResistivityUnits.PicoohmCentimeter:
            return ((value / 100) * 1e-12)
        
        if to_unit == ElectricResistivityUnits.NanoohmCentimeter:
            return ((value / 100) * 1e-09)
        
        if to_unit == ElectricResistivityUnits.MicroohmCentimeter:
            return ((value / 100) * 1e-06)
        
        if to_unit == ElectricResistivityUnits.MilliohmCentimeter:
            return ((value / 100) * 0.001)
        
        if to_unit == ElectricResistivityUnits.KiloohmCentimeter:
            return ((value / 100) * 1000.0)
        
        if to_unit == ElectricResistivityUnits.MegaohmCentimeter:
            return ((value / 100) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_ohm_meters(ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in ohm_meters.

        

        :param meters: The ElectricResistivity value in ohm_meters.
        :type ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(ohm_meters, ElectricResistivityUnits.OhmMeter)

    
    @staticmethod
    def from_ohms_centimeter(ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in ohms_centimeter.

        

        :param meters: The ElectricResistivity value in ohms_centimeter.
        :type ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(ohms_centimeter, ElectricResistivityUnits.OhmCentimeter)

    
    @staticmethod
    def from_picoohm_meters(picoohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in picoohm_meters.

        

        :param meters: The ElectricResistivity value in picoohm_meters.
        :type picoohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(picoohm_meters, ElectricResistivityUnits.PicoohmMeter)

    
    @staticmethod
    def from_nanoohm_meters(nanoohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in nanoohm_meters.

        

        :param meters: The ElectricResistivity value in nanoohm_meters.
        :type nanoohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(nanoohm_meters, ElectricResistivityUnits.NanoohmMeter)

    
    @staticmethod
    def from_microohm_meters(microohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in microohm_meters.

        

        :param meters: The ElectricResistivity value in microohm_meters.
        :type microohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(microohm_meters, ElectricResistivityUnits.MicroohmMeter)

    
    @staticmethod
    def from_milliohm_meters(milliohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in milliohm_meters.

        

        :param meters: The ElectricResistivity value in milliohm_meters.
        :type milliohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(milliohm_meters, ElectricResistivityUnits.MilliohmMeter)

    
    @staticmethod
    def from_kiloohm_meters(kiloohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in kiloohm_meters.

        

        :param meters: The ElectricResistivity value in kiloohm_meters.
        :type kiloohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(kiloohm_meters, ElectricResistivityUnits.KiloohmMeter)

    
    @staticmethod
    def from_megaohm_meters(megaohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in megaohm_meters.

        

        :param meters: The ElectricResistivity value in megaohm_meters.
        :type megaohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(megaohm_meters, ElectricResistivityUnits.MegaohmMeter)

    
    @staticmethod
    def from_picoohms_centimeter(picoohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in picoohms_centimeter.

        

        :param meters: The ElectricResistivity value in picoohms_centimeter.
        :type picoohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(picoohms_centimeter, ElectricResistivityUnits.PicoohmCentimeter)

    
    @staticmethod
    def from_nanoohms_centimeter(nanoohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in nanoohms_centimeter.

        

        :param meters: The ElectricResistivity value in nanoohms_centimeter.
        :type nanoohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(nanoohms_centimeter, ElectricResistivityUnits.NanoohmCentimeter)

    
    @staticmethod
    def from_microohms_centimeter(microohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in microohms_centimeter.

        

        :param meters: The ElectricResistivity value in microohms_centimeter.
        :type microohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(microohms_centimeter, ElectricResistivityUnits.MicroohmCentimeter)

    
    @staticmethod
    def from_milliohms_centimeter(milliohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in milliohms_centimeter.

        

        :param meters: The ElectricResistivity value in milliohms_centimeter.
        :type milliohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(milliohms_centimeter, ElectricResistivityUnits.MilliohmCentimeter)

    
    @staticmethod
    def from_kiloohms_centimeter(kiloohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in kiloohms_centimeter.

        

        :param meters: The ElectricResistivity value in kiloohms_centimeter.
        :type kiloohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(kiloohms_centimeter, ElectricResistivityUnits.KiloohmCentimeter)

    
    @staticmethod
    def from_megaohms_centimeter(megaohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in megaohms_centimeter.

        

        :param meters: The ElectricResistivity value in megaohms_centimeter.
        :type megaohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(megaohms_centimeter, ElectricResistivityUnits.MegaohmCentimeter)

    
    @property
    def ohm_meters(self) -> float:
        """
        
        """
        if self.__ohm_meters != None:
            return self.__ohm_meters
        self.__ohm_meters = self.__convert_from_base(ElectricResistivityUnits.OhmMeter)
        return self.__ohm_meters

    
    @property
    def ohms_centimeter(self) -> float:
        """
        
        """
        if self.__ohms_centimeter != None:
            return self.__ohms_centimeter
        self.__ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.OhmCentimeter)
        return self.__ohms_centimeter

    
    @property
    def picoohm_meters(self) -> float:
        """
        
        """
        if self.__picoohm_meters != None:
            return self.__picoohm_meters
        self.__picoohm_meters = self.__convert_from_base(ElectricResistivityUnits.PicoohmMeter)
        return self.__picoohm_meters

    
    @property
    def nanoohm_meters(self) -> float:
        """
        
        """
        if self.__nanoohm_meters != None:
            return self.__nanoohm_meters
        self.__nanoohm_meters = self.__convert_from_base(ElectricResistivityUnits.NanoohmMeter)
        return self.__nanoohm_meters

    
    @property
    def microohm_meters(self) -> float:
        """
        
        """
        if self.__microohm_meters != None:
            return self.__microohm_meters
        self.__microohm_meters = self.__convert_from_base(ElectricResistivityUnits.MicroohmMeter)
        return self.__microohm_meters

    
    @property
    def milliohm_meters(self) -> float:
        """
        
        """
        if self.__milliohm_meters != None:
            return self.__milliohm_meters
        self.__milliohm_meters = self.__convert_from_base(ElectricResistivityUnits.MilliohmMeter)
        return self.__milliohm_meters

    
    @property
    def kiloohm_meters(self) -> float:
        """
        
        """
        if self.__kiloohm_meters != None:
            return self.__kiloohm_meters
        self.__kiloohm_meters = self.__convert_from_base(ElectricResistivityUnits.KiloohmMeter)
        return self.__kiloohm_meters

    
    @property
    def megaohm_meters(self) -> float:
        """
        
        """
        if self.__megaohm_meters != None:
            return self.__megaohm_meters
        self.__megaohm_meters = self.__convert_from_base(ElectricResistivityUnits.MegaohmMeter)
        return self.__megaohm_meters

    
    @property
    def picoohms_centimeter(self) -> float:
        """
        
        """
        if self.__picoohms_centimeter != None:
            return self.__picoohms_centimeter
        self.__picoohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.PicoohmCentimeter)
        return self.__picoohms_centimeter

    
    @property
    def nanoohms_centimeter(self) -> float:
        """
        
        """
        if self.__nanoohms_centimeter != None:
            return self.__nanoohms_centimeter
        self.__nanoohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.NanoohmCentimeter)
        return self.__nanoohms_centimeter

    
    @property
    def microohms_centimeter(self) -> float:
        """
        
        """
        if self.__microohms_centimeter != None:
            return self.__microohms_centimeter
        self.__microohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MicroohmCentimeter)
        return self.__microohms_centimeter

    
    @property
    def milliohms_centimeter(self) -> float:
        """
        
        """
        if self.__milliohms_centimeter != None:
            return self.__milliohms_centimeter
        self.__milliohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MilliohmCentimeter)
        return self.__milliohms_centimeter

    
    @property
    def kiloohms_centimeter(self) -> float:
        """
        
        """
        if self.__kiloohms_centimeter != None:
            return self.__kiloohms_centimeter
        self.__kiloohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.KiloohmCentimeter)
        return self.__kiloohms_centimeter

    
    @property
    def megaohms_centimeter(self) -> float:
        """
        
        """
        if self.__megaohms_centimeter != None:
            return self.__megaohms_centimeter
        self.__megaohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MegaohmCentimeter)
        return self.__megaohms_centimeter

    
    def to_string(self, unit: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter, fractional_digits: int = None) -> str:
        """
        Format the ElectricResistivity to a string.
        
        Note: the default format for ElectricResistivity is OhmMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricResistivity. Default is 'OhmMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricResistivityUnits.OhmMeter:
            return f"""{super()._truncate_fraction_digits(self.ohm_meters, fractional_digits)} Ω·m"""
        
        if unit == ElectricResistivityUnits.OhmCentimeter:
            return f"""{super()._truncate_fraction_digits(self.ohms_centimeter, fractional_digits)} Ω·cm"""
        
        if unit == ElectricResistivityUnits.PicoohmMeter:
            return f"""{super()._truncate_fraction_digits(self.picoohm_meters, fractional_digits)} pΩ·m"""
        
        if unit == ElectricResistivityUnits.NanoohmMeter:
            return f"""{super()._truncate_fraction_digits(self.nanoohm_meters, fractional_digits)} nΩ·m"""
        
        if unit == ElectricResistivityUnits.MicroohmMeter:
            return f"""{super()._truncate_fraction_digits(self.microohm_meters, fractional_digits)} μΩ·m"""
        
        if unit == ElectricResistivityUnits.MilliohmMeter:
            return f"""{super()._truncate_fraction_digits(self.milliohm_meters, fractional_digits)} mΩ·m"""
        
        if unit == ElectricResistivityUnits.KiloohmMeter:
            return f"""{super()._truncate_fraction_digits(self.kiloohm_meters, fractional_digits)} kΩ·m"""
        
        if unit == ElectricResistivityUnits.MegaohmMeter:
            return f"""{super()._truncate_fraction_digits(self.megaohm_meters, fractional_digits)} MΩ·m"""
        
        if unit == ElectricResistivityUnits.PicoohmCentimeter:
            return f"""{super()._truncate_fraction_digits(self.picoohms_centimeter, fractional_digits)} pΩ·cm"""
        
        if unit == ElectricResistivityUnits.NanoohmCentimeter:
            return f"""{super()._truncate_fraction_digits(self.nanoohms_centimeter, fractional_digits)} nΩ·cm"""
        
        if unit == ElectricResistivityUnits.MicroohmCentimeter:
            return f"""{super()._truncate_fraction_digits(self.microohms_centimeter, fractional_digits)} μΩ·cm"""
        
        if unit == ElectricResistivityUnits.MilliohmCentimeter:
            return f"""{super()._truncate_fraction_digits(self.milliohms_centimeter, fractional_digits)} mΩ·cm"""
        
        if unit == ElectricResistivityUnits.KiloohmCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kiloohms_centimeter, fractional_digits)} kΩ·cm"""
        
        if unit == ElectricResistivityUnits.MegaohmCentimeter:
            return f"""{super()._truncate_fraction_digits(self.megaohms_centimeter, fractional_digits)} MΩ·cm"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter) -> str:
        """
        Get ElectricResistivity unit abbreviation.
        Note! the default abbreviation for ElectricResistivity is OhmMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricResistivityUnits.OhmMeter:
            return """Ω·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.OhmCentimeter:
            return """Ω·cm"""
        
        if unit_abbreviation == ElectricResistivityUnits.PicoohmMeter:
            return """pΩ·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.NanoohmMeter:
            return """nΩ·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.MicroohmMeter:
            return """μΩ·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.MilliohmMeter:
            return """mΩ·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.KiloohmMeter:
            return """kΩ·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.MegaohmMeter:
            return """MΩ·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.PicoohmCentimeter:
            return """pΩ·cm"""
        
        if unit_abbreviation == ElectricResistivityUnits.NanoohmCentimeter:
            return """nΩ·cm"""
        
        if unit_abbreviation == ElectricResistivityUnits.MicroohmCentimeter:
            return """μΩ·cm"""
        
        if unit_abbreviation == ElectricResistivityUnits.MilliohmCentimeter:
            return """mΩ·cm"""
        
        if unit_abbreviation == ElectricResistivityUnits.KiloohmCentimeter:
            return """kΩ·cm"""
        
        if unit_abbreviation == ElectricResistivityUnits.MegaohmCentimeter:
            return """MΩ·cm"""
        