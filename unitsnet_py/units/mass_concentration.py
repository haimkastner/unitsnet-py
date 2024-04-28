from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MassConcentrationUnits(Enum):
        """
            MassConcentrationUnits enumeration
        """
        
        GramPerCubicMillimeter = 'GramPerCubicMillimeter'
        """
            
        """
        
        GramPerCubicCentimeter = 'GramPerCubicCentimeter'
        """
            
        """
        
        GramPerCubicMeter = 'GramPerCubicMeter'
        """
            
        """
        
        GramPerMicroliter = 'GramPerMicroliter'
        """
            
        """
        
        GramPerMilliliter = 'GramPerMilliliter'
        """
            
        """
        
        GramPerDeciliter = 'GramPerDeciliter'
        """
            
        """
        
        GramPerLiter = 'GramPerLiter'
        """
            
        """
        
        TonnePerCubicMillimeter = 'TonnePerCubicMillimeter'
        """
            
        """
        
        TonnePerCubicCentimeter = 'TonnePerCubicCentimeter'
        """
            
        """
        
        TonnePerCubicMeter = 'TonnePerCubicMeter'
        """
            
        """
        
        PoundPerCubicInch = 'PoundPerCubicInch'
        """
            
        """
        
        PoundPerCubicFoot = 'PoundPerCubicFoot'
        """
            
        """
        
        SlugPerCubicFoot = 'SlugPerCubicFoot'
        """
            
        """
        
        PoundPerUSGallon = 'PoundPerUSGallon'
        """
            
        """
        
        OuncePerUSGallon = 'OuncePerUSGallon'
        """
            
        """
        
        OuncePerImperialGallon = 'OuncePerImperialGallon'
        """
            
        """
        
        PoundPerImperialGallon = 'PoundPerImperialGallon'
        """
            
        """
        
        KilogramPerCubicMillimeter = 'KilogramPerCubicMillimeter'
        """
            
        """
        
        KilogramPerCubicCentimeter = 'KilogramPerCubicCentimeter'
        """
            
        """
        
        KilogramPerCubicMeter = 'KilogramPerCubicMeter'
        """
            
        """
        
        MilligramPerCubicMeter = 'MilligramPerCubicMeter'
        """
            
        """
        
        MicrogramPerCubicMeter = 'MicrogramPerCubicMeter'
        """
            
        """
        
        PicogramPerMicroliter = 'PicogramPerMicroliter'
        """
            
        """
        
        NanogramPerMicroliter = 'NanogramPerMicroliter'
        """
            
        """
        
        MicrogramPerMicroliter = 'MicrogramPerMicroliter'
        """
            
        """
        
        MilligramPerMicroliter = 'MilligramPerMicroliter'
        """
            
        """
        
        CentigramPerMicroliter = 'CentigramPerMicroliter'
        """
            
        """
        
        DecigramPerMicroliter = 'DecigramPerMicroliter'
        """
            
        """
        
        PicogramPerMilliliter = 'PicogramPerMilliliter'
        """
            
        """
        
        NanogramPerMilliliter = 'NanogramPerMilliliter'
        """
            
        """
        
        MicrogramPerMilliliter = 'MicrogramPerMilliliter'
        """
            
        """
        
        MilligramPerMilliliter = 'MilligramPerMilliliter'
        """
            
        """
        
        CentigramPerMilliliter = 'CentigramPerMilliliter'
        """
            
        """
        
        DecigramPerMilliliter = 'DecigramPerMilliliter'
        """
            
        """
        
        PicogramPerDeciliter = 'PicogramPerDeciliter'
        """
            
        """
        
        NanogramPerDeciliter = 'NanogramPerDeciliter'
        """
            
        """
        
        MicrogramPerDeciliter = 'MicrogramPerDeciliter'
        """
            
        """
        
        MilligramPerDeciliter = 'MilligramPerDeciliter'
        """
            
        """
        
        CentigramPerDeciliter = 'CentigramPerDeciliter'
        """
            
        """
        
        DecigramPerDeciliter = 'DecigramPerDeciliter'
        """
            
        """
        
        PicogramPerLiter = 'PicogramPerLiter'
        """
            
        """
        
        NanogramPerLiter = 'NanogramPerLiter'
        """
            
        """
        
        MicrogramPerLiter = 'MicrogramPerLiter'
        """
            
        """
        
        MilligramPerLiter = 'MilligramPerLiter'
        """
            
        """
        
        CentigramPerLiter = 'CentigramPerLiter'
        """
            
        """
        
        DecigramPerLiter = 'DecigramPerLiter'
        """
            
        """
        
        KilogramPerLiter = 'KilogramPerLiter'
        """
            
        """
        
        KilopoundPerCubicInch = 'KilopoundPerCubicInch'
        """
            
        """
        
        KilopoundPerCubicFoot = 'KilopoundPerCubicFoot'
        """
            
        """
        

class MassConcentrationDto:
    """
    A DTO representation of a MassConcentration

    Attributes:
        value (float): The value of the MassConcentration.
        unit (MassConcentrationUnits): The specific unit that the MassConcentration value is representing.
    """

    def __init__(self, value: float, unit: MassConcentrationUnits):
        """
        Create a new DTO representation of a MassConcentration

        Parameters:
            value (float): The value of the MassConcentration.
            unit (MassConcentrationUnits): The specific unit that the MassConcentration value is representing.
        """
        self.value: float = value
        """
        The value of the MassConcentration
        """
        self.unit: MassConcentrationUnits = unit
        """
        The specific unit that the MassConcentration value is representing
        """

    def to_json(self):
        """
        Get a MassConcentration DTO JSON object representing the current unit.

        :return: JSON object represents MassConcentration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerCubicMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of MassConcentration DTO from a json representation.

        :param data: The MassConcentration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerCubicMeter"}
        :return: A new instance of MassConcentrationDto.
        :rtype: MassConcentrationDto
        """
        return MassConcentrationDto(value=data["value"], unit=MassConcentrationUnits(data["unit"]))


class MassConcentration(AbstractMeasure):
    """
    In chemistry, the mass concentration ρi (or γi) is defined as the mass of a constituent mi divided by the volume of the mixture V

    Args:
        value (float): The value.
        from_unit (MassConcentrationUnits): The MassConcentration unit to create from, The default unit is KilogramPerCubicMeter
    """
    def __init__(self, value: float, from_unit: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_cubic_millimeter = None
        
        self.__grams_per_cubic_centimeter = None
        
        self.__grams_per_cubic_meter = None
        
        self.__grams_per_microliter = None
        
        self.__grams_per_milliliter = None
        
        self.__grams_per_deciliter = None
        
        self.__grams_per_liter = None
        
        self.__tonnes_per_cubic_millimeter = None
        
        self.__tonnes_per_cubic_centimeter = None
        
        self.__tonnes_per_cubic_meter = None
        
        self.__pounds_per_cubic_inch = None
        
        self.__pounds_per_cubic_foot = None
        
        self.__slugs_per_cubic_foot = None
        
        self.__pounds_per_us_gallon = None
        
        self.__ounces_per_us_gallon = None
        
        self.__ounces_per_imperial_gallon = None
        
        self.__pounds_per_imperial_gallon = None
        
        self.__kilograms_per_cubic_millimeter = None
        
        self.__kilograms_per_cubic_centimeter = None
        
        self.__kilograms_per_cubic_meter = None
        
        self.__milligrams_per_cubic_meter = None
        
        self.__micrograms_per_cubic_meter = None
        
        self.__picograms_per_microliter = None
        
        self.__nanograms_per_microliter = None
        
        self.__micrograms_per_microliter = None
        
        self.__milligrams_per_microliter = None
        
        self.__centigrams_per_microliter = None
        
        self.__decigrams_per_microliter = None
        
        self.__picograms_per_milliliter = None
        
        self.__nanograms_per_milliliter = None
        
        self.__micrograms_per_milliliter = None
        
        self.__milligrams_per_milliliter = None
        
        self.__centigrams_per_milliliter = None
        
        self.__decigrams_per_milliliter = None
        
        self.__picograms_per_deciliter = None
        
        self.__nanograms_per_deciliter = None
        
        self.__micrograms_per_deciliter = None
        
        self.__milligrams_per_deciliter = None
        
        self.__centigrams_per_deciliter = None
        
        self.__decigrams_per_deciliter = None
        
        self.__picograms_per_liter = None
        
        self.__nanograms_per_liter = None
        
        self.__micrograms_per_liter = None
        
        self.__milligrams_per_liter = None
        
        self.__centigrams_per_liter = None
        
        self.__decigrams_per_liter = None
        
        self.__kilograms_per_liter = None
        
        self.__kilopounds_per_cubic_inch = None
        
        self.__kilopounds_per_cubic_foot = None
        

    def convert(self, unit: MassConcentrationUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter) -> MassConcentrationDto:
        """
        Get a new instance of MassConcentration DTO representing the current unit.

        :param hold_in_unit: The specific MassConcentration unit to store the MassConcentration value in the DTO representation.
        :type hold_in_unit: MassConcentrationUnits
        :return: A new instance of MassConcentrationDto.
        :rtype: MassConcentrationDto
        """
        return MassConcentrationDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter):
        """
        Get a MassConcentration DTO JSON object representing the current unit.

        :param hold_in_unit: The specific MassConcentration unit to store the MassConcentration value in the DTO representation.
        :type hold_in_unit: MassConcentrationUnits
        :return: JSON object represents MassConcentration DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerCubicMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(mass_concentration_dto: MassConcentrationDto):
        """
        Obtain a new instance of MassConcentration from a DTO unit object.

        :param mass_concentration_dto: The MassConcentration DTO representation.
        :type mass_concentration_dto: MassConcentrationDto
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(mass_concentration_dto.value, mass_concentration_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of MassConcentration from a DTO unit json representation.

        :param data: The MassConcentration DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerCubicMeter"}
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration.from_dto(MassConcentrationDto.from_json(data))

    def __convert_from_base(self, from_unit: MassConcentrationUnits) -> float:
        value = self._value
        
        if from_unit == MassConcentrationUnits.GramPerCubicMillimeter:
            return (value * 1e-6)
        
        if from_unit == MassConcentrationUnits.GramPerCubicCentimeter:
            return (value * 1e-3)
        
        if from_unit == MassConcentrationUnits.GramPerCubicMeter:
            return (value * 1e3)
        
        if from_unit == MassConcentrationUnits.GramPerMicroliter:
            return (value * 1e-6)
        
        if from_unit == MassConcentrationUnits.GramPerMilliliter:
            return (value * 1e-3)
        
        if from_unit == MassConcentrationUnits.GramPerDeciliter:
            return (value * 1e-1)
        
        if from_unit == MassConcentrationUnits.GramPerLiter:
            return (value)
        
        if from_unit == MassConcentrationUnits.TonnePerCubicMillimeter:
            return (value * 1e-12)
        
        if from_unit == MassConcentrationUnits.TonnePerCubicCentimeter:
            return (value * 1e-9)
        
        if from_unit == MassConcentrationUnits.TonnePerCubicMeter:
            return (value * 0.001)
        
        if from_unit == MassConcentrationUnits.PoundPerCubicInch:
            return (value * 3.6127298147753e-5)
        
        if from_unit == MassConcentrationUnits.PoundPerCubicFoot:
            return (value * 0.062427961)
        
        if from_unit == MassConcentrationUnits.SlugPerCubicFoot:
            return (value * 0.00194032033)
        
        if from_unit == MassConcentrationUnits.PoundPerUSGallon:
            return (value / 1.19826427e2)
        
        if from_unit == MassConcentrationUnits.OuncePerUSGallon:
            return (value * 0.1335264711843)
        
        if from_unit == MassConcentrationUnits.OuncePerImperialGallon:
            return (value * 0.1603586720609)
        
        if from_unit == MassConcentrationUnits.PoundPerImperialGallon:
            return (value / 9.9776398e1)
        
        if from_unit == MassConcentrationUnits.KilogramPerCubicMillimeter:
            return ((value * 1e-6) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KilogramPerCubicCentimeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KilogramPerCubicMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassConcentrationUnits.MilligramPerCubicMeter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassConcentrationUnits.MicrogramPerCubicMeter:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MassConcentrationUnits.PicogramPerMicroliter:
            return ((value * 1e-6) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanogramPerMicroliter:
            return ((value * 1e-6) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicrogramPerMicroliter:
            return ((value * 1e-6) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilligramPerMicroliter:
            return ((value * 1e-6) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentigramPerMicroliter:
            return ((value * 1e-6) / 0.01)
        
        if from_unit == MassConcentrationUnits.DecigramPerMicroliter:
            return ((value * 1e-6) / 0.1)
        
        if from_unit == MassConcentrationUnits.PicogramPerMilliliter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanogramPerMilliliter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicrogramPerMilliliter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilligramPerMilliliter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentigramPerMilliliter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == MassConcentrationUnits.DecigramPerMilliliter:
            return ((value * 1e-3) / 0.1)
        
        if from_unit == MassConcentrationUnits.PicogramPerDeciliter:
            return ((value * 1e-1) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanogramPerDeciliter:
            return ((value * 1e-1) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicrogramPerDeciliter:
            return ((value * 1e-1) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilligramPerDeciliter:
            return ((value * 1e-1) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentigramPerDeciliter:
            return ((value * 1e-1) / 0.01)
        
        if from_unit == MassConcentrationUnits.DecigramPerDeciliter:
            return ((value * 1e-1) / 0.1)
        
        if from_unit == MassConcentrationUnits.PicogramPerLiter:
            return ((value) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanogramPerLiter:
            return ((value) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicrogramPerLiter:
            return ((value) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilligramPerLiter:
            return ((value) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentigramPerLiter:
            return ((value) / 0.01)
        
        if from_unit == MassConcentrationUnits.DecigramPerLiter:
            return ((value) / 0.1)
        
        if from_unit == MassConcentrationUnits.KilogramPerLiter:
            return ((value) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KilopoundPerCubicInch:
            return ((value * 3.6127298147753e-5) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KilopoundPerCubicFoot:
            return ((value * 0.062427961) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassConcentrationUnits) -> float:
        
        if to_unit == MassConcentrationUnits.GramPerCubicMillimeter:
            return (value / 1e-6)
        
        if to_unit == MassConcentrationUnits.GramPerCubicCentimeter:
            return (value / 1e-3)
        
        if to_unit == MassConcentrationUnits.GramPerCubicMeter:
            return (value / 1e3)
        
        if to_unit == MassConcentrationUnits.GramPerMicroliter:
            return (value / 1e-6)
        
        if to_unit == MassConcentrationUnits.GramPerMilliliter:
            return (value / 1e-3)
        
        if to_unit == MassConcentrationUnits.GramPerDeciliter:
            return (value / 1e-1)
        
        if to_unit == MassConcentrationUnits.GramPerLiter:
            return (value)
        
        if to_unit == MassConcentrationUnits.TonnePerCubicMillimeter:
            return (value / 1e-12)
        
        if to_unit == MassConcentrationUnits.TonnePerCubicCentimeter:
            return (value / 1e-9)
        
        if to_unit == MassConcentrationUnits.TonnePerCubicMeter:
            return (value / 0.001)
        
        if to_unit == MassConcentrationUnits.PoundPerCubicInch:
            return (value / 3.6127298147753e-5)
        
        if to_unit == MassConcentrationUnits.PoundPerCubicFoot:
            return (value / 0.062427961)
        
        if to_unit == MassConcentrationUnits.SlugPerCubicFoot:
            return (value * 515.378818)
        
        if to_unit == MassConcentrationUnits.PoundPerUSGallon:
            return (value * 1.19826427e2)
        
        if to_unit == MassConcentrationUnits.OuncePerUSGallon:
            return ( value / 0.1335264711843)
        
        if to_unit == MassConcentrationUnits.OuncePerImperialGallon:
            return ( value / 0.1603586720609)
        
        if to_unit == MassConcentrationUnits.PoundPerImperialGallon:
            return (value * 9.9776398e1)
        
        if to_unit == MassConcentrationUnits.KilogramPerCubicMillimeter:
            return ((value / 1e-6) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KilogramPerCubicCentimeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KilogramPerCubicMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassConcentrationUnits.MilligramPerCubicMeter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassConcentrationUnits.MicrogramPerCubicMeter:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MassConcentrationUnits.PicogramPerMicroliter:
            return ((value / 1e-6) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanogramPerMicroliter:
            return ((value / 1e-6) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicrogramPerMicroliter:
            return ((value / 1e-6) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilligramPerMicroliter:
            return ((value / 1e-6) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentigramPerMicroliter:
            return ((value / 1e-6) * 0.01)
        
        if to_unit == MassConcentrationUnits.DecigramPerMicroliter:
            return ((value / 1e-6) * 0.1)
        
        if to_unit == MassConcentrationUnits.PicogramPerMilliliter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanogramPerMilliliter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicrogramPerMilliliter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilligramPerMilliliter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentigramPerMilliliter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == MassConcentrationUnits.DecigramPerMilliliter:
            return ((value / 1e-3) * 0.1)
        
        if to_unit == MassConcentrationUnits.PicogramPerDeciliter:
            return ((value / 1e-1) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanogramPerDeciliter:
            return ((value / 1e-1) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicrogramPerDeciliter:
            return ((value / 1e-1) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilligramPerDeciliter:
            return ((value / 1e-1) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentigramPerDeciliter:
            return ((value / 1e-1) * 0.01)
        
        if to_unit == MassConcentrationUnits.DecigramPerDeciliter:
            return ((value / 1e-1) * 0.1)
        
        if to_unit == MassConcentrationUnits.PicogramPerLiter:
            return ((value) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanogramPerLiter:
            return ((value) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicrogramPerLiter:
            return ((value) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilligramPerLiter:
            return ((value) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentigramPerLiter:
            return ((value) * 0.01)
        
        if to_unit == MassConcentrationUnits.DecigramPerLiter:
            return ((value) * 0.1)
        
        if to_unit == MassConcentrationUnits.KilogramPerLiter:
            return ((value) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KilopoundPerCubicInch:
            return ((value / 3.6127298147753e-5) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KilopoundPerCubicFoot:
            return ((value / 0.062427961) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_grams_per_cubic_millimeter(grams_per_cubic_millimeter: float):
        """
        Create a new instance of MassConcentration from a value in grams_per_cubic_millimeter.

        

        :param meters: The MassConcentration value in grams_per_cubic_millimeter.
        :type grams_per_cubic_millimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(grams_per_cubic_millimeter, MassConcentrationUnits.GramPerCubicMillimeter)

    
    @staticmethod
    def from_grams_per_cubic_centimeter(grams_per_cubic_centimeter: float):
        """
        Create a new instance of MassConcentration from a value in grams_per_cubic_centimeter.

        

        :param meters: The MassConcentration value in grams_per_cubic_centimeter.
        :type grams_per_cubic_centimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(grams_per_cubic_centimeter, MassConcentrationUnits.GramPerCubicCentimeter)

    
    @staticmethod
    def from_grams_per_cubic_meter(grams_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in grams_per_cubic_meter.

        

        :param meters: The MassConcentration value in grams_per_cubic_meter.
        :type grams_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(grams_per_cubic_meter, MassConcentrationUnits.GramPerCubicMeter)

    
    @staticmethod
    def from_grams_per_microliter(grams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in grams_per_microliter.

        

        :param meters: The MassConcentration value in grams_per_microliter.
        :type grams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(grams_per_microliter, MassConcentrationUnits.GramPerMicroliter)

    
    @staticmethod
    def from_grams_per_milliliter(grams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in grams_per_milliliter.

        

        :param meters: The MassConcentration value in grams_per_milliliter.
        :type grams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(grams_per_milliliter, MassConcentrationUnits.GramPerMilliliter)

    
    @staticmethod
    def from_grams_per_deciliter(grams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in grams_per_deciliter.

        

        :param meters: The MassConcentration value in grams_per_deciliter.
        :type grams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(grams_per_deciliter, MassConcentrationUnits.GramPerDeciliter)

    
    @staticmethod
    def from_grams_per_liter(grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in grams_per_liter.

        

        :param meters: The MassConcentration value in grams_per_liter.
        :type grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(grams_per_liter, MassConcentrationUnits.GramPerLiter)

    
    @staticmethod
    def from_tonnes_per_cubic_millimeter(tonnes_per_cubic_millimeter: float):
        """
        Create a new instance of MassConcentration from a value in tonnes_per_cubic_millimeter.

        

        :param meters: The MassConcentration value in tonnes_per_cubic_millimeter.
        :type tonnes_per_cubic_millimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(tonnes_per_cubic_millimeter, MassConcentrationUnits.TonnePerCubicMillimeter)

    
    @staticmethod
    def from_tonnes_per_cubic_centimeter(tonnes_per_cubic_centimeter: float):
        """
        Create a new instance of MassConcentration from a value in tonnes_per_cubic_centimeter.

        

        :param meters: The MassConcentration value in tonnes_per_cubic_centimeter.
        :type tonnes_per_cubic_centimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(tonnes_per_cubic_centimeter, MassConcentrationUnits.TonnePerCubicCentimeter)

    
    @staticmethod
    def from_tonnes_per_cubic_meter(tonnes_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in tonnes_per_cubic_meter.

        

        :param meters: The MassConcentration value in tonnes_per_cubic_meter.
        :type tonnes_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(tonnes_per_cubic_meter, MassConcentrationUnits.TonnePerCubicMeter)

    
    @staticmethod
    def from_pounds_per_cubic_inch(pounds_per_cubic_inch: float):
        """
        Create a new instance of MassConcentration from a value in pounds_per_cubic_inch.

        

        :param meters: The MassConcentration value in pounds_per_cubic_inch.
        :type pounds_per_cubic_inch: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pounds_per_cubic_inch, MassConcentrationUnits.PoundPerCubicInch)

    
    @staticmethod
    def from_pounds_per_cubic_foot(pounds_per_cubic_foot: float):
        """
        Create a new instance of MassConcentration from a value in pounds_per_cubic_foot.

        

        :param meters: The MassConcentration value in pounds_per_cubic_foot.
        :type pounds_per_cubic_foot: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pounds_per_cubic_foot, MassConcentrationUnits.PoundPerCubicFoot)

    
    @staticmethod
    def from_slugs_per_cubic_foot(slugs_per_cubic_foot: float):
        """
        Create a new instance of MassConcentration from a value in slugs_per_cubic_foot.

        

        :param meters: The MassConcentration value in slugs_per_cubic_foot.
        :type slugs_per_cubic_foot: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(slugs_per_cubic_foot, MassConcentrationUnits.SlugPerCubicFoot)

    
    @staticmethod
    def from_pounds_per_us_gallon(pounds_per_us_gallon: float):
        """
        Create a new instance of MassConcentration from a value in pounds_per_us_gallon.

        

        :param meters: The MassConcentration value in pounds_per_us_gallon.
        :type pounds_per_us_gallon: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pounds_per_us_gallon, MassConcentrationUnits.PoundPerUSGallon)

    
    @staticmethod
    def from_ounces_per_us_gallon(ounces_per_us_gallon: float):
        """
        Create a new instance of MassConcentration from a value in ounces_per_us_gallon.

        

        :param meters: The MassConcentration value in ounces_per_us_gallon.
        :type ounces_per_us_gallon: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(ounces_per_us_gallon, MassConcentrationUnits.OuncePerUSGallon)

    
    @staticmethod
    def from_ounces_per_imperial_gallon(ounces_per_imperial_gallon: float):
        """
        Create a new instance of MassConcentration from a value in ounces_per_imperial_gallon.

        

        :param meters: The MassConcentration value in ounces_per_imperial_gallon.
        :type ounces_per_imperial_gallon: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(ounces_per_imperial_gallon, MassConcentrationUnits.OuncePerImperialGallon)

    
    @staticmethod
    def from_pounds_per_imperial_gallon(pounds_per_imperial_gallon: float):
        """
        Create a new instance of MassConcentration from a value in pounds_per_imperial_gallon.

        

        :param meters: The MassConcentration value in pounds_per_imperial_gallon.
        :type pounds_per_imperial_gallon: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pounds_per_imperial_gallon, MassConcentrationUnits.PoundPerImperialGallon)

    
    @staticmethod
    def from_kilograms_per_cubic_millimeter(kilograms_per_cubic_millimeter: float):
        """
        Create a new instance of MassConcentration from a value in kilograms_per_cubic_millimeter.

        

        :param meters: The MassConcentration value in kilograms_per_cubic_millimeter.
        :type kilograms_per_cubic_millimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilograms_per_cubic_millimeter, MassConcentrationUnits.KilogramPerCubicMillimeter)

    
    @staticmethod
    def from_kilograms_per_cubic_centimeter(kilograms_per_cubic_centimeter: float):
        """
        Create a new instance of MassConcentration from a value in kilograms_per_cubic_centimeter.

        

        :param meters: The MassConcentration value in kilograms_per_cubic_centimeter.
        :type kilograms_per_cubic_centimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilograms_per_cubic_centimeter, MassConcentrationUnits.KilogramPerCubicCentimeter)

    
    @staticmethod
    def from_kilograms_per_cubic_meter(kilograms_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in kilograms_per_cubic_meter.

        

        :param meters: The MassConcentration value in kilograms_per_cubic_meter.
        :type kilograms_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilograms_per_cubic_meter, MassConcentrationUnits.KilogramPerCubicMeter)

    
    @staticmethod
    def from_milligrams_per_cubic_meter(milligrams_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in milligrams_per_cubic_meter.

        

        :param meters: The MassConcentration value in milligrams_per_cubic_meter.
        :type milligrams_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milligrams_per_cubic_meter, MassConcentrationUnits.MilligramPerCubicMeter)

    
    @staticmethod
    def from_micrograms_per_cubic_meter(micrograms_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in micrograms_per_cubic_meter.

        

        :param meters: The MassConcentration value in micrograms_per_cubic_meter.
        :type micrograms_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micrograms_per_cubic_meter, MassConcentrationUnits.MicrogramPerCubicMeter)

    
    @staticmethod
    def from_picograms_per_microliter(picograms_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in picograms_per_microliter.

        

        :param meters: The MassConcentration value in picograms_per_microliter.
        :type picograms_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(picograms_per_microliter, MassConcentrationUnits.PicogramPerMicroliter)

    
    @staticmethod
    def from_nanograms_per_microliter(nanograms_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in nanograms_per_microliter.

        

        :param meters: The MassConcentration value in nanograms_per_microliter.
        :type nanograms_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nanograms_per_microliter, MassConcentrationUnits.NanogramPerMicroliter)

    
    @staticmethod
    def from_micrograms_per_microliter(micrograms_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in micrograms_per_microliter.

        

        :param meters: The MassConcentration value in micrograms_per_microliter.
        :type micrograms_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micrograms_per_microliter, MassConcentrationUnits.MicrogramPerMicroliter)

    
    @staticmethod
    def from_milligrams_per_microliter(milligrams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in milligrams_per_microliter.

        

        :param meters: The MassConcentration value in milligrams_per_microliter.
        :type milligrams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milligrams_per_microliter, MassConcentrationUnits.MilligramPerMicroliter)

    
    @staticmethod
    def from_centigrams_per_microliter(centigrams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in centigrams_per_microliter.

        

        :param meters: The MassConcentration value in centigrams_per_microliter.
        :type centigrams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centigrams_per_microliter, MassConcentrationUnits.CentigramPerMicroliter)

    
    @staticmethod
    def from_decigrams_per_microliter(decigrams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in decigrams_per_microliter.

        

        :param meters: The MassConcentration value in decigrams_per_microliter.
        :type decigrams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(decigrams_per_microliter, MassConcentrationUnits.DecigramPerMicroliter)

    
    @staticmethod
    def from_picograms_per_milliliter(picograms_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in picograms_per_milliliter.

        

        :param meters: The MassConcentration value in picograms_per_milliliter.
        :type picograms_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(picograms_per_milliliter, MassConcentrationUnits.PicogramPerMilliliter)

    
    @staticmethod
    def from_nanograms_per_milliliter(nanograms_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in nanograms_per_milliliter.

        

        :param meters: The MassConcentration value in nanograms_per_milliliter.
        :type nanograms_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nanograms_per_milliliter, MassConcentrationUnits.NanogramPerMilliliter)

    
    @staticmethod
    def from_micrograms_per_milliliter(micrograms_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in micrograms_per_milliliter.

        

        :param meters: The MassConcentration value in micrograms_per_milliliter.
        :type micrograms_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micrograms_per_milliliter, MassConcentrationUnits.MicrogramPerMilliliter)

    
    @staticmethod
    def from_milligrams_per_milliliter(milligrams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in milligrams_per_milliliter.

        

        :param meters: The MassConcentration value in milligrams_per_milliliter.
        :type milligrams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milligrams_per_milliliter, MassConcentrationUnits.MilligramPerMilliliter)

    
    @staticmethod
    def from_centigrams_per_milliliter(centigrams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in centigrams_per_milliliter.

        

        :param meters: The MassConcentration value in centigrams_per_milliliter.
        :type centigrams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centigrams_per_milliliter, MassConcentrationUnits.CentigramPerMilliliter)

    
    @staticmethod
    def from_decigrams_per_milliliter(decigrams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in decigrams_per_milliliter.

        

        :param meters: The MassConcentration value in decigrams_per_milliliter.
        :type decigrams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(decigrams_per_milliliter, MassConcentrationUnits.DecigramPerMilliliter)

    
    @staticmethod
    def from_picograms_per_deciliter(picograms_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in picograms_per_deciliter.

        

        :param meters: The MassConcentration value in picograms_per_deciliter.
        :type picograms_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(picograms_per_deciliter, MassConcentrationUnits.PicogramPerDeciliter)

    
    @staticmethod
    def from_nanograms_per_deciliter(nanograms_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in nanograms_per_deciliter.

        

        :param meters: The MassConcentration value in nanograms_per_deciliter.
        :type nanograms_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nanograms_per_deciliter, MassConcentrationUnits.NanogramPerDeciliter)

    
    @staticmethod
    def from_micrograms_per_deciliter(micrograms_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in micrograms_per_deciliter.

        

        :param meters: The MassConcentration value in micrograms_per_deciliter.
        :type micrograms_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micrograms_per_deciliter, MassConcentrationUnits.MicrogramPerDeciliter)

    
    @staticmethod
    def from_milligrams_per_deciliter(milligrams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in milligrams_per_deciliter.

        

        :param meters: The MassConcentration value in milligrams_per_deciliter.
        :type milligrams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milligrams_per_deciliter, MassConcentrationUnits.MilligramPerDeciliter)

    
    @staticmethod
    def from_centigrams_per_deciliter(centigrams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in centigrams_per_deciliter.

        

        :param meters: The MassConcentration value in centigrams_per_deciliter.
        :type centigrams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centigrams_per_deciliter, MassConcentrationUnits.CentigramPerDeciliter)

    
    @staticmethod
    def from_decigrams_per_deciliter(decigrams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in decigrams_per_deciliter.

        

        :param meters: The MassConcentration value in decigrams_per_deciliter.
        :type decigrams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(decigrams_per_deciliter, MassConcentrationUnits.DecigramPerDeciliter)

    
    @staticmethod
    def from_picograms_per_liter(picograms_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in picograms_per_liter.

        

        :param meters: The MassConcentration value in picograms_per_liter.
        :type picograms_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(picograms_per_liter, MassConcentrationUnits.PicogramPerLiter)

    
    @staticmethod
    def from_nanograms_per_liter(nanograms_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in nanograms_per_liter.

        

        :param meters: The MassConcentration value in nanograms_per_liter.
        :type nanograms_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nanograms_per_liter, MassConcentrationUnits.NanogramPerLiter)

    
    @staticmethod
    def from_micrograms_per_liter(micrograms_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in micrograms_per_liter.

        

        :param meters: The MassConcentration value in micrograms_per_liter.
        :type micrograms_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micrograms_per_liter, MassConcentrationUnits.MicrogramPerLiter)

    
    @staticmethod
    def from_milligrams_per_liter(milligrams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in milligrams_per_liter.

        

        :param meters: The MassConcentration value in milligrams_per_liter.
        :type milligrams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milligrams_per_liter, MassConcentrationUnits.MilligramPerLiter)

    
    @staticmethod
    def from_centigrams_per_liter(centigrams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in centigrams_per_liter.

        

        :param meters: The MassConcentration value in centigrams_per_liter.
        :type centigrams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centigrams_per_liter, MassConcentrationUnits.CentigramPerLiter)

    
    @staticmethod
    def from_decigrams_per_liter(decigrams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in decigrams_per_liter.

        

        :param meters: The MassConcentration value in decigrams_per_liter.
        :type decigrams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(decigrams_per_liter, MassConcentrationUnits.DecigramPerLiter)

    
    @staticmethod
    def from_kilograms_per_liter(kilograms_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in kilograms_per_liter.

        

        :param meters: The MassConcentration value in kilograms_per_liter.
        :type kilograms_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilograms_per_liter, MassConcentrationUnits.KilogramPerLiter)

    
    @staticmethod
    def from_kilopounds_per_cubic_inch(kilopounds_per_cubic_inch: float):
        """
        Create a new instance of MassConcentration from a value in kilopounds_per_cubic_inch.

        

        :param meters: The MassConcentration value in kilopounds_per_cubic_inch.
        :type kilopounds_per_cubic_inch: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilopounds_per_cubic_inch, MassConcentrationUnits.KilopoundPerCubicInch)

    
    @staticmethod
    def from_kilopounds_per_cubic_foot(kilopounds_per_cubic_foot: float):
        """
        Create a new instance of MassConcentration from a value in kilopounds_per_cubic_foot.

        

        :param meters: The MassConcentration value in kilopounds_per_cubic_foot.
        :type kilopounds_per_cubic_foot: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilopounds_per_cubic_foot, MassConcentrationUnits.KilopoundPerCubicFoot)

    
    @property
    def grams_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_millimeter != None:
            return self.__grams_per_cubic_millimeter
        self.__grams_per_cubic_millimeter = self.__convert_from_base(MassConcentrationUnits.GramPerCubicMillimeter)
        return self.__grams_per_cubic_millimeter

    
    @property
    def grams_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_centimeter != None:
            return self.__grams_per_cubic_centimeter
        self.__grams_per_cubic_centimeter = self.__convert_from_base(MassConcentrationUnits.GramPerCubicCentimeter)
        return self.__grams_per_cubic_centimeter

    
    @property
    def grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_meter != None:
            return self.__grams_per_cubic_meter
        self.__grams_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.GramPerCubicMeter)
        return self.__grams_per_cubic_meter

    
    @property
    def grams_per_microliter(self) -> float:
        """
        
        """
        if self.__grams_per_microliter != None:
            return self.__grams_per_microliter
        self.__grams_per_microliter = self.__convert_from_base(MassConcentrationUnits.GramPerMicroliter)
        return self.__grams_per_microliter

    
    @property
    def grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__grams_per_milliliter != None:
            return self.__grams_per_milliliter
        self.__grams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.GramPerMilliliter)
        return self.__grams_per_milliliter

    
    @property
    def grams_per_deciliter(self) -> float:
        """
        
        """
        if self.__grams_per_deciliter != None:
            return self.__grams_per_deciliter
        self.__grams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.GramPerDeciliter)
        return self.__grams_per_deciliter

    
    @property
    def grams_per_liter(self) -> float:
        """
        
        """
        if self.__grams_per_liter != None:
            return self.__grams_per_liter
        self.__grams_per_liter = self.__convert_from_base(MassConcentrationUnits.GramPerLiter)
        return self.__grams_per_liter

    
    @property
    def tonnes_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_millimeter != None:
            return self.__tonnes_per_cubic_millimeter
        self.__tonnes_per_cubic_millimeter = self.__convert_from_base(MassConcentrationUnits.TonnePerCubicMillimeter)
        return self.__tonnes_per_cubic_millimeter

    
    @property
    def tonnes_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_centimeter != None:
            return self.__tonnes_per_cubic_centimeter
        self.__tonnes_per_cubic_centimeter = self.__convert_from_base(MassConcentrationUnits.TonnePerCubicCentimeter)
        return self.__tonnes_per_cubic_centimeter

    
    @property
    def tonnes_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_meter != None:
            return self.__tonnes_per_cubic_meter
        self.__tonnes_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.TonnePerCubicMeter)
        return self.__tonnes_per_cubic_meter

    
    @property
    def pounds_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__pounds_per_cubic_inch != None:
            return self.__pounds_per_cubic_inch
        self.__pounds_per_cubic_inch = self.__convert_from_base(MassConcentrationUnits.PoundPerCubicInch)
        return self.__pounds_per_cubic_inch

    
    @property
    def pounds_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__pounds_per_cubic_foot != None:
            return self.__pounds_per_cubic_foot
        self.__pounds_per_cubic_foot = self.__convert_from_base(MassConcentrationUnits.PoundPerCubicFoot)
        return self.__pounds_per_cubic_foot

    
    @property
    def slugs_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__slugs_per_cubic_foot != None:
            return self.__slugs_per_cubic_foot
        self.__slugs_per_cubic_foot = self.__convert_from_base(MassConcentrationUnits.SlugPerCubicFoot)
        return self.__slugs_per_cubic_foot

    
    @property
    def pounds_per_us_gallon(self) -> float:
        """
        
        """
        if self.__pounds_per_us_gallon != None:
            return self.__pounds_per_us_gallon
        self.__pounds_per_us_gallon = self.__convert_from_base(MassConcentrationUnits.PoundPerUSGallon)
        return self.__pounds_per_us_gallon

    
    @property
    def ounces_per_us_gallon(self) -> float:
        """
        
        """
        if self.__ounces_per_us_gallon != None:
            return self.__ounces_per_us_gallon
        self.__ounces_per_us_gallon = self.__convert_from_base(MassConcentrationUnits.OuncePerUSGallon)
        return self.__ounces_per_us_gallon

    
    @property
    def ounces_per_imperial_gallon(self) -> float:
        """
        
        """
        if self.__ounces_per_imperial_gallon != None:
            return self.__ounces_per_imperial_gallon
        self.__ounces_per_imperial_gallon = self.__convert_from_base(MassConcentrationUnits.OuncePerImperialGallon)
        return self.__ounces_per_imperial_gallon

    
    @property
    def pounds_per_imperial_gallon(self) -> float:
        """
        
        """
        if self.__pounds_per_imperial_gallon != None:
            return self.__pounds_per_imperial_gallon
        self.__pounds_per_imperial_gallon = self.__convert_from_base(MassConcentrationUnits.PoundPerImperialGallon)
        return self.__pounds_per_imperial_gallon

    
    @property
    def kilograms_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_cubic_millimeter != None:
            return self.__kilograms_per_cubic_millimeter
        self.__kilograms_per_cubic_millimeter = self.__convert_from_base(MassConcentrationUnits.KilogramPerCubicMillimeter)
        return self.__kilograms_per_cubic_millimeter

    
    @property
    def kilograms_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_cubic_centimeter != None:
            return self.__kilograms_per_cubic_centimeter
        self.__kilograms_per_cubic_centimeter = self.__convert_from_base(MassConcentrationUnits.KilogramPerCubicCentimeter)
        return self.__kilograms_per_cubic_centimeter

    
    @property
    def kilograms_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilograms_per_cubic_meter != None:
            return self.__kilograms_per_cubic_meter
        self.__kilograms_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.KilogramPerCubicMeter)
        return self.__kilograms_per_cubic_meter

    
    @property
    def milligrams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__milligrams_per_cubic_meter != None:
            return self.__milligrams_per_cubic_meter
        self.__milligrams_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.MilligramPerCubicMeter)
        return self.__milligrams_per_cubic_meter

    
    @property
    def micrograms_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__micrograms_per_cubic_meter != None:
            return self.__micrograms_per_cubic_meter
        self.__micrograms_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.MicrogramPerCubicMeter)
        return self.__micrograms_per_cubic_meter

    
    @property
    def picograms_per_microliter(self) -> float:
        """
        
        """
        if self.__picograms_per_microliter != None:
            return self.__picograms_per_microliter
        self.__picograms_per_microliter = self.__convert_from_base(MassConcentrationUnits.PicogramPerMicroliter)
        return self.__picograms_per_microliter

    
    @property
    def nanograms_per_microliter(self) -> float:
        """
        
        """
        if self.__nanograms_per_microliter != None:
            return self.__nanograms_per_microliter
        self.__nanograms_per_microliter = self.__convert_from_base(MassConcentrationUnits.NanogramPerMicroliter)
        return self.__nanograms_per_microliter

    
    @property
    def micrograms_per_microliter(self) -> float:
        """
        
        """
        if self.__micrograms_per_microliter != None:
            return self.__micrograms_per_microliter
        self.__micrograms_per_microliter = self.__convert_from_base(MassConcentrationUnits.MicrogramPerMicroliter)
        return self.__micrograms_per_microliter

    
    @property
    def milligrams_per_microliter(self) -> float:
        """
        
        """
        if self.__milligrams_per_microliter != None:
            return self.__milligrams_per_microliter
        self.__milligrams_per_microliter = self.__convert_from_base(MassConcentrationUnits.MilligramPerMicroliter)
        return self.__milligrams_per_microliter

    
    @property
    def centigrams_per_microliter(self) -> float:
        """
        
        """
        if self.__centigrams_per_microliter != None:
            return self.__centigrams_per_microliter
        self.__centigrams_per_microliter = self.__convert_from_base(MassConcentrationUnits.CentigramPerMicroliter)
        return self.__centigrams_per_microliter

    
    @property
    def decigrams_per_microliter(self) -> float:
        """
        
        """
        if self.__decigrams_per_microliter != None:
            return self.__decigrams_per_microliter
        self.__decigrams_per_microliter = self.__convert_from_base(MassConcentrationUnits.DecigramPerMicroliter)
        return self.__decigrams_per_microliter

    
    @property
    def picograms_per_milliliter(self) -> float:
        """
        
        """
        if self.__picograms_per_milliliter != None:
            return self.__picograms_per_milliliter
        self.__picograms_per_milliliter = self.__convert_from_base(MassConcentrationUnits.PicogramPerMilliliter)
        return self.__picograms_per_milliliter

    
    @property
    def nanograms_per_milliliter(self) -> float:
        """
        
        """
        if self.__nanograms_per_milliliter != None:
            return self.__nanograms_per_milliliter
        self.__nanograms_per_milliliter = self.__convert_from_base(MassConcentrationUnits.NanogramPerMilliliter)
        return self.__nanograms_per_milliliter

    
    @property
    def micrograms_per_milliliter(self) -> float:
        """
        
        """
        if self.__micrograms_per_milliliter != None:
            return self.__micrograms_per_milliliter
        self.__micrograms_per_milliliter = self.__convert_from_base(MassConcentrationUnits.MicrogramPerMilliliter)
        return self.__micrograms_per_milliliter

    
    @property
    def milligrams_per_milliliter(self) -> float:
        """
        
        """
        if self.__milligrams_per_milliliter != None:
            return self.__milligrams_per_milliliter
        self.__milligrams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.MilligramPerMilliliter)
        return self.__milligrams_per_milliliter

    
    @property
    def centigrams_per_milliliter(self) -> float:
        """
        
        """
        if self.__centigrams_per_milliliter != None:
            return self.__centigrams_per_milliliter
        self.__centigrams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.CentigramPerMilliliter)
        return self.__centigrams_per_milliliter

    
    @property
    def decigrams_per_milliliter(self) -> float:
        """
        
        """
        if self.__decigrams_per_milliliter != None:
            return self.__decigrams_per_milliliter
        self.__decigrams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.DecigramPerMilliliter)
        return self.__decigrams_per_milliliter

    
    @property
    def picograms_per_deciliter(self) -> float:
        """
        
        """
        if self.__picograms_per_deciliter != None:
            return self.__picograms_per_deciliter
        self.__picograms_per_deciliter = self.__convert_from_base(MassConcentrationUnits.PicogramPerDeciliter)
        return self.__picograms_per_deciliter

    
    @property
    def nanograms_per_deciliter(self) -> float:
        """
        
        """
        if self.__nanograms_per_deciliter != None:
            return self.__nanograms_per_deciliter
        self.__nanograms_per_deciliter = self.__convert_from_base(MassConcentrationUnits.NanogramPerDeciliter)
        return self.__nanograms_per_deciliter

    
    @property
    def micrograms_per_deciliter(self) -> float:
        """
        
        """
        if self.__micrograms_per_deciliter != None:
            return self.__micrograms_per_deciliter
        self.__micrograms_per_deciliter = self.__convert_from_base(MassConcentrationUnits.MicrogramPerDeciliter)
        return self.__micrograms_per_deciliter

    
    @property
    def milligrams_per_deciliter(self) -> float:
        """
        
        """
        if self.__milligrams_per_deciliter != None:
            return self.__milligrams_per_deciliter
        self.__milligrams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.MilligramPerDeciliter)
        return self.__milligrams_per_deciliter

    
    @property
    def centigrams_per_deciliter(self) -> float:
        """
        
        """
        if self.__centigrams_per_deciliter != None:
            return self.__centigrams_per_deciliter
        self.__centigrams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.CentigramPerDeciliter)
        return self.__centigrams_per_deciliter

    
    @property
    def decigrams_per_deciliter(self) -> float:
        """
        
        """
        if self.__decigrams_per_deciliter != None:
            return self.__decigrams_per_deciliter
        self.__decigrams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.DecigramPerDeciliter)
        return self.__decigrams_per_deciliter

    
    @property
    def picograms_per_liter(self) -> float:
        """
        
        """
        if self.__picograms_per_liter != None:
            return self.__picograms_per_liter
        self.__picograms_per_liter = self.__convert_from_base(MassConcentrationUnits.PicogramPerLiter)
        return self.__picograms_per_liter

    
    @property
    def nanograms_per_liter(self) -> float:
        """
        
        """
        if self.__nanograms_per_liter != None:
            return self.__nanograms_per_liter
        self.__nanograms_per_liter = self.__convert_from_base(MassConcentrationUnits.NanogramPerLiter)
        return self.__nanograms_per_liter

    
    @property
    def micrograms_per_liter(self) -> float:
        """
        
        """
        if self.__micrograms_per_liter != None:
            return self.__micrograms_per_liter
        self.__micrograms_per_liter = self.__convert_from_base(MassConcentrationUnits.MicrogramPerLiter)
        return self.__micrograms_per_liter

    
    @property
    def milligrams_per_liter(self) -> float:
        """
        
        """
        if self.__milligrams_per_liter != None:
            return self.__milligrams_per_liter
        self.__milligrams_per_liter = self.__convert_from_base(MassConcentrationUnits.MilligramPerLiter)
        return self.__milligrams_per_liter

    
    @property
    def centigrams_per_liter(self) -> float:
        """
        
        """
        if self.__centigrams_per_liter != None:
            return self.__centigrams_per_liter
        self.__centigrams_per_liter = self.__convert_from_base(MassConcentrationUnits.CentigramPerLiter)
        return self.__centigrams_per_liter

    
    @property
    def decigrams_per_liter(self) -> float:
        """
        
        """
        if self.__decigrams_per_liter != None:
            return self.__decigrams_per_liter
        self.__decigrams_per_liter = self.__convert_from_base(MassConcentrationUnits.DecigramPerLiter)
        return self.__decigrams_per_liter

    
    @property
    def kilograms_per_liter(self) -> float:
        """
        
        """
        if self.__kilograms_per_liter != None:
            return self.__kilograms_per_liter
        self.__kilograms_per_liter = self.__convert_from_base(MassConcentrationUnits.KilogramPerLiter)
        return self.__kilograms_per_liter

    
    @property
    def kilopounds_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilopounds_per_cubic_inch != None:
            return self.__kilopounds_per_cubic_inch
        self.__kilopounds_per_cubic_inch = self.__convert_from_base(MassConcentrationUnits.KilopoundPerCubicInch)
        return self.__kilopounds_per_cubic_inch

    
    @property
    def kilopounds_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilopounds_per_cubic_foot != None:
            return self.__kilopounds_per_cubic_foot
        self.__kilopounds_per_cubic_foot = self.__convert_from_base(MassConcentrationUnits.KilopoundPerCubicFoot)
        return self.__kilopounds_per_cubic_foot

    
    def to_string(self, unit: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter, fractional_digits: int = None) -> str:
        """
        Format the MassConcentration to a string.
        
        Note: the default format for MassConcentration is KilogramPerCubicMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the MassConcentration. Default is 'KilogramPerCubicMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MassConcentrationUnits.GramPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_millimeter, fractional_digits)} g/mm³"""
        
        if unit == MassConcentrationUnits.GramPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_centimeter, fractional_digits)} g/cm³"""
        
        if unit == MassConcentrationUnits.GramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_meter, fractional_digits)} g/m³"""
        
        if unit == MassConcentrationUnits.GramPerMicroliter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_microliter, fractional_digits)} g/μL"""
        
        if unit == MassConcentrationUnits.GramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_milliliter, fractional_digits)} g/mL"""
        
        if unit == MassConcentrationUnits.GramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_deciliter, fractional_digits)} g/dL"""
        
        if unit == MassConcentrationUnits.GramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_liter, fractional_digits)} g/L"""
        
        if unit == MassConcentrationUnits.TonnePerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_millimeter, fractional_digits)} t/mm³"""
        
        if unit == MassConcentrationUnits.TonnePerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_centimeter, fractional_digits)} t/cm³"""
        
        if unit == MassConcentrationUnits.TonnePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_meter, fractional_digits)} t/m³"""
        
        if unit == MassConcentrationUnits.PoundPerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_inch, fractional_digits)} lb/in³"""
        
        if unit == MassConcentrationUnits.PoundPerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_foot, fractional_digits)} lb/ft³"""
        
        if unit == MassConcentrationUnits.SlugPerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.slugs_per_cubic_foot, fractional_digits)} slug/ft³"""
        
        if unit == MassConcentrationUnits.PoundPerUSGallon:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_us_gallon, fractional_digits)} ppg (U.S.)"""
        
        if unit == MassConcentrationUnits.OuncePerUSGallon:
            return f"""{super()._truncate_fraction_digits(self.ounces_per_us_gallon, fractional_digits)} oz/gal (U.S.)"""
        
        if unit == MassConcentrationUnits.OuncePerImperialGallon:
            return f"""{super()._truncate_fraction_digits(self.ounces_per_imperial_gallon, fractional_digits)} oz/gal (imp.)"""
        
        if unit == MassConcentrationUnits.PoundPerImperialGallon:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_imperial_gallon, fractional_digits)} ppg (imp.)"""
        
        if unit == MassConcentrationUnits.KilogramPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_cubic_millimeter, fractional_digits)} kg/mm³"""
        
        if unit == MassConcentrationUnits.KilogramPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_cubic_centimeter, fractional_digits)} kg/cm³"""
        
        if unit == MassConcentrationUnits.KilogramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_cubic_meter, fractional_digits)} kg/m³"""
        
        if unit == MassConcentrationUnits.MilligramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_cubic_meter, fractional_digits)} mg/m³"""
        
        if unit == MassConcentrationUnits.MicrogramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_cubic_meter, fractional_digits)} μg/m³"""
        
        if unit == MassConcentrationUnits.PicogramPerMicroliter:
            return f"""{super()._truncate_fraction_digits(self.picograms_per_microliter, fractional_digits)} pg/μL"""
        
        if unit == MassConcentrationUnits.NanogramPerMicroliter:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_microliter, fractional_digits)} ng/μL"""
        
        if unit == MassConcentrationUnits.MicrogramPerMicroliter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_microliter, fractional_digits)} μg/μL"""
        
        if unit == MassConcentrationUnits.MilligramPerMicroliter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_microliter, fractional_digits)} mg/μL"""
        
        if unit == MassConcentrationUnits.CentigramPerMicroliter:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_microliter, fractional_digits)} cg/μL"""
        
        if unit == MassConcentrationUnits.DecigramPerMicroliter:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_microliter, fractional_digits)} dg/μL"""
        
        if unit == MassConcentrationUnits.PicogramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.picograms_per_milliliter, fractional_digits)} pg/mL"""
        
        if unit == MassConcentrationUnits.NanogramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_milliliter, fractional_digits)} ng/mL"""
        
        if unit == MassConcentrationUnits.MicrogramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_milliliter, fractional_digits)} μg/mL"""
        
        if unit == MassConcentrationUnits.MilligramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_milliliter, fractional_digits)} mg/mL"""
        
        if unit == MassConcentrationUnits.CentigramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_milliliter, fractional_digits)} cg/mL"""
        
        if unit == MassConcentrationUnits.DecigramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_milliliter, fractional_digits)} dg/mL"""
        
        if unit == MassConcentrationUnits.PicogramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.picograms_per_deciliter, fractional_digits)} pg/dL"""
        
        if unit == MassConcentrationUnits.NanogramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_deciliter, fractional_digits)} ng/dL"""
        
        if unit == MassConcentrationUnits.MicrogramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_deciliter, fractional_digits)} μg/dL"""
        
        if unit == MassConcentrationUnits.MilligramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_deciliter, fractional_digits)} mg/dL"""
        
        if unit == MassConcentrationUnits.CentigramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_deciliter, fractional_digits)} cg/dL"""
        
        if unit == MassConcentrationUnits.DecigramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_deciliter, fractional_digits)} dg/dL"""
        
        if unit == MassConcentrationUnits.PicogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.picograms_per_liter, fractional_digits)} pg/L"""
        
        if unit == MassConcentrationUnits.NanogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_liter, fractional_digits)} ng/L"""
        
        if unit == MassConcentrationUnits.MicrogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_liter, fractional_digits)} μg/L"""
        
        if unit == MassConcentrationUnits.MilligramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_liter, fractional_digits)} mg/L"""
        
        if unit == MassConcentrationUnits.CentigramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_liter, fractional_digits)} cg/L"""
        
        if unit == MassConcentrationUnits.DecigramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_liter, fractional_digits)} dg/L"""
        
        if unit == MassConcentrationUnits.KilogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_liter, fractional_digits)} kg/L"""
        
        if unit == MassConcentrationUnits.KilopoundPerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_per_cubic_inch, fractional_digits)} klb/in³"""
        
        if unit == MassConcentrationUnits.KilopoundPerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_per_cubic_foot, fractional_digits)} klb/ft³"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter) -> str:
        """
        Get MassConcentration unit abbreviation.
        Note! the default abbreviation for MassConcentration is KilogramPerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassConcentrationUnits.GramPerCubicMillimeter:
            return """g/mm³"""
        
        if unit_abbreviation == MassConcentrationUnits.GramPerCubicCentimeter:
            return """g/cm³"""
        
        if unit_abbreviation == MassConcentrationUnits.GramPerCubicMeter:
            return """g/m³"""
        
        if unit_abbreviation == MassConcentrationUnits.GramPerMicroliter:
            return """g/μL"""
        
        if unit_abbreviation == MassConcentrationUnits.GramPerMilliliter:
            return """g/mL"""
        
        if unit_abbreviation == MassConcentrationUnits.GramPerDeciliter:
            return """g/dL"""
        
        if unit_abbreviation == MassConcentrationUnits.GramPerLiter:
            return """g/L"""
        
        if unit_abbreviation == MassConcentrationUnits.TonnePerCubicMillimeter:
            return """t/mm³"""
        
        if unit_abbreviation == MassConcentrationUnits.TonnePerCubicCentimeter:
            return """t/cm³"""
        
        if unit_abbreviation == MassConcentrationUnits.TonnePerCubicMeter:
            return """t/m³"""
        
        if unit_abbreviation == MassConcentrationUnits.PoundPerCubicInch:
            return """lb/in³"""
        
        if unit_abbreviation == MassConcentrationUnits.PoundPerCubicFoot:
            return """lb/ft³"""
        
        if unit_abbreviation == MassConcentrationUnits.SlugPerCubicFoot:
            return """slug/ft³"""
        
        if unit_abbreviation == MassConcentrationUnits.PoundPerUSGallon:
            return """ppg (U.S.)"""
        
        if unit_abbreviation == MassConcentrationUnits.OuncePerUSGallon:
            return """oz/gal (U.S.)"""
        
        if unit_abbreviation == MassConcentrationUnits.OuncePerImperialGallon:
            return """oz/gal (imp.)"""
        
        if unit_abbreviation == MassConcentrationUnits.PoundPerImperialGallon:
            return """ppg (imp.)"""
        
        if unit_abbreviation == MassConcentrationUnits.KilogramPerCubicMillimeter:
            return """kg/mm³"""
        
        if unit_abbreviation == MassConcentrationUnits.KilogramPerCubicCentimeter:
            return """kg/cm³"""
        
        if unit_abbreviation == MassConcentrationUnits.KilogramPerCubicMeter:
            return """kg/m³"""
        
        if unit_abbreviation == MassConcentrationUnits.MilligramPerCubicMeter:
            return """mg/m³"""
        
        if unit_abbreviation == MassConcentrationUnits.MicrogramPerCubicMeter:
            return """μg/m³"""
        
        if unit_abbreviation == MassConcentrationUnits.PicogramPerMicroliter:
            return """pg/μL"""
        
        if unit_abbreviation == MassConcentrationUnits.NanogramPerMicroliter:
            return """ng/μL"""
        
        if unit_abbreviation == MassConcentrationUnits.MicrogramPerMicroliter:
            return """μg/μL"""
        
        if unit_abbreviation == MassConcentrationUnits.MilligramPerMicroliter:
            return """mg/μL"""
        
        if unit_abbreviation == MassConcentrationUnits.CentigramPerMicroliter:
            return """cg/μL"""
        
        if unit_abbreviation == MassConcentrationUnits.DecigramPerMicroliter:
            return """dg/μL"""
        
        if unit_abbreviation == MassConcentrationUnits.PicogramPerMilliliter:
            return """pg/mL"""
        
        if unit_abbreviation == MassConcentrationUnits.NanogramPerMilliliter:
            return """ng/mL"""
        
        if unit_abbreviation == MassConcentrationUnits.MicrogramPerMilliliter:
            return """μg/mL"""
        
        if unit_abbreviation == MassConcentrationUnits.MilligramPerMilliliter:
            return """mg/mL"""
        
        if unit_abbreviation == MassConcentrationUnits.CentigramPerMilliliter:
            return """cg/mL"""
        
        if unit_abbreviation == MassConcentrationUnits.DecigramPerMilliliter:
            return """dg/mL"""
        
        if unit_abbreviation == MassConcentrationUnits.PicogramPerDeciliter:
            return """pg/dL"""
        
        if unit_abbreviation == MassConcentrationUnits.NanogramPerDeciliter:
            return """ng/dL"""
        
        if unit_abbreviation == MassConcentrationUnits.MicrogramPerDeciliter:
            return """μg/dL"""
        
        if unit_abbreviation == MassConcentrationUnits.MilligramPerDeciliter:
            return """mg/dL"""
        
        if unit_abbreviation == MassConcentrationUnits.CentigramPerDeciliter:
            return """cg/dL"""
        
        if unit_abbreviation == MassConcentrationUnits.DecigramPerDeciliter:
            return """dg/dL"""
        
        if unit_abbreviation == MassConcentrationUnits.PicogramPerLiter:
            return """pg/L"""
        
        if unit_abbreviation == MassConcentrationUnits.NanogramPerLiter:
            return """ng/L"""
        
        if unit_abbreviation == MassConcentrationUnits.MicrogramPerLiter:
            return """μg/L"""
        
        if unit_abbreviation == MassConcentrationUnits.MilligramPerLiter:
            return """mg/L"""
        
        if unit_abbreviation == MassConcentrationUnits.CentigramPerLiter:
            return """cg/L"""
        
        if unit_abbreviation == MassConcentrationUnits.DecigramPerLiter:
            return """dg/L"""
        
        if unit_abbreviation == MassConcentrationUnits.KilogramPerLiter:
            return """kg/L"""
        
        if unit_abbreviation == MassConcentrationUnits.KilopoundPerCubicInch:
            return """klb/in³"""
        
        if unit_abbreviation == MassConcentrationUnits.KilopoundPerCubicFoot:
            return """klb/ft³"""
        