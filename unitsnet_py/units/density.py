from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class DensityUnits(Enum):
        """
            DensityUnits enumeration
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
        
        PoundPerCubicInch = 'PoundPerCubicInch'
        """
            
        """
        
        PoundPerCubicFoot = 'PoundPerCubicFoot'
        """
            
        """
        
        PoundPerCubicYard = 'PoundPerCubicYard'
        """
            Calculated from the definition of <a href="https://en.wikipedia.org/wiki/Pound_(mass)">pound</a> and <a href="https://en.wikipedia.org/wiki/Yard">yard</a> compared to metric kilogram and meter.
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
        
        SlugPerCubicFoot = 'SlugPerCubicFoot'
        """
            
        """
        
        GramPerLiter = 'GramPerLiter'
        """
            
        """
        
        GramPerDeciliter = 'GramPerDeciliter'
        """
            
        """
        
        GramPerMilliliter = 'GramPerMilliliter'
        """
            
        """
        
        PoundPerUSGallon = 'PoundPerUSGallon'
        """
            
        """
        
        PoundPerImperialGallon = 'PoundPerImperialGallon'
        """
            
        """
        
        KilogramPerLiter = 'KilogramPerLiter'
        """
            
        """
        
        TonnePerCubicFoot = 'TonnePerCubicFoot'
        """
            
        """
        
        TonnePerCubicInch = 'TonnePerCubicInch'
        """
            
        """
        
        GramPerCubicFoot = 'GramPerCubicFoot'
        """
            
        """
        
        GramPerCubicInch = 'GramPerCubicInch'
        """
            
        """
        
        PoundPerCubicMeter = 'PoundPerCubicMeter'
        """
            
        """
        
        PoundPerCubicCentimeter = 'PoundPerCubicCentimeter'
        """
            
        """
        
        PoundPerCubicMillimeter = 'PoundPerCubicMillimeter'
        """
            
        """
        
        SlugPerCubicMeter = 'SlugPerCubicMeter'
        """
            
        """
        
        SlugPerCubicCentimeter = 'SlugPerCubicCentimeter'
        """
            
        """
        
        SlugPerCubicMillimeter = 'SlugPerCubicMillimeter'
        """
            
        """
        
        SlugPerCubicInch = 'SlugPerCubicInch'
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
        
        KilopoundPerCubicInch = 'KilopoundPerCubicInch'
        """
            
        """
        
        KilopoundPerCubicFoot = 'KilopoundPerCubicFoot'
        """
            
        """
        
        KilopoundPerCubicYard = 'KilopoundPerCubicYard'
        """
            
        """
        
        FemtogramPerLiter = 'FemtogramPerLiter'
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
        
        FemtogramPerDeciliter = 'FemtogramPerDeciliter'
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
        
        FemtogramPerMilliliter = 'FemtogramPerMilliliter'
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
        

class DensityDto:
    """
    A DTO representation of a Density

    Attributes:
        value (float): The value of the Density.
        unit (DensityUnits): The specific unit that the Density value is representing.
    """

    def __init__(self, value: float, unit: DensityUnits):
        """
        Create a new DTO representation of a Density

        Parameters:
            value (float): The value of the Density.
            unit (DensityUnits): The specific unit that the Density value is representing.
        """
        self.value: float = value
        """
        The value of the Density
        """
        self.unit: DensityUnits = unit
        """
        The specific unit that the Density value is representing
        """

    def to_json(self):
        """
        Get a Density DTO JSON object representing the current unit.

        :return: JSON object represents Density DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerCubicMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Density DTO from a json representation.

        :param data: The Density DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerCubicMeter"}
        :return: A new instance of DensityDto.
        :rtype: DensityDto
        """
        return DensityDto(value=data["value"], unit=DensityUnits(data["unit"]))


class Density(AbstractMeasure):
    """
    The density, or more precisely, the volumetric mass density, of a substance is its mass per unit volume.

    Args:
        value (float): The value.
        from_unit (DensityUnits): The Density unit to create from, The default unit is KilogramPerCubicMeter
    """
    def __init__(self, value: float, from_unit: DensityUnits = DensityUnits.KilogramPerCubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_cubic_millimeter = None
        
        self.__grams_per_cubic_centimeter = None
        
        self.__grams_per_cubic_meter = None
        
        self.__pounds_per_cubic_inch = None
        
        self.__pounds_per_cubic_foot = None
        
        self.__pounds_per_cubic_yard = None
        
        self.__tonnes_per_cubic_millimeter = None
        
        self.__tonnes_per_cubic_centimeter = None
        
        self.__tonnes_per_cubic_meter = None
        
        self.__slugs_per_cubic_foot = None
        
        self.__grams_per_liter = None
        
        self.__grams_per_deci_liter = None
        
        self.__grams_per_milliliter = None
        
        self.__pounds_per_us_gallon = None
        
        self.__pounds_per_imperial_gallon = None
        
        self.__kilograms_per_liter = None
        
        self.__tonnes_per_cubic_foot = None
        
        self.__tonnes_per_cubic_inch = None
        
        self.__grams_per_cubic_foot = None
        
        self.__grams_per_cubic_inch = None
        
        self.__pounds_per_cubic_meter = None
        
        self.__pounds_per_cubic_centimeter = None
        
        self.__pounds_per_cubic_millimeter = None
        
        self.__slugs_per_cubic_meter = None
        
        self.__slugs_per_cubic_centimeter = None
        
        self.__slugs_per_cubic_millimeter = None
        
        self.__slugs_per_cubic_inch = None
        
        self.__kilograms_per_cubic_millimeter = None
        
        self.__kilograms_per_cubic_centimeter = None
        
        self.__kilograms_per_cubic_meter = None
        
        self.__milligrams_per_cubic_meter = None
        
        self.__micrograms_per_cubic_meter = None
        
        self.__kilopounds_per_cubic_inch = None
        
        self.__kilopounds_per_cubic_foot = None
        
        self.__kilopounds_per_cubic_yard = None
        
        self.__femtograms_per_liter = None
        
        self.__picograms_per_liter = None
        
        self.__nanograms_per_liter = None
        
        self.__micrograms_per_liter = None
        
        self.__milligrams_per_liter = None
        
        self.__centigrams_per_liter = None
        
        self.__decigrams_per_liter = None
        
        self.__femtograms_per_deci_liter = None
        
        self.__picograms_per_deci_liter = None
        
        self.__nanograms_per_deci_liter = None
        
        self.__micrograms_per_deci_liter = None
        
        self.__milligrams_per_deci_liter = None
        
        self.__centigrams_per_deci_liter = None
        
        self.__decigrams_per_deci_liter = None
        
        self.__femtograms_per_milliliter = None
        
        self.__picograms_per_milliliter = None
        
        self.__nanograms_per_milliliter = None
        
        self.__micrograms_per_milliliter = None
        
        self.__milligrams_per_milliliter = None
        
        self.__centigrams_per_milliliter = None
        
        self.__decigrams_per_milliliter = None
        

    def convert(self, unit: DensityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: DensityUnits = DensityUnits.KilogramPerCubicMeter) -> DensityDto:
        """
        Get a new instance of Density DTO representing the current unit.

        :param hold_in_unit: The specific Density unit to store the Density value in the DTO representation.
        :type hold_in_unit: DensityUnits
        :return: A new instance of DensityDto.
        :rtype: DensityDto
        """
        return DensityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: DensityUnits = DensityUnits.KilogramPerCubicMeter):
        """
        Get a Density DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Density unit to store the Density value in the DTO representation.
        :type hold_in_unit: DensityUnits
        :return: JSON object represents Density DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "KilogramPerCubicMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(density_dto: DensityDto):
        """
        Obtain a new instance of Density from a DTO unit object.

        :param density_dto: The Density DTO representation.
        :type density_dto: DensityDto
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(density_dto.value, density_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Density from a DTO unit json representation.

        :param data: The Density DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "KilogramPerCubicMeter"}
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density.from_dto(DensityDto.from_json(data))

    def __convert_from_base(self, from_unit: DensityUnits) -> float:
        value = self._value
        
        if from_unit == DensityUnits.GramPerCubicMillimeter:
            return (value * 1e-6)
        
        if from_unit == DensityUnits.GramPerCubicCentimeter:
            return (value * 1e-3)
        
        if from_unit == DensityUnits.GramPerCubicMeter:
            return (value * 1e3)
        
        if from_unit == DensityUnits.PoundPerCubicInch:
            return (value * 3.6127298147753e-5)
        
        if from_unit == DensityUnits.PoundPerCubicFoot:
            return (value * 0.062427961)
        
        if from_unit == DensityUnits.PoundPerCubicYard:
            return (value / (0.45359237 / 0.9144 / 0.9144 / 0.9144))
        
        if from_unit == DensityUnits.TonnePerCubicMillimeter:
            return (value * 1e-12)
        
        if from_unit == DensityUnits.TonnePerCubicCentimeter:
            return (value * 1e-9)
        
        if from_unit == DensityUnits.TonnePerCubicMeter:
            return (value * 0.001)
        
        if from_unit == DensityUnits.SlugPerCubicFoot:
            return (value * 0.00194032033)
        
        if from_unit == DensityUnits.GramPerLiter:
            return (value * 1)
        
        if from_unit == DensityUnits.GramPerDeciliter:
            return (value * 1e-1)
        
        if from_unit == DensityUnits.GramPerMilliliter:
            return (value * 1e-3)
        
        if from_unit == DensityUnits.PoundPerUSGallon:
            return (value / 1.19826427e2)
        
        if from_unit == DensityUnits.PoundPerImperialGallon:
            return (value / 9.9776398e1)
        
        if from_unit == DensityUnits.KilogramPerLiter:
            return (value / 1e3)
        
        if from_unit == DensityUnits.TonnePerCubicFoot:
            return (value / 3.53146667214886e4)
        
        if from_unit == DensityUnits.TonnePerCubicInch:
            return (value / 6.10237440947323e7)
        
        if from_unit == DensityUnits.GramPerCubicFoot:
            return (value / 0.0353146667214886)
        
        if from_unit == DensityUnits.GramPerCubicInch:
            return (value / 61.0237440947323)
        
        if from_unit == DensityUnits.PoundPerCubicMeter:
            return (value * 2.204622621848775)
        
        if from_unit == DensityUnits.PoundPerCubicCentimeter:
            return (value * 2.204622621848775e-6)
        
        if from_unit == DensityUnits.PoundPerCubicMillimeter:
            return (value * 2.204622621848775e-9)
        
        if from_unit == DensityUnits.SlugPerCubicMeter:
            return (value / 14.5939)
        
        if from_unit == DensityUnits.SlugPerCubicCentimeter:
            return (value / 14593903)
        
        if from_unit == DensityUnits.SlugPerCubicMillimeter:
            return (value / 14593903000)
        
        if from_unit == DensityUnits.SlugPerCubicInch:
            return (value / 890574.60201535)
        
        if from_unit == DensityUnits.KilogramPerCubicMillimeter:
            return ((value * 1e-6) / 1000.0)
        
        if from_unit == DensityUnits.KilogramPerCubicCentimeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == DensityUnits.KilogramPerCubicMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == DensityUnits.MilligramPerCubicMeter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == DensityUnits.MicrogramPerCubicMeter:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == DensityUnits.KilopoundPerCubicInch:
            return ((value * 3.6127298147753e-5) / 1000.0)
        
        if from_unit == DensityUnits.KilopoundPerCubicFoot:
            return ((value * 0.062427961) / 1000.0)
        
        if from_unit == DensityUnits.KilopoundPerCubicYard:
            return ((value / (0.45359237 / 0.9144 / 0.9144 / 0.9144)) / 1000.0)
        
        if from_unit == DensityUnits.FemtogramPerLiter:
            return ((value * 1) / 1e-15)
        
        if from_unit == DensityUnits.PicogramPerLiter:
            return ((value * 1) / 1e-12)
        
        if from_unit == DensityUnits.NanogramPerLiter:
            return ((value * 1) / 1e-09)
        
        if from_unit == DensityUnits.MicrogramPerLiter:
            return ((value * 1) / 1e-06)
        
        if from_unit == DensityUnits.MilligramPerLiter:
            return ((value * 1) / 0.001)
        
        if from_unit == DensityUnits.CentigramPerLiter:
            return ((value * 1) / 0.01)
        
        if from_unit == DensityUnits.DecigramPerLiter:
            return ((value * 1) / 0.1)
        
        if from_unit == DensityUnits.FemtogramPerDeciliter:
            return ((value * 1e-1) / 1e-15)
        
        if from_unit == DensityUnits.PicogramPerDeciliter:
            return ((value * 1e-1) / 1e-12)
        
        if from_unit == DensityUnits.NanogramPerDeciliter:
            return ((value * 1e-1) / 1e-09)
        
        if from_unit == DensityUnits.MicrogramPerDeciliter:
            return ((value * 1e-1) / 1e-06)
        
        if from_unit == DensityUnits.MilligramPerDeciliter:
            return ((value * 1e-1) / 0.001)
        
        if from_unit == DensityUnits.CentigramPerDeciliter:
            return ((value * 1e-1) / 0.01)
        
        if from_unit == DensityUnits.DecigramPerDeciliter:
            return ((value * 1e-1) / 0.1)
        
        if from_unit == DensityUnits.FemtogramPerMilliliter:
            return ((value * 1e-3) / 1e-15)
        
        if from_unit == DensityUnits.PicogramPerMilliliter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == DensityUnits.NanogramPerMilliliter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == DensityUnits.MicrogramPerMilliliter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == DensityUnits.MilligramPerMilliliter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == DensityUnits.CentigramPerMilliliter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == DensityUnits.DecigramPerMilliliter:
            return ((value * 1e-3) / 0.1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: DensityUnits) -> float:
        
        if to_unit == DensityUnits.GramPerCubicMillimeter:
            return (value / 1e-6)
        
        if to_unit == DensityUnits.GramPerCubicCentimeter:
            return (value / 1e-3)
        
        if to_unit == DensityUnits.GramPerCubicMeter:
            return (value / 1e3)
        
        if to_unit == DensityUnits.PoundPerCubicInch:
            return (value / 3.6127298147753e-5)
        
        if to_unit == DensityUnits.PoundPerCubicFoot:
            return (value / 0.062427961)
        
        if to_unit == DensityUnits.PoundPerCubicYard:
            return (value * (0.45359237 / 0.9144 / 0.9144 / 0.9144))
        
        if to_unit == DensityUnits.TonnePerCubicMillimeter:
            return (value / 1e-12)
        
        if to_unit == DensityUnits.TonnePerCubicCentimeter:
            return (value / 1e-9)
        
        if to_unit == DensityUnits.TonnePerCubicMeter:
            return (value / 0.001)
        
        if to_unit == DensityUnits.SlugPerCubicFoot:
            return (value * 515.378818)
        
        if to_unit == DensityUnits.GramPerLiter:
            return (value / 1)
        
        if to_unit == DensityUnits.GramPerDeciliter:
            return (value / 1e-1)
        
        if to_unit == DensityUnits.GramPerMilliliter:
            return (value / 1e-3)
        
        if to_unit == DensityUnits.PoundPerUSGallon:
            return (value * 1.19826427e2)
        
        if to_unit == DensityUnits.PoundPerImperialGallon:
            return (value * 9.9776398e1)
        
        if to_unit == DensityUnits.KilogramPerLiter:
            return (value * 1e3)
        
        if to_unit == DensityUnits.TonnePerCubicFoot:
            return (value * 3.53146667214886e4)
        
        if to_unit == DensityUnits.TonnePerCubicInch:
            return (value * 6.10237440947323e7)
        
        if to_unit == DensityUnits.GramPerCubicFoot:
            return (value * 0.0353146667214886)
        
        if to_unit == DensityUnits.GramPerCubicInch:
            return (value * 61.0237440947323)
        
        if to_unit == DensityUnits.PoundPerCubicMeter:
            return (value / 2.204622621848775)
        
        if to_unit == DensityUnits.PoundPerCubicCentimeter:
            return (value / 2.204622621848775e-6)
        
        if to_unit == DensityUnits.PoundPerCubicMillimeter:
            return (value / 2.204622621848775e-9)
        
        if to_unit == DensityUnits.SlugPerCubicMeter:
            return (value * 14.5939)
        
        if to_unit == DensityUnits.SlugPerCubicCentimeter:
            return (value * 14593903)
        
        if to_unit == DensityUnits.SlugPerCubicMillimeter:
            return (value * 14593903000)
        
        if to_unit == DensityUnits.SlugPerCubicInch:
            return (value * 890574.60201535)
        
        if to_unit == DensityUnits.KilogramPerCubicMillimeter:
            return ((value / 1e-6) * 1000.0)
        
        if to_unit == DensityUnits.KilogramPerCubicCentimeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == DensityUnits.KilogramPerCubicMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == DensityUnits.MilligramPerCubicMeter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == DensityUnits.MicrogramPerCubicMeter:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == DensityUnits.KilopoundPerCubicInch:
            return ((value / 3.6127298147753e-5) * 1000.0)
        
        if to_unit == DensityUnits.KilopoundPerCubicFoot:
            return ((value / 0.062427961) * 1000.0)
        
        if to_unit == DensityUnits.KilopoundPerCubicYard:
            return ((value * (0.45359237 / 0.9144 / 0.9144 / 0.9144)) * 1000.0)
        
        if to_unit == DensityUnits.FemtogramPerLiter:
            return ((value / 1) * 1e-15)
        
        if to_unit == DensityUnits.PicogramPerLiter:
            return ((value / 1) * 1e-12)
        
        if to_unit == DensityUnits.NanogramPerLiter:
            return ((value / 1) * 1e-09)
        
        if to_unit == DensityUnits.MicrogramPerLiter:
            return ((value / 1) * 1e-06)
        
        if to_unit == DensityUnits.MilligramPerLiter:
            return ((value / 1) * 0.001)
        
        if to_unit == DensityUnits.CentigramPerLiter:
            return ((value / 1) * 0.01)
        
        if to_unit == DensityUnits.DecigramPerLiter:
            return ((value / 1) * 0.1)
        
        if to_unit == DensityUnits.FemtogramPerDeciliter:
            return ((value / 1e-1) * 1e-15)
        
        if to_unit == DensityUnits.PicogramPerDeciliter:
            return ((value / 1e-1) * 1e-12)
        
        if to_unit == DensityUnits.NanogramPerDeciliter:
            return ((value / 1e-1) * 1e-09)
        
        if to_unit == DensityUnits.MicrogramPerDeciliter:
            return ((value / 1e-1) * 1e-06)
        
        if to_unit == DensityUnits.MilligramPerDeciliter:
            return ((value / 1e-1) * 0.001)
        
        if to_unit == DensityUnits.CentigramPerDeciliter:
            return ((value / 1e-1) * 0.01)
        
        if to_unit == DensityUnits.DecigramPerDeciliter:
            return ((value / 1e-1) * 0.1)
        
        if to_unit == DensityUnits.FemtogramPerMilliliter:
            return ((value / 1e-3) * 1e-15)
        
        if to_unit == DensityUnits.PicogramPerMilliliter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == DensityUnits.NanogramPerMilliliter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == DensityUnits.MicrogramPerMilliliter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == DensityUnits.MilligramPerMilliliter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == DensityUnits.CentigramPerMilliliter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == DensityUnits.DecigramPerMilliliter:
            return ((value / 1e-3) * 0.1)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_grams_per_cubic_millimeter(grams_per_cubic_millimeter: float):
        """
        Create a new instance of Density from a value in grams_per_cubic_millimeter.

        

        :param meters: The Density value in grams_per_cubic_millimeter.
        :type grams_per_cubic_millimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_cubic_millimeter, DensityUnits.GramPerCubicMillimeter)

    
    @staticmethod
    def from_grams_per_cubic_centimeter(grams_per_cubic_centimeter: float):
        """
        Create a new instance of Density from a value in grams_per_cubic_centimeter.

        

        :param meters: The Density value in grams_per_cubic_centimeter.
        :type grams_per_cubic_centimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_cubic_centimeter, DensityUnits.GramPerCubicCentimeter)

    
    @staticmethod
    def from_grams_per_cubic_meter(grams_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in grams_per_cubic_meter.

        

        :param meters: The Density value in grams_per_cubic_meter.
        :type grams_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_cubic_meter, DensityUnits.GramPerCubicMeter)

    
    @staticmethod
    def from_pounds_per_cubic_inch(pounds_per_cubic_inch: float):
        """
        Create a new instance of Density from a value in pounds_per_cubic_inch.

        

        :param meters: The Density value in pounds_per_cubic_inch.
        :type pounds_per_cubic_inch: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_cubic_inch, DensityUnits.PoundPerCubicInch)

    
    @staticmethod
    def from_pounds_per_cubic_foot(pounds_per_cubic_foot: float):
        """
        Create a new instance of Density from a value in pounds_per_cubic_foot.

        

        :param meters: The Density value in pounds_per_cubic_foot.
        :type pounds_per_cubic_foot: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_cubic_foot, DensityUnits.PoundPerCubicFoot)

    
    @staticmethod
    def from_pounds_per_cubic_yard(pounds_per_cubic_yard: float):
        """
        Create a new instance of Density from a value in pounds_per_cubic_yard.

        Calculated from the definition of <a href="https://en.wikipedia.org/wiki/Pound_(mass)">pound</a> and <a href="https://en.wikipedia.org/wiki/Yard">yard</a> compared to metric kilogram and meter.

        :param meters: The Density value in pounds_per_cubic_yard.
        :type pounds_per_cubic_yard: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_cubic_yard, DensityUnits.PoundPerCubicYard)

    
    @staticmethod
    def from_tonnes_per_cubic_millimeter(tonnes_per_cubic_millimeter: float):
        """
        Create a new instance of Density from a value in tonnes_per_cubic_millimeter.

        

        :param meters: The Density value in tonnes_per_cubic_millimeter.
        :type tonnes_per_cubic_millimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(tonnes_per_cubic_millimeter, DensityUnits.TonnePerCubicMillimeter)

    
    @staticmethod
    def from_tonnes_per_cubic_centimeter(tonnes_per_cubic_centimeter: float):
        """
        Create a new instance of Density from a value in tonnes_per_cubic_centimeter.

        

        :param meters: The Density value in tonnes_per_cubic_centimeter.
        :type tonnes_per_cubic_centimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(tonnes_per_cubic_centimeter, DensityUnits.TonnePerCubicCentimeter)

    
    @staticmethod
    def from_tonnes_per_cubic_meter(tonnes_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in tonnes_per_cubic_meter.

        

        :param meters: The Density value in tonnes_per_cubic_meter.
        :type tonnes_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(tonnes_per_cubic_meter, DensityUnits.TonnePerCubicMeter)

    
    @staticmethod
    def from_slugs_per_cubic_foot(slugs_per_cubic_foot: float):
        """
        Create a new instance of Density from a value in slugs_per_cubic_foot.

        

        :param meters: The Density value in slugs_per_cubic_foot.
        :type slugs_per_cubic_foot: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(slugs_per_cubic_foot, DensityUnits.SlugPerCubicFoot)

    
    @staticmethod
    def from_grams_per_liter(grams_per_liter: float):
        """
        Create a new instance of Density from a value in grams_per_liter.

        

        :param meters: The Density value in grams_per_liter.
        :type grams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_liter, DensityUnits.GramPerLiter)

    
    @staticmethod
    def from_grams_per_deci_liter(grams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in grams_per_deci_liter.

        

        :param meters: The Density value in grams_per_deci_liter.
        :type grams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_deci_liter, DensityUnits.GramPerDeciliter)

    
    @staticmethod
    def from_grams_per_milliliter(grams_per_milliliter: float):
        """
        Create a new instance of Density from a value in grams_per_milliliter.

        

        :param meters: The Density value in grams_per_milliliter.
        :type grams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_milliliter, DensityUnits.GramPerMilliliter)

    
    @staticmethod
    def from_pounds_per_us_gallon(pounds_per_us_gallon: float):
        """
        Create a new instance of Density from a value in pounds_per_us_gallon.

        

        :param meters: The Density value in pounds_per_us_gallon.
        :type pounds_per_us_gallon: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_us_gallon, DensityUnits.PoundPerUSGallon)

    
    @staticmethod
    def from_pounds_per_imperial_gallon(pounds_per_imperial_gallon: float):
        """
        Create a new instance of Density from a value in pounds_per_imperial_gallon.

        

        :param meters: The Density value in pounds_per_imperial_gallon.
        :type pounds_per_imperial_gallon: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_imperial_gallon, DensityUnits.PoundPerImperialGallon)

    
    @staticmethod
    def from_kilograms_per_liter(kilograms_per_liter: float):
        """
        Create a new instance of Density from a value in kilograms_per_liter.

        

        :param meters: The Density value in kilograms_per_liter.
        :type kilograms_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilograms_per_liter, DensityUnits.KilogramPerLiter)

    
    @staticmethod
    def from_tonnes_per_cubic_foot(tonnes_per_cubic_foot: float):
        """
        Create a new instance of Density from a value in tonnes_per_cubic_foot.

        

        :param meters: The Density value in tonnes_per_cubic_foot.
        :type tonnes_per_cubic_foot: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(tonnes_per_cubic_foot, DensityUnits.TonnePerCubicFoot)

    
    @staticmethod
    def from_tonnes_per_cubic_inch(tonnes_per_cubic_inch: float):
        """
        Create a new instance of Density from a value in tonnes_per_cubic_inch.

        

        :param meters: The Density value in tonnes_per_cubic_inch.
        :type tonnes_per_cubic_inch: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(tonnes_per_cubic_inch, DensityUnits.TonnePerCubicInch)

    
    @staticmethod
    def from_grams_per_cubic_foot(grams_per_cubic_foot: float):
        """
        Create a new instance of Density from a value in grams_per_cubic_foot.

        

        :param meters: The Density value in grams_per_cubic_foot.
        :type grams_per_cubic_foot: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_cubic_foot, DensityUnits.GramPerCubicFoot)

    
    @staticmethod
    def from_grams_per_cubic_inch(grams_per_cubic_inch: float):
        """
        Create a new instance of Density from a value in grams_per_cubic_inch.

        

        :param meters: The Density value in grams_per_cubic_inch.
        :type grams_per_cubic_inch: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(grams_per_cubic_inch, DensityUnits.GramPerCubicInch)

    
    @staticmethod
    def from_pounds_per_cubic_meter(pounds_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in pounds_per_cubic_meter.

        

        :param meters: The Density value in pounds_per_cubic_meter.
        :type pounds_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_cubic_meter, DensityUnits.PoundPerCubicMeter)

    
    @staticmethod
    def from_pounds_per_cubic_centimeter(pounds_per_cubic_centimeter: float):
        """
        Create a new instance of Density from a value in pounds_per_cubic_centimeter.

        

        :param meters: The Density value in pounds_per_cubic_centimeter.
        :type pounds_per_cubic_centimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_cubic_centimeter, DensityUnits.PoundPerCubicCentimeter)

    
    @staticmethod
    def from_pounds_per_cubic_millimeter(pounds_per_cubic_millimeter: float):
        """
        Create a new instance of Density from a value in pounds_per_cubic_millimeter.

        

        :param meters: The Density value in pounds_per_cubic_millimeter.
        :type pounds_per_cubic_millimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pounds_per_cubic_millimeter, DensityUnits.PoundPerCubicMillimeter)

    
    @staticmethod
    def from_slugs_per_cubic_meter(slugs_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in slugs_per_cubic_meter.

        

        :param meters: The Density value in slugs_per_cubic_meter.
        :type slugs_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(slugs_per_cubic_meter, DensityUnits.SlugPerCubicMeter)

    
    @staticmethod
    def from_slugs_per_cubic_centimeter(slugs_per_cubic_centimeter: float):
        """
        Create a new instance of Density from a value in slugs_per_cubic_centimeter.

        

        :param meters: The Density value in slugs_per_cubic_centimeter.
        :type slugs_per_cubic_centimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(slugs_per_cubic_centimeter, DensityUnits.SlugPerCubicCentimeter)

    
    @staticmethod
    def from_slugs_per_cubic_millimeter(slugs_per_cubic_millimeter: float):
        """
        Create a new instance of Density from a value in slugs_per_cubic_millimeter.

        

        :param meters: The Density value in slugs_per_cubic_millimeter.
        :type slugs_per_cubic_millimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(slugs_per_cubic_millimeter, DensityUnits.SlugPerCubicMillimeter)

    
    @staticmethod
    def from_slugs_per_cubic_inch(slugs_per_cubic_inch: float):
        """
        Create a new instance of Density from a value in slugs_per_cubic_inch.

        

        :param meters: The Density value in slugs_per_cubic_inch.
        :type slugs_per_cubic_inch: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(slugs_per_cubic_inch, DensityUnits.SlugPerCubicInch)

    
    @staticmethod
    def from_kilograms_per_cubic_millimeter(kilograms_per_cubic_millimeter: float):
        """
        Create a new instance of Density from a value in kilograms_per_cubic_millimeter.

        

        :param meters: The Density value in kilograms_per_cubic_millimeter.
        :type kilograms_per_cubic_millimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilograms_per_cubic_millimeter, DensityUnits.KilogramPerCubicMillimeter)

    
    @staticmethod
    def from_kilograms_per_cubic_centimeter(kilograms_per_cubic_centimeter: float):
        """
        Create a new instance of Density from a value in kilograms_per_cubic_centimeter.

        

        :param meters: The Density value in kilograms_per_cubic_centimeter.
        :type kilograms_per_cubic_centimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilograms_per_cubic_centimeter, DensityUnits.KilogramPerCubicCentimeter)

    
    @staticmethod
    def from_kilograms_per_cubic_meter(kilograms_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in kilograms_per_cubic_meter.

        

        :param meters: The Density value in kilograms_per_cubic_meter.
        :type kilograms_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilograms_per_cubic_meter, DensityUnits.KilogramPerCubicMeter)

    
    @staticmethod
    def from_milligrams_per_cubic_meter(milligrams_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in milligrams_per_cubic_meter.

        

        :param meters: The Density value in milligrams_per_cubic_meter.
        :type milligrams_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milligrams_per_cubic_meter, DensityUnits.MilligramPerCubicMeter)

    
    @staticmethod
    def from_micrograms_per_cubic_meter(micrograms_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in micrograms_per_cubic_meter.

        

        :param meters: The Density value in micrograms_per_cubic_meter.
        :type micrograms_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micrograms_per_cubic_meter, DensityUnits.MicrogramPerCubicMeter)

    
    @staticmethod
    def from_kilopounds_per_cubic_inch(kilopounds_per_cubic_inch: float):
        """
        Create a new instance of Density from a value in kilopounds_per_cubic_inch.

        

        :param meters: The Density value in kilopounds_per_cubic_inch.
        :type kilopounds_per_cubic_inch: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilopounds_per_cubic_inch, DensityUnits.KilopoundPerCubicInch)

    
    @staticmethod
    def from_kilopounds_per_cubic_foot(kilopounds_per_cubic_foot: float):
        """
        Create a new instance of Density from a value in kilopounds_per_cubic_foot.

        

        :param meters: The Density value in kilopounds_per_cubic_foot.
        :type kilopounds_per_cubic_foot: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilopounds_per_cubic_foot, DensityUnits.KilopoundPerCubicFoot)

    
    @staticmethod
    def from_kilopounds_per_cubic_yard(kilopounds_per_cubic_yard: float):
        """
        Create a new instance of Density from a value in kilopounds_per_cubic_yard.

        

        :param meters: The Density value in kilopounds_per_cubic_yard.
        :type kilopounds_per_cubic_yard: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilopounds_per_cubic_yard, DensityUnits.KilopoundPerCubicYard)

    
    @staticmethod
    def from_femtograms_per_liter(femtograms_per_liter: float):
        """
        Create a new instance of Density from a value in femtograms_per_liter.

        

        :param meters: The Density value in femtograms_per_liter.
        :type femtograms_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(femtograms_per_liter, DensityUnits.FemtogramPerLiter)

    
    @staticmethod
    def from_picograms_per_liter(picograms_per_liter: float):
        """
        Create a new instance of Density from a value in picograms_per_liter.

        

        :param meters: The Density value in picograms_per_liter.
        :type picograms_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(picograms_per_liter, DensityUnits.PicogramPerLiter)

    
    @staticmethod
    def from_nanograms_per_liter(nanograms_per_liter: float):
        """
        Create a new instance of Density from a value in nanograms_per_liter.

        

        :param meters: The Density value in nanograms_per_liter.
        :type nanograms_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(nanograms_per_liter, DensityUnits.NanogramPerLiter)

    
    @staticmethod
    def from_micrograms_per_liter(micrograms_per_liter: float):
        """
        Create a new instance of Density from a value in micrograms_per_liter.

        

        :param meters: The Density value in micrograms_per_liter.
        :type micrograms_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micrograms_per_liter, DensityUnits.MicrogramPerLiter)

    
    @staticmethod
    def from_milligrams_per_liter(milligrams_per_liter: float):
        """
        Create a new instance of Density from a value in milligrams_per_liter.

        

        :param meters: The Density value in milligrams_per_liter.
        :type milligrams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milligrams_per_liter, DensityUnits.MilligramPerLiter)

    
    @staticmethod
    def from_centigrams_per_liter(centigrams_per_liter: float):
        """
        Create a new instance of Density from a value in centigrams_per_liter.

        

        :param meters: The Density value in centigrams_per_liter.
        :type centigrams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(centigrams_per_liter, DensityUnits.CentigramPerLiter)

    
    @staticmethod
    def from_decigrams_per_liter(decigrams_per_liter: float):
        """
        Create a new instance of Density from a value in decigrams_per_liter.

        

        :param meters: The Density value in decigrams_per_liter.
        :type decigrams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(decigrams_per_liter, DensityUnits.DecigramPerLiter)

    
    @staticmethod
    def from_femtograms_per_deci_liter(femtograms_per_deci_liter: float):
        """
        Create a new instance of Density from a value in femtograms_per_deci_liter.

        

        :param meters: The Density value in femtograms_per_deci_liter.
        :type femtograms_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(femtograms_per_deci_liter, DensityUnits.FemtogramPerDeciliter)

    
    @staticmethod
    def from_picograms_per_deci_liter(picograms_per_deci_liter: float):
        """
        Create a new instance of Density from a value in picograms_per_deci_liter.

        

        :param meters: The Density value in picograms_per_deci_liter.
        :type picograms_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(picograms_per_deci_liter, DensityUnits.PicogramPerDeciliter)

    
    @staticmethod
    def from_nanograms_per_deci_liter(nanograms_per_deci_liter: float):
        """
        Create a new instance of Density from a value in nanograms_per_deci_liter.

        

        :param meters: The Density value in nanograms_per_deci_liter.
        :type nanograms_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(nanograms_per_deci_liter, DensityUnits.NanogramPerDeciliter)

    
    @staticmethod
    def from_micrograms_per_deci_liter(micrograms_per_deci_liter: float):
        """
        Create a new instance of Density from a value in micrograms_per_deci_liter.

        

        :param meters: The Density value in micrograms_per_deci_liter.
        :type micrograms_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micrograms_per_deci_liter, DensityUnits.MicrogramPerDeciliter)

    
    @staticmethod
    def from_milligrams_per_deci_liter(milligrams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in milligrams_per_deci_liter.

        

        :param meters: The Density value in milligrams_per_deci_liter.
        :type milligrams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milligrams_per_deci_liter, DensityUnits.MilligramPerDeciliter)

    
    @staticmethod
    def from_centigrams_per_deci_liter(centigrams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in centigrams_per_deci_liter.

        

        :param meters: The Density value in centigrams_per_deci_liter.
        :type centigrams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(centigrams_per_deci_liter, DensityUnits.CentigramPerDeciliter)

    
    @staticmethod
    def from_decigrams_per_deci_liter(decigrams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in decigrams_per_deci_liter.

        

        :param meters: The Density value in decigrams_per_deci_liter.
        :type decigrams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(decigrams_per_deci_liter, DensityUnits.DecigramPerDeciliter)

    
    @staticmethod
    def from_femtograms_per_milliliter(femtograms_per_milliliter: float):
        """
        Create a new instance of Density from a value in femtograms_per_milliliter.

        

        :param meters: The Density value in femtograms_per_milliliter.
        :type femtograms_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(femtograms_per_milliliter, DensityUnits.FemtogramPerMilliliter)

    
    @staticmethod
    def from_picograms_per_milliliter(picograms_per_milliliter: float):
        """
        Create a new instance of Density from a value in picograms_per_milliliter.

        

        :param meters: The Density value in picograms_per_milliliter.
        :type picograms_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(picograms_per_milliliter, DensityUnits.PicogramPerMilliliter)

    
    @staticmethod
    def from_nanograms_per_milliliter(nanograms_per_milliliter: float):
        """
        Create a new instance of Density from a value in nanograms_per_milliliter.

        

        :param meters: The Density value in nanograms_per_milliliter.
        :type nanograms_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(nanograms_per_milliliter, DensityUnits.NanogramPerMilliliter)

    
    @staticmethod
    def from_micrograms_per_milliliter(micrograms_per_milliliter: float):
        """
        Create a new instance of Density from a value in micrograms_per_milliliter.

        

        :param meters: The Density value in micrograms_per_milliliter.
        :type micrograms_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micrograms_per_milliliter, DensityUnits.MicrogramPerMilliliter)

    
    @staticmethod
    def from_milligrams_per_milliliter(milligrams_per_milliliter: float):
        """
        Create a new instance of Density from a value in milligrams_per_milliliter.

        

        :param meters: The Density value in milligrams_per_milliliter.
        :type milligrams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milligrams_per_milliliter, DensityUnits.MilligramPerMilliliter)

    
    @staticmethod
    def from_centigrams_per_milliliter(centigrams_per_milliliter: float):
        """
        Create a new instance of Density from a value in centigrams_per_milliliter.

        

        :param meters: The Density value in centigrams_per_milliliter.
        :type centigrams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(centigrams_per_milliliter, DensityUnits.CentigramPerMilliliter)

    
    @staticmethod
    def from_decigrams_per_milliliter(decigrams_per_milliliter: float):
        """
        Create a new instance of Density from a value in decigrams_per_milliliter.

        

        :param meters: The Density value in decigrams_per_milliliter.
        :type decigrams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(decigrams_per_milliliter, DensityUnits.DecigramPerMilliliter)

    
    @property
    def grams_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_millimeter != None:
            return self.__grams_per_cubic_millimeter
        self.__grams_per_cubic_millimeter = self.__convert_from_base(DensityUnits.GramPerCubicMillimeter)
        return self.__grams_per_cubic_millimeter

    
    @property
    def grams_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_centimeter != None:
            return self.__grams_per_cubic_centimeter
        self.__grams_per_cubic_centimeter = self.__convert_from_base(DensityUnits.GramPerCubicCentimeter)
        return self.__grams_per_cubic_centimeter

    
    @property
    def grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_meter != None:
            return self.__grams_per_cubic_meter
        self.__grams_per_cubic_meter = self.__convert_from_base(DensityUnits.GramPerCubicMeter)
        return self.__grams_per_cubic_meter

    
    @property
    def pounds_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__pounds_per_cubic_inch != None:
            return self.__pounds_per_cubic_inch
        self.__pounds_per_cubic_inch = self.__convert_from_base(DensityUnits.PoundPerCubicInch)
        return self.__pounds_per_cubic_inch

    
    @property
    def pounds_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__pounds_per_cubic_foot != None:
            return self.__pounds_per_cubic_foot
        self.__pounds_per_cubic_foot = self.__convert_from_base(DensityUnits.PoundPerCubicFoot)
        return self.__pounds_per_cubic_foot

    
    @property
    def pounds_per_cubic_yard(self) -> float:
        """
        Calculated from the definition of <a href="https://en.wikipedia.org/wiki/Pound_(mass)">pound</a> and <a href="https://en.wikipedia.org/wiki/Yard">yard</a> compared to metric kilogram and meter.
        """
        if self.__pounds_per_cubic_yard != None:
            return self.__pounds_per_cubic_yard
        self.__pounds_per_cubic_yard = self.__convert_from_base(DensityUnits.PoundPerCubicYard)
        return self.__pounds_per_cubic_yard

    
    @property
    def tonnes_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_millimeter != None:
            return self.__tonnes_per_cubic_millimeter
        self.__tonnes_per_cubic_millimeter = self.__convert_from_base(DensityUnits.TonnePerCubicMillimeter)
        return self.__tonnes_per_cubic_millimeter

    
    @property
    def tonnes_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_centimeter != None:
            return self.__tonnes_per_cubic_centimeter
        self.__tonnes_per_cubic_centimeter = self.__convert_from_base(DensityUnits.TonnePerCubicCentimeter)
        return self.__tonnes_per_cubic_centimeter

    
    @property
    def tonnes_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_meter != None:
            return self.__tonnes_per_cubic_meter
        self.__tonnes_per_cubic_meter = self.__convert_from_base(DensityUnits.TonnePerCubicMeter)
        return self.__tonnes_per_cubic_meter

    
    @property
    def slugs_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__slugs_per_cubic_foot != None:
            return self.__slugs_per_cubic_foot
        self.__slugs_per_cubic_foot = self.__convert_from_base(DensityUnits.SlugPerCubicFoot)
        return self.__slugs_per_cubic_foot

    
    @property
    def grams_per_liter(self) -> float:
        """
        
        """
        if self.__grams_per_liter != None:
            return self.__grams_per_liter
        self.__grams_per_liter = self.__convert_from_base(DensityUnits.GramPerLiter)
        return self.__grams_per_liter

    
    @property
    def grams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__grams_per_deci_liter != None:
            return self.__grams_per_deci_liter
        self.__grams_per_deci_liter = self.__convert_from_base(DensityUnits.GramPerDeciliter)
        return self.__grams_per_deci_liter

    
    @property
    def grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__grams_per_milliliter != None:
            return self.__grams_per_milliliter
        self.__grams_per_milliliter = self.__convert_from_base(DensityUnits.GramPerMilliliter)
        return self.__grams_per_milliliter

    
    @property
    def pounds_per_us_gallon(self) -> float:
        """
        
        """
        if self.__pounds_per_us_gallon != None:
            return self.__pounds_per_us_gallon
        self.__pounds_per_us_gallon = self.__convert_from_base(DensityUnits.PoundPerUSGallon)
        return self.__pounds_per_us_gallon

    
    @property
    def pounds_per_imperial_gallon(self) -> float:
        """
        
        """
        if self.__pounds_per_imperial_gallon != None:
            return self.__pounds_per_imperial_gallon
        self.__pounds_per_imperial_gallon = self.__convert_from_base(DensityUnits.PoundPerImperialGallon)
        return self.__pounds_per_imperial_gallon

    
    @property
    def kilograms_per_liter(self) -> float:
        """
        
        """
        if self.__kilograms_per_liter != None:
            return self.__kilograms_per_liter
        self.__kilograms_per_liter = self.__convert_from_base(DensityUnits.KilogramPerLiter)
        return self.__kilograms_per_liter

    
    @property
    def tonnes_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_foot != None:
            return self.__tonnes_per_cubic_foot
        self.__tonnes_per_cubic_foot = self.__convert_from_base(DensityUnits.TonnePerCubicFoot)
        return self.__tonnes_per_cubic_foot

    
    @property
    def tonnes_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__tonnes_per_cubic_inch != None:
            return self.__tonnes_per_cubic_inch
        self.__tonnes_per_cubic_inch = self.__convert_from_base(DensityUnits.TonnePerCubicInch)
        return self.__tonnes_per_cubic_inch

    
    @property
    def grams_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_foot != None:
            return self.__grams_per_cubic_foot
        self.__grams_per_cubic_foot = self.__convert_from_base(DensityUnits.GramPerCubicFoot)
        return self.__grams_per_cubic_foot

    
    @property
    def grams_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__grams_per_cubic_inch != None:
            return self.__grams_per_cubic_inch
        self.__grams_per_cubic_inch = self.__convert_from_base(DensityUnits.GramPerCubicInch)
        return self.__grams_per_cubic_inch

    
    @property
    def pounds_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__pounds_per_cubic_meter != None:
            return self.__pounds_per_cubic_meter
        self.__pounds_per_cubic_meter = self.__convert_from_base(DensityUnits.PoundPerCubicMeter)
        return self.__pounds_per_cubic_meter

    
    @property
    def pounds_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__pounds_per_cubic_centimeter != None:
            return self.__pounds_per_cubic_centimeter
        self.__pounds_per_cubic_centimeter = self.__convert_from_base(DensityUnits.PoundPerCubicCentimeter)
        return self.__pounds_per_cubic_centimeter

    
    @property
    def pounds_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__pounds_per_cubic_millimeter != None:
            return self.__pounds_per_cubic_millimeter
        self.__pounds_per_cubic_millimeter = self.__convert_from_base(DensityUnits.PoundPerCubicMillimeter)
        return self.__pounds_per_cubic_millimeter

    
    @property
    def slugs_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__slugs_per_cubic_meter != None:
            return self.__slugs_per_cubic_meter
        self.__slugs_per_cubic_meter = self.__convert_from_base(DensityUnits.SlugPerCubicMeter)
        return self.__slugs_per_cubic_meter

    
    @property
    def slugs_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__slugs_per_cubic_centimeter != None:
            return self.__slugs_per_cubic_centimeter
        self.__slugs_per_cubic_centimeter = self.__convert_from_base(DensityUnits.SlugPerCubicCentimeter)
        return self.__slugs_per_cubic_centimeter

    
    @property
    def slugs_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__slugs_per_cubic_millimeter != None:
            return self.__slugs_per_cubic_millimeter
        self.__slugs_per_cubic_millimeter = self.__convert_from_base(DensityUnits.SlugPerCubicMillimeter)
        return self.__slugs_per_cubic_millimeter

    
    @property
    def slugs_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__slugs_per_cubic_inch != None:
            return self.__slugs_per_cubic_inch
        self.__slugs_per_cubic_inch = self.__convert_from_base(DensityUnits.SlugPerCubicInch)
        return self.__slugs_per_cubic_inch

    
    @property
    def kilograms_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_cubic_millimeter != None:
            return self.__kilograms_per_cubic_millimeter
        self.__kilograms_per_cubic_millimeter = self.__convert_from_base(DensityUnits.KilogramPerCubicMillimeter)
        return self.__kilograms_per_cubic_millimeter

    
    @property
    def kilograms_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__kilograms_per_cubic_centimeter != None:
            return self.__kilograms_per_cubic_centimeter
        self.__kilograms_per_cubic_centimeter = self.__convert_from_base(DensityUnits.KilogramPerCubicCentimeter)
        return self.__kilograms_per_cubic_centimeter

    
    @property
    def kilograms_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilograms_per_cubic_meter != None:
            return self.__kilograms_per_cubic_meter
        self.__kilograms_per_cubic_meter = self.__convert_from_base(DensityUnits.KilogramPerCubicMeter)
        return self.__kilograms_per_cubic_meter

    
    @property
    def milligrams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__milligrams_per_cubic_meter != None:
            return self.__milligrams_per_cubic_meter
        self.__milligrams_per_cubic_meter = self.__convert_from_base(DensityUnits.MilligramPerCubicMeter)
        return self.__milligrams_per_cubic_meter

    
    @property
    def micrograms_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__micrograms_per_cubic_meter != None:
            return self.__micrograms_per_cubic_meter
        self.__micrograms_per_cubic_meter = self.__convert_from_base(DensityUnits.MicrogramPerCubicMeter)
        return self.__micrograms_per_cubic_meter

    
    @property
    def kilopounds_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilopounds_per_cubic_inch != None:
            return self.__kilopounds_per_cubic_inch
        self.__kilopounds_per_cubic_inch = self.__convert_from_base(DensityUnits.KilopoundPerCubicInch)
        return self.__kilopounds_per_cubic_inch

    
    @property
    def kilopounds_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilopounds_per_cubic_foot != None:
            return self.__kilopounds_per_cubic_foot
        self.__kilopounds_per_cubic_foot = self.__convert_from_base(DensityUnits.KilopoundPerCubicFoot)
        return self.__kilopounds_per_cubic_foot

    
    @property
    def kilopounds_per_cubic_yard(self) -> float:
        """
        
        """
        if self.__kilopounds_per_cubic_yard != None:
            return self.__kilopounds_per_cubic_yard
        self.__kilopounds_per_cubic_yard = self.__convert_from_base(DensityUnits.KilopoundPerCubicYard)
        return self.__kilopounds_per_cubic_yard

    
    @property
    def femtograms_per_liter(self) -> float:
        """
        
        """
        if self.__femtograms_per_liter != None:
            return self.__femtograms_per_liter
        self.__femtograms_per_liter = self.__convert_from_base(DensityUnits.FemtogramPerLiter)
        return self.__femtograms_per_liter

    
    @property
    def picograms_per_liter(self) -> float:
        """
        
        """
        if self.__picograms_per_liter != None:
            return self.__picograms_per_liter
        self.__picograms_per_liter = self.__convert_from_base(DensityUnits.PicogramPerLiter)
        return self.__picograms_per_liter

    
    @property
    def nanograms_per_liter(self) -> float:
        """
        
        """
        if self.__nanograms_per_liter != None:
            return self.__nanograms_per_liter
        self.__nanograms_per_liter = self.__convert_from_base(DensityUnits.NanogramPerLiter)
        return self.__nanograms_per_liter

    
    @property
    def micrograms_per_liter(self) -> float:
        """
        
        """
        if self.__micrograms_per_liter != None:
            return self.__micrograms_per_liter
        self.__micrograms_per_liter = self.__convert_from_base(DensityUnits.MicrogramPerLiter)
        return self.__micrograms_per_liter

    
    @property
    def milligrams_per_liter(self) -> float:
        """
        
        """
        if self.__milligrams_per_liter != None:
            return self.__milligrams_per_liter
        self.__milligrams_per_liter = self.__convert_from_base(DensityUnits.MilligramPerLiter)
        return self.__milligrams_per_liter

    
    @property
    def centigrams_per_liter(self) -> float:
        """
        
        """
        if self.__centigrams_per_liter != None:
            return self.__centigrams_per_liter
        self.__centigrams_per_liter = self.__convert_from_base(DensityUnits.CentigramPerLiter)
        return self.__centigrams_per_liter

    
    @property
    def decigrams_per_liter(self) -> float:
        """
        
        """
        if self.__decigrams_per_liter != None:
            return self.__decigrams_per_liter
        self.__decigrams_per_liter = self.__convert_from_base(DensityUnits.DecigramPerLiter)
        return self.__decigrams_per_liter

    
    @property
    def femtograms_per_deci_liter(self) -> float:
        """
        
        """
        if self.__femtograms_per_deci_liter != None:
            return self.__femtograms_per_deci_liter
        self.__femtograms_per_deci_liter = self.__convert_from_base(DensityUnits.FemtogramPerDeciliter)
        return self.__femtograms_per_deci_liter

    
    @property
    def picograms_per_deci_liter(self) -> float:
        """
        
        """
        if self.__picograms_per_deci_liter != None:
            return self.__picograms_per_deci_liter
        self.__picograms_per_deci_liter = self.__convert_from_base(DensityUnits.PicogramPerDeciliter)
        return self.__picograms_per_deci_liter

    
    @property
    def nanograms_per_deci_liter(self) -> float:
        """
        
        """
        if self.__nanograms_per_deci_liter != None:
            return self.__nanograms_per_deci_liter
        self.__nanograms_per_deci_liter = self.__convert_from_base(DensityUnits.NanogramPerDeciliter)
        return self.__nanograms_per_deci_liter

    
    @property
    def micrograms_per_deci_liter(self) -> float:
        """
        
        """
        if self.__micrograms_per_deci_liter != None:
            return self.__micrograms_per_deci_liter
        self.__micrograms_per_deci_liter = self.__convert_from_base(DensityUnits.MicrogramPerDeciliter)
        return self.__micrograms_per_deci_liter

    
    @property
    def milligrams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__milligrams_per_deci_liter != None:
            return self.__milligrams_per_deci_liter
        self.__milligrams_per_deci_liter = self.__convert_from_base(DensityUnits.MilligramPerDeciliter)
        return self.__milligrams_per_deci_liter

    
    @property
    def centigrams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__centigrams_per_deci_liter != None:
            return self.__centigrams_per_deci_liter
        self.__centigrams_per_deci_liter = self.__convert_from_base(DensityUnits.CentigramPerDeciliter)
        return self.__centigrams_per_deci_liter

    
    @property
    def decigrams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__decigrams_per_deci_liter != None:
            return self.__decigrams_per_deci_liter
        self.__decigrams_per_deci_liter = self.__convert_from_base(DensityUnits.DecigramPerDeciliter)
        return self.__decigrams_per_deci_liter

    
    @property
    def femtograms_per_milliliter(self) -> float:
        """
        
        """
        if self.__femtograms_per_milliliter != None:
            return self.__femtograms_per_milliliter
        self.__femtograms_per_milliliter = self.__convert_from_base(DensityUnits.FemtogramPerMilliliter)
        return self.__femtograms_per_milliliter

    
    @property
    def picograms_per_milliliter(self) -> float:
        """
        
        """
        if self.__picograms_per_milliliter != None:
            return self.__picograms_per_milliliter
        self.__picograms_per_milliliter = self.__convert_from_base(DensityUnits.PicogramPerMilliliter)
        return self.__picograms_per_milliliter

    
    @property
    def nanograms_per_milliliter(self) -> float:
        """
        
        """
        if self.__nanograms_per_milliliter != None:
            return self.__nanograms_per_milliliter
        self.__nanograms_per_milliliter = self.__convert_from_base(DensityUnits.NanogramPerMilliliter)
        return self.__nanograms_per_milliliter

    
    @property
    def micrograms_per_milliliter(self) -> float:
        """
        
        """
        if self.__micrograms_per_milliliter != None:
            return self.__micrograms_per_milliliter
        self.__micrograms_per_milliliter = self.__convert_from_base(DensityUnits.MicrogramPerMilliliter)
        return self.__micrograms_per_milliliter

    
    @property
    def milligrams_per_milliliter(self) -> float:
        """
        
        """
        if self.__milligrams_per_milliliter != None:
            return self.__milligrams_per_milliliter
        self.__milligrams_per_milliliter = self.__convert_from_base(DensityUnits.MilligramPerMilliliter)
        return self.__milligrams_per_milliliter

    
    @property
    def centigrams_per_milliliter(self) -> float:
        """
        
        """
        if self.__centigrams_per_milliliter != None:
            return self.__centigrams_per_milliliter
        self.__centigrams_per_milliliter = self.__convert_from_base(DensityUnits.CentigramPerMilliliter)
        return self.__centigrams_per_milliliter

    
    @property
    def decigrams_per_milliliter(self) -> float:
        """
        
        """
        if self.__decigrams_per_milliliter != None:
            return self.__decigrams_per_milliliter
        self.__decigrams_per_milliliter = self.__convert_from_base(DensityUnits.DecigramPerMilliliter)
        return self.__decigrams_per_milliliter

    
    def to_string(self, unit: DensityUnits = DensityUnits.KilogramPerCubicMeter, fractional_digits: int = None) -> str:
        """
        Format the Density to a string.
        
        Note: the default format for Density is KilogramPerCubicMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Density. Default is 'KilogramPerCubicMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == DensityUnits.GramPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_millimeter, fractional_digits)} g/mm³"""
        
        if unit == DensityUnits.GramPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_centimeter, fractional_digits)} g/cm³"""
        
        if unit == DensityUnits.GramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_meter, fractional_digits)} g/m³"""
        
        if unit == DensityUnits.PoundPerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_inch, fractional_digits)} lb/in³"""
        
        if unit == DensityUnits.PoundPerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_foot, fractional_digits)} lb/ft³"""
        
        if unit == DensityUnits.PoundPerCubicYard:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_yard, fractional_digits)} lb/yd³"""
        
        if unit == DensityUnits.TonnePerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_millimeter, fractional_digits)} t/mm³"""
        
        if unit == DensityUnits.TonnePerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_centimeter, fractional_digits)} t/cm³"""
        
        if unit == DensityUnits.TonnePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_meter, fractional_digits)} t/m³"""
        
        if unit == DensityUnits.SlugPerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.slugs_per_cubic_foot, fractional_digits)} slug/ft³"""
        
        if unit == DensityUnits.GramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_liter, fractional_digits)} g/L"""
        
        if unit == DensityUnits.GramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_deci_liter, fractional_digits)} g/dl"""
        
        if unit == DensityUnits.GramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.grams_per_milliliter, fractional_digits)} g/ml"""
        
        if unit == DensityUnits.PoundPerUSGallon:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_us_gallon, fractional_digits)} ppg (U.S.)"""
        
        if unit == DensityUnits.PoundPerImperialGallon:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_imperial_gallon, fractional_digits)} ppg (imp.)"""
        
        if unit == DensityUnits.KilogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_liter, fractional_digits)} kg/l"""
        
        if unit == DensityUnits.TonnePerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_foot, fractional_digits)} t/ft³"""
        
        if unit == DensityUnits.TonnePerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.tonnes_per_cubic_inch, fractional_digits)} t/in³"""
        
        if unit == DensityUnits.GramPerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_foot, fractional_digits)} g/ft³"""
        
        if unit == DensityUnits.GramPerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.grams_per_cubic_inch, fractional_digits)} g/in³"""
        
        if unit == DensityUnits.PoundPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_meter, fractional_digits)} lb/m³"""
        
        if unit == DensityUnits.PoundPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_centimeter, fractional_digits)} lb/cm³"""
        
        if unit == DensityUnits.PoundPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.pounds_per_cubic_millimeter, fractional_digits)} lb/mm³"""
        
        if unit == DensityUnits.SlugPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.slugs_per_cubic_meter, fractional_digits)} slug/m³"""
        
        if unit == DensityUnits.SlugPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.slugs_per_cubic_centimeter, fractional_digits)} slug/cm³"""
        
        if unit == DensityUnits.SlugPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.slugs_per_cubic_millimeter, fractional_digits)} slug/mm³"""
        
        if unit == DensityUnits.SlugPerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.slugs_per_cubic_inch, fractional_digits)} slug/in³"""
        
        if unit == DensityUnits.KilogramPerCubicMillimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_cubic_millimeter, fractional_digits)} kg/mm³"""
        
        if unit == DensityUnits.KilogramPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_cubic_centimeter, fractional_digits)} kg/cm³"""
        
        if unit == DensityUnits.KilogramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.kilograms_per_cubic_meter, fractional_digits)} kg/m³"""
        
        if unit == DensityUnits.MilligramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_cubic_meter, fractional_digits)} mg/m³"""
        
        if unit == DensityUnits.MicrogramPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_cubic_meter, fractional_digits)} μg/m³"""
        
        if unit == DensityUnits.KilopoundPerCubicInch:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_per_cubic_inch, fractional_digits)} klb/in³"""
        
        if unit == DensityUnits.KilopoundPerCubicFoot:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_per_cubic_foot, fractional_digits)} klb/ft³"""
        
        if unit == DensityUnits.KilopoundPerCubicYard:
            return f"""{super()._truncate_fraction_digits(self.kilopounds_per_cubic_yard, fractional_digits)} klb/yd³"""
        
        if unit == DensityUnits.FemtogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.femtograms_per_liter, fractional_digits)} fg/L"""
        
        if unit == DensityUnits.PicogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.picograms_per_liter, fractional_digits)} pg/L"""
        
        if unit == DensityUnits.NanogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_liter, fractional_digits)} ng/L"""
        
        if unit == DensityUnits.MicrogramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_liter, fractional_digits)} μg/L"""
        
        if unit == DensityUnits.MilligramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_liter, fractional_digits)} mg/L"""
        
        if unit == DensityUnits.CentigramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_liter, fractional_digits)} cg/L"""
        
        if unit == DensityUnits.DecigramPerLiter:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_liter, fractional_digits)} dg/L"""
        
        if unit == DensityUnits.FemtogramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.femtograms_per_deci_liter, fractional_digits)} fg/dl"""
        
        if unit == DensityUnits.PicogramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.picograms_per_deci_liter, fractional_digits)} pg/dl"""
        
        if unit == DensityUnits.NanogramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_deci_liter, fractional_digits)} ng/dl"""
        
        if unit == DensityUnits.MicrogramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_deci_liter, fractional_digits)} μg/dl"""
        
        if unit == DensityUnits.MilligramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_deci_liter, fractional_digits)} mg/dl"""
        
        if unit == DensityUnits.CentigramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_deci_liter, fractional_digits)} cg/dl"""
        
        if unit == DensityUnits.DecigramPerDeciliter:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_deci_liter, fractional_digits)} dg/dl"""
        
        if unit == DensityUnits.FemtogramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.femtograms_per_milliliter, fractional_digits)} fg/ml"""
        
        if unit == DensityUnits.PicogramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.picograms_per_milliliter, fractional_digits)} pg/ml"""
        
        if unit == DensityUnits.NanogramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.nanograms_per_milliliter, fractional_digits)} ng/ml"""
        
        if unit == DensityUnits.MicrogramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.micrograms_per_milliliter, fractional_digits)} μg/ml"""
        
        if unit == DensityUnits.MilligramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.milligrams_per_milliliter, fractional_digits)} mg/ml"""
        
        if unit == DensityUnits.CentigramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.centigrams_per_milliliter, fractional_digits)} cg/ml"""
        
        if unit == DensityUnits.DecigramPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.decigrams_per_milliliter, fractional_digits)} dg/ml"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: DensityUnits = DensityUnits.KilogramPerCubicMeter) -> str:
        """
        Get Density unit abbreviation.
        Note! the default abbreviation for Density is KilogramPerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == DensityUnits.GramPerCubicMillimeter:
            return """g/mm³"""
        
        if unit_abbreviation == DensityUnits.GramPerCubicCentimeter:
            return """g/cm³"""
        
        if unit_abbreviation == DensityUnits.GramPerCubicMeter:
            return """g/m³"""
        
        if unit_abbreviation == DensityUnits.PoundPerCubicInch:
            return """lb/in³"""
        
        if unit_abbreviation == DensityUnits.PoundPerCubicFoot:
            return """lb/ft³"""
        
        if unit_abbreviation == DensityUnits.PoundPerCubicYard:
            return """lb/yd³"""
        
        if unit_abbreviation == DensityUnits.TonnePerCubicMillimeter:
            return """t/mm³"""
        
        if unit_abbreviation == DensityUnits.TonnePerCubicCentimeter:
            return """t/cm³"""
        
        if unit_abbreviation == DensityUnits.TonnePerCubicMeter:
            return """t/m³"""
        
        if unit_abbreviation == DensityUnits.SlugPerCubicFoot:
            return """slug/ft³"""
        
        if unit_abbreviation == DensityUnits.GramPerLiter:
            return """g/L"""
        
        if unit_abbreviation == DensityUnits.GramPerDeciliter:
            return """g/dl"""
        
        if unit_abbreviation == DensityUnits.GramPerMilliliter:
            return """g/ml"""
        
        if unit_abbreviation == DensityUnits.PoundPerUSGallon:
            return """ppg (U.S.)"""
        
        if unit_abbreviation == DensityUnits.PoundPerImperialGallon:
            return """ppg (imp.)"""
        
        if unit_abbreviation == DensityUnits.KilogramPerLiter:
            return """kg/l"""
        
        if unit_abbreviation == DensityUnits.TonnePerCubicFoot:
            return """t/ft³"""
        
        if unit_abbreviation == DensityUnits.TonnePerCubicInch:
            return """t/in³"""
        
        if unit_abbreviation == DensityUnits.GramPerCubicFoot:
            return """g/ft³"""
        
        if unit_abbreviation == DensityUnits.GramPerCubicInch:
            return """g/in³"""
        
        if unit_abbreviation == DensityUnits.PoundPerCubicMeter:
            return """lb/m³"""
        
        if unit_abbreviation == DensityUnits.PoundPerCubicCentimeter:
            return """lb/cm³"""
        
        if unit_abbreviation == DensityUnits.PoundPerCubicMillimeter:
            return """lb/mm³"""
        
        if unit_abbreviation == DensityUnits.SlugPerCubicMeter:
            return """slug/m³"""
        
        if unit_abbreviation == DensityUnits.SlugPerCubicCentimeter:
            return """slug/cm³"""
        
        if unit_abbreviation == DensityUnits.SlugPerCubicMillimeter:
            return """slug/mm³"""
        
        if unit_abbreviation == DensityUnits.SlugPerCubicInch:
            return """slug/in³"""
        
        if unit_abbreviation == DensityUnits.KilogramPerCubicMillimeter:
            return """kg/mm³"""
        
        if unit_abbreviation == DensityUnits.KilogramPerCubicCentimeter:
            return """kg/cm³"""
        
        if unit_abbreviation == DensityUnits.KilogramPerCubicMeter:
            return """kg/m³"""
        
        if unit_abbreviation == DensityUnits.MilligramPerCubicMeter:
            return """mg/m³"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerCubicMeter:
            return """μg/m³"""
        
        if unit_abbreviation == DensityUnits.KilopoundPerCubicInch:
            return """klb/in³"""
        
        if unit_abbreviation == DensityUnits.KilopoundPerCubicFoot:
            return """klb/ft³"""
        
        if unit_abbreviation == DensityUnits.KilopoundPerCubicYard:
            return """klb/yd³"""
        
        if unit_abbreviation == DensityUnits.FemtogramPerLiter:
            return """fg/L"""
        
        if unit_abbreviation == DensityUnits.PicogramPerLiter:
            return """pg/L"""
        
        if unit_abbreviation == DensityUnits.NanogramPerLiter:
            return """ng/L"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerLiter:
            return """μg/L"""
        
        if unit_abbreviation == DensityUnits.MilligramPerLiter:
            return """mg/L"""
        
        if unit_abbreviation == DensityUnits.CentigramPerLiter:
            return """cg/L"""
        
        if unit_abbreviation == DensityUnits.DecigramPerLiter:
            return """dg/L"""
        
        if unit_abbreviation == DensityUnits.FemtogramPerDeciliter:
            return """fg/dl"""
        
        if unit_abbreviation == DensityUnits.PicogramPerDeciliter:
            return """pg/dl"""
        
        if unit_abbreviation == DensityUnits.NanogramPerDeciliter:
            return """ng/dl"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerDeciliter:
            return """μg/dl"""
        
        if unit_abbreviation == DensityUnits.MilligramPerDeciliter:
            return """mg/dl"""
        
        if unit_abbreviation == DensityUnits.CentigramPerDeciliter:
            return """cg/dl"""
        
        if unit_abbreviation == DensityUnits.DecigramPerDeciliter:
            return """dg/dl"""
        
        if unit_abbreviation == DensityUnits.FemtogramPerMilliliter:
            return """fg/ml"""
        
        if unit_abbreviation == DensityUnits.PicogramPerMilliliter:
            return """pg/ml"""
        
        if unit_abbreviation == DensityUnits.NanogramPerMilliliter:
            return """ng/ml"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerMilliliter:
            return """μg/ml"""
        
        if unit_abbreviation == DensityUnits.MilligramPerMilliliter:
            return """mg/ml"""
        
        if unit_abbreviation == DensityUnits.CentigramPerMilliliter:
            return """cg/ml"""
        
        if unit_abbreviation == DensityUnits.DecigramPerMilliliter:
            return """dg/ml"""
        