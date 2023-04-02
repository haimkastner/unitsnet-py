from enum import Enum
import math
import string


class DensityUnits(Enum):
        """
            DensityUnits enumeration
        """
        
        GramPerCubicMillimeter = 'gram_per_cubic_millimeter'
        """
            
        """
        
        GramPerCubicCentimeter = 'gram_per_cubic_centimeter'
        """
            
        """
        
        GramPerCubicMeter = 'gram_per_cubic_meter'
        """
            
        """
        
        PoundPerCubicInch = 'pound_per_cubic_inch'
        """
            
        """
        
        PoundPerCubicFoot = 'pound_per_cubic_foot'
        """
            
        """
        
        TonnePerCubicMillimeter = 'tonne_per_cubic_millimeter'
        """
            
        """
        
        TonnePerCubicCentimeter = 'tonne_per_cubic_centimeter'
        """
            
        """
        
        TonnePerCubicMeter = 'tonne_per_cubic_meter'
        """
            
        """
        
        SlugPerCubicFoot = 'slug_per_cubic_foot'
        """
            
        """
        
        GramPerLiter = 'gram_per_liter'
        """
            
        """
        
        GramPerDeciliter = 'gram_per_deciliter'
        """
            
        """
        
        GramPerMilliliter = 'gram_per_milliliter'
        """
            
        """
        
        PoundPerUSGallon = 'pound_per_us_gallon'
        """
            
        """
        
        PoundPerImperialGallon = 'pound_per_imperial_gallon'
        """
            
        """
        
        KilogramPerLiter = 'kilogram_per_liter'
        """
            
        """
        
        TonnePerCubicFoot = 'tonne_per_cubic_foot'
        """
            
        """
        
        TonnePerCubicInch = 'tonne_per_cubic_inch'
        """
            
        """
        
        GramPerCubicFoot = 'gram_per_cubic_foot'
        """
            
        """
        
        GramPerCubicInch = 'gram_per_cubic_inch'
        """
            
        """
        
        PoundPerCubicMeter = 'pound_per_cubic_meter'
        """
            
        """
        
        PoundPerCubicCentimeter = 'pound_per_cubic_centimeter'
        """
            
        """
        
        PoundPerCubicMillimeter = 'pound_per_cubic_millimeter'
        """
            
        """
        
        SlugPerCubicMeter = 'slug_per_cubic_meter'
        """
            
        """
        
        SlugPerCubicCentimeter = 'slug_per_cubic_centimeter'
        """
            
        """
        
        SlugPerCubicMillimeter = 'slug_per_cubic_millimeter'
        """
            
        """
        
        SlugPerCubicInch = 'slug_per_cubic_inch'
        """
            
        """
        
        KilogramPerCubicMillimeter = 'kilogram_per_cubic_millimeter'
        """
            
        """
        
        KilogramPerCubicCentimeter = 'kilogram_per_cubic_centimeter'
        """
            
        """
        
        KilogramPerCubicMeter = 'kilogram_per_cubic_meter'
        """
            
        """
        
        MilligramPerCubicMeter = 'milligram_per_cubic_meter'
        """
            
        """
        
        MicrogramPerCubicMeter = 'microgram_per_cubic_meter'
        """
            
        """
        
        KilopoundPerCubicInch = 'kilopound_per_cubic_inch'
        """
            
        """
        
        KilopoundPerCubicFoot = 'kilopound_per_cubic_foot'
        """
            
        """
        
        PicogramPerLiter = 'picogram_per_liter'
        """
            
        """
        
        NanogramPerLiter = 'nanogram_per_liter'
        """
            
        """
        
        MicrogramPerLiter = 'microgram_per_liter'
        """
            
        """
        
        MilligramPerLiter = 'milligram_per_liter'
        """
            
        """
        
        CentigramPerLiter = 'centigram_per_liter'
        """
            
        """
        
        DecigramPerLiter = 'decigram_per_liter'
        """
            
        """
        
        PicogramPerDeciliter = 'picogram_per_deciliter'
        """
            
        """
        
        NanogramPerDeciliter = 'nanogram_per_deciliter'
        """
            
        """
        
        MicrogramPerDeciliter = 'microgram_per_deciliter'
        """
            
        """
        
        MilligramPerDeciliter = 'milligram_per_deciliter'
        """
            
        """
        
        CentigramPerDeciliter = 'centigram_per_deciliter'
        """
            
        """
        
        DecigramPerDeciliter = 'decigram_per_deciliter'
        """
            
        """
        
        PicogramPerMilliliter = 'picogram_per_milliliter'
        """
            
        """
        
        NanogramPerMilliliter = 'nanogram_per_milliliter'
        """
            
        """
        
        MicrogramPerMilliliter = 'microgram_per_milliliter'
        """
            
        """
        
        MilligramPerMilliliter = 'milligram_per_milliliter'
        """
            
        """
        
        CentigramPerMilliliter = 'centigram_per_milliliter'
        """
            
        """
        
        DecigramPerMilliliter = 'decigram_per_milliliter'
        """
            
        """
        

class Density:
    """
    The density, or more precisely, the volumetric mass density, of a substance is its mass per unit volume.

    Args:
        value (float): The value.
        from_unit (DensityUnits): The Density unit to create from, The default unit is KilogramPerCubicMeter
    """
    def __init__(self, value: float, from_unit: DensityUnits = DensityUnits.KilogramPerCubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_cubic_millimeter = None
        
        self.__grams_per_cubic_centimeter = None
        
        self.__grams_per_cubic_meter = None
        
        self.__pounds_per_cubic_inch = None
        
        self.__pounds_per_cubic_foot = None
        
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
        
        self.__picograms_per_liter = None
        
        self.__nanograms_per_liter = None
        
        self.__micrograms_per_liter = None
        
        self.__milligrams_per_liter = None
        
        self.__centigrams_per_liter = None
        
        self.__decigrams_per_liter = None
        
        self.__picograms_per_deci_liter = None
        
        self.__nanograms_per_deci_liter = None
        
        self.__micrograms_per_deci_liter = None
        
        self.__milligrams_per_deci_liter = None
        
        self.__centigrams_per_deci_liter = None
        
        self.__decigrams_per_deci_liter = None
        
        self.__picograms_per_milliliter = None
        
        self.__nanograms_per_milliliter = None
        
        self.__micrograms_per_milliliter = None
        
        self.__milligrams_per_milliliter = None
        
        self.__centigrams_per_milliliter = None
        
        self.__decigrams_per_milliliter = None
        

    def __convert_from_base(self, from_unit: DensityUnits) -> float:
        value = self.__value
        
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
        return self.__value

    
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

    
    def to_string(self, unit: DensityUnits = DensityUnits.KilogramPerCubicMeter) -> string:
        """
        Format the Density to string.
        Note! the default format for Density is KilogramPerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == DensityUnits.GramPerCubicMillimeter:
            return f"""{self.grams_per_cubic_millimeter} g/mm³"""
        
        if unit == DensityUnits.GramPerCubicCentimeter:
            return f"""{self.grams_per_cubic_centimeter} g/cm³"""
        
        if unit == DensityUnits.GramPerCubicMeter:
            return f"""{self.grams_per_cubic_meter} g/m³"""
        
        if unit == DensityUnits.PoundPerCubicInch:
            return f"""{self.pounds_per_cubic_inch} lb/in³"""
        
        if unit == DensityUnits.PoundPerCubicFoot:
            return f"""{self.pounds_per_cubic_foot} lb/ft³"""
        
        if unit == DensityUnits.TonnePerCubicMillimeter:
            return f"""{self.tonnes_per_cubic_millimeter} t/mm³"""
        
        if unit == DensityUnits.TonnePerCubicCentimeter:
            return f"""{self.tonnes_per_cubic_centimeter} t/cm³"""
        
        if unit == DensityUnits.TonnePerCubicMeter:
            return f"""{self.tonnes_per_cubic_meter} t/m³"""
        
        if unit == DensityUnits.SlugPerCubicFoot:
            return f"""{self.slugs_per_cubic_foot} slug/ft³"""
        
        if unit == DensityUnits.GramPerLiter:
            return f"""{self.grams_per_liter} g/L"""
        
        if unit == DensityUnits.GramPerDeciliter:
            return f"""{self.grams_per_deci_liter} g/dl"""
        
        if unit == DensityUnits.GramPerMilliliter:
            return f"""{self.grams_per_milliliter} g/ml"""
        
        if unit == DensityUnits.PoundPerUSGallon:
            return f"""{self.pounds_per_us_gallon} ppg (U.S.)"""
        
        if unit == DensityUnits.PoundPerImperialGallon:
            return f"""{self.pounds_per_imperial_gallon} ppg (imp.)"""
        
        if unit == DensityUnits.KilogramPerLiter:
            return f"""{self.kilograms_per_liter} kg/l"""
        
        if unit == DensityUnits.TonnePerCubicFoot:
            return f"""{self.tonnes_per_cubic_foot} t/ft³"""
        
        if unit == DensityUnits.TonnePerCubicInch:
            return f"""{self.tonnes_per_cubic_inch} t/in³"""
        
        if unit == DensityUnits.GramPerCubicFoot:
            return f"""{self.grams_per_cubic_foot} g/ft³"""
        
        if unit == DensityUnits.GramPerCubicInch:
            return f"""{self.grams_per_cubic_inch} g/in³"""
        
        if unit == DensityUnits.PoundPerCubicMeter:
            return f"""{self.pounds_per_cubic_meter} lb/m³"""
        
        if unit == DensityUnits.PoundPerCubicCentimeter:
            return f"""{self.pounds_per_cubic_centimeter} lb/cm³"""
        
        if unit == DensityUnits.PoundPerCubicMillimeter:
            return f"""{self.pounds_per_cubic_millimeter} lb/mm³"""
        
        if unit == DensityUnits.SlugPerCubicMeter:
            return f"""{self.slugs_per_cubic_meter} slug/m³"""
        
        if unit == DensityUnits.SlugPerCubicCentimeter:
            return f"""{self.slugs_per_cubic_centimeter} slug/cm³"""
        
        if unit == DensityUnits.SlugPerCubicMillimeter:
            return f"""{self.slugs_per_cubic_millimeter} slug/mm³"""
        
        if unit == DensityUnits.SlugPerCubicInch:
            return f"""{self.slugs_per_cubic_inch} slug/in³"""
        
        if unit == DensityUnits.KilogramPerCubicMillimeter:
            return f"""{self.kilograms_per_cubic_millimeter} """
        
        if unit == DensityUnits.KilogramPerCubicCentimeter:
            return f"""{self.kilograms_per_cubic_centimeter} """
        
        if unit == DensityUnits.KilogramPerCubicMeter:
            return f"""{self.kilograms_per_cubic_meter} """
        
        if unit == DensityUnits.MilligramPerCubicMeter:
            return f"""{self.milligrams_per_cubic_meter} """
        
        if unit == DensityUnits.MicrogramPerCubicMeter:
            return f"""{self.micrograms_per_cubic_meter} """
        
        if unit == DensityUnits.KilopoundPerCubicInch:
            return f"""{self.kilopounds_per_cubic_inch} """
        
        if unit == DensityUnits.KilopoundPerCubicFoot:
            return f"""{self.kilopounds_per_cubic_foot} """
        
        if unit == DensityUnits.PicogramPerLiter:
            return f"""{self.picograms_per_liter} """
        
        if unit == DensityUnits.NanogramPerLiter:
            return f"""{self.nanograms_per_liter} """
        
        if unit == DensityUnits.MicrogramPerLiter:
            return f"""{self.micrograms_per_liter} """
        
        if unit == DensityUnits.MilligramPerLiter:
            return f"""{self.milligrams_per_liter} """
        
        if unit == DensityUnits.CentigramPerLiter:
            return f"""{self.centigrams_per_liter} """
        
        if unit == DensityUnits.DecigramPerLiter:
            return f"""{self.decigrams_per_liter} """
        
        if unit == DensityUnits.PicogramPerDeciliter:
            return f"""{self.picograms_per_deci_liter} """
        
        if unit == DensityUnits.NanogramPerDeciliter:
            return f"""{self.nanograms_per_deci_liter} """
        
        if unit == DensityUnits.MicrogramPerDeciliter:
            return f"""{self.micrograms_per_deci_liter} """
        
        if unit == DensityUnits.MilligramPerDeciliter:
            return f"""{self.milligrams_per_deci_liter} """
        
        if unit == DensityUnits.CentigramPerDeciliter:
            return f"""{self.centigrams_per_deci_liter} """
        
        if unit == DensityUnits.DecigramPerDeciliter:
            return f"""{self.decigrams_per_deci_liter} """
        
        if unit == DensityUnits.PicogramPerMilliliter:
            return f"""{self.picograms_per_milliliter} """
        
        if unit == DensityUnits.NanogramPerMilliliter:
            return f"""{self.nanograms_per_milliliter} """
        
        if unit == DensityUnits.MicrogramPerMilliliter:
            return f"""{self.micrograms_per_milliliter} """
        
        if unit == DensityUnits.MilligramPerMilliliter:
            return f"""{self.milligrams_per_milliliter} """
        
        if unit == DensityUnits.CentigramPerMilliliter:
            return f"""{self.centigrams_per_milliliter} """
        
        if unit == DensityUnits.DecigramPerMilliliter:
            return f"""{self.decigrams_per_milliliter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: DensityUnits = DensityUnits.KilogramPerCubicMeter) -> string:
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
            return """"""
        
        if unit_abbreviation == DensityUnits.KilogramPerCubicCentimeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.KilogramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilligramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.KilopoundPerCubicInch:
            return """"""
        
        if unit_abbreviation == DensityUnits.KilopoundPerCubicFoot:
            return """"""
        
        if unit_abbreviation == DensityUnits.PicogramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.NanogramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilligramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.CentigramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.DecigramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.PicogramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.NanogramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilligramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.CentigramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.DecigramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.PicogramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.NanogramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicrogramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilligramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.CentigramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.DecigramPerMilliliter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for +: 'Density' and '{}'".format(type(other).__name__))
        return Density(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for *: 'Density' and '{}'".format(type(other).__name__))
        return Density(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for -: 'Density' and '{}'".format(type(other).__name__))
        return Density(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for /: 'Density' and '{}'".format(type(other).__name__))
        return Density(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for %: 'Density' and '{}'".format(type(other).__name__))
        return Density(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for **: 'Density' and '{}'".format(type(other).__name__))
        return Density(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for ==: 'Density' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for <: 'Density' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for >: 'Density' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for <=: 'Density' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Density):
            raise TypeError("unsupported operand type(s) for >=: 'Density' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value