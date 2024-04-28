from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LuminosityUnits(Enum):
        """
            LuminosityUnits enumeration
        """
        
        Watt = 'Watt'
        """
            
        """
        
        SolarLuminosity = 'SolarLuminosity'
        """
            
        """
        
        Femtowatt = 'Femtowatt'
        """
            
        """
        
        Picowatt = 'Picowatt'
        """
            
        """
        
        Nanowatt = 'Nanowatt'
        """
            
        """
        
        Microwatt = 'Microwatt'
        """
            
        """
        
        Milliwatt = 'Milliwatt'
        """
            
        """
        
        Deciwatt = 'Deciwatt'
        """
            
        """
        
        Decawatt = 'Decawatt'
        """
            
        """
        
        Kilowatt = 'Kilowatt'
        """
            
        """
        
        Megawatt = 'Megawatt'
        """
            
        """
        
        Gigawatt = 'Gigawatt'
        """
            
        """
        
        Terawatt = 'Terawatt'
        """
            
        """
        
        Petawatt = 'Petawatt'
        """
            
        """
        

class LuminosityDto:
    """
    A DTO representation of a Luminosity

    Attributes:
        value (float): The value of the Luminosity.
        unit (LuminosityUnits): The specific unit that the Luminosity value is representing.
    """

    def __init__(self, value: float, unit: LuminosityUnits):
        """
        Create a new DTO representation of a Luminosity

        Parameters:
            value (float): The value of the Luminosity.
            unit (LuminosityUnits): The specific unit that the Luminosity value is representing.
        """
        self.value: float = value
        """
        The value of the Luminosity
        """
        self.unit: LuminosityUnits = unit
        """
        The specific unit that the Luminosity value is representing
        """

    def to_json(self):
        """
        Get a Luminosity DTO JSON object representing the current unit.

        :return: JSON object represents Luminosity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Watt"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Luminosity DTO from a json representation.

        :param data: The Luminosity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Watt"}
        :return: A new instance of LuminosityDto.
        :rtype: LuminosityDto
        """
        return LuminosityDto(value=data["value"], unit=LuminosityUnits(data["unit"]))


class Luminosity(AbstractMeasure):
    """
    Luminosity is an absolute measure of radiated electromagnetic power (light), the radiant power emitted by a light-emitting object.

    Args:
        value (float): The value.
        from_unit (LuminosityUnits): The Luminosity unit to create from, The default unit is Watt
    """
    def __init__(self, value: float, from_unit: LuminosityUnits = LuminosityUnits.Watt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts = None
        
        self.__solar_luminosities = None
        
        self.__femtowatts = None
        
        self.__picowatts = None
        
        self.__nanowatts = None
        
        self.__microwatts = None
        
        self.__milliwatts = None
        
        self.__deciwatts = None
        
        self.__decawatts = None
        
        self.__kilowatts = None
        
        self.__megawatts = None
        
        self.__gigawatts = None
        
        self.__terawatts = None
        
        self.__petawatts = None
        

    def convert(self, unit: LuminosityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: LuminosityUnits = LuminosityUnits.Watt) -> LuminosityDto:
        """
        Get a new instance of Luminosity DTO representing the current unit.

        :param hold_in_unit: The specific Luminosity unit to store the Luminosity value in the DTO representation.
        :type hold_in_unit: LuminosityUnits
        :return: A new instance of LuminosityDto.
        :rtype: LuminosityDto
        """
        return LuminosityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: LuminosityUnits = LuminosityUnits.Watt):
        """
        Get a Luminosity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Luminosity unit to store the Luminosity value in the DTO representation.
        :type hold_in_unit: LuminosityUnits
        :return: JSON object represents Luminosity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Watt"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(luminosity_dto: LuminosityDto):
        """
        Obtain a new instance of Luminosity from a DTO unit object.

        :param luminosity_dto: The Luminosity DTO representation.
        :type luminosity_dto: LuminosityDto
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(luminosity_dto.value, luminosity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Luminosity from a DTO unit json representation.

        :param data: The Luminosity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Watt"}
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity.from_dto(LuminosityDto.from_json(data))

    def __convert_from_base(self, from_unit: LuminosityUnits) -> float:
        value = self._value
        
        if from_unit == LuminosityUnits.Watt:
            return (value)
        
        if from_unit == LuminosityUnits.SolarLuminosity:
            return (value / 3.846e26)
        
        if from_unit == LuminosityUnits.Femtowatt:
            return ((value) / 1e-15)
        
        if from_unit == LuminosityUnits.Picowatt:
            return ((value) / 1e-12)
        
        if from_unit == LuminosityUnits.Nanowatt:
            return ((value) / 1e-09)
        
        if from_unit == LuminosityUnits.Microwatt:
            return ((value) / 1e-06)
        
        if from_unit == LuminosityUnits.Milliwatt:
            return ((value) / 0.001)
        
        if from_unit == LuminosityUnits.Deciwatt:
            return ((value) / 0.1)
        
        if from_unit == LuminosityUnits.Decawatt:
            return ((value) / 10.0)
        
        if from_unit == LuminosityUnits.Kilowatt:
            return ((value) / 1000.0)
        
        if from_unit == LuminosityUnits.Megawatt:
            return ((value) / 1000000.0)
        
        if from_unit == LuminosityUnits.Gigawatt:
            return ((value) / 1000000000.0)
        
        if from_unit == LuminosityUnits.Terawatt:
            return ((value) / 1000000000000.0)
        
        if from_unit == LuminosityUnits.Petawatt:
            return ((value) / 1000000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminosityUnits) -> float:
        
        if to_unit == LuminosityUnits.Watt:
            return (value)
        
        if to_unit == LuminosityUnits.SolarLuminosity:
            return (value * 3.846e26)
        
        if to_unit == LuminosityUnits.Femtowatt:
            return ((value) * 1e-15)
        
        if to_unit == LuminosityUnits.Picowatt:
            return ((value) * 1e-12)
        
        if to_unit == LuminosityUnits.Nanowatt:
            return ((value) * 1e-09)
        
        if to_unit == LuminosityUnits.Microwatt:
            return ((value) * 1e-06)
        
        if to_unit == LuminosityUnits.Milliwatt:
            return ((value) * 0.001)
        
        if to_unit == LuminosityUnits.Deciwatt:
            return ((value) * 0.1)
        
        if to_unit == LuminosityUnits.Decawatt:
            return ((value) * 10.0)
        
        if to_unit == LuminosityUnits.Kilowatt:
            return ((value) * 1000.0)
        
        if to_unit == LuminosityUnits.Megawatt:
            return ((value) * 1000000.0)
        
        if to_unit == LuminosityUnits.Gigawatt:
            return ((value) * 1000000000.0)
        
        if to_unit == LuminosityUnits.Terawatt:
            return ((value) * 1000000000000.0)
        
        if to_unit == LuminosityUnits.Petawatt:
            return ((value) * 1000000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts(watts: float):
        """
        Create a new instance of Luminosity from a value in watts.

        

        :param meters: The Luminosity value in watts.
        :type watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(watts, LuminosityUnits.Watt)

    
    @staticmethod
    def from_solar_luminosities(solar_luminosities: float):
        """
        Create a new instance of Luminosity from a value in solar_luminosities.

        

        :param meters: The Luminosity value in solar_luminosities.
        :type solar_luminosities: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(solar_luminosities, LuminosityUnits.SolarLuminosity)

    
    @staticmethod
    def from_femtowatts(femtowatts: float):
        """
        Create a new instance of Luminosity from a value in femtowatts.

        

        :param meters: The Luminosity value in femtowatts.
        :type femtowatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(femtowatts, LuminosityUnits.Femtowatt)

    
    @staticmethod
    def from_picowatts(picowatts: float):
        """
        Create a new instance of Luminosity from a value in picowatts.

        

        :param meters: The Luminosity value in picowatts.
        :type picowatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(picowatts, LuminosityUnits.Picowatt)

    
    @staticmethod
    def from_nanowatts(nanowatts: float):
        """
        Create a new instance of Luminosity from a value in nanowatts.

        

        :param meters: The Luminosity value in nanowatts.
        :type nanowatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(nanowatts, LuminosityUnits.Nanowatt)

    
    @staticmethod
    def from_microwatts(microwatts: float):
        """
        Create a new instance of Luminosity from a value in microwatts.

        

        :param meters: The Luminosity value in microwatts.
        :type microwatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(microwatts, LuminosityUnits.Microwatt)

    
    @staticmethod
    def from_milliwatts(milliwatts: float):
        """
        Create a new instance of Luminosity from a value in milliwatts.

        

        :param meters: The Luminosity value in milliwatts.
        :type milliwatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(milliwatts, LuminosityUnits.Milliwatt)

    
    @staticmethod
    def from_deciwatts(deciwatts: float):
        """
        Create a new instance of Luminosity from a value in deciwatts.

        

        :param meters: The Luminosity value in deciwatts.
        :type deciwatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(deciwatts, LuminosityUnits.Deciwatt)

    
    @staticmethod
    def from_decawatts(decawatts: float):
        """
        Create a new instance of Luminosity from a value in decawatts.

        

        :param meters: The Luminosity value in decawatts.
        :type decawatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(decawatts, LuminosityUnits.Decawatt)

    
    @staticmethod
    def from_kilowatts(kilowatts: float):
        """
        Create a new instance of Luminosity from a value in kilowatts.

        

        :param meters: The Luminosity value in kilowatts.
        :type kilowatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(kilowatts, LuminosityUnits.Kilowatt)

    
    @staticmethod
    def from_megawatts(megawatts: float):
        """
        Create a new instance of Luminosity from a value in megawatts.

        

        :param meters: The Luminosity value in megawatts.
        :type megawatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(megawatts, LuminosityUnits.Megawatt)

    
    @staticmethod
    def from_gigawatts(gigawatts: float):
        """
        Create a new instance of Luminosity from a value in gigawatts.

        

        :param meters: The Luminosity value in gigawatts.
        :type gigawatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(gigawatts, LuminosityUnits.Gigawatt)

    
    @staticmethod
    def from_terawatts(terawatts: float):
        """
        Create a new instance of Luminosity from a value in terawatts.

        

        :param meters: The Luminosity value in terawatts.
        :type terawatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(terawatts, LuminosityUnits.Terawatt)

    
    @staticmethod
    def from_petawatts(petawatts: float):
        """
        Create a new instance of Luminosity from a value in petawatts.

        

        :param meters: The Luminosity value in petawatts.
        :type petawatts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(petawatts, LuminosityUnits.Petawatt)

    
    @property
    def watts(self) -> float:
        """
        
        """
        if self.__watts != None:
            return self.__watts
        self.__watts = self.__convert_from_base(LuminosityUnits.Watt)
        return self.__watts

    
    @property
    def solar_luminosities(self) -> float:
        """
        
        """
        if self.__solar_luminosities != None:
            return self.__solar_luminosities
        self.__solar_luminosities = self.__convert_from_base(LuminosityUnits.SolarLuminosity)
        return self.__solar_luminosities

    
    @property
    def femtowatts(self) -> float:
        """
        
        """
        if self.__femtowatts != None:
            return self.__femtowatts
        self.__femtowatts = self.__convert_from_base(LuminosityUnits.Femtowatt)
        return self.__femtowatts

    
    @property
    def picowatts(self) -> float:
        """
        
        """
        if self.__picowatts != None:
            return self.__picowatts
        self.__picowatts = self.__convert_from_base(LuminosityUnits.Picowatt)
        return self.__picowatts

    
    @property
    def nanowatts(self) -> float:
        """
        
        """
        if self.__nanowatts != None:
            return self.__nanowatts
        self.__nanowatts = self.__convert_from_base(LuminosityUnits.Nanowatt)
        return self.__nanowatts

    
    @property
    def microwatts(self) -> float:
        """
        
        """
        if self.__microwatts != None:
            return self.__microwatts
        self.__microwatts = self.__convert_from_base(LuminosityUnits.Microwatt)
        return self.__microwatts

    
    @property
    def milliwatts(self) -> float:
        """
        
        """
        if self.__milliwatts != None:
            return self.__milliwatts
        self.__milliwatts = self.__convert_from_base(LuminosityUnits.Milliwatt)
        return self.__milliwatts

    
    @property
    def deciwatts(self) -> float:
        """
        
        """
        if self.__deciwatts != None:
            return self.__deciwatts
        self.__deciwatts = self.__convert_from_base(LuminosityUnits.Deciwatt)
        return self.__deciwatts

    
    @property
    def decawatts(self) -> float:
        """
        
        """
        if self.__decawatts != None:
            return self.__decawatts
        self.__decawatts = self.__convert_from_base(LuminosityUnits.Decawatt)
        return self.__decawatts

    
    @property
    def kilowatts(self) -> float:
        """
        
        """
        if self.__kilowatts != None:
            return self.__kilowatts
        self.__kilowatts = self.__convert_from_base(LuminosityUnits.Kilowatt)
        return self.__kilowatts

    
    @property
    def megawatts(self) -> float:
        """
        
        """
        if self.__megawatts != None:
            return self.__megawatts
        self.__megawatts = self.__convert_from_base(LuminosityUnits.Megawatt)
        return self.__megawatts

    
    @property
    def gigawatts(self) -> float:
        """
        
        """
        if self.__gigawatts != None:
            return self.__gigawatts
        self.__gigawatts = self.__convert_from_base(LuminosityUnits.Gigawatt)
        return self.__gigawatts

    
    @property
    def terawatts(self) -> float:
        """
        
        """
        if self.__terawatts != None:
            return self.__terawatts
        self.__terawatts = self.__convert_from_base(LuminosityUnits.Terawatt)
        return self.__terawatts

    
    @property
    def petawatts(self) -> float:
        """
        
        """
        if self.__petawatts != None:
            return self.__petawatts
        self.__petawatts = self.__convert_from_base(LuminosityUnits.Petawatt)
        return self.__petawatts

    
    def to_string(self, unit: LuminosityUnits = LuminosityUnits.Watt, fractional_digits: int = None) -> str:
        """
        Format the Luminosity to a string.
        
        Note: the default format for Luminosity is Watt.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Luminosity. Default is 'Watt'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == LuminosityUnits.Watt:
            return f"""{super()._truncate_fraction_digits(self.watts, fractional_digits)} W"""
        
        if unit == LuminosityUnits.SolarLuminosity:
            return f"""{super()._truncate_fraction_digits(self.solar_luminosities, fractional_digits)} L⊙"""
        
        if unit == LuminosityUnits.Femtowatt:
            return f"""{super()._truncate_fraction_digits(self.femtowatts, fractional_digits)} fW"""
        
        if unit == LuminosityUnits.Picowatt:
            return f"""{super()._truncate_fraction_digits(self.picowatts, fractional_digits)} pW"""
        
        if unit == LuminosityUnits.Nanowatt:
            return f"""{super()._truncate_fraction_digits(self.nanowatts, fractional_digits)} nW"""
        
        if unit == LuminosityUnits.Microwatt:
            return f"""{super()._truncate_fraction_digits(self.microwatts, fractional_digits)} μW"""
        
        if unit == LuminosityUnits.Milliwatt:
            return f"""{super()._truncate_fraction_digits(self.milliwatts, fractional_digits)} mW"""
        
        if unit == LuminosityUnits.Deciwatt:
            return f"""{super()._truncate_fraction_digits(self.deciwatts, fractional_digits)} dW"""
        
        if unit == LuminosityUnits.Decawatt:
            return f"""{super()._truncate_fraction_digits(self.decawatts, fractional_digits)} daW"""
        
        if unit == LuminosityUnits.Kilowatt:
            return f"""{super()._truncate_fraction_digits(self.kilowatts, fractional_digits)} kW"""
        
        if unit == LuminosityUnits.Megawatt:
            return f"""{super()._truncate_fraction_digits(self.megawatts, fractional_digits)} MW"""
        
        if unit == LuminosityUnits.Gigawatt:
            return f"""{super()._truncate_fraction_digits(self.gigawatts, fractional_digits)} GW"""
        
        if unit == LuminosityUnits.Terawatt:
            return f"""{super()._truncate_fraction_digits(self.terawatts, fractional_digits)} TW"""
        
        if unit == LuminosityUnits.Petawatt:
            return f"""{super()._truncate_fraction_digits(self.petawatts, fractional_digits)} PW"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminosityUnits = LuminosityUnits.Watt) -> str:
        """
        Get Luminosity unit abbreviation.
        Note! the default abbreviation for Luminosity is Watt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminosityUnits.Watt:
            return """W"""
        
        if unit_abbreviation == LuminosityUnits.SolarLuminosity:
            return """L⊙"""
        
        if unit_abbreviation == LuminosityUnits.Femtowatt:
            return """fW"""
        
        if unit_abbreviation == LuminosityUnits.Picowatt:
            return """pW"""
        
        if unit_abbreviation == LuminosityUnits.Nanowatt:
            return """nW"""
        
        if unit_abbreviation == LuminosityUnits.Microwatt:
            return """μW"""
        
        if unit_abbreviation == LuminosityUnits.Milliwatt:
            return """mW"""
        
        if unit_abbreviation == LuminosityUnits.Deciwatt:
            return """dW"""
        
        if unit_abbreviation == LuminosityUnits.Decawatt:
            return """daW"""
        
        if unit_abbreviation == LuminosityUnits.Kilowatt:
            return """kW"""
        
        if unit_abbreviation == LuminosityUnits.Megawatt:
            return """MW"""
        
        if unit_abbreviation == LuminosityUnits.Gigawatt:
            return """GW"""
        
        if unit_abbreviation == LuminosityUnits.Terawatt:
            return """TW"""
        
        if unit_abbreviation == LuminosityUnits.Petawatt:
            return """PW"""
        