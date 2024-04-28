from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AmountOfSubstanceUnits(Enum):
        """
            AmountOfSubstanceUnits enumeration
        """
        
        Mole = 'Mole'
        """
            
        """
        
        PoundMole = 'PoundMole'
        """
            
        """
        
        Femtomole = 'Femtomole'
        """
            
        """
        
        Picomole = 'Picomole'
        """
            
        """
        
        Nanomole = 'Nanomole'
        """
            
        """
        
        Micromole = 'Micromole'
        """
            
        """
        
        Millimole = 'Millimole'
        """
            
        """
        
        Centimole = 'Centimole'
        """
            
        """
        
        Decimole = 'Decimole'
        """
            
        """
        
        Kilomole = 'Kilomole'
        """
            
        """
        
        Megamole = 'Megamole'
        """
            
        """
        
        NanopoundMole = 'NanopoundMole'
        """
            
        """
        
        MicropoundMole = 'MicropoundMole'
        """
            
        """
        
        MillipoundMole = 'MillipoundMole'
        """
            
        """
        
        CentipoundMole = 'CentipoundMole'
        """
            
        """
        
        DecipoundMole = 'DecipoundMole'
        """
            
        """
        
        KilopoundMole = 'KilopoundMole'
        """
            
        """
        

class AmountOfSubstanceDto:
    """
    A DTO representation of a AmountOfSubstance

    Attributes:
        value (float): The value of the AmountOfSubstance.
        unit (AmountOfSubstanceUnits): The specific unit that the AmountOfSubstance value is representing.
    """

    def __init__(self, value: float, unit: AmountOfSubstanceUnits):
        """
        Create a new DTO representation of a AmountOfSubstance

        Parameters:
            value (float): The value of the AmountOfSubstance.
            unit (AmountOfSubstanceUnits): The specific unit that the AmountOfSubstance value is representing.
        """
        self.value: float = value
        """
        The value of the AmountOfSubstance
        """
        self.unit: AmountOfSubstanceUnits = unit
        """
        The specific unit that the AmountOfSubstance value is representing
        """

    def to_json(self):
        """
        Get a AmountOfSubstance DTO JSON object representing the current unit.

        :return: JSON object represents AmountOfSubstance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Mole"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of AmountOfSubstance DTO from a json representation.

        :param data: The AmountOfSubstance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Mole"}
        :return: A new instance of AmountOfSubstanceDto.
        :rtype: AmountOfSubstanceDto
        """
        return AmountOfSubstanceDto(value=data["value"], unit=AmountOfSubstanceUnits(data["unit"]))


class AmountOfSubstance(AbstractMeasure):
    """
    Mole is the amount of substance containing Avagadro's Number (6.02 x 10 ^ 23) of real particles such as molecules,atoms, ions or radicals.

    Args:
        value (float): The value.
        from_unit (AmountOfSubstanceUnits): The AmountOfSubstance unit to create from, The default unit is Mole
    """
    def __init__(self, value: float, from_unit: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__moles = None
        
        self.__pound_moles = None
        
        self.__femtomoles = None
        
        self.__picomoles = None
        
        self.__nanomoles = None
        
        self.__micromoles = None
        
        self.__millimoles = None
        
        self.__centimoles = None
        
        self.__decimoles = None
        
        self.__kilomoles = None
        
        self.__megamoles = None
        
        self.__nanopound_moles = None
        
        self.__micropound_moles = None
        
        self.__millipound_moles = None
        
        self.__centipound_moles = None
        
        self.__decipound_moles = None
        
        self.__kilopound_moles = None
        

    def convert(self, unit: AmountOfSubstanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole) -> AmountOfSubstanceDto:
        """
        Get a new instance of AmountOfSubstance DTO representing the current unit.

        :param hold_in_unit: The specific AmountOfSubstance unit to store the AmountOfSubstance value in the DTO representation.
        :type hold_in_unit: AmountOfSubstanceUnits
        :return: A new instance of AmountOfSubstanceDto.
        :rtype: AmountOfSubstanceDto
        """
        return AmountOfSubstanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole):
        """
        Get a AmountOfSubstance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific AmountOfSubstance unit to store the AmountOfSubstance value in the DTO representation.
        :type hold_in_unit: AmountOfSubstanceUnits
        :return: JSON object represents AmountOfSubstance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Mole"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(amount_of_substance_dto: AmountOfSubstanceDto):
        """
        Obtain a new instance of AmountOfSubstance from a DTO unit object.

        :param amount_of_substance_dto: The AmountOfSubstance DTO representation.
        :type amount_of_substance_dto: AmountOfSubstanceDto
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(amount_of_substance_dto.value, amount_of_substance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of AmountOfSubstance from a DTO unit json representation.

        :param data: The AmountOfSubstance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Mole"}
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance.from_dto(AmountOfSubstanceDto.from_json(data))

    def __convert_from_base(self, from_unit: AmountOfSubstanceUnits) -> float:
        value = self._value
        
        if from_unit == AmountOfSubstanceUnits.Mole:
            return (value)
        
        if from_unit == AmountOfSubstanceUnits.PoundMole:
            return (value / 453.59237)
        
        if from_unit == AmountOfSubstanceUnits.Femtomole:
            return ((value) / 1e-15)
        
        if from_unit == AmountOfSubstanceUnits.Picomole:
            return ((value) / 1e-12)
        
        if from_unit == AmountOfSubstanceUnits.Nanomole:
            return ((value) / 1e-09)
        
        if from_unit == AmountOfSubstanceUnits.Micromole:
            return ((value) / 1e-06)
        
        if from_unit == AmountOfSubstanceUnits.Millimole:
            return ((value) / 0.001)
        
        if from_unit == AmountOfSubstanceUnits.Centimole:
            return ((value) / 0.01)
        
        if from_unit == AmountOfSubstanceUnits.Decimole:
            return ((value) / 0.1)
        
        if from_unit == AmountOfSubstanceUnits.Kilomole:
            return ((value) / 1000.0)
        
        if from_unit == AmountOfSubstanceUnits.Megamole:
            return ((value) / 1000000.0)
        
        if from_unit == AmountOfSubstanceUnits.NanopoundMole:
            return ((value / 453.59237) / 1e-09)
        
        if from_unit == AmountOfSubstanceUnits.MicropoundMole:
            return ((value / 453.59237) / 1e-06)
        
        if from_unit == AmountOfSubstanceUnits.MillipoundMole:
            return ((value / 453.59237) / 0.001)
        
        if from_unit == AmountOfSubstanceUnits.CentipoundMole:
            return ((value / 453.59237) / 0.01)
        
        if from_unit == AmountOfSubstanceUnits.DecipoundMole:
            return ((value / 453.59237) / 0.1)
        
        if from_unit == AmountOfSubstanceUnits.KilopoundMole:
            return ((value / 453.59237) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AmountOfSubstanceUnits) -> float:
        
        if to_unit == AmountOfSubstanceUnits.Mole:
            return (value)
        
        if to_unit == AmountOfSubstanceUnits.PoundMole:
            return (value * 453.59237)
        
        if to_unit == AmountOfSubstanceUnits.Femtomole:
            return ((value) * 1e-15)
        
        if to_unit == AmountOfSubstanceUnits.Picomole:
            return ((value) * 1e-12)
        
        if to_unit == AmountOfSubstanceUnits.Nanomole:
            return ((value) * 1e-09)
        
        if to_unit == AmountOfSubstanceUnits.Micromole:
            return ((value) * 1e-06)
        
        if to_unit == AmountOfSubstanceUnits.Millimole:
            return ((value) * 0.001)
        
        if to_unit == AmountOfSubstanceUnits.Centimole:
            return ((value) * 0.01)
        
        if to_unit == AmountOfSubstanceUnits.Decimole:
            return ((value) * 0.1)
        
        if to_unit == AmountOfSubstanceUnits.Kilomole:
            return ((value) * 1000.0)
        
        if to_unit == AmountOfSubstanceUnits.Megamole:
            return ((value) * 1000000.0)
        
        if to_unit == AmountOfSubstanceUnits.NanopoundMole:
            return ((value * 453.59237) * 1e-09)
        
        if to_unit == AmountOfSubstanceUnits.MicropoundMole:
            return ((value * 453.59237) * 1e-06)
        
        if to_unit == AmountOfSubstanceUnits.MillipoundMole:
            return ((value * 453.59237) * 0.001)
        
        if to_unit == AmountOfSubstanceUnits.CentipoundMole:
            return ((value * 453.59237) * 0.01)
        
        if to_unit == AmountOfSubstanceUnits.DecipoundMole:
            return ((value * 453.59237) * 0.1)
        
        if to_unit == AmountOfSubstanceUnits.KilopoundMole:
            return ((value * 453.59237) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_moles(moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in moles.

        

        :param meters: The AmountOfSubstance value in moles.
        :type moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(moles, AmountOfSubstanceUnits.Mole)

    
    @staticmethod
    def from_pound_moles(pound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in pound_moles.

        

        :param meters: The AmountOfSubstance value in pound_moles.
        :type pound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(pound_moles, AmountOfSubstanceUnits.PoundMole)

    
    @staticmethod
    def from_femtomoles(femtomoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in femtomoles.

        

        :param meters: The AmountOfSubstance value in femtomoles.
        :type femtomoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(femtomoles, AmountOfSubstanceUnits.Femtomole)

    
    @staticmethod
    def from_picomoles(picomoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in picomoles.

        

        :param meters: The AmountOfSubstance value in picomoles.
        :type picomoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(picomoles, AmountOfSubstanceUnits.Picomole)

    
    @staticmethod
    def from_nanomoles(nanomoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in nanomoles.

        

        :param meters: The AmountOfSubstance value in nanomoles.
        :type nanomoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(nanomoles, AmountOfSubstanceUnits.Nanomole)

    
    @staticmethod
    def from_micromoles(micromoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in micromoles.

        

        :param meters: The AmountOfSubstance value in micromoles.
        :type micromoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(micromoles, AmountOfSubstanceUnits.Micromole)

    
    @staticmethod
    def from_millimoles(millimoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in millimoles.

        

        :param meters: The AmountOfSubstance value in millimoles.
        :type millimoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(millimoles, AmountOfSubstanceUnits.Millimole)

    
    @staticmethod
    def from_centimoles(centimoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in centimoles.

        

        :param meters: The AmountOfSubstance value in centimoles.
        :type centimoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(centimoles, AmountOfSubstanceUnits.Centimole)

    
    @staticmethod
    def from_decimoles(decimoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in decimoles.

        

        :param meters: The AmountOfSubstance value in decimoles.
        :type decimoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(decimoles, AmountOfSubstanceUnits.Decimole)

    
    @staticmethod
    def from_kilomoles(kilomoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in kilomoles.

        

        :param meters: The AmountOfSubstance value in kilomoles.
        :type kilomoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(kilomoles, AmountOfSubstanceUnits.Kilomole)

    
    @staticmethod
    def from_megamoles(megamoles: float):
        """
        Create a new instance of AmountOfSubstance from a value in megamoles.

        

        :param meters: The AmountOfSubstance value in megamoles.
        :type megamoles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(megamoles, AmountOfSubstanceUnits.Megamole)

    
    @staticmethod
    def from_nanopound_moles(nanopound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in nanopound_moles.

        

        :param meters: The AmountOfSubstance value in nanopound_moles.
        :type nanopound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(nanopound_moles, AmountOfSubstanceUnits.NanopoundMole)

    
    @staticmethod
    def from_micropound_moles(micropound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in micropound_moles.

        

        :param meters: The AmountOfSubstance value in micropound_moles.
        :type micropound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(micropound_moles, AmountOfSubstanceUnits.MicropoundMole)

    
    @staticmethod
    def from_millipound_moles(millipound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in millipound_moles.

        

        :param meters: The AmountOfSubstance value in millipound_moles.
        :type millipound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(millipound_moles, AmountOfSubstanceUnits.MillipoundMole)

    
    @staticmethod
    def from_centipound_moles(centipound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in centipound_moles.

        

        :param meters: The AmountOfSubstance value in centipound_moles.
        :type centipound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(centipound_moles, AmountOfSubstanceUnits.CentipoundMole)

    
    @staticmethod
    def from_decipound_moles(decipound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in decipound_moles.

        

        :param meters: The AmountOfSubstance value in decipound_moles.
        :type decipound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(decipound_moles, AmountOfSubstanceUnits.DecipoundMole)

    
    @staticmethod
    def from_kilopound_moles(kilopound_moles: float):
        """
        Create a new instance of AmountOfSubstance from a value in kilopound_moles.

        

        :param meters: The AmountOfSubstance value in kilopound_moles.
        :type kilopound_moles: float
        :return: A new instance of AmountOfSubstance.
        :rtype: AmountOfSubstance
        """
        return AmountOfSubstance(kilopound_moles, AmountOfSubstanceUnits.KilopoundMole)

    
    @property
    def moles(self) -> float:
        """
        
        """
        if self.__moles != None:
            return self.__moles
        self.__moles = self.__convert_from_base(AmountOfSubstanceUnits.Mole)
        return self.__moles

    
    @property
    def pound_moles(self) -> float:
        """
        
        """
        if self.__pound_moles != None:
            return self.__pound_moles
        self.__pound_moles = self.__convert_from_base(AmountOfSubstanceUnits.PoundMole)
        return self.__pound_moles

    
    @property
    def femtomoles(self) -> float:
        """
        
        """
        if self.__femtomoles != None:
            return self.__femtomoles
        self.__femtomoles = self.__convert_from_base(AmountOfSubstanceUnits.Femtomole)
        return self.__femtomoles

    
    @property
    def picomoles(self) -> float:
        """
        
        """
        if self.__picomoles != None:
            return self.__picomoles
        self.__picomoles = self.__convert_from_base(AmountOfSubstanceUnits.Picomole)
        return self.__picomoles

    
    @property
    def nanomoles(self) -> float:
        """
        
        """
        if self.__nanomoles != None:
            return self.__nanomoles
        self.__nanomoles = self.__convert_from_base(AmountOfSubstanceUnits.Nanomole)
        return self.__nanomoles

    
    @property
    def micromoles(self) -> float:
        """
        
        """
        if self.__micromoles != None:
            return self.__micromoles
        self.__micromoles = self.__convert_from_base(AmountOfSubstanceUnits.Micromole)
        return self.__micromoles

    
    @property
    def millimoles(self) -> float:
        """
        
        """
        if self.__millimoles != None:
            return self.__millimoles
        self.__millimoles = self.__convert_from_base(AmountOfSubstanceUnits.Millimole)
        return self.__millimoles

    
    @property
    def centimoles(self) -> float:
        """
        
        """
        if self.__centimoles != None:
            return self.__centimoles
        self.__centimoles = self.__convert_from_base(AmountOfSubstanceUnits.Centimole)
        return self.__centimoles

    
    @property
    def decimoles(self) -> float:
        """
        
        """
        if self.__decimoles != None:
            return self.__decimoles
        self.__decimoles = self.__convert_from_base(AmountOfSubstanceUnits.Decimole)
        return self.__decimoles

    
    @property
    def kilomoles(self) -> float:
        """
        
        """
        if self.__kilomoles != None:
            return self.__kilomoles
        self.__kilomoles = self.__convert_from_base(AmountOfSubstanceUnits.Kilomole)
        return self.__kilomoles

    
    @property
    def megamoles(self) -> float:
        """
        
        """
        if self.__megamoles != None:
            return self.__megamoles
        self.__megamoles = self.__convert_from_base(AmountOfSubstanceUnits.Megamole)
        return self.__megamoles

    
    @property
    def nanopound_moles(self) -> float:
        """
        
        """
        if self.__nanopound_moles != None:
            return self.__nanopound_moles
        self.__nanopound_moles = self.__convert_from_base(AmountOfSubstanceUnits.NanopoundMole)
        return self.__nanopound_moles

    
    @property
    def micropound_moles(self) -> float:
        """
        
        """
        if self.__micropound_moles != None:
            return self.__micropound_moles
        self.__micropound_moles = self.__convert_from_base(AmountOfSubstanceUnits.MicropoundMole)
        return self.__micropound_moles

    
    @property
    def millipound_moles(self) -> float:
        """
        
        """
        if self.__millipound_moles != None:
            return self.__millipound_moles
        self.__millipound_moles = self.__convert_from_base(AmountOfSubstanceUnits.MillipoundMole)
        return self.__millipound_moles

    
    @property
    def centipound_moles(self) -> float:
        """
        
        """
        if self.__centipound_moles != None:
            return self.__centipound_moles
        self.__centipound_moles = self.__convert_from_base(AmountOfSubstanceUnits.CentipoundMole)
        return self.__centipound_moles

    
    @property
    def decipound_moles(self) -> float:
        """
        
        """
        if self.__decipound_moles != None:
            return self.__decipound_moles
        self.__decipound_moles = self.__convert_from_base(AmountOfSubstanceUnits.DecipoundMole)
        return self.__decipound_moles

    
    @property
    def kilopound_moles(self) -> float:
        """
        
        """
        if self.__kilopound_moles != None:
            return self.__kilopound_moles
        self.__kilopound_moles = self.__convert_from_base(AmountOfSubstanceUnits.KilopoundMole)
        return self.__kilopound_moles

    
    def to_string(self, unit: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole, fractional_digits: int = None) -> str:
        """
        Format the AmountOfSubstance to a string.
        
        Note: the default format for AmountOfSubstance is Mole.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the AmountOfSubstance. Default is 'Mole'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == AmountOfSubstanceUnits.Mole:
            return f"""{super()._truncate_fraction_digits(self.moles, fractional_digits)} mol"""
        
        if unit == AmountOfSubstanceUnits.PoundMole:
            return f"""{super()._truncate_fraction_digits(self.pound_moles, fractional_digits)} lbmol"""
        
        if unit == AmountOfSubstanceUnits.Femtomole:
            return f"""{super()._truncate_fraction_digits(self.femtomoles, fractional_digits)} fmol"""
        
        if unit == AmountOfSubstanceUnits.Picomole:
            return f"""{super()._truncate_fraction_digits(self.picomoles, fractional_digits)} pmol"""
        
        if unit == AmountOfSubstanceUnits.Nanomole:
            return f"""{super()._truncate_fraction_digits(self.nanomoles, fractional_digits)} nmol"""
        
        if unit == AmountOfSubstanceUnits.Micromole:
            return f"""{super()._truncate_fraction_digits(self.micromoles, fractional_digits)} μmol"""
        
        if unit == AmountOfSubstanceUnits.Millimole:
            return f"""{super()._truncate_fraction_digits(self.millimoles, fractional_digits)} mmol"""
        
        if unit == AmountOfSubstanceUnits.Centimole:
            return f"""{super()._truncate_fraction_digits(self.centimoles, fractional_digits)} cmol"""
        
        if unit == AmountOfSubstanceUnits.Decimole:
            return f"""{super()._truncate_fraction_digits(self.decimoles, fractional_digits)} dmol"""
        
        if unit == AmountOfSubstanceUnits.Kilomole:
            return f"""{super()._truncate_fraction_digits(self.kilomoles, fractional_digits)} kmol"""
        
        if unit == AmountOfSubstanceUnits.Megamole:
            return f"""{super()._truncate_fraction_digits(self.megamoles, fractional_digits)} Mmol"""
        
        if unit == AmountOfSubstanceUnits.NanopoundMole:
            return f"""{super()._truncate_fraction_digits(self.nanopound_moles, fractional_digits)} nlbmol"""
        
        if unit == AmountOfSubstanceUnits.MicropoundMole:
            return f"""{super()._truncate_fraction_digits(self.micropound_moles, fractional_digits)} μlbmol"""
        
        if unit == AmountOfSubstanceUnits.MillipoundMole:
            return f"""{super()._truncate_fraction_digits(self.millipound_moles, fractional_digits)} mlbmol"""
        
        if unit == AmountOfSubstanceUnits.CentipoundMole:
            return f"""{super()._truncate_fraction_digits(self.centipound_moles, fractional_digits)} clbmol"""
        
        if unit == AmountOfSubstanceUnits.DecipoundMole:
            return f"""{super()._truncate_fraction_digits(self.decipound_moles, fractional_digits)} dlbmol"""
        
        if unit == AmountOfSubstanceUnits.KilopoundMole:
            return f"""{super()._truncate_fraction_digits(self.kilopound_moles, fractional_digits)} klbmol"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AmountOfSubstanceUnits = AmountOfSubstanceUnits.Mole) -> str:
        """
        Get AmountOfSubstance unit abbreviation.
        Note! the default abbreviation for AmountOfSubstance is Mole.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AmountOfSubstanceUnits.Mole:
            return """mol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.PoundMole:
            return """lbmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Femtomole:
            return """fmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Picomole:
            return """pmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Nanomole:
            return """nmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Micromole:
            return """μmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Millimole:
            return """mmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Centimole:
            return """cmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Decimole:
            return """dmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Kilomole:
            return """kmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.Megamole:
            return """Mmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.NanopoundMole:
            return """nlbmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.MicropoundMole:
            return """μlbmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.MillipoundMole:
            return """mlbmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.CentipoundMole:
            return """clbmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.DecipoundMole:
            return """dlbmol"""
        
        if unit_abbreviation == AmountOfSubstanceUnits.KilopoundMole:
            return """klbmol"""
        