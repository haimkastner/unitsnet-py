from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MolarMassUnits(Enum):
        """
            MolarMassUnits enumeration
        """
        
        GramPerMole = 'gram_per_mole'
        """
            
        """
        
        KilogramPerKilomole = 'kilogram_per_kilomole'
        """
            
        """
        
        PoundPerMole = 'pound_per_mole'
        """
            
        """
        
        NanogramPerMole = 'nanogram_per_mole'
        """
            
        """
        
        MicrogramPerMole = 'microgram_per_mole'
        """
            
        """
        
        MilligramPerMole = 'milligram_per_mole'
        """
            
        """
        
        CentigramPerMole = 'centigram_per_mole'
        """
            
        """
        
        DecigramPerMole = 'decigram_per_mole'
        """
            
        """
        
        DecagramPerMole = 'decagram_per_mole'
        """
            
        """
        
        HectogramPerMole = 'hectogram_per_mole'
        """
            
        """
        
        KilogramPerMole = 'kilogram_per_mole'
        """
            
        """
        
        KilopoundPerMole = 'kilopound_per_mole'
        """
            
        """
        
        MegapoundPerMole = 'megapound_per_mole'
        """
            
        """
        

class MolarMass(AbstractMeasure):
    """
    In chemistry, the molar mass M is a physical property defined as the mass of a given substance (chemical element or chemical compound) divided by the amount of substance.

    Args:
        value (float): The value.
        from_unit (MolarMassUnits): The MolarMass unit to create from, The default unit is KilogramPerMole
    """
    def __init__(self, value: float, from_unit: MolarMassUnits = MolarMassUnits.KilogramPerMole):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_mole = None
        
        self.__kilograms_per_kilomole = None
        
        self.__pounds_per_mole = None
        
        self.__nanograms_per_mole = None
        
        self.__micrograms_per_mole = None
        
        self.__milligrams_per_mole = None
        
        self.__centigrams_per_mole = None
        
        self.__decigrams_per_mole = None
        
        self.__decagrams_per_mole = None
        
        self.__hectograms_per_mole = None
        
        self.__kilograms_per_mole = None
        
        self.__kilopounds_per_mole = None
        
        self.__megapounds_per_mole = None
        

    def convert(self, unit: MolarMassUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: MolarMassUnits) -> float:
        value = self._value
        
        if from_unit == MolarMassUnits.GramPerMole:
            return (value * 1e3)
        
        if from_unit == MolarMassUnits.KilogramPerKilomole:
            return (value * 1e3)
        
        if from_unit == MolarMassUnits.PoundPerMole:
            return (value / 0.45359237)
        
        if from_unit == MolarMassUnits.NanogramPerMole:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == MolarMassUnits.MicrogramPerMole:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MolarMassUnits.MilligramPerMole:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MolarMassUnits.CentigramPerMole:
            return ((value * 1e3) / 0.01)
        
        if from_unit == MolarMassUnits.DecigramPerMole:
            return ((value * 1e3) / 0.1)
        
        if from_unit == MolarMassUnits.DecagramPerMole:
            return ((value * 1e3) / 10.0)
        
        if from_unit == MolarMassUnits.HectogramPerMole:
            return ((value * 1e3) / 100.0)
        
        if from_unit == MolarMassUnits.KilogramPerMole:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MolarMassUnits.KilopoundPerMole:
            return ((value / 0.45359237) / 1000.0)
        
        if from_unit == MolarMassUnits.MegapoundPerMole:
            return ((value / 0.45359237) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MolarMassUnits) -> float:
        
        if to_unit == MolarMassUnits.GramPerMole:
            return (value / 1e3)
        
        if to_unit == MolarMassUnits.KilogramPerKilomole:
            return (value / 1e3)
        
        if to_unit == MolarMassUnits.PoundPerMole:
            return (value * 0.45359237)
        
        if to_unit == MolarMassUnits.NanogramPerMole:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == MolarMassUnits.MicrogramPerMole:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MolarMassUnits.MilligramPerMole:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MolarMassUnits.CentigramPerMole:
            return ((value / 1e3) * 0.01)
        
        if to_unit == MolarMassUnits.DecigramPerMole:
            return ((value / 1e3) * 0.1)
        
        if to_unit == MolarMassUnits.DecagramPerMole:
            return ((value / 1e3) * 10.0)
        
        if to_unit == MolarMassUnits.HectogramPerMole:
            return ((value / 1e3) * 100.0)
        
        if to_unit == MolarMassUnits.KilogramPerMole:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MolarMassUnits.KilopoundPerMole:
            return ((value * 0.45359237) * 1000.0)
        
        if to_unit == MolarMassUnits.MegapoundPerMole:
            return ((value * 0.45359237) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_grams_per_mole(grams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in grams_per_mole.

        

        :param meters: The MolarMass value in grams_per_mole.
        :type grams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(grams_per_mole, MolarMassUnits.GramPerMole)

    
    @staticmethod
    def from_kilograms_per_kilomole(kilograms_per_kilomole: float):
        """
        Create a new instance of MolarMass from a value in kilograms_per_kilomole.

        

        :param meters: The MolarMass value in kilograms_per_kilomole.
        :type kilograms_per_kilomole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(kilograms_per_kilomole, MolarMassUnits.KilogramPerKilomole)

    
    @staticmethod
    def from_pounds_per_mole(pounds_per_mole: float):
        """
        Create a new instance of MolarMass from a value in pounds_per_mole.

        

        :param meters: The MolarMass value in pounds_per_mole.
        :type pounds_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(pounds_per_mole, MolarMassUnits.PoundPerMole)

    
    @staticmethod
    def from_nanograms_per_mole(nanograms_per_mole: float):
        """
        Create a new instance of MolarMass from a value in nanograms_per_mole.

        

        :param meters: The MolarMass value in nanograms_per_mole.
        :type nanograms_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(nanograms_per_mole, MolarMassUnits.NanogramPerMole)

    
    @staticmethod
    def from_micrograms_per_mole(micrograms_per_mole: float):
        """
        Create a new instance of MolarMass from a value in micrograms_per_mole.

        

        :param meters: The MolarMass value in micrograms_per_mole.
        :type micrograms_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(micrograms_per_mole, MolarMassUnits.MicrogramPerMole)

    
    @staticmethod
    def from_milligrams_per_mole(milligrams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in milligrams_per_mole.

        

        :param meters: The MolarMass value in milligrams_per_mole.
        :type milligrams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(milligrams_per_mole, MolarMassUnits.MilligramPerMole)

    
    @staticmethod
    def from_centigrams_per_mole(centigrams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in centigrams_per_mole.

        

        :param meters: The MolarMass value in centigrams_per_mole.
        :type centigrams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(centigrams_per_mole, MolarMassUnits.CentigramPerMole)

    
    @staticmethod
    def from_decigrams_per_mole(decigrams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in decigrams_per_mole.

        

        :param meters: The MolarMass value in decigrams_per_mole.
        :type decigrams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(decigrams_per_mole, MolarMassUnits.DecigramPerMole)

    
    @staticmethod
    def from_decagrams_per_mole(decagrams_per_mole: float):
        """
        Create a new instance of MolarMass from a value in decagrams_per_mole.

        

        :param meters: The MolarMass value in decagrams_per_mole.
        :type decagrams_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(decagrams_per_mole, MolarMassUnits.DecagramPerMole)

    
    @staticmethod
    def from_hectograms_per_mole(hectograms_per_mole: float):
        """
        Create a new instance of MolarMass from a value in hectograms_per_mole.

        

        :param meters: The MolarMass value in hectograms_per_mole.
        :type hectograms_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(hectograms_per_mole, MolarMassUnits.HectogramPerMole)

    
    @staticmethod
    def from_kilograms_per_mole(kilograms_per_mole: float):
        """
        Create a new instance of MolarMass from a value in kilograms_per_mole.

        

        :param meters: The MolarMass value in kilograms_per_mole.
        :type kilograms_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(kilograms_per_mole, MolarMassUnits.KilogramPerMole)

    
    @staticmethod
    def from_kilopounds_per_mole(kilopounds_per_mole: float):
        """
        Create a new instance of MolarMass from a value in kilopounds_per_mole.

        

        :param meters: The MolarMass value in kilopounds_per_mole.
        :type kilopounds_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(kilopounds_per_mole, MolarMassUnits.KilopoundPerMole)

    
    @staticmethod
    def from_megapounds_per_mole(megapounds_per_mole: float):
        """
        Create a new instance of MolarMass from a value in megapounds_per_mole.

        

        :param meters: The MolarMass value in megapounds_per_mole.
        :type megapounds_per_mole: float
        :return: A new instance of MolarMass.
        :rtype: MolarMass
        """
        return MolarMass(megapounds_per_mole, MolarMassUnits.MegapoundPerMole)

    
    @property
    def grams_per_mole(self) -> float:
        """
        
        """
        if self.__grams_per_mole != None:
            return self.__grams_per_mole
        self.__grams_per_mole = self.__convert_from_base(MolarMassUnits.GramPerMole)
        return self.__grams_per_mole

    
    @property
    def kilograms_per_kilomole(self) -> float:
        """
        
        """
        if self.__kilograms_per_kilomole != None:
            return self.__kilograms_per_kilomole
        self.__kilograms_per_kilomole = self.__convert_from_base(MolarMassUnits.KilogramPerKilomole)
        return self.__kilograms_per_kilomole

    
    @property
    def pounds_per_mole(self) -> float:
        """
        
        """
        if self.__pounds_per_mole != None:
            return self.__pounds_per_mole
        self.__pounds_per_mole = self.__convert_from_base(MolarMassUnits.PoundPerMole)
        return self.__pounds_per_mole

    
    @property
    def nanograms_per_mole(self) -> float:
        """
        
        """
        if self.__nanograms_per_mole != None:
            return self.__nanograms_per_mole
        self.__nanograms_per_mole = self.__convert_from_base(MolarMassUnits.NanogramPerMole)
        return self.__nanograms_per_mole

    
    @property
    def micrograms_per_mole(self) -> float:
        """
        
        """
        if self.__micrograms_per_mole != None:
            return self.__micrograms_per_mole
        self.__micrograms_per_mole = self.__convert_from_base(MolarMassUnits.MicrogramPerMole)
        return self.__micrograms_per_mole

    
    @property
    def milligrams_per_mole(self) -> float:
        """
        
        """
        if self.__milligrams_per_mole != None:
            return self.__milligrams_per_mole
        self.__milligrams_per_mole = self.__convert_from_base(MolarMassUnits.MilligramPerMole)
        return self.__milligrams_per_mole

    
    @property
    def centigrams_per_mole(self) -> float:
        """
        
        """
        if self.__centigrams_per_mole != None:
            return self.__centigrams_per_mole
        self.__centigrams_per_mole = self.__convert_from_base(MolarMassUnits.CentigramPerMole)
        return self.__centigrams_per_mole

    
    @property
    def decigrams_per_mole(self) -> float:
        """
        
        """
        if self.__decigrams_per_mole != None:
            return self.__decigrams_per_mole
        self.__decigrams_per_mole = self.__convert_from_base(MolarMassUnits.DecigramPerMole)
        return self.__decigrams_per_mole

    
    @property
    def decagrams_per_mole(self) -> float:
        """
        
        """
        if self.__decagrams_per_mole != None:
            return self.__decagrams_per_mole
        self.__decagrams_per_mole = self.__convert_from_base(MolarMassUnits.DecagramPerMole)
        return self.__decagrams_per_mole

    
    @property
    def hectograms_per_mole(self) -> float:
        """
        
        """
        if self.__hectograms_per_mole != None:
            return self.__hectograms_per_mole
        self.__hectograms_per_mole = self.__convert_from_base(MolarMassUnits.HectogramPerMole)
        return self.__hectograms_per_mole

    
    @property
    def kilograms_per_mole(self) -> float:
        """
        
        """
        if self.__kilograms_per_mole != None:
            return self.__kilograms_per_mole
        self.__kilograms_per_mole = self.__convert_from_base(MolarMassUnits.KilogramPerMole)
        return self.__kilograms_per_mole

    
    @property
    def kilopounds_per_mole(self) -> float:
        """
        
        """
        if self.__kilopounds_per_mole != None:
            return self.__kilopounds_per_mole
        self.__kilopounds_per_mole = self.__convert_from_base(MolarMassUnits.KilopoundPerMole)
        return self.__kilopounds_per_mole

    
    @property
    def megapounds_per_mole(self) -> float:
        """
        
        """
        if self.__megapounds_per_mole != None:
            return self.__megapounds_per_mole
        self.__megapounds_per_mole = self.__convert_from_base(MolarMassUnits.MegapoundPerMole)
        return self.__megapounds_per_mole

    
    def to_string(self, unit: MolarMassUnits = MolarMassUnits.KilogramPerMole) -> str:
        """
        Format the MolarMass to string.
        Note! the default format for MolarMass is KilogramPerMole.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MolarMassUnits.GramPerMole:
            return f"""{self.grams_per_mole} g/mol"""
        
        if unit == MolarMassUnits.KilogramPerKilomole:
            return f"""{self.kilograms_per_kilomole} kg/kmol"""
        
        if unit == MolarMassUnits.PoundPerMole:
            return f"""{self.pounds_per_mole} lb/mol"""
        
        if unit == MolarMassUnits.NanogramPerMole:
            return f"""{self.nanograms_per_mole} ng/mol"""
        
        if unit == MolarMassUnits.MicrogramPerMole:
            return f"""{self.micrograms_per_mole} μg/mol"""
        
        if unit == MolarMassUnits.MilligramPerMole:
            return f"""{self.milligrams_per_mole} mg/mol"""
        
        if unit == MolarMassUnits.CentigramPerMole:
            return f"""{self.centigrams_per_mole} cg/mol"""
        
        if unit == MolarMassUnits.DecigramPerMole:
            return f"""{self.decigrams_per_mole} dg/mol"""
        
        if unit == MolarMassUnits.DecagramPerMole:
            return f"""{self.decagrams_per_mole} dag/mol"""
        
        if unit == MolarMassUnits.HectogramPerMole:
            return f"""{self.hectograms_per_mole} hg/mol"""
        
        if unit == MolarMassUnits.KilogramPerMole:
            return f"""{self.kilograms_per_mole} kg/mol"""
        
        if unit == MolarMassUnits.KilopoundPerMole:
            return f"""{self.kilopounds_per_mole} klb/mol"""
        
        if unit == MolarMassUnits.MegapoundPerMole:
            return f"""{self.megapounds_per_mole} Mlb/mol"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MolarMassUnits = MolarMassUnits.KilogramPerMole) -> str:
        """
        Get MolarMass unit abbreviation.
        Note! the default abbreviation for MolarMass is KilogramPerMole.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MolarMassUnits.GramPerMole:
            return """g/mol"""
        
        if unit_abbreviation == MolarMassUnits.KilogramPerKilomole:
            return """kg/kmol"""
        
        if unit_abbreviation == MolarMassUnits.PoundPerMole:
            return """lb/mol"""
        
        if unit_abbreviation == MolarMassUnits.NanogramPerMole:
            return """ng/mol"""
        
        if unit_abbreviation == MolarMassUnits.MicrogramPerMole:
            return """μg/mol"""
        
        if unit_abbreviation == MolarMassUnits.MilligramPerMole:
            return """mg/mol"""
        
        if unit_abbreviation == MolarMassUnits.CentigramPerMole:
            return """cg/mol"""
        
        if unit_abbreviation == MolarMassUnits.DecigramPerMole:
            return """dg/mol"""
        
        if unit_abbreviation == MolarMassUnits.DecagramPerMole:
            return """dag/mol"""
        
        if unit_abbreviation == MolarMassUnits.HectogramPerMole:
            return """hg/mol"""
        
        if unit_abbreviation == MolarMassUnits.KilogramPerMole:
            return """kg/mol"""
        
        if unit_abbreviation == MolarMassUnits.KilopoundPerMole:
            return """klb/mol"""
        
        if unit_abbreviation == MolarMassUnits.MegapoundPerMole:
            return """Mlb/mol"""
        