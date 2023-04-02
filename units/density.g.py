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
        
        KiloGramPerCubicMillimeter = 'kilo_gram_per_cubic_millimeter'
        """
            
        """
        
        KiloGramPerCubicCentimeter = 'kilo_gram_per_cubic_centimeter'
        """
            
        """
        
        KiloGramPerCubicMeter = 'kilo_gram_per_cubic_meter'
        """
            
        """
        
        MilliGramPerCubicMeter = 'milli_gram_per_cubic_meter'
        """
            
        """
        
        MicroGramPerCubicMeter = 'micro_gram_per_cubic_meter'
        """
            
        """
        
        KiloPoundPerCubicInch = 'kilo_pound_per_cubic_inch'
        """
            
        """
        
        KiloPoundPerCubicFoot = 'kilo_pound_per_cubic_foot'
        """
            
        """
        
        PicoGramPerLiter = 'pico_gram_per_liter'
        """
            
        """
        
        NanoGramPerLiter = 'nano_gram_per_liter'
        """
            
        """
        
        MicroGramPerLiter = 'micro_gram_per_liter'
        """
            
        """
        
        MilliGramPerLiter = 'milli_gram_per_liter'
        """
            
        """
        
        CentiGramPerLiter = 'centi_gram_per_liter'
        """
            
        """
        
        DeciGramPerLiter = 'deci_gram_per_liter'
        """
            
        """
        
        PicoGramPerDeciliter = 'pico_gram_per_deciliter'
        """
            
        """
        
        NanoGramPerDeciliter = 'nano_gram_per_deciliter'
        """
            
        """
        
        MicroGramPerDeciliter = 'micro_gram_per_deciliter'
        """
            
        """
        
        MilliGramPerDeciliter = 'milli_gram_per_deciliter'
        """
            
        """
        
        CentiGramPerDeciliter = 'centi_gram_per_deciliter'
        """
            
        """
        
        DeciGramPerDeciliter = 'deci_gram_per_deciliter'
        """
            
        """
        
        PicoGramPerMilliliter = 'pico_gram_per_milliliter'
        """
            
        """
        
        NanoGramPerMilliliter = 'nano_gram_per_milliliter'
        """
            
        """
        
        MicroGramPerMilliliter = 'micro_gram_per_milliliter'
        """
            
        """
        
        MilliGramPerMilliliter = 'milli_gram_per_milliliter'
        """
            
        """
        
        CentiGramPerMilliliter = 'centi_gram_per_milliliter'
        """
            
        """
        
        DeciGramPerMilliliter = 'deci_gram_per_milliliter'
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
        
        self.__kilo_grams_per_cubic_millimeter = None
        
        self.__kilo_grams_per_cubic_centimeter = None
        
        self.__kilo_grams_per_cubic_meter = None
        
        self.__milli_grams_per_cubic_meter = None
        
        self.__micro_grams_per_cubic_meter = None
        
        self.__kilo_pounds_per_cubic_inch = None
        
        self.__kilo_pounds_per_cubic_foot = None
        
        self.__pico_grams_per_liter = None
        
        self.__nano_grams_per_liter = None
        
        self.__micro_grams_per_liter = None
        
        self.__milli_grams_per_liter = None
        
        self.__centi_grams_per_liter = None
        
        self.__deci_grams_per_liter = None
        
        self.__pico_grams_per_deci_liter = None
        
        self.__nano_grams_per_deci_liter = None
        
        self.__micro_grams_per_deci_liter = None
        
        self.__milli_grams_per_deci_liter = None
        
        self.__centi_grams_per_deci_liter = None
        
        self.__deci_grams_per_deci_liter = None
        
        self.__pico_grams_per_milliliter = None
        
        self.__nano_grams_per_milliliter = None
        
        self.__micro_grams_per_milliliter = None
        
        self.__milli_grams_per_milliliter = None
        
        self.__centi_grams_per_milliliter = None
        
        self.__deci_grams_per_milliliter = None
        

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
        
        if from_unit == DensityUnits.KiloGramPerCubicMillimeter:
            return ((value * 1e-6) / 1000.0)
        
        if from_unit == DensityUnits.KiloGramPerCubicCentimeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == DensityUnits.KiloGramPerCubicMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == DensityUnits.MilliGramPerCubicMeter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == DensityUnits.MicroGramPerCubicMeter:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == DensityUnits.KiloPoundPerCubicInch:
            return ((value * 3.6127298147753e-5) / 1000.0)
        
        if from_unit == DensityUnits.KiloPoundPerCubicFoot:
            return ((value * 0.062427961) / 1000.0)
        
        if from_unit == DensityUnits.PicoGramPerLiter:
            return ((value * 1) / 1e-12)
        
        if from_unit == DensityUnits.NanoGramPerLiter:
            return ((value * 1) / 1e-09)
        
        if from_unit == DensityUnits.MicroGramPerLiter:
            return ((value * 1) / 1e-06)
        
        if from_unit == DensityUnits.MilliGramPerLiter:
            return ((value * 1) / 0.001)
        
        if from_unit == DensityUnits.CentiGramPerLiter:
            return ((value * 1) / 0.01)
        
        if from_unit == DensityUnits.DeciGramPerLiter:
            return ((value * 1) / 0.1)
        
        if from_unit == DensityUnits.PicoGramPerDeciliter:
            return ((value * 1e-1) / 1e-12)
        
        if from_unit == DensityUnits.NanoGramPerDeciliter:
            return ((value * 1e-1) / 1e-09)
        
        if from_unit == DensityUnits.MicroGramPerDeciliter:
            return ((value * 1e-1) / 1e-06)
        
        if from_unit == DensityUnits.MilliGramPerDeciliter:
            return ((value * 1e-1) / 0.001)
        
        if from_unit == DensityUnits.CentiGramPerDeciliter:
            return ((value * 1e-1) / 0.01)
        
        if from_unit == DensityUnits.DeciGramPerDeciliter:
            return ((value * 1e-1) / 0.1)
        
        if from_unit == DensityUnits.PicoGramPerMilliliter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == DensityUnits.NanoGramPerMilliliter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == DensityUnits.MicroGramPerMilliliter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == DensityUnits.MilliGramPerMilliliter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == DensityUnits.CentiGramPerMilliliter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == DensityUnits.DeciGramPerMilliliter:
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
        
        if to_unit == DensityUnits.KiloGramPerCubicMillimeter:
            return ((value / 1e-6) * 1000.0)
        
        if to_unit == DensityUnits.KiloGramPerCubicCentimeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == DensityUnits.KiloGramPerCubicMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == DensityUnits.MilliGramPerCubicMeter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == DensityUnits.MicroGramPerCubicMeter:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == DensityUnits.KiloPoundPerCubicInch:
            return ((value / 3.6127298147753e-5) * 1000.0)
        
        if to_unit == DensityUnits.KiloPoundPerCubicFoot:
            return ((value / 0.062427961) * 1000.0)
        
        if to_unit == DensityUnits.PicoGramPerLiter:
            return ((value / 1) * 1e-12)
        
        if to_unit == DensityUnits.NanoGramPerLiter:
            return ((value / 1) * 1e-09)
        
        if to_unit == DensityUnits.MicroGramPerLiter:
            return ((value / 1) * 1e-06)
        
        if to_unit == DensityUnits.MilliGramPerLiter:
            return ((value / 1) * 0.001)
        
        if to_unit == DensityUnits.CentiGramPerLiter:
            return ((value / 1) * 0.01)
        
        if to_unit == DensityUnits.DeciGramPerLiter:
            return ((value / 1) * 0.1)
        
        if to_unit == DensityUnits.PicoGramPerDeciliter:
            return ((value / 1e-1) * 1e-12)
        
        if to_unit == DensityUnits.NanoGramPerDeciliter:
            return ((value / 1e-1) * 1e-09)
        
        if to_unit == DensityUnits.MicroGramPerDeciliter:
            return ((value / 1e-1) * 1e-06)
        
        if to_unit == DensityUnits.MilliGramPerDeciliter:
            return ((value / 1e-1) * 0.001)
        
        if to_unit == DensityUnits.CentiGramPerDeciliter:
            return ((value / 1e-1) * 0.01)
        
        if to_unit == DensityUnits.DeciGramPerDeciliter:
            return ((value / 1e-1) * 0.1)
        
        if to_unit == DensityUnits.PicoGramPerMilliliter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == DensityUnits.NanoGramPerMilliliter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == DensityUnits.MicroGramPerMilliliter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == DensityUnits.MilliGramPerMilliliter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == DensityUnits.CentiGramPerMilliliter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == DensityUnits.DeciGramPerMilliliter:
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
    def from_kilo_grams_per_cubic_millimeter(kilo_grams_per_cubic_millimeter: float):
        """
        Create a new instance of Density from a value in kilo_grams_per_cubic_millimeter.

        

        :param meters: The Density value in kilo_grams_per_cubic_millimeter.
        :type kilo_grams_per_cubic_millimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilo_grams_per_cubic_millimeter, DensityUnits.KiloGramPerCubicMillimeter)

    
    @staticmethod
    def from_kilo_grams_per_cubic_centimeter(kilo_grams_per_cubic_centimeter: float):
        """
        Create a new instance of Density from a value in kilo_grams_per_cubic_centimeter.

        

        :param meters: The Density value in kilo_grams_per_cubic_centimeter.
        :type kilo_grams_per_cubic_centimeter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilo_grams_per_cubic_centimeter, DensityUnits.KiloGramPerCubicCentimeter)

    
    @staticmethod
    def from_kilo_grams_per_cubic_meter(kilo_grams_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in kilo_grams_per_cubic_meter.

        

        :param meters: The Density value in kilo_grams_per_cubic_meter.
        :type kilo_grams_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilo_grams_per_cubic_meter, DensityUnits.KiloGramPerCubicMeter)

    
    @staticmethod
    def from_milli_grams_per_cubic_meter(milli_grams_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in milli_grams_per_cubic_meter.

        

        :param meters: The Density value in milli_grams_per_cubic_meter.
        :type milli_grams_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milli_grams_per_cubic_meter, DensityUnits.MilliGramPerCubicMeter)

    
    @staticmethod
    def from_micro_grams_per_cubic_meter(micro_grams_per_cubic_meter: float):
        """
        Create a new instance of Density from a value in micro_grams_per_cubic_meter.

        

        :param meters: The Density value in micro_grams_per_cubic_meter.
        :type micro_grams_per_cubic_meter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micro_grams_per_cubic_meter, DensityUnits.MicroGramPerCubicMeter)

    
    @staticmethod
    def from_kilo_pounds_per_cubic_inch(kilo_pounds_per_cubic_inch: float):
        """
        Create a new instance of Density from a value in kilo_pounds_per_cubic_inch.

        

        :param meters: The Density value in kilo_pounds_per_cubic_inch.
        :type kilo_pounds_per_cubic_inch: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilo_pounds_per_cubic_inch, DensityUnits.KiloPoundPerCubicInch)

    
    @staticmethod
    def from_kilo_pounds_per_cubic_foot(kilo_pounds_per_cubic_foot: float):
        """
        Create a new instance of Density from a value in kilo_pounds_per_cubic_foot.

        

        :param meters: The Density value in kilo_pounds_per_cubic_foot.
        :type kilo_pounds_per_cubic_foot: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(kilo_pounds_per_cubic_foot, DensityUnits.KiloPoundPerCubicFoot)

    
    @staticmethod
    def from_pico_grams_per_liter(pico_grams_per_liter: float):
        """
        Create a new instance of Density from a value in pico_grams_per_liter.

        

        :param meters: The Density value in pico_grams_per_liter.
        :type pico_grams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pico_grams_per_liter, DensityUnits.PicoGramPerLiter)

    
    @staticmethod
    def from_nano_grams_per_liter(nano_grams_per_liter: float):
        """
        Create a new instance of Density from a value in nano_grams_per_liter.

        

        :param meters: The Density value in nano_grams_per_liter.
        :type nano_grams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(nano_grams_per_liter, DensityUnits.NanoGramPerLiter)

    
    @staticmethod
    def from_micro_grams_per_liter(micro_grams_per_liter: float):
        """
        Create a new instance of Density from a value in micro_grams_per_liter.

        

        :param meters: The Density value in micro_grams_per_liter.
        :type micro_grams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micro_grams_per_liter, DensityUnits.MicroGramPerLiter)

    
    @staticmethod
    def from_milli_grams_per_liter(milli_grams_per_liter: float):
        """
        Create a new instance of Density from a value in milli_grams_per_liter.

        

        :param meters: The Density value in milli_grams_per_liter.
        :type milli_grams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milli_grams_per_liter, DensityUnits.MilliGramPerLiter)

    
    @staticmethod
    def from_centi_grams_per_liter(centi_grams_per_liter: float):
        """
        Create a new instance of Density from a value in centi_grams_per_liter.

        

        :param meters: The Density value in centi_grams_per_liter.
        :type centi_grams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(centi_grams_per_liter, DensityUnits.CentiGramPerLiter)

    
    @staticmethod
    def from_deci_grams_per_liter(deci_grams_per_liter: float):
        """
        Create a new instance of Density from a value in deci_grams_per_liter.

        

        :param meters: The Density value in deci_grams_per_liter.
        :type deci_grams_per_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(deci_grams_per_liter, DensityUnits.DeciGramPerLiter)

    
    @staticmethod
    def from_pico_grams_per_deci_liter(pico_grams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in pico_grams_per_deci_liter.

        

        :param meters: The Density value in pico_grams_per_deci_liter.
        :type pico_grams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pico_grams_per_deci_liter, DensityUnits.PicoGramPerDeciliter)

    
    @staticmethod
    def from_nano_grams_per_deci_liter(nano_grams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in nano_grams_per_deci_liter.

        

        :param meters: The Density value in nano_grams_per_deci_liter.
        :type nano_grams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(nano_grams_per_deci_liter, DensityUnits.NanoGramPerDeciliter)

    
    @staticmethod
    def from_micro_grams_per_deci_liter(micro_grams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in micro_grams_per_deci_liter.

        

        :param meters: The Density value in micro_grams_per_deci_liter.
        :type micro_grams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micro_grams_per_deci_liter, DensityUnits.MicroGramPerDeciliter)

    
    @staticmethod
    def from_milli_grams_per_deci_liter(milli_grams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in milli_grams_per_deci_liter.

        

        :param meters: The Density value in milli_grams_per_deci_liter.
        :type milli_grams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milli_grams_per_deci_liter, DensityUnits.MilliGramPerDeciliter)

    
    @staticmethod
    def from_centi_grams_per_deci_liter(centi_grams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in centi_grams_per_deci_liter.

        

        :param meters: The Density value in centi_grams_per_deci_liter.
        :type centi_grams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(centi_grams_per_deci_liter, DensityUnits.CentiGramPerDeciliter)

    
    @staticmethod
    def from_deci_grams_per_deci_liter(deci_grams_per_deci_liter: float):
        """
        Create a new instance of Density from a value in deci_grams_per_deci_liter.

        

        :param meters: The Density value in deci_grams_per_deci_liter.
        :type deci_grams_per_deci_liter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(deci_grams_per_deci_liter, DensityUnits.DeciGramPerDeciliter)

    
    @staticmethod
    def from_pico_grams_per_milliliter(pico_grams_per_milliliter: float):
        """
        Create a new instance of Density from a value in pico_grams_per_milliliter.

        

        :param meters: The Density value in pico_grams_per_milliliter.
        :type pico_grams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(pico_grams_per_milliliter, DensityUnits.PicoGramPerMilliliter)

    
    @staticmethod
    def from_nano_grams_per_milliliter(nano_grams_per_milliliter: float):
        """
        Create a new instance of Density from a value in nano_grams_per_milliliter.

        

        :param meters: The Density value in nano_grams_per_milliliter.
        :type nano_grams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(nano_grams_per_milliliter, DensityUnits.NanoGramPerMilliliter)

    
    @staticmethod
    def from_micro_grams_per_milliliter(micro_grams_per_milliliter: float):
        """
        Create a new instance of Density from a value in micro_grams_per_milliliter.

        

        :param meters: The Density value in micro_grams_per_milliliter.
        :type micro_grams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(micro_grams_per_milliliter, DensityUnits.MicroGramPerMilliliter)

    
    @staticmethod
    def from_milli_grams_per_milliliter(milli_grams_per_milliliter: float):
        """
        Create a new instance of Density from a value in milli_grams_per_milliliter.

        

        :param meters: The Density value in milli_grams_per_milliliter.
        :type milli_grams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(milli_grams_per_milliliter, DensityUnits.MilliGramPerMilliliter)

    
    @staticmethod
    def from_centi_grams_per_milliliter(centi_grams_per_milliliter: float):
        """
        Create a new instance of Density from a value in centi_grams_per_milliliter.

        

        :param meters: The Density value in centi_grams_per_milliliter.
        :type centi_grams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(centi_grams_per_milliliter, DensityUnits.CentiGramPerMilliliter)

    
    @staticmethod
    def from_deci_grams_per_milliliter(deci_grams_per_milliliter: float):
        """
        Create a new instance of Density from a value in deci_grams_per_milliliter.

        

        :param meters: The Density value in deci_grams_per_milliliter.
        :type deci_grams_per_milliliter: float
        :return: A new instance of Density.
        :rtype: Density
        """
        return Density(deci_grams_per_milliliter, DensityUnits.DeciGramPerMilliliter)

    
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
    def kilo_grams_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_cubic_millimeter != None:
            return self.__kilo_grams_per_cubic_millimeter
        self.__kilo_grams_per_cubic_millimeter = self.__convert_from_base(DensityUnits.KiloGramPerCubicMillimeter)
        return self.__kilo_grams_per_cubic_millimeter

    
    @property
    def kilo_grams_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_cubic_centimeter != None:
            return self.__kilo_grams_per_cubic_centimeter
        self.__kilo_grams_per_cubic_centimeter = self.__convert_from_base(DensityUnits.KiloGramPerCubicCentimeter)
        return self.__kilo_grams_per_cubic_centimeter

    
    @property
    def kilo_grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_cubic_meter != None:
            return self.__kilo_grams_per_cubic_meter
        self.__kilo_grams_per_cubic_meter = self.__convert_from_base(DensityUnits.KiloGramPerCubicMeter)
        return self.__kilo_grams_per_cubic_meter

    
    @property
    def milli_grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_cubic_meter != None:
            return self.__milli_grams_per_cubic_meter
        self.__milli_grams_per_cubic_meter = self.__convert_from_base(DensityUnits.MilliGramPerCubicMeter)
        return self.__milli_grams_per_cubic_meter

    
    @property
    def micro_grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_cubic_meter != None:
            return self.__micro_grams_per_cubic_meter
        self.__micro_grams_per_cubic_meter = self.__convert_from_base(DensityUnits.MicroGramPerCubicMeter)
        return self.__micro_grams_per_cubic_meter

    
    @property
    def kilo_pounds_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilo_pounds_per_cubic_inch != None:
            return self.__kilo_pounds_per_cubic_inch
        self.__kilo_pounds_per_cubic_inch = self.__convert_from_base(DensityUnits.KiloPoundPerCubicInch)
        return self.__kilo_pounds_per_cubic_inch

    
    @property
    def kilo_pounds_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilo_pounds_per_cubic_foot != None:
            return self.__kilo_pounds_per_cubic_foot
        self.__kilo_pounds_per_cubic_foot = self.__convert_from_base(DensityUnits.KiloPoundPerCubicFoot)
        return self.__kilo_pounds_per_cubic_foot

    
    @property
    def pico_grams_per_liter(self) -> float:
        """
        
        """
        if self.__pico_grams_per_liter != None:
            return self.__pico_grams_per_liter
        self.__pico_grams_per_liter = self.__convert_from_base(DensityUnits.PicoGramPerLiter)
        return self.__pico_grams_per_liter

    
    @property
    def nano_grams_per_liter(self) -> float:
        """
        
        """
        if self.__nano_grams_per_liter != None:
            return self.__nano_grams_per_liter
        self.__nano_grams_per_liter = self.__convert_from_base(DensityUnits.NanoGramPerLiter)
        return self.__nano_grams_per_liter

    
    @property
    def micro_grams_per_liter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_liter != None:
            return self.__micro_grams_per_liter
        self.__micro_grams_per_liter = self.__convert_from_base(DensityUnits.MicroGramPerLiter)
        return self.__micro_grams_per_liter

    
    @property
    def milli_grams_per_liter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_liter != None:
            return self.__milli_grams_per_liter
        self.__milli_grams_per_liter = self.__convert_from_base(DensityUnits.MilliGramPerLiter)
        return self.__milli_grams_per_liter

    
    @property
    def centi_grams_per_liter(self) -> float:
        """
        
        """
        if self.__centi_grams_per_liter != None:
            return self.__centi_grams_per_liter
        self.__centi_grams_per_liter = self.__convert_from_base(DensityUnits.CentiGramPerLiter)
        return self.__centi_grams_per_liter

    
    @property
    def deci_grams_per_liter(self) -> float:
        """
        
        """
        if self.__deci_grams_per_liter != None:
            return self.__deci_grams_per_liter
        self.__deci_grams_per_liter = self.__convert_from_base(DensityUnits.DeciGramPerLiter)
        return self.__deci_grams_per_liter

    
    @property
    def pico_grams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__pico_grams_per_deci_liter != None:
            return self.__pico_grams_per_deci_liter
        self.__pico_grams_per_deci_liter = self.__convert_from_base(DensityUnits.PicoGramPerDeciliter)
        return self.__pico_grams_per_deci_liter

    
    @property
    def nano_grams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__nano_grams_per_deci_liter != None:
            return self.__nano_grams_per_deci_liter
        self.__nano_grams_per_deci_liter = self.__convert_from_base(DensityUnits.NanoGramPerDeciliter)
        return self.__nano_grams_per_deci_liter

    
    @property
    def micro_grams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_deci_liter != None:
            return self.__micro_grams_per_deci_liter
        self.__micro_grams_per_deci_liter = self.__convert_from_base(DensityUnits.MicroGramPerDeciliter)
        return self.__micro_grams_per_deci_liter

    
    @property
    def milli_grams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_deci_liter != None:
            return self.__milli_grams_per_deci_liter
        self.__milli_grams_per_deci_liter = self.__convert_from_base(DensityUnits.MilliGramPerDeciliter)
        return self.__milli_grams_per_deci_liter

    
    @property
    def centi_grams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__centi_grams_per_deci_liter != None:
            return self.__centi_grams_per_deci_liter
        self.__centi_grams_per_deci_liter = self.__convert_from_base(DensityUnits.CentiGramPerDeciliter)
        return self.__centi_grams_per_deci_liter

    
    @property
    def deci_grams_per_deci_liter(self) -> float:
        """
        
        """
        if self.__deci_grams_per_deci_liter != None:
            return self.__deci_grams_per_deci_liter
        self.__deci_grams_per_deci_liter = self.__convert_from_base(DensityUnits.DeciGramPerDeciliter)
        return self.__deci_grams_per_deci_liter

    
    @property
    def pico_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__pico_grams_per_milliliter != None:
            return self.__pico_grams_per_milliliter
        self.__pico_grams_per_milliliter = self.__convert_from_base(DensityUnits.PicoGramPerMilliliter)
        return self.__pico_grams_per_milliliter

    
    @property
    def nano_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__nano_grams_per_milliliter != None:
            return self.__nano_grams_per_milliliter
        self.__nano_grams_per_milliliter = self.__convert_from_base(DensityUnits.NanoGramPerMilliliter)
        return self.__nano_grams_per_milliliter

    
    @property
    def micro_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_milliliter != None:
            return self.__micro_grams_per_milliliter
        self.__micro_grams_per_milliliter = self.__convert_from_base(DensityUnits.MicroGramPerMilliliter)
        return self.__micro_grams_per_milliliter

    
    @property
    def milli_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_milliliter != None:
            return self.__milli_grams_per_milliliter
        self.__milli_grams_per_milliliter = self.__convert_from_base(DensityUnits.MilliGramPerMilliliter)
        return self.__milli_grams_per_milliliter

    
    @property
    def centi_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__centi_grams_per_milliliter != None:
            return self.__centi_grams_per_milliliter
        self.__centi_grams_per_milliliter = self.__convert_from_base(DensityUnits.CentiGramPerMilliliter)
        return self.__centi_grams_per_milliliter

    
    @property
    def deci_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__deci_grams_per_milliliter != None:
            return self.__deci_grams_per_milliliter
        self.__deci_grams_per_milliliter = self.__convert_from_base(DensityUnits.DeciGramPerMilliliter)
        return self.__deci_grams_per_milliliter

    
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
        
        if unit == DensityUnits.KiloGramPerCubicMillimeter:
            return f"""{self.kilo_grams_per_cubic_millimeter} """
        
        if unit == DensityUnits.KiloGramPerCubicCentimeter:
            return f"""{self.kilo_grams_per_cubic_centimeter} """
        
        if unit == DensityUnits.KiloGramPerCubicMeter:
            return f"""{self.kilo_grams_per_cubic_meter} """
        
        if unit == DensityUnits.MilliGramPerCubicMeter:
            return f"""{self.milli_grams_per_cubic_meter} """
        
        if unit == DensityUnits.MicroGramPerCubicMeter:
            return f"""{self.micro_grams_per_cubic_meter} """
        
        if unit == DensityUnits.KiloPoundPerCubicInch:
            return f"""{self.kilo_pounds_per_cubic_inch} """
        
        if unit == DensityUnits.KiloPoundPerCubicFoot:
            return f"""{self.kilo_pounds_per_cubic_foot} """
        
        if unit == DensityUnits.PicoGramPerLiter:
            return f"""{self.pico_grams_per_liter} """
        
        if unit == DensityUnits.NanoGramPerLiter:
            return f"""{self.nano_grams_per_liter} """
        
        if unit == DensityUnits.MicroGramPerLiter:
            return f"""{self.micro_grams_per_liter} """
        
        if unit == DensityUnits.MilliGramPerLiter:
            return f"""{self.milli_grams_per_liter} """
        
        if unit == DensityUnits.CentiGramPerLiter:
            return f"""{self.centi_grams_per_liter} """
        
        if unit == DensityUnits.DeciGramPerLiter:
            return f"""{self.deci_grams_per_liter} """
        
        if unit == DensityUnits.PicoGramPerDeciliter:
            return f"""{self.pico_grams_per_deci_liter} """
        
        if unit == DensityUnits.NanoGramPerDeciliter:
            return f"""{self.nano_grams_per_deci_liter} """
        
        if unit == DensityUnits.MicroGramPerDeciliter:
            return f"""{self.micro_grams_per_deci_liter} """
        
        if unit == DensityUnits.MilliGramPerDeciliter:
            return f"""{self.milli_grams_per_deci_liter} """
        
        if unit == DensityUnits.CentiGramPerDeciliter:
            return f"""{self.centi_grams_per_deci_liter} """
        
        if unit == DensityUnits.DeciGramPerDeciliter:
            return f"""{self.deci_grams_per_deci_liter} """
        
        if unit == DensityUnits.PicoGramPerMilliliter:
            return f"""{self.pico_grams_per_milliliter} """
        
        if unit == DensityUnits.NanoGramPerMilliliter:
            return f"""{self.nano_grams_per_milliliter} """
        
        if unit == DensityUnits.MicroGramPerMilliliter:
            return f"""{self.micro_grams_per_milliliter} """
        
        if unit == DensityUnits.MilliGramPerMilliliter:
            return f"""{self.milli_grams_per_milliliter} """
        
        if unit == DensityUnits.CentiGramPerMilliliter:
            return f"""{self.centi_grams_per_milliliter} """
        
        if unit == DensityUnits.DeciGramPerMilliliter:
            return f"""{self.deci_grams_per_milliliter} """
        
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
        
        if unit_abbreviation == DensityUnits.KiloGramPerCubicMillimeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.KiloGramPerCubicCentimeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.KiloGramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilliGramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicroGramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == DensityUnits.KiloPoundPerCubicInch:
            return """"""
        
        if unit_abbreviation == DensityUnits.KiloPoundPerCubicFoot:
            return """"""
        
        if unit_abbreviation == DensityUnits.PicoGramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.NanoGramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicroGramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilliGramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.CentiGramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.DeciGramPerLiter:
            return """"""
        
        if unit_abbreviation == DensityUnits.PicoGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.NanoGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicroGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilliGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.CentiGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.DeciGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.PicoGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.NanoGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MicroGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.MilliGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.CentiGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == DensityUnits.DeciGramPerMilliliter:
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