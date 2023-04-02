from enum import Enum
import math
import string


class MassConcentrationUnits(Enum):
        """
            MassConcentrationUnits enumeration
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
        
        GramPerMicroliter = 'gram_per_microliter'
        """
            
        """
        
        GramPerMilliliter = 'gram_per_milliliter'
        """
            
        """
        
        GramPerDeciliter = 'gram_per_deciliter'
        """
            
        """
        
        GramPerLiter = 'gram_per_liter'
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
        
        PoundPerCubicInch = 'pound_per_cubic_inch'
        """
            
        """
        
        PoundPerCubicFoot = 'pound_per_cubic_foot'
        """
            
        """
        
        SlugPerCubicFoot = 'slug_per_cubic_foot'
        """
            
        """
        
        PoundPerUSGallon = 'pound_per_us_gallon'
        """
            
        """
        
        OuncePerUSGallon = 'ounce_per_us_gallon'
        """
            
        """
        
        OuncePerImperialGallon = 'ounce_per_imperial_gallon'
        """
            
        """
        
        PoundPerImperialGallon = 'pound_per_imperial_gallon'
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
        
        PicoGramPerMicroliter = 'pico_gram_per_microliter'
        """
            
        """
        
        NanoGramPerMicroliter = 'nano_gram_per_microliter'
        """
            
        """
        
        MicroGramPerMicroliter = 'micro_gram_per_microliter'
        """
            
        """
        
        MilliGramPerMicroliter = 'milli_gram_per_microliter'
        """
            
        """
        
        CentiGramPerMicroliter = 'centi_gram_per_microliter'
        """
            
        """
        
        DeciGramPerMicroliter = 'deci_gram_per_microliter'
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
        
        KiloGramPerLiter = 'kilo_gram_per_liter'
        """
            
        """
        
        KiloPoundPerCubicInch = 'kilo_pound_per_cubic_inch'
        """
            
        """
        
        KiloPoundPerCubicFoot = 'kilo_pound_per_cubic_foot'
        """
            
        """
        
    
class MassConcentration:
    """
    In chemistry, the mass concentration ρi (or γi) is defined as the mass of a constituent mi divided by the volume of the mixture V

    Args:
        value (float): The value.
        from_unit (MassConcentrationUnits): The MassConcentration unit to create from, The default unit is KilogramPerCubicMeter
    """
    def __init__(self, value: float, from_unit: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__kilo_grams_per_cubic_millimeter = None
        
        self.__kilo_grams_per_cubic_centimeter = None
        
        self.__kilo_grams_per_cubic_meter = None
        
        self.__milli_grams_per_cubic_meter = None
        
        self.__micro_grams_per_cubic_meter = None
        
        self.__pico_grams_per_microliter = None
        
        self.__nano_grams_per_microliter = None
        
        self.__micro_grams_per_microliter = None
        
        self.__milli_grams_per_microliter = None
        
        self.__centi_grams_per_microliter = None
        
        self.__deci_grams_per_microliter = None
        
        self.__pico_grams_per_milliliter = None
        
        self.__nano_grams_per_milliliter = None
        
        self.__micro_grams_per_milliliter = None
        
        self.__milli_grams_per_milliliter = None
        
        self.__centi_grams_per_milliliter = None
        
        self.__deci_grams_per_milliliter = None
        
        self.__pico_grams_per_deciliter = None
        
        self.__nano_grams_per_deciliter = None
        
        self.__micro_grams_per_deciliter = None
        
        self.__milli_grams_per_deciliter = None
        
        self.__centi_grams_per_deciliter = None
        
        self.__deci_grams_per_deciliter = None
        
        self.__pico_grams_per_liter = None
        
        self.__nano_grams_per_liter = None
        
        self.__micro_grams_per_liter = None
        
        self.__milli_grams_per_liter = None
        
        self.__centi_grams_per_liter = None
        
        self.__deci_grams_per_liter = None
        
        self.__kilo_grams_per_liter = None
        
        self.__kilo_pounds_per_cubic_inch = None
        
        self.__kilo_pounds_per_cubic_foot = None
        

    def __convert_from_base(self, from_unit: MassConcentrationUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == MassConcentrationUnits.KiloGramPerCubicMillimeter:
            return ((value * 1e-6) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KiloGramPerCubicCentimeter:
            return ((value * 1e-3) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KiloGramPerCubicMeter:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassConcentrationUnits.MilliGramPerCubicMeter:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassConcentrationUnits.MicroGramPerCubicMeter:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MassConcentrationUnits.PicoGramPerMicroliter:
            return ((value * 1e-6) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanoGramPerMicroliter:
            return ((value * 1e-6) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicroGramPerMicroliter:
            return ((value * 1e-6) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilliGramPerMicroliter:
            return ((value * 1e-6) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentiGramPerMicroliter:
            return ((value * 1e-6) / 0.01)
        
        if from_unit == MassConcentrationUnits.DeciGramPerMicroliter:
            return ((value * 1e-6) / 0.1)
        
        if from_unit == MassConcentrationUnits.PicoGramPerMilliliter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanoGramPerMilliliter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicroGramPerMilliliter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilliGramPerMilliliter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentiGramPerMilliliter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == MassConcentrationUnits.DeciGramPerMilliliter:
            return ((value * 1e-3) / 0.1)
        
        if from_unit == MassConcentrationUnits.PicoGramPerDeciliter:
            return ((value * 1e-1) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanoGramPerDeciliter:
            return ((value * 1e-1) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicroGramPerDeciliter:
            return ((value * 1e-1) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilliGramPerDeciliter:
            return ((value * 1e-1) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentiGramPerDeciliter:
            return ((value * 1e-1) / 0.01)
        
        if from_unit == MassConcentrationUnits.DeciGramPerDeciliter:
            return ((value * 1e-1) / 0.1)
        
        if from_unit == MassConcentrationUnits.PicoGramPerLiter:
            return ((value) / 1e-12)
        
        if from_unit == MassConcentrationUnits.NanoGramPerLiter:
            return ((value) / 1e-09)
        
        if from_unit == MassConcentrationUnits.MicroGramPerLiter:
            return ((value) / 1e-06)
        
        if from_unit == MassConcentrationUnits.MilliGramPerLiter:
            return ((value) / 0.001)
        
        if from_unit == MassConcentrationUnits.CentiGramPerLiter:
            return ((value) / 0.01)
        
        if from_unit == MassConcentrationUnits.DeciGramPerLiter:
            return ((value) / 0.1)
        
        if from_unit == MassConcentrationUnits.KiloGramPerLiter:
            return ((value) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KiloPoundPerCubicInch:
            return ((value * 3.6127298147753e-5) / 1000.0)
        
        if from_unit == MassConcentrationUnits.KiloPoundPerCubicFoot:
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
        
        if to_unit == MassConcentrationUnits.KiloGramPerCubicMillimeter:
            return ((value / 1e-6) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KiloGramPerCubicCentimeter:
            return ((value / 1e-3) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KiloGramPerCubicMeter:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassConcentrationUnits.MilliGramPerCubicMeter:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassConcentrationUnits.MicroGramPerCubicMeter:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MassConcentrationUnits.PicoGramPerMicroliter:
            return ((value / 1e-6) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanoGramPerMicroliter:
            return ((value / 1e-6) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicroGramPerMicroliter:
            return ((value / 1e-6) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilliGramPerMicroliter:
            return ((value / 1e-6) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentiGramPerMicroliter:
            return ((value / 1e-6) * 0.01)
        
        if to_unit == MassConcentrationUnits.DeciGramPerMicroliter:
            return ((value / 1e-6) * 0.1)
        
        if to_unit == MassConcentrationUnits.PicoGramPerMilliliter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanoGramPerMilliliter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicroGramPerMilliliter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilliGramPerMilliliter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentiGramPerMilliliter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == MassConcentrationUnits.DeciGramPerMilliliter:
            return ((value / 1e-3) * 0.1)
        
        if to_unit == MassConcentrationUnits.PicoGramPerDeciliter:
            return ((value / 1e-1) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanoGramPerDeciliter:
            return ((value / 1e-1) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicroGramPerDeciliter:
            return ((value / 1e-1) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilliGramPerDeciliter:
            return ((value / 1e-1) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentiGramPerDeciliter:
            return ((value / 1e-1) * 0.01)
        
        if to_unit == MassConcentrationUnits.DeciGramPerDeciliter:
            return ((value / 1e-1) * 0.1)
        
        if to_unit == MassConcentrationUnits.PicoGramPerLiter:
            return ((value) * 1e-12)
        
        if to_unit == MassConcentrationUnits.NanoGramPerLiter:
            return ((value) * 1e-09)
        
        if to_unit == MassConcentrationUnits.MicroGramPerLiter:
            return ((value) * 1e-06)
        
        if to_unit == MassConcentrationUnits.MilliGramPerLiter:
            return ((value) * 0.001)
        
        if to_unit == MassConcentrationUnits.CentiGramPerLiter:
            return ((value) * 0.01)
        
        if to_unit == MassConcentrationUnits.DeciGramPerLiter:
            return ((value) * 0.1)
        
        if to_unit == MassConcentrationUnits.KiloGramPerLiter:
            return ((value) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KiloPoundPerCubicInch:
            return ((value / 3.6127298147753e-5) * 1000.0)
        
        if to_unit == MassConcentrationUnits.KiloPoundPerCubicFoot:
            return ((value / 0.062427961) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_kilo_grams_per_cubic_millimeter(kilo_grams_per_cubic_millimeter: float):
        """
        Create a new instance of MassConcentration from a value in kilo_grams_per_cubic_millimeter.

        

        :param meters: The MassConcentration value in kilo_grams_per_cubic_millimeter.
        :type kilo_grams_per_cubic_millimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilo_grams_per_cubic_millimeter, MassConcentrationUnits.KiloGramPerCubicMillimeter)

    
    @staticmethod
    def from_kilo_grams_per_cubic_centimeter(kilo_grams_per_cubic_centimeter: float):
        """
        Create a new instance of MassConcentration from a value in kilo_grams_per_cubic_centimeter.

        

        :param meters: The MassConcentration value in kilo_grams_per_cubic_centimeter.
        :type kilo_grams_per_cubic_centimeter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilo_grams_per_cubic_centimeter, MassConcentrationUnits.KiloGramPerCubicCentimeter)

    
    @staticmethod
    def from_kilo_grams_per_cubic_meter(kilo_grams_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in kilo_grams_per_cubic_meter.

        

        :param meters: The MassConcentration value in kilo_grams_per_cubic_meter.
        :type kilo_grams_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilo_grams_per_cubic_meter, MassConcentrationUnits.KiloGramPerCubicMeter)

    
    @staticmethod
    def from_milli_grams_per_cubic_meter(milli_grams_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in milli_grams_per_cubic_meter.

        

        :param meters: The MassConcentration value in milli_grams_per_cubic_meter.
        :type milli_grams_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milli_grams_per_cubic_meter, MassConcentrationUnits.MilliGramPerCubicMeter)

    
    @staticmethod
    def from_micro_grams_per_cubic_meter(micro_grams_per_cubic_meter: float):
        """
        Create a new instance of MassConcentration from a value in micro_grams_per_cubic_meter.

        

        :param meters: The MassConcentration value in micro_grams_per_cubic_meter.
        :type micro_grams_per_cubic_meter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micro_grams_per_cubic_meter, MassConcentrationUnits.MicroGramPerCubicMeter)

    
    @staticmethod
    def from_pico_grams_per_microliter(pico_grams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in pico_grams_per_microliter.

        

        :param meters: The MassConcentration value in pico_grams_per_microliter.
        :type pico_grams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pico_grams_per_microliter, MassConcentrationUnits.PicoGramPerMicroliter)

    
    @staticmethod
    def from_nano_grams_per_microliter(nano_grams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in nano_grams_per_microliter.

        

        :param meters: The MassConcentration value in nano_grams_per_microliter.
        :type nano_grams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nano_grams_per_microliter, MassConcentrationUnits.NanoGramPerMicroliter)

    
    @staticmethod
    def from_micro_grams_per_microliter(micro_grams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in micro_grams_per_microliter.

        

        :param meters: The MassConcentration value in micro_grams_per_microliter.
        :type micro_grams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micro_grams_per_microliter, MassConcentrationUnits.MicroGramPerMicroliter)

    
    @staticmethod
    def from_milli_grams_per_microliter(milli_grams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in milli_grams_per_microliter.

        

        :param meters: The MassConcentration value in milli_grams_per_microliter.
        :type milli_grams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milli_grams_per_microliter, MassConcentrationUnits.MilliGramPerMicroliter)

    
    @staticmethod
    def from_centi_grams_per_microliter(centi_grams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in centi_grams_per_microliter.

        

        :param meters: The MassConcentration value in centi_grams_per_microliter.
        :type centi_grams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centi_grams_per_microliter, MassConcentrationUnits.CentiGramPerMicroliter)

    
    @staticmethod
    def from_deci_grams_per_microliter(deci_grams_per_microliter: float):
        """
        Create a new instance of MassConcentration from a value in deci_grams_per_microliter.

        

        :param meters: The MassConcentration value in deci_grams_per_microliter.
        :type deci_grams_per_microliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(deci_grams_per_microliter, MassConcentrationUnits.DeciGramPerMicroliter)

    
    @staticmethod
    def from_pico_grams_per_milliliter(pico_grams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in pico_grams_per_milliliter.

        

        :param meters: The MassConcentration value in pico_grams_per_milliliter.
        :type pico_grams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pico_grams_per_milliliter, MassConcentrationUnits.PicoGramPerMilliliter)

    
    @staticmethod
    def from_nano_grams_per_milliliter(nano_grams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in nano_grams_per_milliliter.

        

        :param meters: The MassConcentration value in nano_grams_per_milliliter.
        :type nano_grams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nano_grams_per_milliliter, MassConcentrationUnits.NanoGramPerMilliliter)

    
    @staticmethod
    def from_micro_grams_per_milliliter(micro_grams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in micro_grams_per_milliliter.

        

        :param meters: The MassConcentration value in micro_grams_per_milliliter.
        :type micro_grams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micro_grams_per_milliliter, MassConcentrationUnits.MicroGramPerMilliliter)

    
    @staticmethod
    def from_milli_grams_per_milliliter(milli_grams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in milli_grams_per_milliliter.

        

        :param meters: The MassConcentration value in milli_grams_per_milliliter.
        :type milli_grams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milli_grams_per_milliliter, MassConcentrationUnits.MilliGramPerMilliliter)

    
    @staticmethod
    def from_centi_grams_per_milliliter(centi_grams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in centi_grams_per_milliliter.

        

        :param meters: The MassConcentration value in centi_grams_per_milliliter.
        :type centi_grams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centi_grams_per_milliliter, MassConcentrationUnits.CentiGramPerMilliliter)

    
    @staticmethod
    def from_deci_grams_per_milliliter(deci_grams_per_milliliter: float):
        """
        Create a new instance of MassConcentration from a value in deci_grams_per_milliliter.

        

        :param meters: The MassConcentration value in deci_grams_per_milliliter.
        :type deci_grams_per_milliliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(deci_grams_per_milliliter, MassConcentrationUnits.DeciGramPerMilliliter)

    
    @staticmethod
    def from_pico_grams_per_deciliter(pico_grams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in pico_grams_per_deciliter.

        

        :param meters: The MassConcentration value in pico_grams_per_deciliter.
        :type pico_grams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pico_grams_per_deciliter, MassConcentrationUnits.PicoGramPerDeciliter)

    
    @staticmethod
    def from_nano_grams_per_deciliter(nano_grams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in nano_grams_per_deciliter.

        

        :param meters: The MassConcentration value in nano_grams_per_deciliter.
        :type nano_grams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nano_grams_per_deciliter, MassConcentrationUnits.NanoGramPerDeciliter)

    
    @staticmethod
    def from_micro_grams_per_deciliter(micro_grams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in micro_grams_per_deciliter.

        

        :param meters: The MassConcentration value in micro_grams_per_deciliter.
        :type micro_grams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micro_grams_per_deciliter, MassConcentrationUnits.MicroGramPerDeciliter)

    
    @staticmethod
    def from_milli_grams_per_deciliter(milli_grams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in milli_grams_per_deciliter.

        

        :param meters: The MassConcentration value in milli_grams_per_deciliter.
        :type milli_grams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milli_grams_per_deciliter, MassConcentrationUnits.MilliGramPerDeciliter)

    
    @staticmethod
    def from_centi_grams_per_deciliter(centi_grams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in centi_grams_per_deciliter.

        

        :param meters: The MassConcentration value in centi_grams_per_deciliter.
        :type centi_grams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centi_grams_per_deciliter, MassConcentrationUnits.CentiGramPerDeciliter)

    
    @staticmethod
    def from_deci_grams_per_deciliter(deci_grams_per_deciliter: float):
        """
        Create a new instance of MassConcentration from a value in deci_grams_per_deciliter.

        

        :param meters: The MassConcentration value in deci_grams_per_deciliter.
        :type deci_grams_per_deciliter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(deci_grams_per_deciliter, MassConcentrationUnits.DeciGramPerDeciliter)

    
    @staticmethod
    def from_pico_grams_per_liter(pico_grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in pico_grams_per_liter.

        

        :param meters: The MassConcentration value in pico_grams_per_liter.
        :type pico_grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(pico_grams_per_liter, MassConcentrationUnits.PicoGramPerLiter)

    
    @staticmethod
    def from_nano_grams_per_liter(nano_grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in nano_grams_per_liter.

        

        :param meters: The MassConcentration value in nano_grams_per_liter.
        :type nano_grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(nano_grams_per_liter, MassConcentrationUnits.NanoGramPerLiter)

    
    @staticmethod
    def from_micro_grams_per_liter(micro_grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in micro_grams_per_liter.

        

        :param meters: The MassConcentration value in micro_grams_per_liter.
        :type micro_grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(micro_grams_per_liter, MassConcentrationUnits.MicroGramPerLiter)

    
    @staticmethod
    def from_milli_grams_per_liter(milli_grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in milli_grams_per_liter.

        

        :param meters: The MassConcentration value in milli_grams_per_liter.
        :type milli_grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(milli_grams_per_liter, MassConcentrationUnits.MilliGramPerLiter)

    
    @staticmethod
    def from_centi_grams_per_liter(centi_grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in centi_grams_per_liter.

        

        :param meters: The MassConcentration value in centi_grams_per_liter.
        :type centi_grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(centi_grams_per_liter, MassConcentrationUnits.CentiGramPerLiter)

    
    @staticmethod
    def from_deci_grams_per_liter(deci_grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in deci_grams_per_liter.

        

        :param meters: The MassConcentration value in deci_grams_per_liter.
        :type deci_grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(deci_grams_per_liter, MassConcentrationUnits.DeciGramPerLiter)

    
    @staticmethod
    def from_kilo_grams_per_liter(kilo_grams_per_liter: float):
        """
        Create a new instance of MassConcentration from a value in kilo_grams_per_liter.

        

        :param meters: The MassConcentration value in kilo_grams_per_liter.
        :type kilo_grams_per_liter: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilo_grams_per_liter, MassConcentrationUnits.KiloGramPerLiter)

    
    @staticmethod
    def from_kilo_pounds_per_cubic_inch(kilo_pounds_per_cubic_inch: float):
        """
        Create a new instance of MassConcentration from a value in kilo_pounds_per_cubic_inch.

        

        :param meters: The MassConcentration value in kilo_pounds_per_cubic_inch.
        :type kilo_pounds_per_cubic_inch: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilo_pounds_per_cubic_inch, MassConcentrationUnits.KiloPoundPerCubicInch)

    
    @staticmethod
    def from_kilo_pounds_per_cubic_foot(kilo_pounds_per_cubic_foot: float):
        """
        Create a new instance of MassConcentration from a value in kilo_pounds_per_cubic_foot.

        

        :param meters: The MassConcentration value in kilo_pounds_per_cubic_foot.
        :type kilo_pounds_per_cubic_foot: float
        :return: A new instance of MassConcentration.
        :rtype: MassConcentration
        """
        return MassConcentration(kilo_pounds_per_cubic_foot, MassConcentrationUnits.KiloPoundPerCubicFoot)

    
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
    def kilo_grams_per_cubic_millimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_cubic_millimeter != None:
            return self.__kilo_grams_per_cubic_millimeter
        self.__kilo_grams_per_cubic_millimeter = self.__convert_from_base(MassConcentrationUnits.KiloGramPerCubicMillimeter)
        return self.__kilo_grams_per_cubic_millimeter

    
    @property
    def kilo_grams_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_cubic_centimeter != None:
            return self.__kilo_grams_per_cubic_centimeter
        self.__kilo_grams_per_cubic_centimeter = self.__convert_from_base(MassConcentrationUnits.KiloGramPerCubicCentimeter)
        return self.__kilo_grams_per_cubic_centimeter

    
    @property
    def kilo_grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_cubic_meter != None:
            return self.__kilo_grams_per_cubic_meter
        self.__kilo_grams_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.KiloGramPerCubicMeter)
        return self.__kilo_grams_per_cubic_meter

    
    @property
    def milli_grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_cubic_meter != None:
            return self.__milli_grams_per_cubic_meter
        self.__milli_grams_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.MilliGramPerCubicMeter)
        return self.__milli_grams_per_cubic_meter

    
    @property
    def micro_grams_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_cubic_meter != None:
            return self.__micro_grams_per_cubic_meter
        self.__micro_grams_per_cubic_meter = self.__convert_from_base(MassConcentrationUnits.MicroGramPerCubicMeter)
        return self.__micro_grams_per_cubic_meter

    
    @property
    def pico_grams_per_microliter(self) -> float:
        """
        
        """
        if self.__pico_grams_per_microliter != None:
            return self.__pico_grams_per_microliter
        self.__pico_grams_per_microliter = self.__convert_from_base(MassConcentrationUnits.PicoGramPerMicroliter)
        return self.__pico_grams_per_microliter

    
    @property
    def nano_grams_per_microliter(self) -> float:
        """
        
        """
        if self.__nano_grams_per_microliter != None:
            return self.__nano_grams_per_microliter
        self.__nano_grams_per_microliter = self.__convert_from_base(MassConcentrationUnits.NanoGramPerMicroliter)
        return self.__nano_grams_per_microliter

    
    @property
    def micro_grams_per_microliter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_microliter != None:
            return self.__micro_grams_per_microliter
        self.__micro_grams_per_microliter = self.__convert_from_base(MassConcentrationUnits.MicroGramPerMicroliter)
        return self.__micro_grams_per_microliter

    
    @property
    def milli_grams_per_microliter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_microliter != None:
            return self.__milli_grams_per_microliter
        self.__milli_grams_per_microliter = self.__convert_from_base(MassConcentrationUnits.MilliGramPerMicroliter)
        return self.__milli_grams_per_microliter

    
    @property
    def centi_grams_per_microliter(self) -> float:
        """
        
        """
        if self.__centi_grams_per_microliter != None:
            return self.__centi_grams_per_microliter
        self.__centi_grams_per_microliter = self.__convert_from_base(MassConcentrationUnits.CentiGramPerMicroliter)
        return self.__centi_grams_per_microliter

    
    @property
    def deci_grams_per_microliter(self) -> float:
        """
        
        """
        if self.__deci_grams_per_microliter != None:
            return self.__deci_grams_per_microliter
        self.__deci_grams_per_microliter = self.__convert_from_base(MassConcentrationUnits.DeciGramPerMicroliter)
        return self.__deci_grams_per_microliter

    
    @property
    def pico_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__pico_grams_per_milliliter != None:
            return self.__pico_grams_per_milliliter
        self.__pico_grams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.PicoGramPerMilliliter)
        return self.__pico_grams_per_milliliter

    
    @property
    def nano_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__nano_grams_per_milliliter != None:
            return self.__nano_grams_per_milliliter
        self.__nano_grams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.NanoGramPerMilliliter)
        return self.__nano_grams_per_milliliter

    
    @property
    def micro_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_milliliter != None:
            return self.__micro_grams_per_milliliter
        self.__micro_grams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.MicroGramPerMilliliter)
        return self.__micro_grams_per_milliliter

    
    @property
    def milli_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_milliliter != None:
            return self.__milli_grams_per_milliliter
        self.__milli_grams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.MilliGramPerMilliliter)
        return self.__milli_grams_per_milliliter

    
    @property
    def centi_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__centi_grams_per_milliliter != None:
            return self.__centi_grams_per_milliliter
        self.__centi_grams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.CentiGramPerMilliliter)
        return self.__centi_grams_per_milliliter

    
    @property
    def deci_grams_per_milliliter(self) -> float:
        """
        
        """
        if self.__deci_grams_per_milliliter != None:
            return self.__deci_grams_per_milliliter
        self.__deci_grams_per_milliliter = self.__convert_from_base(MassConcentrationUnits.DeciGramPerMilliliter)
        return self.__deci_grams_per_milliliter

    
    @property
    def pico_grams_per_deciliter(self) -> float:
        """
        
        """
        if self.__pico_grams_per_deciliter != None:
            return self.__pico_grams_per_deciliter
        self.__pico_grams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.PicoGramPerDeciliter)
        return self.__pico_grams_per_deciliter

    
    @property
    def nano_grams_per_deciliter(self) -> float:
        """
        
        """
        if self.__nano_grams_per_deciliter != None:
            return self.__nano_grams_per_deciliter
        self.__nano_grams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.NanoGramPerDeciliter)
        return self.__nano_grams_per_deciliter

    
    @property
    def micro_grams_per_deciliter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_deciliter != None:
            return self.__micro_grams_per_deciliter
        self.__micro_grams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.MicroGramPerDeciliter)
        return self.__micro_grams_per_deciliter

    
    @property
    def milli_grams_per_deciliter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_deciliter != None:
            return self.__milli_grams_per_deciliter
        self.__milli_grams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.MilliGramPerDeciliter)
        return self.__milli_grams_per_deciliter

    
    @property
    def centi_grams_per_deciliter(self) -> float:
        """
        
        """
        if self.__centi_grams_per_deciliter != None:
            return self.__centi_grams_per_deciliter
        self.__centi_grams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.CentiGramPerDeciliter)
        return self.__centi_grams_per_deciliter

    
    @property
    def deci_grams_per_deciliter(self) -> float:
        """
        
        """
        if self.__deci_grams_per_deciliter != None:
            return self.__deci_grams_per_deciliter
        self.__deci_grams_per_deciliter = self.__convert_from_base(MassConcentrationUnits.DeciGramPerDeciliter)
        return self.__deci_grams_per_deciliter

    
    @property
    def pico_grams_per_liter(self) -> float:
        """
        
        """
        if self.__pico_grams_per_liter != None:
            return self.__pico_grams_per_liter
        self.__pico_grams_per_liter = self.__convert_from_base(MassConcentrationUnits.PicoGramPerLiter)
        return self.__pico_grams_per_liter

    
    @property
    def nano_grams_per_liter(self) -> float:
        """
        
        """
        if self.__nano_grams_per_liter != None:
            return self.__nano_grams_per_liter
        self.__nano_grams_per_liter = self.__convert_from_base(MassConcentrationUnits.NanoGramPerLiter)
        return self.__nano_grams_per_liter

    
    @property
    def micro_grams_per_liter(self) -> float:
        """
        
        """
        if self.__micro_grams_per_liter != None:
            return self.__micro_grams_per_liter
        self.__micro_grams_per_liter = self.__convert_from_base(MassConcentrationUnits.MicroGramPerLiter)
        return self.__micro_grams_per_liter

    
    @property
    def milli_grams_per_liter(self) -> float:
        """
        
        """
        if self.__milli_grams_per_liter != None:
            return self.__milli_grams_per_liter
        self.__milli_grams_per_liter = self.__convert_from_base(MassConcentrationUnits.MilliGramPerLiter)
        return self.__milli_grams_per_liter

    
    @property
    def centi_grams_per_liter(self) -> float:
        """
        
        """
        if self.__centi_grams_per_liter != None:
            return self.__centi_grams_per_liter
        self.__centi_grams_per_liter = self.__convert_from_base(MassConcentrationUnits.CentiGramPerLiter)
        return self.__centi_grams_per_liter

    
    @property
    def deci_grams_per_liter(self) -> float:
        """
        
        """
        if self.__deci_grams_per_liter != None:
            return self.__deci_grams_per_liter
        self.__deci_grams_per_liter = self.__convert_from_base(MassConcentrationUnits.DeciGramPerLiter)
        return self.__deci_grams_per_liter

    
    @property
    def kilo_grams_per_liter(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_liter != None:
            return self.__kilo_grams_per_liter
        self.__kilo_grams_per_liter = self.__convert_from_base(MassConcentrationUnits.KiloGramPerLiter)
        return self.__kilo_grams_per_liter

    
    @property
    def kilo_pounds_per_cubic_inch(self) -> float:
        """
        
        """
        if self.__kilo_pounds_per_cubic_inch != None:
            return self.__kilo_pounds_per_cubic_inch
        self.__kilo_pounds_per_cubic_inch = self.__convert_from_base(MassConcentrationUnits.KiloPoundPerCubicInch)
        return self.__kilo_pounds_per_cubic_inch

    
    @property
    def kilo_pounds_per_cubic_foot(self) -> float:
        """
        
        """
        if self.__kilo_pounds_per_cubic_foot != None:
            return self.__kilo_pounds_per_cubic_foot
        self.__kilo_pounds_per_cubic_foot = self.__convert_from_base(MassConcentrationUnits.KiloPoundPerCubicFoot)
        return self.__kilo_pounds_per_cubic_foot

    
    def to_string(self, unit: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter) -> string:
        """
        Format the MassConcentration to string.
        Note! the default format for MassConcentration is KilogramPerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MassConcentrationUnits.GramPerCubicMillimeter:
            return f"""{self.grams_per_cubic_millimeter} g/mm³"""
        
        if unit == MassConcentrationUnits.GramPerCubicCentimeter:
            return f"""{self.grams_per_cubic_centimeter} g/cm³"""
        
        if unit == MassConcentrationUnits.GramPerCubicMeter:
            return f"""{self.grams_per_cubic_meter} g/m³"""
        
        if unit == MassConcentrationUnits.GramPerMicroliter:
            return f"""{self.grams_per_microliter} g/μL"""
        
        if unit == MassConcentrationUnits.GramPerMilliliter:
            return f"""{self.grams_per_milliliter} g/mL"""
        
        if unit == MassConcentrationUnits.GramPerDeciliter:
            return f"""{self.grams_per_deciliter} g/dL"""
        
        if unit == MassConcentrationUnits.GramPerLiter:
            return f"""{self.grams_per_liter} g/L"""
        
        if unit == MassConcentrationUnits.TonnePerCubicMillimeter:
            return f"""{self.tonnes_per_cubic_millimeter} t/mm³"""
        
        if unit == MassConcentrationUnits.TonnePerCubicCentimeter:
            return f"""{self.tonnes_per_cubic_centimeter} t/cm³"""
        
        if unit == MassConcentrationUnits.TonnePerCubicMeter:
            return f"""{self.tonnes_per_cubic_meter} t/m³"""
        
        if unit == MassConcentrationUnits.PoundPerCubicInch:
            return f"""{self.pounds_per_cubic_inch} lb/in³"""
        
        if unit == MassConcentrationUnits.PoundPerCubicFoot:
            return f"""{self.pounds_per_cubic_foot} lb/ft³"""
        
        if unit == MassConcentrationUnits.SlugPerCubicFoot:
            return f"""{self.slugs_per_cubic_foot} slug/ft³"""
        
        if unit == MassConcentrationUnits.PoundPerUSGallon:
            return f"""{self.pounds_per_us_gallon} ppg (U.S.)"""
        
        if unit == MassConcentrationUnits.OuncePerUSGallon:
            return f"""{self.ounces_per_us_gallon} oz/gal (U.S.)"""
        
        if unit == MassConcentrationUnits.OuncePerImperialGallon:
            return f"""{self.ounces_per_imperial_gallon} oz/gal (imp.)"""
        
        if unit == MassConcentrationUnits.PoundPerImperialGallon:
            return f"""{self.pounds_per_imperial_gallon} ppg (imp.)"""
        
        if unit == MassConcentrationUnits.KiloGramPerCubicMillimeter:
            return f"""{self.kilo_grams_per_cubic_millimeter} """
        
        if unit == MassConcentrationUnits.KiloGramPerCubicCentimeter:
            return f"""{self.kilo_grams_per_cubic_centimeter} """
        
        if unit == MassConcentrationUnits.KiloGramPerCubicMeter:
            return f"""{self.kilo_grams_per_cubic_meter} """
        
        if unit == MassConcentrationUnits.MilliGramPerCubicMeter:
            return f"""{self.milli_grams_per_cubic_meter} """
        
        if unit == MassConcentrationUnits.MicroGramPerCubicMeter:
            return f"""{self.micro_grams_per_cubic_meter} """
        
        if unit == MassConcentrationUnits.PicoGramPerMicroliter:
            return f"""{self.pico_grams_per_microliter} """
        
        if unit == MassConcentrationUnits.NanoGramPerMicroliter:
            return f"""{self.nano_grams_per_microliter} """
        
        if unit == MassConcentrationUnits.MicroGramPerMicroliter:
            return f"""{self.micro_grams_per_microliter} """
        
        if unit == MassConcentrationUnits.MilliGramPerMicroliter:
            return f"""{self.milli_grams_per_microliter} """
        
        if unit == MassConcentrationUnits.CentiGramPerMicroliter:
            return f"""{self.centi_grams_per_microliter} """
        
        if unit == MassConcentrationUnits.DeciGramPerMicroliter:
            return f"""{self.deci_grams_per_microliter} """
        
        if unit == MassConcentrationUnits.PicoGramPerMilliliter:
            return f"""{self.pico_grams_per_milliliter} """
        
        if unit == MassConcentrationUnits.NanoGramPerMilliliter:
            return f"""{self.nano_grams_per_milliliter} """
        
        if unit == MassConcentrationUnits.MicroGramPerMilliliter:
            return f"""{self.micro_grams_per_milliliter} """
        
        if unit == MassConcentrationUnits.MilliGramPerMilliliter:
            return f"""{self.milli_grams_per_milliliter} """
        
        if unit == MassConcentrationUnits.CentiGramPerMilliliter:
            return f"""{self.centi_grams_per_milliliter} """
        
        if unit == MassConcentrationUnits.DeciGramPerMilliliter:
            return f"""{self.deci_grams_per_milliliter} """
        
        if unit == MassConcentrationUnits.PicoGramPerDeciliter:
            return f"""{self.pico_grams_per_deciliter} """
        
        if unit == MassConcentrationUnits.NanoGramPerDeciliter:
            return f"""{self.nano_grams_per_deciliter} """
        
        if unit == MassConcentrationUnits.MicroGramPerDeciliter:
            return f"""{self.micro_grams_per_deciliter} """
        
        if unit == MassConcentrationUnits.MilliGramPerDeciliter:
            return f"""{self.milli_grams_per_deciliter} """
        
        if unit == MassConcentrationUnits.CentiGramPerDeciliter:
            return f"""{self.centi_grams_per_deciliter} """
        
        if unit == MassConcentrationUnits.DeciGramPerDeciliter:
            return f"""{self.deci_grams_per_deciliter} """
        
        if unit == MassConcentrationUnits.PicoGramPerLiter:
            return f"""{self.pico_grams_per_liter} """
        
        if unit == MassConcentrationUnits.NanoGramPerLiter:
            return f"""{self.nano_grams_per_liter} """
        
        if unit == MassConcentrationUnits.MicroGramPerLiter:
            return f"""{self.micro_grams_per_liter} """
        
        if unit == MassConcentrationUnits.MilliGramPerLiter:
            return f"""{self.milli_grams_per_liter} """
        
        if unit == MassConcentrationUnits.CentiGramPerLiter:
            return f"""{self.centi_grams_per_liter} """
        
        if unit == MassConcentrationUnits.DeciGramPerLiter:
            return f"""{self.deci_grams_per_liter} """
        
        if unit == MassConcentrationUnits.KiloGramPerLiter:
            return f"""{self.kilo_grams_per_liter} """
        
        if unit == MassConcentrationUnits.KiloPoundPerCubicInch:
            return f"""{self.kilo_pounds_per_cubic_inch} """
        
        if unit == MassConcentrationUnits.KiloPoundPerCubicFoot:
            return f"""{self.kilo_pounds_per_cubic_foot} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassConcentrationUnits = MassConcentrationUnits.KilogramPerCubicMeter) -> string:
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
        
        if unit_abbreviation == MassConcentrationUnits.KiloGramPerCubicMillimeter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.KiloGramPerCubicCentimeter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.KiloGramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MilliGramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MicroGramPerCubicMeter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.PicoGramPerMicroliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.NanoGramPerMicroliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MicroGramPerMicroliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MilliGramPerMicroliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.CentiGramPerMicroliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.DeciGramPerMicroliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.PicoGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.NanoGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MicroGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MilliGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.CentiGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.DeciGramPerMilliliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.PicoGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.NanoGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MicroGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MilliGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.CentiGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.DeciGramPerDeciliter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.PicoGramPerLiter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.NanoGramPerLiter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MicroGramPerLiter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.MilliGramPerLiter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.CentiGramPerLiter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.DeciGramPerLiter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.KiloGramPerLiter:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.KiloPoundPerCubicInch:
            return """"""
        
        if unit_abbreviation == MassConcentrationUnits.KiloPoundPerCubicFoot:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for +: 'MassConcentration' and '{}'".format(type(other).__name__))
        return MassConcentration(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for *: 'MassConcentration' and '{}'".format(type(other).__name__))
        return MassConcentration(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for -: 'MassConcentration' and '{}'".format(type(other).__name__))
        return MassConcentration(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for /: 'MassConcentration' and '{}'".format(type(other).__name__))
        return MassConcentration(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for %: 'MassConcentration' and '{}'".format(type(other).__name__))
        return MassConcentration(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for **: 'MassConcentration' and '{}'".format(type(other).__name__))
        return MassConcentration(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for ==: 'MassConcentration' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for <: 'MassConcentration' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for >: 'MassConcentration' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for <=: 'MassConcentration' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MassConcentration):
            raise TypeError("unsupported operand type(s) for >=: 'MassConcentration' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value