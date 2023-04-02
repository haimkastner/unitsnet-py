from enum import Enum
import math
import string


class MassFractionUnits(Enum):
        """
            MassFractionUnits enumeration
        """
        
        DecimalFraction = 'decimal_fraction'
        """
            
        """
        
        GramPerGram = 'gram_per_gram'
        """
            
        """
        
        GramPerKilogram = 'gram_per_kilogram'
        """
            
        """
        
        Percent = 'percent'
        """
            
        """
        
        PartPerThousand = 'part_per_thousand'
        """
            
        """
        
        PartPerMillion = 'part_per_million'
        """
            
        """
        
        PartPerBillion = 'part_per_billion'
        """
            
        """
        
        PartPerTrillion = 'part_per_trillion'
        """
            
        """
        
        NanoGramPerGram = 'nano_gram_per_gram'
        """
            
        """
        
        MicroGramPerGram = 'micro_gram_per_gram'
        """
            
        """
        
        MilliGramPerGram = 'milli_gram_per_gram'
        """
            
        """
        
        CentiGramPerGram = 'centi_gram_per_gram'
        """
            
        """
        
        DeciGramPerGram = 'deci_gram_per_gram'
        """
            
        """
        
        DecaGramPerGram = 'deca_gram_per_gram'
        """
            
        """
        
        HectoGramPerGram = 'hecto_gram_per_gram'
        """
            
        """
        
        KiloGramPerGram = 'kilo_gram_per_gram'
        """
            
        """
        
        NanoGramPerKilogram = 'nano_gram_per_kilogram'
        """
            
        """
        
        MicroGramPerKilogram = 'micro_gram_per_kilogram'
        """
            
        """
        
        MilliGramPerKilogram = 'milli_gram_per_kilogram'
        """
            
        """
        
        CentiGramPerKilogram = 'centi_gram_per_kilogram'
        """
            
        """
        
        DeciGramPerKilogram = 'deci_gram_per_kilogram'
        """
            
        """
        
        DecaGramPerKilogram = 'deca_gram_per_kilogram'
        """
            
        """
        
        HectoGramPerKilogram = 'hecto_gram_per_kilogram'
        """
            
        """
        
        KiloGramPerKilogram = 'kilo_gram_per_kilogram'
        """
            
        """
        

class MassFraction:
    """
    The mass fraction is defined as the mass of a constituent divided by the total mass of the mixture.

    Args:
        value (float): The value.
        from_unit (MassFractionUnits): The MassFraction unit to create from, The default unit is DecimalFraction
    """
    def __init__(self, value: float, from_unit: MassFractionUnits = MassFractionUnits.DecimalFraction):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__decimal_fractions = None
        
        self.__grams_per_gram = None
        
        self.__grams_per_kilogram = None
        
        self.__percent = None
        
        self.__parts_per_thousand = None
        
        self.__parts_per_million = None
        
        self.__parts_per_billion = None
        
        self.__parts_per_trillion = None
        
        self.__nano_grams_per_gram = None
        
        self.__micro_grams_per_gram = None
        
        self.__milli_grams_per_gram = None
        
        self.__centi_grams_per_gram = None
        
        self.__deci_grams_per_gram = None
        
        self.__deca_grams_per_gram = None
        
        self.__hecto_grams_per_gram = None
        
        self.__kilo_grams_per_gram = None
        
        self.__nano_grams_per_kilogram = None
        
        self.__micro_grams_per_kilogram = None
        
        self.__milli_grams_per_kilogram = None
        
        self.__centi_grams_per_kilogram = None
        
        self.__deci_grams_per_kilogram = None
        
        self.__deca_grams_per_kilogram = None
        
        self.__hecto_grams_per_kilogram = None
        
        self.__kilo_grams_per_kilogram = None
        

    def __convert_from_base(self, from_unit: MassFractionUnits) -> float:
        value = self.__value
        
        if from_unit == MassFractionUnits.DecimalFraction:
            return (value)
        
        if from_unit == MassFractionUnits.GramPerGram:
            return (value)
        
        if from_unit == MassFractionUnits.GramPerKilogram:
            return (value * 1e3)
        
        if from_unit == MassFractionUnits.Percent:
            return (value * 1e2)
        
        if from_unit == MassFractionUnits.PartPerThousand:
            return (value * 1e3)
        
        if from_unit == MassFractionUnits.PartPerMillion:
            return (value * 1e6)
        
        if from_unit == MassFractionUnits.PartPerBillion:
            return (value * 1e9)
        
        if from_unit == MassFractionUnits.PartPerTrillion:
            return (value * 1e12)
        
        if from_unit == MassFractionUnits.NanoGramPerGram:
            return ((value) / 1e-09)
        
        if from_unit == MassFractionUnits.MicroGramPerGram:
            return ((value) / 1e-06)
        
        if from_unit == MassFractionUnits.MilliGramPerGram:
            return ((value) / 0.001)
        
        if from_unit == MassFractionUnits.CentiGramPerGram:
            return ((value) / 0.01)
        
        if from_unit == MassFractionUnits.DeciGramPerGram:
            return ((value) / 0.1)
        
        if from_unit == MassFractionUnits.DecaGramPerGram:
            return ((value) / 10.0)
        
        if from_unit == MassFractionUnits.HectoGramPerGram:
            return ((value) / 100.0)
        
        if from_unit == MassFractionUnits.KiloGramPerGram:
            return ((value) / 1000.0)
        
        if from_unit == MassFractionUnits.NanoGramPerKilogram:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == MassFractionUnits.MicroGramPerKilogram:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MassFractionUnits.MilliGramPerKilogram:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassFractionUnits.CentiGramPerKilogram:
            return ((value * 1e3) / 0.01)
        
        if from_unit == MassFractionUnits.DeciGramPerKilogram:
            return ((value * 1e3) / 0.1)
        
        if from_unit == MassFractionUnits.DecaGramPerKilogram:
            return ((value * 1e3) / 10.0)
        
        if from_unit == MassFractionUnits.HectoGramPerKilogram:
            return ((value * 1e3) / 100.0)
        
        if from_unit == MassFractionUnits.KiloGramPerKilogram:
            return ((value * 1e3) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassFractionUnits) -> float:
        
        if to_unit == MassFractionUnits.DecimalFraction:
            return (value)
        
        if to_unit == MassFractionUnits.GramPerGram:
            return (value)
        
        if to_unit == MassFractionUnits.GramPerKilogram:
            return (value / 1e3)
        
        if to_unit == MassFractionUnits.Percent:
            return (value / 1e2)
        
        if to_unit == MassFractionUnits.PartPerThousand:
            return (value / 1e3)
        
        if to_unit == MassFractionUnits.PartPerMillion:
            return (value / 1e6)
        
        if to_unit == MassFractionUnits.PartPerBillion:
            return (value / 1e9)
        
        if to_unit == MassFractionUnits.PartPerTrillion:
            return (value / 1e12)
        
        if to_unit == MassFractionUnits.NanoGramPerGram:
            return ((value) * 1e-09)
        
        if to_unit == MassFractionUnits.MicroGramPerGram:
            return ((value) * 1e-06)
        
        if to_unit == MassFractionUnits.MilliGramPerGram:
            return ((value) * 0.001)
        
        if to_unit == MassFractionUnits.CentiGramPerGram:
            return ((value) * 0.01)
        
        if to_unit == MassFractionUnits.DeciGramPerGram:
            return ((value) * 0.1)
        
        if to_unit == MassFractionUnits.DecaGramPerGram:
            return ((value) * 10.0)
        
        if to_unit == MassFractionUnits.HectoGramPerGram:
            return ((value) * 100.0)
        
        if to_unit == MassFractionUnits.KiloGramPerGram:
            return ((value) * 1000.0)
        
        if to_unit == MassFractionUnits.NanoGramPerKilogram:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == MassFractionUnits.MicroGramPerKilogram:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MassFractionUnits.MilliGramPerKilogram:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassFractionUnits.CentiGramPerKilogram:
            return ((value / 1e3) * 0.01)
        
        if to_unit == MassFractionUnits.DeciGramPerKilogram:
            return ((value / 1e3) * 0.1)
        
        if to_unit == MassFractionUnits.DecaGramPerKilogram:
            return ((value / 1e3) * 10.0)
        
        if to_unit == MassFractionUnits.HectoGramPerKilogram:
            return ((value / 1e3) * 100.0)
        
        if to_unit == MassFractionUnits.KiloGramPerKilogram:
            return ((value / 1e3) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_decimal_fractions(decimal_fractions: float):
        """
        Create a new instance of MassFraction from a value in decimal_fractions.

        

        :param meters: The MassFraction value in decimal_fractions.
        :type decimal_fractions: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(decimal_fractions, MassFractionUnits.DecimalFraction)

    
    @staticmethod
    def from_grams_per_gram(grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in grams_per_gram.

        

        :param meters: The MassFraction value in grams_per_gram.
        :type grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(grams_per_gram, MassFractionUnits.GramPerGram)

    
    @staticmethod
    def from_grams_per_kilogram(grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in grams_per_kilogram.

        

        :param meters: The MassFraction value in grams_per_kilogram.
        :type grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(grams_per_kilogram, MassFractionUnits.GramPerKilogram)

    
    @staticmethod
    def from_percent(percent: float):
        """
        Create a new instance of MassFraction from a value in percent.

        

        :param meters: The MassFraction value in percent.
        :type percent: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(percent, MassFractionUnits.Percent)

    
    @staticmethod
    def from_parts_per_thousand(parts_per_thousand: float):
        """
        Create a new instance of MassFraction from a value in parts_per_thousand.

        

        :param meters: The MassFraction value in parts_per_thousand.
        :type parts_per_thousand: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(parts_per_thousand, MassFractionUnits.PartPerThousand)

    
    @staticmethod
    def from_parts_per_million(parts_per_million: float):
        """
        Create a new instance of MassFraction from a value in parts_per_million.

        

        :param meters: The MassFraction value in parts_per_million.
        :type parts_per_million: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(parts_per_million, MassFractionUnits.PartPerMillion)

    
    @staticmethod
    def from_parts_per_billion(parts_per_billion: float):
        """
        Create a new instance of MassFraction from a value in parts_per_billion.

        

        :param meters: The MassFraction value in parts_per_billion.
        :type parts_per_billion: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(parts_per_billion, MassFractionUnits.PartPerBillion)

    
    @staticmethod
    def from_parts_per_trillion(parts_per_trillion: float):
        """
        Create a new instance of MassFraction from a value in parts_per_trillion.

        

        :param meters: The MassFraction value in parts_per_trillion.
        :type parts_per_trillion: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(parts_per_trillion, MassFractionUnits.PartPerTrillion)

    
    @staticmethod
    def from_nano_grams_per_gram(nano_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in nano_grams_per_gram.

        

        :param meters: The MassFraction value in nano_grams_per_gram.
        :type nano_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(nano_grams_per_gram, MassFractionUnits.NanoGramPerGram)

    
    @staticmethod
    def from_micro_grams_per_gram(micro_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in micro_grams_per_gram.

        

        :param meters: The MassFraction value in micro_grams_per_gram.
        :type micro_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(micro_grams_per_gram, MassFractionUnits.MicroGramPerGram)

    
    @staticmethod
    def from_milli_grams_per_gram(milli_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in milli_grams_per_gram.

        

        :param meters: The MassFraction value in milli_grams_per_gram.
        :type milli_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(milli_grams_per_gram, MassFractionUnits.MilliGramPerGram)

    
    @staticmethod
    def from_centi_grams_per_gram(centi_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in centi_grams_per_gram.

        

        :param meters: The MassFraction value in centi_grams_per_gram.
        :type centi_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(centi_grams_per_gram, MassFractionUnits.CentiGramPerGram)

    
    @staticmethod
    def from_deci_grams_per_gram(deci_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in deci_grams_per_gram.

        

        :param meters: The MassFraction value in deci_grams_per_gram.
        :type deci_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(deci_grams_per_gram, MassFractionUnits.DeciGramPerGram)

    
    @staticmethod
    def from_deca_grams_per_gram(deca_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in deca_grams_per_gram.

        

        :param meters: The MassFraction value in deca_grams_per_gram.
        :type deca_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(deca_grams_per_gram, MassFractionUnits.DecaGramPerGram)

    
    @staticmethod
    def from_hecto_grams_per_gram(hecto_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in hecto_grams_per_gram.

        

        :param meters: The MassFraction value in hecto_grams_per_gram.
        :type hecto_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(hecto_grams_per_gram, MassFractionUnits.HectoGramPerGram)

    
    @staticmethod
    def from_kilo_grams_per_gram(kilo_grams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in kilo_grams_per_gram.

        

        :param meters: The MassFraction value in kilo_grams_per_gram.
        :type kilo_grams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(kilo_grams_per_gram, MassFractionUnits.KiloGramPerGram)

    
    @staticmethod
    def from_nano_grams_per_kilogram(nano_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in nano_grams_per_kilogram.

        

        :param meters: The MassFraction value in nano_grams_per_kilogram.
        :type nano_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(nano_grams_per_kilogram, MassFractionUnits.NanoGramPerKilogram)

    
    @staticmethod
    def from_micro_grams_per_kilogram(micro_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in micro_grams_per_kilogram.

        

        :param meters: The MassFraction value in micro_grams_per_kilogram.
        :type micro_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(micro_grams_per_kilogram, MassFractionUnits.MicroGramPerKilogram)

    
    @staticmethod
    def from_milli_grams_per_kilogram(milli_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in milli_grams_per_kilogram.

        

        :param meters: The MassFraction value in milli_grams_per_kilogram.
        :type milli_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(milli_grams_per_kilogram, MassFractionUnits.MilliGramPerKilogram)

    
    @staticmethod
    def from_centi_grams_per_kilogram(centi_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in centi_grams_per_kilogram.

        

        :param meters: The MassFraction value in centi_grams_per_kilogram.
        :type centi_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(centi_grams_per_kilogram, MassFractionUnits.CentiGramPerKilogram)

    
    @staticmethod
    def from_deci_grams_per_kilogram(deci_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in deci_grams_per_kilogram.

        

        :param meters: The MassFraction value in deci_grams_per_kilogram.
        :type deci_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(deci_grams_per_kilogram, MassFractionUnits.DeciGramPerKilogram)

    
    @staticmethod
    def from_deca_grams_per_kilogram(deca_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in deca_grams_per_kilogram.

        

        :param meters: The MassFraction value in deca_grams_per_kilogram.
        :type deca_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(deca_grams_per_kilogram, MassFractionUnits.DecaGramPerKilogram)

    
    @staticmethod
    def from_hecto_grams_per_kilogram(hecto_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in hecto_grams_per_kilogram.

        

        :param meters: The MassFraction value in hecto_grams_per_kilogram.
        :type hecto_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(hecto_grams_per_kilogram, MassFractionUnits.HectoGramPerKilogram)

    
    @staticmethod
    def from_kilo_grams_per_kilogram(kilo_grams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in kilo_grams_per_kilogram.

        

        :param meters: The MassFraction value in kilo_grams_per_kilogram.
        :type kilo_grams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(kilo_grams_per_kilogram, MassFractionUnits.KiloGramPerKilogram)

    
    @property
    def decimal_fractions(self) -> float:
        """
        
        """
        if self.__decimal_fractions != None:
            return self.__decimal_fractions
        self.__decimal_fractions = self.__convert_from_base(MassFractionUnits.DecimalFraction)
        return self.__decimal_fractions

    
    @property
    def grams_per_gram(self) -> float:
        """
        
        """
        if self.__grams_per_gram != None:
            return self.__grams_per_gram
        self.__grams_per_gram = self.__convert_from_base(MassFractionUnits.GramPerGram)
        return self.__grams_per_gram

    
    @property
    def grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__grams_per_kilogram != None:
            return self.__grams_per_kilogram
        self.__grams_per_kilogram = self.__convert_from_base(MassFractionUnits.GramPerKilogram)
        return self.__grams_per_kilogram

    
    @property
    def percent(self) -> float:
        """
        
        """
        if self.__percent != None:
            return self.__percent
        self.__percent = self.__convert_from_base(MassFractionUnits.Percent)
        return self.__percent

    
    @property
    def parts_per_thousand(self) -> float:
        """
        
        """
        if self.__parts_per_thousand != None:
            return self.__parts_per_thousand
        self.__parts_per_thousand = self.__convert_from_base(MassFractionUnits.PartPerThousand)
        return self.__parts_per_thousand

    
    @property
    def parts_per_million(self) -> float:
        """
        
        """
        if self.__parts_per_million != None:
            return self.__parts_per_million
        self.__parts_per_million = self.__convert_from_base(MassFractionUnits.PartPerMillion)
        return self.__parts_per_million

    
    @property
    def parts_per_billion(self) -> float:
        """
        
        """
        if self.__parts_per_billion != None:
            return self.__parts_per_billion
        self.__parts_per_billion = self.__convert_from_base(MassFractionUnits.PartPerBillion)
        return self.__parts_per_billion

    
    @property
    def parts_per_trillion(self) -> float:
        """
        
        """
        if self.__parts_per_trillion != None:
            return self.__parts_per_trillion
        self.__parts_per_trillion = self.__convert_from_base(MassFractionUnits.PartPerTrillion)
        return self.__parts_per_trillion

    
    @property
    def nano_grams_per_gram(self) -> float:
        """
        
        """
        if self.__nano_grams_per_gram != None:
            return self.__nano_grams_per_gram
        self.__nano_grams_per_gram = self.__convert_from_base(MassFractionUnits.NanoGramPerGram)
        return self.__nano_grams_per_gram

    
    @property
    def micro_grams_per_gram(self) -> float:
        """
        
        """
        if self.__micro_grams_per_gram != None:
            return self.__micro_grams_per_gram
        self.__micro_grams_per_gram = self.__convert_from_base(MassFractionUnits.MicroGramPerGram)
        return self.__micro_grams_per_gram

    
    @property
    def milli_grams_per_gram(self) -> float:
        """
        
        """
        if self.__milli_grams_per_gram != None:
            return self.__milli_grams_per_gram
        self.__milli_grams_per_gram = self.__convert_from_base(MassFractionUnits.MilliGramPerGram)
        return self.__milli_grams_per_gram

    
    @property
    def centi_grams_per_gram(self) -> float:
        """
        
        """
        if self.__centi_grams_per_gram != None:
            return self.__centi_grams_per_gram
        self.__centi_grams_per_gram = self.__convert_from_base(MassFractionUnits.CentiGramPerGram)
        return self.__centi_grams_per_gram

    
    @property
    def deci_grams_per_gram(self) -> float:
        """
        
        """
        if self.__deci_grams_per_gram != None:
            return self.__deci_grams_per_gram
        self.__deci_grams_per_gram = self.__convert_from_base(MassFractionUnits.DeciGramPerGram)
        return self.__deci_grams_per_gram

    
    @property
    def deca_grams_per_gram(self) -> float:
        """
        
        """
        if self.__deca_grams_per_gram != None:
            return self.__deca_grams_per_gram
        self.__deca_grams_per_gram = self.__convert_from_base(MassFractionUnits.DecaGramPerGram)
        return self.__deca_grams_per_gram

    
    @property
    def hecto_grams_per_gram(self) -> float:
        """
        
        """
        if self.__hecto_grams_per_gram != None:
            return self.__hecto_grams_per_gram
        self.__hecto_grams_per_gram = self.__convert_from_base(MassFractionUnits.HectoGramPerGram)
        return self.__hecto_grams_per_gram

    
    @property
    def kilo_grams_per_gram(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_gram != None:
            return self.__kilo_grams_per_gram
        self.__kilo_grams_per_gram = self.__convert_from_base(MassFractionUnits.KiloGramPerGram)
        return self.__kilo_grams_per_gram

    
    @property
    def nano_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__nano_grams_per_kilogram != None:
            return self.__nano_grams_per_kilogram
        self.__nano_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.NanoGramPerKilogram)
        return self.__nano_grams_per_kilogram

    
    @property
    def micro_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__micro_grams_per_kilogram != None:
            return self.__micro_grams_per_kilogram
        self.__micro_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.MicroGramPerKilogram)
        return self.__micro_grams_per_kilogram

    
    @property
    def milli_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__milli_grams_per_kilogram != None:
            return self.__milli_grams_per_kilogram
        self.__milli_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.MilliGramPerKilogram)
        return self.__milli_grams_per_kilogram

    
    @property
    def centi_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__centi_grams_per_kilogram != None:
            return self.__centi_grams_per_kilogram
        self.__centi_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.CentiGramPerKilogram)
        return self.__centi_grams_per_kilogram

    
    @property
    def deci_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__deci_grams_per_kilogram != None:
            return self.__deci_grams_per_kilogram
        self.__deci_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.DeciGramPerKilogram)
        return self.__deci_grams_per_kilogram

    
    @property
    def deca_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__deca_grams_per_kilogram != None:
            return self.__deca_grams_per_kilogram
        self.__deca_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.DecaGramPerKilogram)
        return self.__deca_grams_per_kilogram

    
    @property
    def hecto_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__hecto_grams_per_kilogram != None:
            return self.__hecto_grams_per_kilogram
        self.__hecto_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.HectoGramPerKilogram)
        return self.__hecto_grams_per_kilogram

    
    @property
    def kilo_grams_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_kilogram != None:
            return self.__kilo_grams_per_kilogram
        self.__kilo_grams_per_kilogram = self.__convert_from_base(MassFractionUnits.KiloGramPerKilogram)
        return self.__kilo_grams_per_kilogram

    
    def to_string(self, unit: MassFractionUnits = MassFractionUnits.DecimalFraction) -> string:
        """
        Format the MassFraction to string.
        Note! the default format for MassFraction is DecimalFraction.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MassFractionUnits.DecimalFraction:
            return f"""{self.decimal_fractions} """
        
        if unit == MassFractionUnits.GramPerGram:
            return f"""{self.grams_per_gram} g/g"""
        
        if unit == MassFractionUnits.GramPerKilogram:
            return f"""{self.grams_per_kilogram} g/kg"""
        
        if unit == MassFractionUnits.Percent:
            return f"""{self.percent} %"""
        
        if unit == MassFractionUnits.PartPerThousand:
            return f"""{self.parts_per_thousand} ‰"""
        
        if unit == MassFractionUnits.PartPerMillion:
            return f"""{self.parts_per_million} ppm"""
        
        if unit == MassFractionUnits.PartPerBillion:
            return f"""{self.parts_per_billion} ppb"""
        
        if unit == MassFractionUnits.PartPerTrillion:
            return f"""{self.parts_per_trillion} ppt"""
        
        if unit == MassFractionUnits.NanoGramPerGram:
            return f"""{self.nano_grams_per_gram} """
        
        if unit == MassFractionUnits.MicroGramPerGram:
            return f"""{self.micro_grams_per_gram} """
        
        if unit == MassFractionUnits.MilliGramPerGram:
            return f"""{self.milli_grams_per_gram} """
        
        if unit == MassFractionUnits.CentiGramPerGram:
            return f"""{self.centi_grams_per_gram} """
        
        if unit == MassFractionUnits.DeciGramPerGram:
            return f"""{self.deci_grams_per_gram} """
        
        if unit == MassFractionUnits.DecaGramPerGram:
            return f"""{self.deca_grams_per_gram} """
        
        if unit == MassFractionUnits.HectoGramPerGram:
            return f"""{self.hecto_grams_per_gram} """
        
        if unit == MassFractionUnits.KiloGramPerGram:
            return f"""{self.kilo_grams_per_gram} """
        
        if unit == MassFractionUnits.NanoGramPerKilogram:
            return f"""{self.nano_grams_per_kilogram} """
        
        if unit == MassFractionUnits.MicroGramPerKilogram:
            return f"""{self.micro_grams_per_kilogram} """
        
        if unit == MassFractionUnits.MilliGramPerKilogram:
            return f"""{self.milli_grams_per_kilogram} """
        
        if unit == MassFractionUnits.CentiGramPerKilogram:
            return f"""{self.centi_grams_per_kilogram} """
        
        if unit == MassFractionUnits.DeciGramPerKilogram:
            return f"""{self.deci_grams_per_kilogram} """
        
        if unit == MassFractionUnits.DecaGramPerKilogram:
            return f"""{self.deca_grams_per_kilogram} """
        
        if unit == MassFractionUnits.HectoGramPerKilogram:
            return f"""{self.hecto_grams_per_kilogram} """
        
        if unit == MassFractionUnits.KiloGramPerKilogram:
            return f"""{self.kilo_grams_per_kilogram} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassFractionUnits = MassFractionUnits.DecimalFraction) -> string:
        """
        Get MassFraction unit abbreviation.
        Note! the default abbreviation for MassFraction is DecimalFraction.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassFractionUnits.DecimalFraction:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.GramPerGram:
            return """g/g"""
        
        if unit_abbreviation == MassFractionUnits.GramPerKilogram:
            return """g/kg"""
        
        if unit_abbreviation == MassFractionUnits.Percent:
            return """%"""
        
        if unit_abbreviation == MassFractionUnits.PartPerThousand:
            return """‰"""
        
        if unit_abbreviation == MassFractionUnits.PartPerMillion:
            return """ppm"""
        
        if unit_abbreviation == MassFractionUnits.PartPerBillion:
            return """ppb"""
        
        if unit_abbreviation == MassFractionUnits.PartPerTrillion:
            return """ppt"""
        
        if unit_abbreviation == MassFractionUnits.NanoGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.MicroGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.MilliGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.CentiGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.DeciGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.DecaGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.HectoGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.KiloGramPerGram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.NanoGramPerKilogram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.MicroGramPerKilogram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.MilliGramPerKilogram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.CentiGramPerKilogram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.DeciGramPerKilogram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.DecaGramPerKilogram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.HectoGramPerKilogram:
            return """"""
        
        if unit_abbreviation == MassFractionUnits.KiloGramPerKilogram:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for +: 'MassFraction' and '{}'".format(type(other).__name__))
        return MassFraction(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for *: 'MassFraction' and '{}'".format(type(other).__name__))
        return MassFraction(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for -: 'MassFraction' and '{}'".format(type(other).__name__))
        return MassFraction(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for /: 'MassFraction' and '{}'".format(type(other).__name__))
        return MassFraction(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for %: 'MassFraction' and '{}'".format(type(other).__name__))
        return MassFraction(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for **: 'MassFraction' and '{}'".format(type(other).__name__))
        return MassFraction(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for ==: 'MassFraction' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for <: 'MassFraction' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for >: 'MassFraction' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for <=: 'MassFraction' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MassFraction):
            raise TypeError("unsupported operand type(s) for >=: 'MassFraction' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value