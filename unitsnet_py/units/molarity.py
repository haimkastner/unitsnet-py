from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolarityUnits(Enum):
        """
            MolarityUnits enumeration
        """
        
        MolePerCubicMeter = 'MolePerCubicMeter'
        """
            
        """
        
        MolePerLiter = 'MolePerLiter'
        """
            
        """
        
        PoundMolePerCubicFoot = 'PoundMolePerCubicFoot'
        """
            
        """
        
        KilomolePerCubicMeter = 'KilomolePerCubicMeter'
        """
            
        """
        
        FemtomolePerLiter = 'FemtomolePerLiter'
        """
            
        """
        
        PicomolePerLiter = 'PicomolePerLiter'
        """
            
        """
        
        NanomolePerLiter = 'NanomolePerLiter'
        """
            
        """
        
        MicromolePerLiter = 'MicromolePerLiter'
        """
            
        """
        
        MillimolePerLiter = 'MillimolePerLiter'
        """
            
        """
        
        CentimolePerLiter = 'CentimolePerLiter'
        """
            
        """
        
        DecimolePerLiter = 'DecimolePerLiter'
        """
            
        """
        

class MolarityDto:
    """
    A DTO representation of a Molarity

    Attributes:
        value (float): The value of the Molarity.
        unit (MolarityUnits): The specific unit that the Molarity value is representing.
    """

    def __init__(self, value: float, unit: MolarityUnits):
        """
        Create a new DTO representation of a Molarity

        Parameters:
            value (float): The value of the Molarity.
            unit (MolarityUnits): The specific unit that the Molarity value is representing.
        """
        self.value: float = value
        """
        The value of the Molarity
        """
        self.unit: MolarityUnits = unit
        """
        The specific unit that the Molarity value is representing
        """

    def to_json(self):
        """
        Get a Molarity DTO JSON object representing the current unit.

        :return: JSON object represents Molarity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MolePerCubicMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Molarity DTO from a json representation.

        :param data: The Molarity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MolePerCubicMeter"}
        :return: A new instance of MolarityDto.
        :rtype: MolarityDto
        """
        return MolarityDto(value=data["value"], unit=MolarityUnits(data["unit"]))


class Molarity(AbstractMeasure):
    """
    Molar concentration, also called molarity, amount concentration or substance concentration, is a measure of the concentration of a solute in a solution, or of any chemical species, in terms of amount of substance in a given volume.

    Args:
        value (float): The value.
        from_unit (MolarityUnits): The Molarity unit to create from, The default unit is MolePerCubicMeter
    """
    def __init__(self, value: float, from_unit: MolarityUnits = MolarityUnits.MolePerCubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__moles_per_cubic_meter = None
        
        self.__moles_per_liter = None
        
        self.__pound_moles_per_cubic_foot = None
        
        self.__kilomoles_per_cubic_meter = None
        
        self.__femtomoles_per_liter = None
        
        self.__picomoles_per_liter = None
        
        self.__nanomoles_per_liter = None
        
        self.__micromoles_per_liter = None
        
        self.__millimoles_per_liter = None
        
        self.__centimoles_per_liter = None
        
        self.__decimoles_per_liter = None
        

    def convert(self, unit: MolarityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MolarityUnits = MolarityUnits.MolePerCubicMeter) -> MolarityDto:
        """
        Get a new instance of Molarity DTO representing the current unit.

        :param hold_in_unit: The specific Molarity unit to store the Molarity value in the DTO representation.
        :type hold_in_unit: MolarityUnits
        :return: A new instance of MolarityDto.
        :rtype: MolarityDto
        """
        return MolarityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MolarityUnits = MolarityUnits.MolePerCubicMeter):
        """
        Get a Molarity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Molarity unit to store the Molarity value in the DTO representation.
        :type hold_in_unit: MolarityUnits
        :return: JSON object represents Molarity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "MolePerCubicMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(molarity_dto: MolarityDto):
        """
        Obtain a new instance of Molarity from a DTO unit object.

        :param molarity_dto: The Molarity DTO representation.
        :type molarity_dto: MolarityDto
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(molarity_dto.value, molarity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Molarity from a DTO unit json representation.

        :param data: The Molarity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "MolePerCubicMeter"}
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity.from_dto(MolarityDto.from_json(data))

    def __convert_from_base(self, from_unit: MolarityUnits) -> float:
        value = self._value
        
        if from_unit == MolarityUnits.MolePerCubicMeter:
            return (value)
        
        if from_unit == MolarityUnits.MolePerLiter:
            return (value * 1e-3)
        
        if from_unit == MolarityUnits.PoundMolePerCubicFoot:
            return (value * 6.2427960576144611956325455827221e-5)
        
        if from_unit == MolarityUnits.KilomolePerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == MolarityUnits.FemtomolePerLiter:
            return ((value * 1e-3) / 1e-15)
        
        if from_unit == MolarityUnits.PicomolePerLiter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == MolarityUnits.NanomolePerLiter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == MolarityUnits.MicromolePerLiter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == MolarityUnits.MillimolePerLiter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == MolarityUnits.CentimolePerLiter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == MolarityUnits.DecimolePerLiter:
            return ((value * 1e-3) / 0.1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarityUnits) -> float:
        
        if to_unit == MolarityUnits.MolePerCubicMeter:
            return (value)
        
        if to_unit == MolarityUnits.MolePerLiter:
            return (value / 1e-3)
        
        if to_unit == MolarityUnits.PoundMolePerCubicFoot:
            return (value / 6.2427960576144611956325455827221e-5)
        
        if to_unit == MolarityUnits.KilomolePerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == MolarityUnits.FemtomolePerLiter:
            return ((value / 1e-3) * 1e-15)
        
        if to_unit == MolarityUnits.PicomolePerLiter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == MolarityUnits.NanomolePerLiter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == MolarityUnits.MicromolePerLiter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == MolarityUnits.MillimolePerLiter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == MolarityUnits.CentimolePerLiter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == MolarityUnits.DecimolePerLiter:
            return ((value / 1e-3) * 0.1)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_moles_per_cubic_meter(moles_per_cubic_meter: float):
        """
        Create a new instance of Molarity from a value in moles_per_cubic_meter.

        

        :param meters: The Molarity value in moles_per_cubic_meter.
        :type moles_per_cubic_meter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(moles_per_cubic_meter, MolarityUnits.MolePerCubicMeter)

    
    @staticmethod
    def from_moles_per_liter(moles_per_liter: float):
        """
        Create a new instance of Molarity from a value in moles_per_liter.

        

        :param meters: The Molarity value in moles_per_liter.
        :type moles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(moles_per_liter, MolarityUnits.MolePerLiter)

    
    @staticmethod
    def from_pound_moles_per_cubic_foot(pound_moles_per_cubic_foot: float):
        """
        Create a new instance of Molarity from a value in pound_moles_per_cubic_foot.

        

        :param meters: The Molarity value in pound_moles_per_cubic_foot.
        :type pound_moles_per_cubic_foot: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(pound_moles_per_cubic_foot, MolarityUnits.PoundMolePerCubicFoot)

    
    @staticmethod
    def from_kilomoles_per_cubic_meter(kilomoles_per_cubic_meter: float):
        """
        Create a new instance of Molarity from a value in kilomoles_per_cubic_meter.

        

        :param meters: The Molarity value in kilomoles_per_cubic_meter.
        :type kilomoles_per_cubic_meter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(kilomoles_per_cubic_meter, MolarityUnits.KilomolePerCubicMeter)

    
    @staticmethod
    def from_femtomoles_per_liter(femtomoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in femtomoles_per_liter.

        

        :param meters: The Molarity value in femtomoles_per_liter.
        :type femtomoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(femtomoles_per_liter, MolarityUnits.FemtomolePerLiter)

    
    @staticmethod
    def from_picomoles_per_liter(picomoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in picomoles_per_liter.

        

        :param meters: The Molarity value in picomoles_per_liter.
        :type picomoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(picomoles_per_liter, MolarityUnits.PicomolePerLiter)

    
    @staticmethod
    def from_nanomoles_per_liter(nanomoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in nanomoles_per_liter.

        

        :param meters: The Molarity value in nanomoles_per_liter.
        :type nanomoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(nanomoles_per_liter, MolarityUnits.NanomolePerLiter)

    
    @staticmethod
    def from_micromoles_per_liter(micromoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in micromoles_per_liter.

        

        :param meters: The Molarity value in micromoles_per_liter.
        :type micromoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(micromoles_per_liter, MolarityUnits.MicromolePerLiter)

    
    @staticmethod
    def from_millimoles_per_liter(millimoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in millimoles_per_liter.

        

        :param meters: The Molarity value in millimoles_per_liter.
        :type millimoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(millimoles_per_liter, MolarityUnits.MillimolePerLiter)

    
    @staticmethod
    def from_centimoles_per_liter(centimoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in centimoles_per_liter.

        

        :param meters: The Molarity value in centimoles_per_liter.
        :type centimoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(centimoles_per_liter, MolarityUnits.CentimolePerLiter)

    
    @staticmethod
    def from_decimoles_per_liter(decimoles_per_liter: float):
        """
        Create a new instance of Molarity from a value in decimoles_per_liter.

        

        :param meters: The Molarity value in decimoles_per_liter.
        :type decimoles_per_liter: float
        :return: A new instance of Molarity.
        :rtype: Molarity
        """
        return Molarity(decimoles_per_liter, MolarityUnits.DecimolePerLiter)

    
    @property
    def moles_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__moles_per_cubic_meter != None:
            return self.__moles_per_cubic_meter
        self.__moles_per_cubic_meter = self.__convert_from_base(MolarityUnits.MolePerCubicMeter)
        return self.__moles_per_cubic_meter

    
    @property
    def moles_per_liter(self) -> float:
        """
        
        """
        if self.__moles_per_liter != None:
            return self.__moles_per_liter
        self.__moles_per_liter = self.__convert_from_base(MolarityUnits.MolePerLiter)
        return self.__moles_per_liter

    
    @property
    def pound_moles_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__pound_moles_per_cubic_foot != None:
            return self.__pound_moles_per_cubic_foot
        self.__pound_moles_per_cubic_foot = self.__convert_from_base(MolarityUnits.PoundMolePerCubicFoot)
        return self.__pound_moles_per_cubic_foot

    
    @property
    def kilomoles_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilomoles_per_cubic_meter != None:
            return self.__kilomoles_per_cubic_meter
        self.__kilomoles_per_cubic_meter = self.__convert_from_base(MolarityUnits.KilomolePerCubicMeter)
        return self.__kilomoles_per_cubic_meter

    
    @property
    def femtomoles_per_liter(self) -> float:
        """
        
        """
        if self.__femtomoles_per_liter != None:
            return self.__femtomoles_per_liter
        self.__femtomoles_per_liter = self.__convert_from_base(MolarityUnits.FemtomolePerLiter)
        return self.__femtomoles_per_liter

    
    @property
    def picomoles_per_liter(self) -> float:
        """
        
        """
        if self.__picomoles_per_liter != None:
            return self.__picomoles_per_liter
        self.__picomoles_per_liter = self.__convert_from_base(MolarityUnits.PicomolePerLiter)
        return self.__picomoles_per_liter

    
    @property
    def nanomoles_per_liter(self) -> float:
        """
        
        """
        if self.__nanomoles_per_liter != None:
            return self.__nanomoles_per_liter
        self.__nanomoles_per_liter = self.__convert_from_base(MolarityUnits.NanomolePerLiter)
        return self.__nanomoles_per_liter

    
    @property
    def micromoles_per_liter(self) -> float:
        """
        
        """
        if self.__micromoles_per_liter != None:
            return self.__micromoles_per_liter
        self.__micromoles_per_liter = self.__convert_from_base(MolarityUnits.MicromolePerLiter)
        return self.__micromoles_per_liter

    
    @property
    def millimoles_per_liter(self) -> float:
        """
        
        """
        if self.__millimoles_per_liter != None:
            return self.__millimoles_per_liter
        self.__millimoles_per_liter = self.__convert_from_base(MolarityUnits.MillimolePerLiter)
        return self.__millimoles_per_liter

    
    @property
    def centimoles_per_liter(self) -> float:
        """
        
        """
        if self.__centimoles_per_liter != None:
            return self.__centimoles_per_liter
        self.__centimoles_per_liter = self.__convert_from_base(MolarityUnits.CentimolePerLiter)
        return self.__centimoles_per_liter

    
    @property
    def decimoles_per_liter(self) -> float:
        """
        
        """
        if self.__decimoles_per_liter != None:
            return self.__decimoles_per_liter
        self.__decimoles_per_liter = self.__convert_from_base(MolarityUnits.DecimolePerLiter)
        return self.__decimoles_per_liter

    
    def to_string(self, unit: MolarityUnits = MolarityUnits.MolePerCubicMeter, fractional_digits: int = None) -> str:
        """
        Format the Molarity to a string.
        
        Note: the default format for Molarity is MolePerCubicMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Molarity. Default is 'MolePerCubicMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MolarityUnits.MolePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.moles_per_cubic_meter, fractional_digits)} mol/m³"""
        
        if unit == MolarityUnits.MolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.moles_per_liter, fractional_digits)} mol/L"""
        
        if unit == MolarityUnits.PoundMolePerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.pound_moles_per_cubic_foot, fractional_digits)} lbmol/ft³"""
        
        if unit == MolarityUnits.KilomolePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.kilomoles_per_cubic_meter, fractional_digits)} kmol/m³"""
        
        if unit == MolarityUnits.FemtomolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.femtomoles_per_liter, fractional_digits)} fmol/L"""
        
        if unit == MolarityUnits.PicomolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.picomoles_per_liter, fractional_digits)} pmol/L"""
        
        if unit == MolarityUnits.NanomolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.nanomoles_per_liter, fractional_digits)} nmol/L"""
        
        if unit == MolarityUnits.MicromolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.micromoles_per_liter, fractional_digits)} μmol/L"""
        
        if unit == MolarityUnits.MillimolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.millimoles_per_liter, fractional_digits)} mmol/L"""
        
        if unit == MolarityUnits.CentimolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.centimoles_per_liter, fractional_digits)} cmol/L"""
        
        if unit == MolarityUnits.DecimolePerLiter:
            return f"""{super()._truncate_fraction_digits(self.decimoles_per_liter, fractional_digits)} dmol/L"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarityUnits = MolarityUnits.MolePerCubicMeter) -> str:
        """
        Get Molarity unit abbreviation.
        Note! the default abbreviation for Molarity is MolePerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarityUnits.MolePerCubicMeter:
            return """mol/m³"""
        
        if unit_abbreviation == MolarityUnits.MolePerLiter:
            return """mol/L"""
        
        if unit_abbreviation == MolarityUnits.PoundMolePerCubicFoot:
            return """lbmol/ft³"""
        
        if unit_abbreviation == MolarityUnits.KilomolePerCubicMeter:
            return """kmol/m³"""
        
        if unit_abbreviation == MolarityUnits.FemtomolePerLiter:
            return """fmol/L"""
        
        if unit_abbreviation == MolarityUnits.PicomolePerLiter:
            return """pmol/L"""
        
        if unit_abbreviation == MolarityUnits.NanomolePerLiter:
            return """nmol/L"""
        
        if unit_abbreviation == MolarityUnits.MicromolePerLiter:
            return """μmol/L"""
        
        if unit_abbreviation == MolarityUnits.MillimolePerLiter:
            return """mmol/L"""
        
        if unit_abbreviation == MolarityUnits.CentimolePerLiter:
            return """cmol/L"""
        
        if unit_abbreviation == MolarityUnits.DecimolePerLiter:
            return """dmol/L"""
        