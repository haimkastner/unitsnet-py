from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class VolumeConcentrationUnits(Enum):
        """
            VolumeConcentrationUnits enumeration
        """
        
        DecimalFraction = 'decimal_fraction'
        """
            
        """
        
        LitersPerLiter = 'liters_per_liter'
        """
            
        """
        
        LitersPerMililiter = 'liters_per_mililiter'
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
        
        PicolitersPerLiter = 'picoliters_per_liter'
        """
            
        """
        
        NanolitersPerLiter = 'nanoliters_per_liter'
        """
            
        """
        
        MicrolitersPerLiter = 'microliters_per_liter'
        """
            
        """
        
        MillilitersPerLiter = 'milliliters_per_liter'
        """
            
        """
        
        CentilitersPerLiter = 'centiliters_per_liter'
        """
            
        """
        
        DecilitersPerLiter = 'deciliters_per_liter'
        """
            
        """
        
        PicolitersPerMililiter = 'picoliters_per_mililiter'
        """
            
        """
        
        NanolitersPerMililiter = 'nanoliters_per_mililiter'
        """
            
        """
        
        MicrolitersPerMililiter = 'microliters_per_mililiter'
        """
            
        """
        
        MillilitersPerMililiter = 'milliliters_per_mililiter'
        """
            
        """
        
        CentilitersPerMililiter = 'centiliters_per_mililiter'
        """
            
        """
        
        DecilitersPerMililiter = 'deciliters_per_mililiter'
        """
            
        """
        

class VolumeConcentration(AbstractMeasure):
    """
    The volume concentration (not to be confused with volume fraction) is defined as the volume of a constituent divided by the total volume of the mixture.

    Args:
        value (float): The value.
        from_unit (VolumeConcentrationUnits): The VolumeConcentration unit to create from, The default unit is DecimalFraction
    """
    def __init__(self, value: float, from_unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__decimal_fractions = None
        
        self.__liters_per_liter = None
        
        self.__liters_per_mililiter = None
        
        self.__percent = None
        
        self.__parts_per_thousand = None
        
        self.__parts_per_million = None
        
        self.__parts_per_billion = None
        
        self.__parts_per_trillion = None
        
        self.__picoliters_per_liter = None
        
        self.__nanoliters_per_liter = None
        
        self.__microliters_per_liter = None
        
        self.__milliliters_per_liter = None
        
        self.__centiliters_per_liter = None
        
        self.__deciliters_per_liter = None
        
        self.__picoliters_per_mililiter = None
        
        self.__nanoliters_per_mililiter = None
        
        self.__microliters_per_mililiter = None
        
        self.__milliliters_per_mililiter = None
        
        self.__centiliters_per_mililiter = None
        
        self.__deciliters_per_mililiter = None
        

    def convert(self, unit: VolumeConcentrationUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: VolumeConcentrationUnits) -> float:
        value = self._value
        
        if from_unit == VolumeConcentrationUnits.DecimalFraction:
            return (value)
        
        if from_unit == VolumeConcentrationUnits.LitersPerLiter:
            return (value)
        
        if from_unit == VolumeConcentrationUnits.LitersPerMililiter:
            return (value * 1e-3)
        
        if from_unit == VolumeConcentrationUnits.Percent:
            return (value * 1e2)
        
        if from_unit == VolumeConcentrationUnits.PartPerThousand:
            return (value * 1e3)
        
        if from_unit == VolumeConcentrationUnits.PartPerMillion:
            return (value * 1e6)
        
        if from_unit == VolumeConcentrationUnits.PartPerBillion:
            return (value * 1e9)
        
        if from_unit == VolumeConcentrationUnits.PartPerTrillion:
            return (value * 1e12)
        
        if from_unit == VolumeConcentrationUnits.PicolitersPerLiter:
            return ((value) / 1e-12)
        
        if from_unit == VolumeConcentrationUnits.NanolitersPerLiter:
            return ((value) / 1e-09)
        
        if from_unit == VolumeConcentrationUnits.MicrolitersPerLiter:
            return ((value) / 1e-06)
        
        if from_unit == VolumeConcentrationUnits.MillilitersPerLiter:
            return ((value) / 0.001)
        
        if from_unit == VolumeConcentrationUnits.CentilitersPerLiter:
            return ((value) / 0.01)
        
        if from_unit == VolumeConcentrationUnits.DecilitersPerLiter:
            return ((value) / 0.1)
        
        if from_unit == VolumeConcentrationUnits.PicolitersPerMililiter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == VolumeConcentrationUnits.NanolitersPerMililiter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == VolumeConcentrationUnits.MicrolitersPerMililiter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == VolumeConcentrationUnits.MillilitersPerMililiter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == VolumeConcentrationUnits.CentilitersPerMililiter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == VolumeConcentrationUnits.DecilitersPerMililiter:
            return ((value * 1e-3) / 0.1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumeConcentrationUnits) -> float:
        
        if to_unit == VolumeConcentrationUnits.DecimalFraction:
            return (value)
        
        if to_unit == VolumeConcentrationUnits.LitersPerLiter:
            return (value)
        
        if to_unit == VolumeConcentrationUnits.LitersPerMililiter:
            return (value / 1e-3)
        
        if to_unit == VolumeConcentrationUnits.Percent:
            return (value / 1e2)
        
        if to_unit == VolumeConcentrationUnits.PartPerThousand:
            return (value / 1e3)
        
        if to_unit == VolumeConcentrationUnits.PartPerMillion:
            return (value / 1e6)
        
        if to_unit == VolumeConcentrationUnits.PartPerBillion:
            return (value / 1e9)
        
        if to_unit == VolumeConcentrationUnits.PartPerTrillion:
            return (value / 1e12)
        
        if to_unit == VolumeConcentrationUnits.PicolitersPerLiter:
            return ((value) * 1e-12)
        
        if to_unit == VolumeConcentrationUnits.NanolitersPerLiter:
            return ((value) * 1e-09)
        
        if to_unit == VolumeConcentrationUnits.MicrolitersPerLiter:
            return ((value) * 1e-06)
        
        if to_unit == VolumeConcentrationUnits.MillilitersPerLiter:
            return ((value) * 0.001)
        
        if to_unit == VolumeConcentrationUnits.CentilitersPerLiter:
            return ((value) * 0.01)
        
        if to_unit == VolumeConcentrationUnits.DecilitersPerLiter:
            return ((value) * 0.1)
        
        if to_unit == VolumeConcentrationUnits.PicolitersPerMililiter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == VolumeConcentrationUnits.NanolitersPerMililiter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == VolumeConcentrationUnits.MicrolitersPerMililiter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == VolumeConcentrationUnits.MillilitersPerMililiter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == VolumeConcentrationUnits.CentilitersPerMililiter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == VolumeConcentrationUnits.DecilitersPerMililiter:
            return ((value / 1e-3) * 0.1)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_decimal_fractions(decimal_fractions: float):
        """
        Create a new instance of VolumeConcentration from a value in decimal_fractions.

        

        :param meters: The VolumeConcentration value in decimal_fractions.
        :type decimal_fractions: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(decimal_fractions, VolumeConcentrationUnits.DecimalFraction)

    
    @staticmethod
    def from_liters_per_liter(liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in liters_per_liter.

        

        :param meters: The VolumeConcentration value in liters_per_liter.
        :type liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(liters_per_liter, VolumeConcentrationUnits.LitersPerLiter)

    
    @staticmethod
    def from_liters_per_mililiter(liters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in liters_per_mililiter.

        

        :param meters: The VolumeConcentration value in liters_per_mililiter.
        :type liters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(liters_per_mililiter, VolumeConcentrationUnits.LitersPerMililiter)

    
    @staticmethod
    def from_percent(percent: float):
        """
        Create a new instance of VolumeConcentration from a value in percent.

        

        :param meters: The VolumeConcentration value in percent.
        :type percent: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(percent, VolumeConcentrationUnits.Percent)

    
    @staticmethod
    def from_parts_per_thousand(parts_per_thousand: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_thousand.

        

        :param meters: The VolumeConcentration value in parts_per_thousand.
        :type parts_per_thousand: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_thousand, VolumeConcentrationUnits.PartPerThousand)

    
    @staticmethod
    def from_parts_per_million(parts_per_million: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_million.

        

        :param meters: The VolumeConcentration value in parts_per_million.
        :type parts_per_million: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_million, VolumeConcentrationUnits.PartPerMillion)

    
    @staticmethod
    def from_parts_per_billion(parts_per_billion: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_billion.

        

        :param meters: The VolumeConcentration value in parts_per_billion.
        :type parts_per_billion: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_billion, VolumeConcentrationUnits.PartPerBillion)

    
    @staticmethod
    def from_parts_per_trillion(parts_per_trillion: float):
        """
        Create a new instance of VolumeConcentration from a value in parts_per_trillion.

        

        :param meters: The VolumeConcentration value in parts_per_trillion.
        :type parts_per_trillion: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(parts_per_trillion, VolumeConcentrationUnits.PartPerTrillion)

    
    @staticmethod
    def from_picoliters_per_liter(picoliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in picoliters_per_liter.

        

        :param meters: The VolumeConcentration value in picoliters_per_liter.
        :type picoliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(picoliters_per_liter, VolumeConcentrationUnits.PicolitersPerLiter)

    
    @staticmethod
    def from_nanoliters_per_liter(nanoliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in nanoliters_per_liter.

        

        :param meters: The VolumeConcentration value in nanoliters_per_liter.
        :type nanoliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(nanoliters_per_liter, VolumeConcentrationUnits.NanolitersPerLiter)

    
    @staticmethod
    def from_microliters_per_liter(microliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in microliters_per_liter.

        

        :param meters: The VolumeConcentration value in microliters_per_liter.
        :type microliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(microliters_per_liter, VolumeConcentrationUnits.MicrolitersPerLiter)

    
    @staticmethod
    def from_milliliters_per_liter(milliliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in milliliters_per_liter.

        

        :param meters: The VolumeConcentration value in milliliters_per_liter.
        :type milliliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(milliliters_per_liter, VolumeConcentrationUnits.MillilitersPerLiter)

    
    @staticmethod
    def from_centiliters_per_liter(centiliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in centiliters_per_liter.

        

        :param meters: The VolumeConcentration value in centiliters_per_liter.
        :type centiliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(centiliters_per_liter, VolumeConcentrationUnits.CentilitersPerLiter)

    
    @staticmethod
    def from_deciliters_per_liter(deciliters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in deciliters_per_liter.

        

        :param meters: The VolumeConcentration value in deciliters_per_liter.
        :type deciliters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(deciliters_per_liter, VolumeConcentrationUnits.DecilitersPerLiter)

    
    @staticmethod
    def from_picoliters_per_mililiter(picoliters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in picoliters_per_mililiter.

        

        :param meters: The VolumeConcentration value in picoliters_per_mililiter.
        :type picoliters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(picoliters_per_mililiter, VolumeConcentrationUnits.PicolitersPerMililiter)

    
    @staticmethod
    def from_nanoliters_per_mililiter(nanoliters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in nanoliters_per_mililiter.

        

        :param meters: The VolumeConcentration value in nanoliters_per_mililiter.
        :type nanoliters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(nanoliters_per_mililiter, VolumeConcentrationUnits.NanolitersPerMililiter)

    
    @staticmethod
    def from_microliters_per_mililiter(microliters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in microliters_per_mililiter.

        

        :param meters: The VolumeConcentration value in microliters_per_mililiter.
        :type microliters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(microliters_per_mililiter, VolumeConcentrationUnits.MicrolitersPerMililiter)

    
    @staticmethod
    def from_milliliters_per_mililiter(milliliters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in milliliters_per_mililiter.

        

        :param meters: The VolumeConcentration value in milliliters_per_mililiter.
        :type milliliters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(milliliters_per_mililiter, VolumeConcentrationUnits.MillilitersPerMililiter)

    
    @staticmethod
    def from_centiliters_per_mililiter(centiliters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in centiliters_per_mililiter.

        

        :param meters: The VolumeConcentration value in centiliters_per_mililiter.
        :type centiliters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(centiliters_per_mililiter, VolumeConcentrationUnits.CentilitersPerMililiter)

    
    @staticmethod
    def from_deciliters_per_mililiter(deciliters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in deciliters_per_mililiter.

        

        :param meters: The VolumeConcentration value in deciliters_per_mililiter.
        :type deciliters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(deciliters_per_mililiter, VolumeConcentrationUnits.DecilitersPerMililiter)

    
    @property
    def decimal_fractions(self) -> float:
        """
        
        """
        if self.__decimal_fractions != None:
            return self.__decimal_fractions
        self.__decimal_fractions = self.__convert_from_base(VolumeConcentrationUnits.DecimalFraction)
        return self.__decimal_fractions

    
    @property
    def liters_per_liter(self) -> float:
        """
        
        """
        if self.__liters_per_liter != None:
            return self.__liters_per_liter
        self.__liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.LitersPerLiter)
        return self.__liters_per_liter

    
    @property
    def liters_per_mililiter(self) -> float:
        """
        
        """
        if self.__liters_per_mililiter != None:
            return self.__liters_per_mililiter
        self.__liters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.LitersPerMililiter)
        return self.__liters_per_mililiter

    
    @property
    def percent(self) -> float:
        """
        
        """
        if self.__percent != None:
            return self.__percent
        self.__percent = self.__convert_from_base(VolumeConcentrationUnits.Percent)
        return self.__percent

    
    @property
    def parts_per_thousand(self) -> float:
        """
        
        """
        if self.__parts_per_thousand != None:
            return self.__parts_per_thousand
        self.__parts_per_thousand = self.__convert_from_base(VolumeConcentrationUnits.PartPerThousand)
        return self.__parts_per_thousand

    
    @property
    def parts_per_million(self) -> float:
        """
        
        """
        if self.__parts_per_million != None:
            return self.__parts_per_million
        self.__parts_per_million = self.__convert_from_base(VolumeConcentrationUnits.PartPerMillion)
        return self.__parts_per_million

    
    @property
    def parts_per_billion(self) -> float:
        """
        
        """
        if self.__parts_per_billion != None:
            return self.__parts_per_billion
        self.__parts_per_billion = self.__convert_from_base(VolumeConcentrationUnits.PartPerBillion)
        return self.__parts_per_billion

    
    @property
    def parts_per_trillion(self) -> float:
        """
        
        """
        if self.__parts_per_trillion != None:
            return self.__parts_per_trillion
        self.__parts_per_trillion = self.__convert_from_base(VolumeConcentrationUnits.PartPerTrillion)
        return self.__parts_per_trillion

    
    @property
    def picoliters_per_liter(self) -> float:
        """
        
        """
        if self.__picoliters_per_liter != None:
            return self.__picoliters_per_liter
        self.__picoliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.PicolitersPerLiter)
        return self.__picoliters_per_liter

    
    @property
    def nanoliters_per_liter(self) -> float:
        """
        
        """
        if self.__nanoliters_per_liter != None:
            return self.__nanoliters_per_liter
        self.__nanoliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.NanolitersPerLiter)
        return self.__nanoliters_per_liter

    
    @property
    def microliters_per_liter(self) -> float:
        """
        
        """
        if self.__microliters_per_liter != None:
            return self.__microliters_per_liter
        self.__microliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.MicrolitersPerLiter)
        return self.__microliters_per_liter

    
    @property
    def milliliters_per_liter(self) -> float:
        """
        
        """
        if self.__milliliters_per_liter != None:
            return self.__milliliters_per_liter
        self.__milliliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.MillilitersPerLiter)
        return self.__milliliters_per_liter

    
    @property
    def centiliters_per_liter(self) -> float:
        """
        
        """
        if self.__centiliters_per_liter != None:
            return self.__centiliters_per_liter
        self.__centiliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.CentilitersPerLiter)
        return self.__centiliters_per_liter

    
    @property
    def deciliters_per_liter(self) -> float:
        """
        
        """
        if self.__deciliters_per_liter != None:
            return self.__deciliters_per_liter
        self.__deciliters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.DecilitersPerLiter)
        return self.__deciliters_per_liter

    
    @property
    def picoliters_per_mililiter(self) -> float:
        """
        
        """
        if self.__picoliters_per_mililiter != None:
            return self.__picoliters_per_mililiter
        self.__picoliters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.PicolitersPerMililiter)
        return self.__picoliters_per_mililiter

    
    @property
    def nanoliters_per_mililiter(self) -> float:
        """
        
        """
        if self.__nanoliters_per_mililiter != None:
            return self.__nanoliters_per_mililiter
        self.__nanoliters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.NanolitersPerMililiter)
        return self.__nanoliters_per_mililiter

    
    @property
    def microliters_per_mililiter(self) -> float:
        """
        
        """
        if self.__microliters_per_mililiter != None:
            return self.__microliters_per_mililiter
        self.__microliters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.MicrolitersPerMililiter)
        return self.__microliters_per_mililiter

    
    @property
    def milliliters_per_mililiter(self) -> float:
        """
        
        """
        if self.__milliliters_per_mililiter != None:
            return self.__milliliters_per_mililiter
        self.__milliliters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.MillilitersPerMililiter)
        return self.__milliliters_per_mililiter

    
    @property
    def centiliters_per_mililiter(self) -> float:
        """
        
        """
        if self.__centiliters_per_mililiter != None:
            return self.__centiliters_per_mililiter
        self.__centiliters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.CentilitersPerMililiter)
        return self.__centiliters_per_mililiter

    
    @property
    def deciliters_per_mililiter(self) -> float:
        """
        
        """
        if self.__deciliters_per_mililiter != None:
            return self.__deciliters_per_mililiter
        self.__deciliters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.DecilitersPerMililiter)
        return self.__deciliters_per_mililiter

    
    def to_string(self, unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction) -> str:
        """
        Format the VolumeConcentration to string.
        Note! the default format for VolumeConcentration is DecimalFraction.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == VolumeConcentrationUnits.DecimalFraction:
            return f"""{self.decimal_fractions} """
        
        if unit == VolumeConcentrationUnits.LitersPerLiter:
            return f"""{self.liters_per_liter} L/L"""
        
        if unit == VolumeConcentrationUnits.LitersPerMililiter:
            return f"""{self.liters_per_mililiter} L/mL"""
        
        if unit == VolumeConcentrationUnits.Percent:
            return f"""{self.percent} %"""
        
        if unit == VolumeConcentrationUnits.PartPerThousand:
            return f"""{self.parts_per_thousand} ‰"""
        
        if unit == VolumeConcentrationUnits.PartPerMillion:
            return f"""{self.parts_per_million} ppm"""
        
        if unit == VolumeConcentrationUnits.PartPerBillion:
            return f"""{self.parts_per_billion} ppb"""
        
        if unit == VolumeConcentrationUnits.PartPerTrillion:
            return f"""{self.parts_per_trillion} ppt"""
        
        if unit == VolumeConcentrationUnits.PicolitersPerLiter:
            return f"""{self.picoliters_per_liter} pL/L"""
        
        if unit == VolumeConcentrationUnits.NanolitersPerLiter:
            return f"""{self.nanoliters_per_liter} nL/L"""
        
        if unit == VolumeConcentrationUnits.MicrolitersPerLiter:
            return f"""{self.microliters_per_liter} μL/L"""
        
        if unit == VolumeConcentrationUnits.MillilitersPerLiter:
            return f"""{self.milliliters_per_liter} mL/L"""
        
        if unit == VolumeConcentrationUnits.CentilitersPerLiter:
            return f"""{self.centiliters_per_liter} cL/L"""
        
        if unit == VolumeConcentrationUnits.DecilitersPerLiter:
            return f"""{self.deciliters_per_liter} dL/L"""
        
        if unit == VolumeConcentrationUnits.PicolitersPerMililiter:
            return f"""{self.picoliters_per_mililiter} pL/mL"""
        
        if unit == VolumeConcentrationUnits.NanolitersPerMililiter:
            return f"""{self.nanoliters_per_mililiter} nL/mL"""
        
        if unit == VolumeConcentrationUnits.MicrolitersPerMililiter:
            return f"""{self.microliters_per_mililiter} μL/mL"""
        
        if unit == VolumeConcentrationUnits.MillilitersPerMililiter:
            return f"""{self.milliliters_per_mililiter} mL/mL"""
        
        if unit == VolumeConcentrationUnits.CentilitersPerMililiter:
            return f"""{self.centiliters_per_mililiter} cL/mL"""
        
        if unit == VolumeConcentrationUnits.DecilitersPerMililiter:
            return f"""{self.deciliters_per_mililiter} dL/mL"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction) -> str:
        """
        Get VolumeConcentration unit abbreviation.
        Note! the default abbreviation for VolumeConcentration is DecimalFraction.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumeConcentrationUnits.DecimalFraction:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.LitersPerLiter:
            return """L/L"""
        
        if unit_abbreviation == VolumeConcentrationUnits.LitersPerMililiter:
            return """L/mL"""
        
        if unit_abbreviation == VolumeConcentrationUnits.Percent:
            return """%"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerThousand:
            return """‰"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerMillion:
            return """ppm"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerBillion:
            return """ppb"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PartPerTrillion:
            return """ppt"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PicolitersPerLiter:
            return """pL/L"""
        
        if unit_abbreviation == VolumeConcentrationUnits.NanolitersPerLiter:
            return """nL/L"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MicrolitersPerLiter:
            return """μL/L"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MillilitersPerLiter:
            return """mL/L"""
        
        if unit_abbreviation == VolumeConcentrationUnits.CentilitersPerLiter:
            return """cL/L"""
        
        if unit_abbreviation == VolumeConcentrationUnits.DecilitersPerLiter:
            return """dL/L"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PicolitersPerMililiter:
            return """pL/mL"""
        
        if unit_abbreviation == VolumeConcentrationUnits.NanolitersPerMililiter:
            return """nL/mL"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MicrolitersPerMililiter:
            return """μL/mL"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MillilitersPerMililiter:
            return """mL/mL"""
        
        if unit_abbreviation == VolumeConcentrationUnits.CentilitersPerMililiter:
            return """cL/mL"""
        
        if unit_abbreviation == VolumeConcentrationUnits.DecilitersPerMililiter:
            return """dL/mL"""
        