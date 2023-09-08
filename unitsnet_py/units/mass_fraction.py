from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



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
        
        NanogramPerGram = 'nanogram_per_gram'
        """
            
        """
        
        MicrogramPerGram = 'microgram_per_gram'
        """
            
        """
        
        MilligramPerGram = 'milligram_per_gram'
        """
            
        """
        
        CentigramPerGram = 'centigram_per_gram'
        """
            
        """
        
        DecigramPerGram = 'decigram_per_gram'
        """
            
        """
        
        DecagramPerGram = 'decagram_per_gram'
        """
            
        """
        
        HectogramPerGram = 'hectogram_per_gram'
        """
            
        """
        
        KilogramPerGram = 'kilogram_per_gram'
        """
            
        """
        
        NanogramPerKilogram = 'nanogram_per_kilogram'
        """
            
        """
        
        MicrogramPerKilogram = 'microgram_per_kilogram'
        """
            
        """
        
        MilligramPerKilogram = 'milligram_per_kilogram'
        """
            
        """
        
        CentigramPerKilogram = 'centigram_per_kilogram'
        """
            
        """
        
        DecigramPerKilogram = 'decigram_per_kilogram'
        """
            
        """
        
        DecagramPerKilogram = 'decagram_per_kilogram'
        """
            
        """
        
        HectogramPerKilogram = 'hectogram_per_kilogram'
        """
            
        """
        
        KilogramPerKilogram = 'kilogram_per_kilogram'
        """
            
        """
        

class MassFraction(AbstractMeasure):
    """
    The mass fraction is defined as the mass of a constituent divided by the total mass of the mixture.

    Args:
        value (float): The value.
        from_unit (MassFractionUnits): The MassFraction unit to create from, The default unit is DecimalFraction
    """
    def __init__(self, value: float, from_unit: MassFractionUnits = MassFractionUnits.DecimalFraction):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decimal_fractions = None
        
        self.__grams_per_gram = None
        
        self.__grams_per_kilogram = None
        
        self.__percent = None
        
        self.__parts_per_thousand = None
        
        self.__parts_per_million = None
        
        self.__parts_per_billion = None
        
        self.__parts_per_trillion = None
        
        self.__nanograms_per_gram = None
        
        self.__micrograms_per_gram = None
        
        self.__milligrams_per_gram = None
        
        self.__centigrams_per_gram = None
        
        self.__decigrams_per_gram = None
        
        self.__decagrams_per_gram = None
        
        self.__hectograms_per_gram = None
        
        self.__kilograms_per_gram = None
        
        self.__nanograms_per_kilogram = None
        
        self.__micrograms_per_kilogram = None
        
        self.__milligrams_per_kilogram = None
        
        self.__centigrams_per_kilogram = None
        
        self.__decigrams_per_kilogram = None
        
        self.__decagrams_per_kilogram = None
        
        self.__hectograms_per_kilogram = None
        
        self.__kilograms_per_kilogram = None
        

    def convert(self, unit: MassFractionUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: MassFractionUnits) -> float:
        value = self._value
        
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
        
        if from_unit == MassFractionUnits.NanogramPerGram:
            return ((value) / 1e-09)
        
        if from_unit == MassFractionUnits.MicrogramPerGram:
            return ((value) / 1e-06)
        
        if from_unit == MassFractionUnits.MilligramPerGram:
            return ((value) / 0.001)
        
        if from_unit == MassFractionUnits.CentigramPerGram:
            return ((value) / 0.01)
        
        if from_unit == MassFractionUnits.DecigramPerGram:
            return ((value) / 0.1)
        
        if from_unit == MassFractionUnits.DecagramPerGram:
            return ((value) / 10.0)
        
        if from_unit == MassFractionUnits.HectogramPerGram:
            return ((value) / 100.0)
        
        if from_unit == MassFractionUnits.KilogramPerGram:
            return ((value) / 1000.0)
        
        if from_unit == MassFractionUnits.NanogramPerKilogram:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == MassFractionUnits.MicrogramPerKilogram:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MassFractionUnits.MilligramPerKilogram:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassFractionUnits.CentigramPerKilogram:
            return ((value * 1e3) / 0.01)
        
        if from_unit == MassFractionUnits.DecigramPerKilogram:
            return ((value * 1e3) / 0.1)
        
        if from_unit == MassFractionUnits.DecagramPerKilogram:
            return ((value * 1e3) / 10.0)
        
        if from_unit == MassFractionUnits.HectogramPerKilogram:
            return ((value * 1e3) / 100.0)
        
        if from_unit == MassFractionUnits.KilogramPerKilogram:
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
        
        if to_unit == MassFractionUnits.NanogramPerGram:
            return ((value) * 1e-09)
        
        if to_unit == MassFractionUnits.MicrogramPerGram:
            return ((value) * 1e-06)
        
        if to_unit == MassFractionUnits.MilligramPerGram:
            return ((value) * 0.001)
        
        if to_unit == MassFractionUnits.CentigramPerGram:
            return ((value) * 0.01)
        
        if to_unit == MassFractionUnits.DecigramPerGram:
            return ((value) * 0.1)
        
        if to_unit == MassFractionUnits.DecagramPerGram:
            return ((value) * 10.0)
        
        if to_unit == MassFractionUnits.HectogramPerGram:
            return ((value) * 100.0)
        
        if to_unit == MassFractionUnits.KilogramPerGram:
            return ((value) * 1000.0)
        
        if to_unit == MassFractionUnits.NanogramPerKilogram:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == MassFractionUnits.MicrogramPerKilogram:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MassFractionUnits.MilligramPerKilogram:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassFractionUnits.CentigramPerKilogram:
            return ((value / 1e3) * 0.01)
        
        if to_unit == MassFractionUnits.DecigramPerKilogram:
            return ((value / 1e3) * 0.1)
        
        if to_unit == MassFractionUnits.DecagramPerKilogram:
            return ((value / 1e3) * 10.0)
        
        if to_unit == MassFractionUnits.HectogramPerKilogram:
            return ((value / 1e3) * 100.0)
        
        if to_unit == MassFractionUnits.KilogramPerKilogram:
            return ((value / 1e3) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_nanograms_per_gram(nanograms_per_gram: float):
        """
        Create a new instance of MassFraction from a value in nanograms_per_gram.

        

        :param meters: The MassFraction value in nanograms_per_gram.
        :type nanograms_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(nanograms_per_gram, MassFractionUnits.NanogramPerGram)

    
    @staticmethod
    def from_micrograms_per_gram(micrograms_per_gram: float):
        """
        Create a new instance of MassFraction from a value in micrograms_per_gram.

        

        :param meters: The MassFraction value in micrograms_per_gram.
        :type micrograms_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(micrograms_per_gram, MassFractionUnits.MicrogramPerGram)

    
    @staticmethod
    def from_milligrams_per_gram(milligrams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in milligrams_per_gram.

        

        :param meters: The MassFraction value in milligrams_per_gram.
        :type milligrams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(milligrams_per_gram, MassFractionUnits.MilligramPerGram)

    
    @staticmethod
    def from_centigrams_per_gram(centigrams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in centigrams_per_gram.

        

        :param meters: The MassFraction value in centigrams_per_gram.
        :type centigrams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(centigrams_per_gram, MassFractionUnits.CentigramPerGram)

    
    @staticmethod
    def from_decigrams_per_gram(decigrams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in decigrams_per_gram.

        

        :param meters: The MassFraction value in decigrams_per_gram.
        :type decigrams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(decigrams_per_gram, MassFractionUnits.DecigramPerGram)

    
    @staticmethod
    def from_decagrams_per_gram(decagrams_per_gram: float):
        """
        Create a new instance of MassFraction from a value in decagrams_per_gram.

        

        :param meters: The MassFraction value in decagrams_per_gram.
        :type decagrams_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(decagrams_per_gram, MassFractionUnits.DecagramPerGram)

    
    @staticmethod
    def from_hectograms_per_gram(hectograms_per_gram: float):
        """
        Create a new instance of MassFraction from a value in hectograms_per_gram.

        

        :param meters: The MassFraction value in hectograms_per_gram.
        :type hectograms_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(hectograms_per_gram, MassFractionUnits.HectogramPerGram)

    
    @staticmethod
    def from_kilograms_per_gram(kilograms_per_gram: float):
        """
        Create a new instance of MassFraction from a value in kilograms_per_gram.

        

        :param meters: The MassFraction value in kilograms_per_gram.
        :type kilograms_per_gram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(kilograms_per_gram, MassFractionUnits.KilogramPerGram)

    
    @staticmethod
    def from_nanograms_per_kilogram(nanograms_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in nanograms_per_kilogram.

        

        :param meters: The MassFraction value in nanograms_per_kilogram.
        :type nanograms_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(nanograms_per_kilogram, MassFractionUnits.NanogramPerKilogram)

    
    @staticmethod
    def from_micrograms_per_kilogram(micrograms_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in micrograms_per_kilogram.

        

        :param meters: The MassFraction value in micrograms_per_kilogram.
        :type micrograms_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(micrograms_per_kilogram, MassFractionUnits.MicrogramPerKilogram)

    
    @staticmethod
    def from_milligrams_per_kilogram(milligrams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in milligrams_per_kilogram.

        

        :param meters: The MassFraction value in milligrams_per_kilogram.
        :type milligrams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(milligrams_per_kilogram, MassFractionUnits.MilligramPerKilogram)

    
    @staticmethod
    def from_centigrams_per_kilogram(centigrams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in centigrams_per_kilogram.

        

        :param meters: The MassFraction value in centigrams_per_kilogram.
        :type centigrams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(centigrams_per_kilogram, MassFractionUnits.CentigramPerKilogram)

    
    @staticmethod
    def from_decigrams_per_kilogram(decigrams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in decigrams_per_kilogram.

        

        :param meters: The MassFraction value in decigrams_per_kilogram.
        :type decigrams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(decigrams_per_kilogram, MassFractionUnits.DecigramPerKilogram)

    
    @staticmethod
    def from_decagrams_per_kilogram(decagrams_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in decagrams_per_kilogram.

        

        :param meters: The MassFraction value in decagrams_per_kilogram.
        :type decagrams_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(decagrams_per_kilogram, MassFractionUnits.DecagramPerKilogram)

    
    @staticmethod
    def from_hectograms_per_kilogram(hectograms_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in hectograms_per_kilogram.

        

        :param meters: The MassFraction value in hectograms_per_kilogram.
        :type hectograms_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(hectograms_per_kilogram, MassFractionUnits.HectogramPerKilogram)

    
    @staticmethod
    def from_kilograms_per_kilogram(kilograms_per_kilogram: float):
        """
        Create a new instance of MassFraction from a value in kilograms_per_kilogram.

        

        :param meters: The MassFraction value in kilograms_per_kilogram.
        :type kilograms_per_kilogram: float
        :return: A new instance of MassFraction.
        :rtype: MassFraction
        """
        return MassFraction(kilograms_per_kilogram, MassFractionUnits.KilogramPerKilogram)

    
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
    def nanograms_per_gram(self) -> float:
        """
        
        """
        if self.__nanograms_per_gram != None:
            return self.__nanograms_per_gram
        self.__nanograms_per_gram = self.__convert_from_base(MassFractionUnits.NanogramPerGram)
        return self.__nanograms_per_gram

    
    @property
    def micrograms_per_gram(self) -> float:
        """
        
        """
        if self.__micrograms_per_gram != None:
            return self.__micrograms_per_gram
        self.__micrograms_per_gram = self.__convert_from_base(MassFractionUnits.MicrogramPerGram)
        return self.__micrograms_per_gram

    
    @property
    def milligrams_per_gram(self) -> float:
        """
        
        """
        if self.__milligrams_per_gram != None:
            return self.__milligrams_per_gram
        self.__milligrams_per_gram = self.__convert_from_base(MassFractionUnits.MilligramPerGram)
        return self.__milligrams_per_gram

    
    @property
    def centigrams_per_gram(self) -> float:
        """
        
        """
        if self.__centigrams_per_gram != None:
            return self.__centigrams_per_gram
        self.__centigrams_per_gram = self.__convert_from_base(MassFractionUnits.CentigramPerGram)
        return self.__centigrams_per_gram

    
    @property
    def decigrams_per_gram(self) -> float:
        """
        
        """
        if self.__decigrams_per_gram != None:
            return self.__decigrams_per_gram
        self.__decigrams_per_gram = self.__convert_from_base(MassFractionUnits.DecigramPerGram)
        return self.__decigrams_per_gram

    
    @property
    def decagrams_per_gram(self) -> float:
        """
        
        """
        if self.__decagrams_per_gram != None:
            return self.__decagrams_per_gram
        self.__decagrams_per_gram = self.__convert_from_base(MassFractionUnits.DecagramPerGram)
        return self.__decagrams_per_gram

    
    @property
    def hectograms_per_gram(self) -> float:
        """
        
        """
        if self.__hectograms_per_gram != None:
            return self.__hectograms_per_gram
        self.__hectograms_per_gram = self.__convert_from_base(MassFractionUnits.HectogramPerGram)
        return self.__hectograms_per_gram

    
    @property
    def kilograms_per_gram(self) -> float:
        """
        
        """
        if self.__kilograms_per_gram != None:
            return self.__kilograms_per_gram
        self.__kilograms_per_gram = self.__convert_from_base(MassFractionUnits.KilogramPerGram)
        return self.__kilograms_per_gram

    
    @property
    def nanograms_per_kilogram(self) -> float:
        """
        
        """
        if self.__nanograms_per_kilogram != None:
            return self.__nanograms_per_kilogram
        self.__nanograms_per_kilogram = self.__convert_from_base(MassFractionUnits.NanogramPerKilogram)
        return self.__nanograms_per_kilogram

    
    @property
    def micrograms_per_kilogram(self) -> float:
        """
        
        """
        if self.__micrograms_per_kilogram != None:
            return self.__micrograms_per_kilogram
        self.__micrograms_per_kilogram = self.__convert_from_base(MassFractionUnits.MicrogramPerKilogram)
        return self.__micrograms_per_kilogram

    
    @property
    def milligrams_per_kilogram(self) -> float:
        """
        
        """
        if self.__milligrams_per_kilogram != None:
            return self.__milligrams_per_kilogram
        self.__milligrams_per_kilogram = self.__convert_from_base(MassFractionUnits.MilligramPerKilogram)
        return self.__milligrams_per_kilogram

    
    @property
    def centigrams_per_kilogram(self) -> float:
        """
        
        """
        if self.__centigrams_per_kilogram != None:
            return self.__centigrams_per_kilogram
        self.__centigrams_per_kilogram = self.__convert_from_base(MassFractionUnits.CentigramPerKilogram)
        return self.__centigrams_per_kilogram

    
    @property
    def decigrams_per_kilogram(self) -> float:
        """
        
        """
        if self.__decigrams_per_kilogram != None:
            return self.__decigrams_per_kilogram
        self.__decigrams_per_kilogram = self.__convert_from_base(MassFractionUnits.DecigramPerKilogram)
        return self.__decigrams_per_kilogram

    
    @property
    def decagrams_per_kilogram(self) -> float:
        """
        
        """
        if self.__decagrams_per_kilogram != None:
            return self.__decagrams_per_kilogram
        self.__decagrams_per_kilogram = self.__convert_from_base(MassFractionUnits.DecagramPerKilogram)
        return self.__decagrams_per_kilogram

    
    @property
    def hectograms_per_kilogram(self) -> float:
        """
        
        """
        if self.__hectograms_per_kilogram != None:
            return self.__hectograms_per_kilogram
        self.__hectograms_per_kilogram = self.__convert_from_base(MassFractionUnits.HectogramPerKilogram)
        return self.__hectograms_per_kilogram

    
    @property
    def kilograms_per_kilogram(self) -> float:
        """
        
        """
        if self.__kilograms_per_kilogram != None:
            return self.__kilograms_per_kilogram
        self.__kilograms_per_kilogram = self.__convert_from_base(MassFractionUnits.KilogramPerKilogram)
        return self.__kilograms_per_kilogram

    
    def to_string(self, unit: MassFractionUnits = MassFractionUnits.DecimalFraction) -> str:
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
        
        if unit == MassFractionUnits.NanogramPerGram:
            return f"""{self.nanograms_per_gram} ng/g"""
        
        if unit == MassFractionUnits.MicrogramPerGram:
            return f"""{self.micrograms_per_gram} μg/g"""
        
        if unit == MassFractionUnits.MilligramPerGram:
            return f"""{self.milligrams_per_gram} mg/g"""
        
        if unit == MassFractionUnits.CentigramPerGram:
            return f"""{self.centigrams_per_gram} cg/g"""
        
        if unit == MassFractionUnits.DecigramPerGram:
            return f"""{self.decigrams_per_gram} dg/g"""
        
        if unit == MassFractionUnits.DecagramPerGram:
            return f"""{self.decagrams_per_gram} dag/g"""
        
        if unit == MassFractionUnits.HectogramPerGram:
            return f"""{self.hectograms_per_gram} hg/g"""
        
        if unit == MassFractionUnits.KilogramPerGram:
            return f"""{self.kilograms_per_gram} kg/g"""
        
        if unit == MassFractionUnits.NanogramPerKilogram:
            return f"""{self.nanograms_per_kilogram} ng/kg"""
        
        if unit == MassFractionUnits.MicrogramPerKilogram:
            return f"""{self.micrograms_per_kilogram} μg/kg"""
        
        if unit == MassFractionUnits.MilligramPerKilogram:
            return f"""{self.milligrams_per_kilogram} mg/kg"""
        
        if unit == MassFractionUnits.CentigramPerKilogram:
            return f"""{self.centigrams_per_kilogram} cg/kg"""
        
        if unit == MassFractionUnits.DecigramPerKilogram:
            return f"""{self.decigrams_per_kilogram} dg/kg"""
        
        if unit == MassFractionUnits.DecagramPerKilogram:
            return f"""{self.decagrams_per_kilogram} dag/kg"""
        
        if unit == MassFractionUnits.HectogramPerKilogram:
            return f"""{self.hectograms_per_kilogram} hg/kg"""
        
        if unit == MassFractionUnits.KilogramPerKilogram:
            return f"""{self.kilograms_per_kilogram} kg/kg"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassFractionUnits = MassFractionUnits.DecimalFraction) -> str:
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
        
        if unit_abbreviation == MassFractionUnits.NanogramPerGram:
            return """ng/g"""
        
        if unit_abbreviation == MassFractionUnits.MicrogramPerGram:
            return """μg/g"""
        
        if unit_abbreviation == MassFractionUnits.MilligramPerGram:
            return """mg/g"""
        
        if unit_abbreviation == MassFractionUnits.CentigramPerGram:
            return """cg/g"""
        
        if unit_abbreviation == MassFractionUnits.DecigramPerGram:
            return """dg/g"""
        
        if unit_abbreviation == MassFractionUnits.DecagramPerGram:
            return """dag/g"""
        
        if unit_abbreviation == MassFractionUnits.HectogramPerGram:
            return """hg/g"""
        
        if unit_abbreviation == MassFractionUnits.KilogramPerGram:
            return """kg/g"""
        
        if unit_abbreviation == MassFractionUnits.NanogramPerKilogram:
            return """ng/kg"""
        
        if unit_abbreviation == MassFractionUnits.MicrogramPerKilogram:
            return """μg/kg"""
        
        if unit_abbreviation == MassFractionUnits.MilligramPerKilogram:
            return """mg/kg"""
        
        if unit_abbreviation == MassFractionUnits.CentigramPerKilogram:
            return """cg/kg"""
        
        if unit_abbreviation == MassFractionUnits.DecigramPerKilogram:
            return """dg/kg"""
        
        if unit_abbreviation == MassFractionUnits.DecagramPerKilogram:
            return """dag/kg"""
        
        if unit_abbreviation == MassFractionUnits.HectogramPerKilogram:
            return """hg/kg"""
        
        if unit_abbreviation == MassFractionUnits.KilogramPerKilogram:
            return """kg/kg"""
        