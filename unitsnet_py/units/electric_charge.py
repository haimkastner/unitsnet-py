from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricChargeUnits(Enum):
        """
            ElectricChargeUnits enumeration
        """
        
        Coulomb = 'Coulomb'
        """
            
        """
        
        AmpereHour = 'AmpereHour'
        """
            
        """
        
        Picocoulomb = 'Picocoulomb'
        """
            
        """
        
        Nanocoulomb = 'Nanocoulomb'
        """
            
        """
        
        Microcoulomb = 'Microcoulomb'
        """
            
        """
        
        Millicoulomb = 'Millicoulomb'
        """
            
        """
        
        Kilocoulomb = 'Kilocoulomb'
        """
            
        """
        
        Megacoulomb = 'Megacoulomb'
        """
            
        """
        
        MilliampereHour = 'MilliampereHour'
        """
            
        """
        
        KiloampereHour = 'KiloampereHour'
        """
            
        """
        
        MegaampereHour = 'MegaampereHour'
        """
            
        """
        

class ElectricChargeDto:
    """
    A DTO representation of a ElectricCharge

    Attributes:
        value (float): The value of the ElectricCharge.
        unit (ElectricChargeUnits): The specific unit that the ElectricCharge value is representing.
    """

    def __init__(self, value: float, unit: ElectricChargeUnits):
        """
        Create a new DTO representation of a ElectricCharge

        Parameters:
            value (float): The value of the ElectricCharge.
            unit (ElectricChargeUnits): The specific unit that the ElectricCharge value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricCharge
        """
        self.unit: ElectricChargeUnits = unit
        """
        The specific unit that the ElectricCharge value is representing
        """

    def to_json(self):
        """
        Get a ElectricCharge DTO JSON object representing the current unit.

        :return: JSON object represents ElectricCharge DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Coulomb"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricCharge DTO from a json representation.

        :param data: The ElectricCharge DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Coulomb"}
        :return: A new instance of ElectricChargeDto.
        :rtype: ElectricChargeDto
        """
        return ElectricChargeDto(value=data["value"], unit=ElectricChargeUnits(data["unit"]))


class ElectricCharge(AbstractMeasure):
    """
    Electric charge is the physical property of matter that causes it to experience a force when placed in an electromagnetic field.

    Args:
        value (float): The value.
        from_unit (ElectricChargeUnits): The ElectricCharge unit to create from, The default unit is Coulomb
    """
    def __init__(self, value: float, from_unit: ElectricChargeUnits = ElectricChargeUnits.Coulomb):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__coulombs = None
        
        self.__ampere_hours = None
        
        self.__picocoulombs = None
        
        self.__nanocoulombs = None
        
        self.__microcoulombs = None
        
        self.__millicoulombs = None
        
        self.__kilocoulombs = None
        
        self.__megacoulombs = None
        
        self.__milliampere_hours = None
        
        self.__kiloampere_hours = None
        
        self.__megaampere_hours = None
        

    def convert(self, unit: ElectricChargeUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricChargeUnits = ElectricChargeUnits.Coulomb) -> ElectricChargeDto:
        """
        Get a new instance of ElectricCharge DTO representing the current unit.

        :param hold_in_unit: The specific ElectricCharge unit to store the ElectricCharge value in the DTO representation.
        :type hold_in_unit: ElectricChargeUnits
        :return: A new instance of ElectricChargeDto.
        :rtype: ElectricChargeDto
        """
        return ElectricChargeDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricChargeUnits = ElectricChargeUnits.Coulomb):
        """
        Get a ElectricCharge DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricCharge unit to store the ElectricCharge value in the DTO representation.
        :type hold_in_unit: ElectricChargeUnits
        :return: JSON object represents ElectricCharge DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Coulomb"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_charge_dto: ElectricChargeDto):
        """
        Obtain a new instance of ElectricCharge from a DTO unit object.

        :param electric_charge_dto: The ElectricCharge DTO representation.
        :type electric_charge_dto: ElectricChargeDto
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(electric_charge_dto.value, electric_charge_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricCharge from a DTO unit json representation.

        :param data: The ElectricCharge DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Coulomb"}
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge.from_dto(ElectricChargeDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricChargeUnits) -> float:
        value = self._value
        
        if from_unit == ElectricChargeUnits.Coulomb:
            return (value)
        
        if from_unit == ElectricChargeUnits.AmpereHour:
            return (value * 2.77777777777e-4)
        
        if from_unit == ElectricChargeUnits.Picocoulomb:
            return ((value) / 1e-12)
        
        if from_unit == ElectricChargeUnits.Nanocoulomb:
            return ((value) / 1e-09)
        
        if from_unit == ElectricChargeUnits.Microcoulomb:
            return ((value) / 1e-06)
        
        if from_unit == ElectricChargeUnits.Millicoulomb:
            return ((value) / 0.001)
        
        if from_unit == ElectricChargeUnits.Kilocoulomb:
            return ((value) / 1000.0)
        
        if from_unit == ElectricChargeUnits.Megacoulomb:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricChargeUnits.MilliampereHour:
            return ((value * 2.77777777777e-4) / 0.001)
        
        if from_unit == ElectricChargeUnits.KiloampereHour:
            return ((value * 2.77777777777e-4) / 1000.0)
        
        if from_unit == ElectricChargeUnits.MegaampereHour:
            return ((value * 2.77777777777e-4) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricChargeUnits) -> float:
        
        if to_unit == ElectricChargeUnits.Coulomb:
            return (value)
        
        if to_unit == ElectricChargeUnits.AmpereHour:
            return (value / 2.77777777777e-4)
        
        if to_unit == ElectricChargeUnits.Picocoulomb:
            return ((value) * 1e-12)
        
        if to_unit == ElectricChargeUnits.Nanocoulomb:
            return ((value) * 1e-09)
        
        if to_unit == ElectricChargeUnits.Microcoulomb:
            return ((value) * 1e-06)
        
        if to_unit == ElectricChargeUnits.Millicoulomb:
            return ((value) * 0.001)
        
        if to_unit == ElectricChargeUnits.Kilocoulomb:
            return ((value) * 1000.0)
        
        if to_unit == ElectricChargeUnits.Megacoulomb:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricChargeUnits.MilliampereHour:
            return ((value / 2.77777777777e-4) * 0.001)
        
        if to_unit == ElectricChargeUnits.KiloampereHour:
            return ((value / 2.77777777777e-4) * 1000.0)
        
        if to_unit == ElectricChargeUnits.MegaampereHour:
            return ((value / 2.77777777777e-4) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_coulombs(coulombs: float):
        """
        Create a new instance of ElectricCharge from a value in coulombs.

        

        :param meters: The ElectricCharge value in coulombs.
        :type coulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(coulombs, ElectricChargeUnits.Coulomb)

    
    @staticmethod
    def from_ampere_hours(ampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in ampere_hours.

        

        :param meters: The ElectricCharge value in ampere_hours.
        :type ampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(ampere_hours, ElectricChargeUnits.AmpereHour)

    
    @staticmethod
    def from_picocoulombs(picocoulombs: float):
        """
        Create a new instance of ElectricCharge from a value in picocoulombs.

        

        :param meters: The ElectricCharge value in picocoulombs.
        :type picocoulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(picocoulombs, ElectricChargeUnits.Picocoulomb)

    
    @staticmethod
    def from_nanocoulombs(nanocoulombs: float):
        """
        Create a new instance of ElectricCharge from a value in nanocoulombs.

        

        :param meters: The ElectricCharge value in nanocoulombs.
        :type nanocoulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(nanocoulombs, ElectricChargeUnits.Nanocoulomb)

    
    @staticmethod
    def from_microcoulombs(microcoulombs: float):
        """
        Create a new instance of ElectricCharge from a value in microcoulombs.

        

        :param meters: The ElectricCharge value in microcoulombs.
        :type microcoulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(microcoulombs, ElectricChargeUnits.Microcoulomb)

    
    @staticmethod
    def from_millicoulombs(millicoulombs: float):
        """
        Create a new instance of ElectricCharge from a value in millicoulombs.

        

        :param meters: The ElectricCharge value in millicoulombs.
        :type millicoulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(millicoulombs, ElectricChargeUnits.Millicoulomb)

    
    @staticmethod
    def from_kilocoulombs(kilocoulombs: float):
        """
        Create a new instance of ElectricCharge from a value in kilocoulombs.

        

        :param meters: The ElectricCharge value in kilocoulombs.
        :type kilocoulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(kilocoulombs, ElectricChargeUnits.Kilocoulomb)

    
    @staticmethod
    def from_megacoulombs(megacoulombs: float):
        """
        Create a new instance of ElectricCharge from a value in megacoulombs.

        

        :param meters: The ElectricCharge value in megacoulombs.
        :type megacoulombs: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(megacoulombs, ElectricChargeUnits.Megacoulomb)

    
    @staticmethod
    def from_milliampere_hours(milliampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in milliampere_hours.

        

        :param meters: The ElectricCharge value in milliampere_hours.
        :type milliampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(milliampere_hours, ElectricChargeUnits.MilliampereHour)

    
    @staticmethod
    def from_kiloampere_hours(kiloampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in kiloampere_hours.

        

        :param meters: The ElectricCharge value in kiloampere_hours.
        :type kiloampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(kiloampere_hours, ElectricChargeUnits.KiloampereHour)

    
    @staticmethod
    def from_megaampere_hours(megaampere_hours: float):
        """
        Create a new instance of ElectricCharge from a value in megaampere_hours.

        

        :param meters: The ElectricCharge value in megaampere_hours.
        :type megaampere_hours: float
        :return: A new instance of ElectricCharge.
        :rtype: ElectricCharge
        """
        return ElectricCharge(megaampere_hours, ElectricChargeUnits.MegaampereHour)

    
    @property
    def coulombs(self) -> float:
        """
        
        """
        if self.__coulombs != None:
            return self.__coulombs
        self.__coulombs = self.__convert_from_base(ElectricChargeUnits.Coulomb)
        return self.__coulombs

    
    @property
    def ampere_hours(self) -> float:
        """
        
        """
        if self.__ampere_hours != None:
            return self.__ampere_hours
        self.__ampere_hours = self.__convert_from_base(ElectricChargeUnits.AmpereHour)
        return self.__ampere_hours

    
    @property
    def picocoulombs(self) -> float:
        """
        
        """
        if self.__picocoulombs != None:
            return self.__picocoulombs
        self.__picocoulombs = self.__convert_from_base(ElectricChargeUnits.Picocoulomb)
        return self.__picocoulombs

    
    @property
    def nanocoulombs(self) -> float:
        """
        
        """
        if self.__nanocoulombs != None:
            return self.__nanocoulombs
        self.__nanocoulombs = self.__convert_from_base(ElectricChargeUnits.Nanocoulomb)
        return self.__nanocoulombs

    
    @property
    def microcoulombs(self) -> float:
        """
        
        """
        if self.__microcoulombs != None:
            return self.__microcoulombs
        self.__microcoulombs = self.__convert_from_base(ElectricChargeUnits.Microcoulomb)
        return self.__microcoulombs

    
    @property
    def millicoulombs(self) -> float:
        """
        
        """
        if self.__millicoulombs != None:
            return self.__millicoulombs
        self.__millicoulombs = self.__convert_from_base(ElectricChargeUnits.Millicoulomb)
        return self.__millicoulombs

    
    @property
    def kilocoulombs(self) -> float:
        """
        
        """
        if self.__kilocoulombs != None:
            return self.__kilocoulombs
        self.__kilocoulombs = self.__convert_from_base(ElectricChargeUnits.Kilocoulomb)
        return self.__kilocoulombs

    
    @property
    def megacoulombs(self) -> float:
        """
        
        """
        if self.__megacoulombs != None:
            return self.__megacoulombs
        self.__megacoulombs = self.__convert_from_base(ElectricChargeUnits.Megacoulomb)
        return self.__megacoulombs

    
    @property
    def milliampere_hours(self) -> float:
        """
        
        """
        if self.__milliampere_hours != None:
            return self.__milliampere_hours
        self.__milliampere_hours = self.__convert_from_base(ElectricChargeUnits.MilliampereHour)
        return self.__milliampere_hours

    
    @property
    def kiloampere_hours(self) -> float:
        """
        
        """
        if self.__kiloampere_hours != None:
            return self.__kiloampere_hours
        self.__kiloampere_hours = self.__convert_from_base(ElectricChargeUnits.KiloampereHour)
        return self.__kiloampere_hours

    
    @property
    def megaampere_hours(self) -> float:
        """
        
        """
        if self.__megaampere_hours != None:
            return self.__megaampere_hours
        self.__megaampere_hours = self.__convert_from_base(ElectricChargeUnits.MegaampereHour)
        return self.__megaampere_hours

    
    def to_string(self, unit: ElectricChargeUnits = ElectricChargeUnits.Coulomb, fractional_digits: int = None) -> str:
        """
        Format the ElectricCharge to a string.
        
        Note: the default format for ElectricCharge is Coulomb.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricCharge. Default is 'Coulomb'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricChargeUnits.Coulomb:
            return f"""{super()._truncate_fraction_digits(self.coulombs, fractional_digits)} C"""
        
        if unit == ElectricChargeUnits.AmpereHour:
            return f"""{super()._truncate_fraction_digits(self.ampere_hours, fractional_digits)} A-h"""
        
        if unit == ElectricChargeUnits.Picocoulomb:
            return f"""{super()._truncate_fraction_digits(self.picocoulombs, fractional_digits)} pC"""
        
        if unit == ElectricChargeUnits.Nanocoulomb:
            return f"""{super()._truncate_fraction_digits(self.nanocoulombs, fractional_digits)} nC"""
        
        if unit == ElectricChargeUnits.Microcoulomb:
            return f"""{super()._truncate_fraction_digits(self.microcoulombs, fractional_digits)} μC"""
        
        if unit == ElectricChargeUnits.Millicoulomb:
            return f"""{super()._truncate_fraction_digits(self.millicoulombs, fractional_digits)} mC"""
        
        if unit == ElectricChargeUnits.Kilocoulomb:
            return f"""{super()._truncate_fraction_digits(self.kilocoulombs, fractional_digits)} kC"""
        
        if unit == ElectricChargeUnits.Megacoulomb:
            return f"""{super()._truncate_fraction_digits(self.megacoulombs, fractional_digits)} MC"""
        
        if unit == ElectricChargeUnits.MilliampereHour:
            return f"""{super()._truncate_fraction_digits(self.milliampere_hours, fractional_digits)} mA-h"""
        
        if unit == ElectricChargeUnits.KiloampereHour:
            return f"""{super()._truncate_fraction_digits(self.kiloampere_hours, fractional_digits)} kA-h"""
        
        if unit == ElectricChargeUnits.MegaampereHour:
            return f"""{super()._truncate_fraction_digits(self.megaampere_hours, fractional_digits)} MA-h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricChargeUnits = ElectricChargeUnits.Coulomb) -> str:
        """
        Get ElectricCharge unit abbreviation.
        Note! the default abbreviation for ElectricCharge is Coulomb.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricChargeUnits.Coulomb:
            return """C"""
        
        if unit_abbreviation == ElectricChargeUnits.AmpereHour:
            return """A-h"""
        
        if unit_abbreviation == ElectricChargeUnits.Picocoulomb:
            return """pC"""
        
        if unit_abbreviation == ElectricChargeUnits.Nanocoulomb:
            return """nC"""
        
        if unit_abbreviation == ElectricChargeUnits.Microcoulomb:
            return """μC"""
        
        if unit_abbreviation == ElectricChargeUnits.Millicoulomb:
            return """mC"""
        
        if unit_abbreviation == ElectricChargeUnits.Kilocoulomb:
            return """kC"""
        
        if unit_abbreviation == ElectricChargeUnits.Megacoulomb:
            return """MC"""
        
        if unit_abbreviation == ElectricChargeUnits.MilliampereHour:
            return """mA-h"""
        
        if unit_abbreviation == ElectricChargeUnits.KiloampereHour:
            return """kA-h"""
        
        if unit_abbreviation == ElectricChargeUnits.MegaampereHour:
            return """MA-h"""
        