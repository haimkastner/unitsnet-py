from enum import Enum
import math
import string


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
        
        PicoLitersPerLiter = 'pico_liters_per_liter'
        """
            
        """
        
        NanoLitersPerLiter = 'nano_liters_per_liter'
        """
            
        """
        
        MicroLitersPerLiter = 'micro_liters_per_liter'
        """
            
        """
        
        MilliLitersPerLiter = 'milli_liters_per_liter'
        """
            
        """
        
        CentiLitersPerLiter = 'centi_liters_per_liter'
        """
            
        """
        
        DeciLitersPerLiter = 'deci_liters_per_liter'
        """
            
        """
        
        PicoLitersPerMililiter = 'pico_liters_per_mililiter'
        """
            
        """
        
        NanoLitersPerMililiter = 'nano_liters_per_mililiter'
        """
            
        """
        
        MicroLitersPerMililiter = 'micro_liters_per_mililiter'
        """
            
        """
        
        MilliLitersPerMililiter = 'milli_liters_per_mililiter'
        """
            
        """
        
        CentiLitersPerMililiter = 'centi_liters_per_mililiter'
        """
            
        """
        
        DeciLitersPerMililiter = 'deci_liters_per_mililiter'
        """
            
        """
        
    
class VolumeConcentration:
    """
    The volume concentration (not to be confused with volume fraction) is defined as the volume of a constituent divided by the total volume of the mixture.

    Args:
        value (float): The value.
        from_unit (VolumeConcentrationUnits): The VolumeConcentration unit to create from, The default unit is DecimalFraction
    """
    def __init__(self, value: float, from_unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__decimal_fractions = None
        
        self.__liters_per_liter = None
        
        self.__liters_per_mililiter = None
        
        self.__percent = None
        
        self.__parts_per_thousand = None
        
        self.__parts_per_million = None
        
        self.__parts_per_billion = None
        
        self.__parts_per_trillion = None
        
        self.__pico_liters_per_liter = None
        
        self.__nano_liters_per_liter = None
        
        self.__micro_liters_per_liter = None
        
        self.__milli_liters_per_liter = None
        
        self.__centi_liters_per_liter = None
        
        self.__deci_liters_per_liter = None
        
        self.__pico_liters_per_mililiter = None
        
        self.__nano_liters_per_mililiter = None
        
        self.__micro_liters_per_mililiter = None
        
        self.__milli_liters_per_mililiter = None
        
        self.__centi_liters_per_mililiter = None
        
        self.__deci_liters_per_mililiter = None
        

    def __convert_from_base(self, from_unit: VolumeConcentrationUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == VolumeConcentrationUnits.PicoLitersPerLiter:
            return ((value) / 1e-12)
        
        if from_unit == VolumeConcentrationUnits.NanoLitersPerLiter:
            return ((value) / 1e-09)
        
        if from_unit == VolumeConcentrationUnits.MicroLitersPerLiter:
            return ((value) / 1e-06)
        
        if from_unit == VolumeConcentrationUnits.MilliLitersPerLiter:
            return ((value) / 0.001)
        
        if from_unit == VolumeConcentrationUnits.CentiLitersPerLiter:
            return ((value) / 0.01)
        
        if from_unit == VolumeConcentrationUnits.DeciLitersPerLiter:
            return ((value) / 0.1)
        
        if from_unit == VolumeConcentrationUnits.PicoLitersPerMililiter:
            return ((value * 1e-3) / 1e-12)
        
        if from_unit == VolumeConcentrationUnits.NanoLitersPerMililiter:
            return ((value * 1e-3) / 1e-09)
        
        if from_unit == VolumeConcentrationUnits.MicroLitersPerMililiter:
            return ((value * 1e-3) / 1e-06)
        
        if from_unit == VolumeConcentrationUnits.MilliLitersPerMililiter:
            return ((value * 1e-3) / 0.001)
        
        if from_unit == VolumeConcentrationUnits.CentiLitersPerMililiter:
            return ((value * 1e-3) / 0.01)
        
        if from_unit == VolumeConcentrationUnits.DeciLitersPerMililiter:
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
        
        if to_unit == VolumeConcentrationUnits.PicoLitersPerLiter:
            return ((value) * 1e-12)
        
        if to_unit == VolumeConcentrationUnits.NanoLitersPerLiter:
            return ((value) * 1e-09)
        
        if to_unit == VolumeConcentrationUnits.MicroLitersPerLiter:
            return ((value) * 1e-06)
        
        if to_unit == VolumeConcentrationUnits.MilliLitersPerLiter:
            return ((value) * 0.001)
        
        if to_unit == VolumeConcentrationUnits.CentiLitersPerLiter:
            return ((value) * 0.01)
        
        if to_unit == VolumeConcentrationUnits.DeciLitersPerLiter:
            return ((value) * 0.1)
        
        if to_unit == VolumeConcentrationUnits.PicoLitersPerMililiter:
            return ((value / 1e-3) * 1e-12)
        
        if to_unit == VolumeConcentrationUnits.NanoLitersPerMililiter:
            return ((value / 1e-3) * 1e-09)
        
        if to_unit == VolumeConcentrationUnits.MicroLitersPerMililiter:
            return ((value / 1e-3) * 1e-06)
        
        if to_unit == VolumeConcentrationUnits.MilliLitersPerMililiter:
            return ((value / 1e-3) * 0.001)
        
        if to_unit == VolumeConcentrationUnits.CentiLitersPerMililiter:
            return ((value / 1e-3) * 0.01)
        
        if to_unit == VolumeConcentrationUnits.DeciLitersPerMililiter:
            return ((value / 1e-3) * 0.1)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_pico_liters_per_liter(pico_liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in pico_liters_per_liter.

        

        :param meters: The VolumeConcentration value in pico_liters_per_liter.
        :type pico_liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(pico_liters_per_liter, VolumeConcentrationUnits.PicoLitersPerLiter)

    
    @staticmethod
    def from_nano_liters_per_liter(nano_liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in nano_liters_per_liter.

        

        :param meters: The VolumeConcentration value in nano_liters_per_liter.
        :type nano_liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(nano_liters_per_liter, VolumeConcentrationUnits.NanoLitersPerLiter)

    
    @staticmethod
    def from_micro_liters_per_liter(micro_liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in micro_liters_per_liter.

        

        :param meters: The VolumeConcentration value in micro_liters_per_liter.
        :type micro_liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(micro_liters_per_liter, VolumeConcentrationUnits.MicroLitersPerLiter)

    
    @staticmethod
    def from_milli_liters_per_liter(milli_liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in milli_liters_per_liter.

        

        :param meters: The VolumeConcentration value in milli_liters_per_liter.
        :type milli_liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(milli_liters_per_liter, VolumeConcentrationUnits.MilliLitersPerLiter)

    
    @staticmethod
    def from_centi_liters_per_liter(centi_liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in centi_liters_per_liter.

        

        :param meters: The VolumeConcentration value in centi_liters_per_liter.
        :type centi_liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(centi_liters_per_liter, VolumeConcentrationUnits.CentiLitersPerLiter)

    
    @staticmethod
    def from_deci_liters_per_liter(deci_liters_per_liter: float):
        """
        Create a new instance of VolumeConcentration from a value in deci_liters_per_liter.

        

        :param meters: The VolumeConcentration value in deci_liters_per_liter.
        :type deci_liters_per_liter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(deci_liters_per_liter, VolumeConcentrationUnits.DeciLitersPerLiter)

    
    @staticmethod
    def from_pico_liters_per_mililiter(pico_liters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in pico_liters_per_mililiter.

        

        :param meters: The VolumeConcentration value in pico_liters_per_mililiter.
        :type pico_liters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(pico_liters_per_mililiter, VolumeConcentrationUnits.PicoLitersPerMililiter)

    
    @staticmethod
    def from_nano_liters_per_mililiter(nano_liters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in nano_liters_per_mililiter.

        

        :param meters: The VolumeConcentration value in nano_liters_per_mililiter.
        :type nano_liters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(nano_liters_per_mililiter, VolumeConcentrationUnits.NanoLitersPerMililiter)

    
    @staticmethod
    def from_micro_liters_per_mililiter(micro_liters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in micro_liters_per_mililiter.

        

        :param meters: The VolumeConcentration value in micro_liters_per_mililiter.
        :type micro_liters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(micro_liters_per_mililiter, VolumeConcentrationUnits.MicroLitersPerMililiter)

    
    @staticmethod
    def from_milli_liters_per_mililiter(milli_liters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in milli_liters_per_mililiter.

        

        :param meters: The VolumeConcentration value in milli_liters_per_mililiter.
        :type milli_liters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(milli_liters_per_mililiter, VolumeConcentrationUnits.MilliLitersPerMililiter)

    
    @staticmethod
    def from_centi_liters_per_mililiter(centi_liters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in centi_liters_per_mililiter.

        

        :param meters: The VolumeConcentration value in centi_liters_per_mililiter.
        :type centi_liters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(centi_liters_per_mililiter, VolumeConcentrationUnits.CentiLitersPerMililiter)

    
    @staticmethod
    def from_deci_liters_per_mililiter(deci_liters_per_mililiter: float):
        """
        Create a new instance of VolumeConcentration from a value in deci_liters_per_mililiter.

        

        :param meters: The VolumeConcentration value in deci_liters_per_mililiter.
        :type deci_liters_per_mililiter: float
        :return: A new instance of VolumeConcentration.
        :rtype: VolumeConcentration
        """
        return VolumeConcentration(deci_liters_per_mililiter, VolumeConcentrationUnits.DeciLitersPerMililiter)

    
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
    def pico_liters_per_liter(self) -> float:
        """
        
        """
        if self.__pico_liters_per_liter != None:
            return self.__pico_liters_per_liter
        self.__pico_liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.PicoLitersPerLiter)
        return self.__pico_liters_per_liter

    
    @property
    def nano_liters_per_liter(self) -> float:
        """
        
        """
        if self.__nano_liters_per_liter != None:
            return self.__nano_liters_per_liter
        self.__nano_liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.NanoLitersPerLiter)
        return self.__nano_liters_per_liter

    
    @property
    def micro_liters_per_liter(self) -> float:
        """
        
        """
        if self.__micro_liters_per_liter != None:
            return self.__micro_liters_per_liter
        self.__micro_liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.MicroLitersPerLiter)
        return self.__micro_liters_per_liter

    
    @property
    def milli_liters_per_liter(self) -> float:
        """
        
        """
        if self.__milli_liters_per_liter != None:
            return self.__milli_liters_per_liter
        self.__milli_liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.MilliLitersPerLiter)
        return self.__milli_liters_per_liter

    
    @property
    def centi_liters_per_liter(self) -> float:
        """
        
        """
        if self.__centi_liters_per_liter != None:
            return self.__centi_liters_per_liter
        self.__centi_liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.CentiLitersPerLiter)
        return self.__centi_liters_per_liter

    
    @property
    def deci_liters_per_liter(self) -> float:
        """
        
        """
        if self.__deci_liters_per_liter != None:
            return self.__deci_liters_per_liter
        self.__deci_liters_per_liter = self.__convert_from_base(VolumeConcentrationUnits.DeciLitersPerLiter)
        return self.__deci_liters_per_liter

    
    @property
    def pico_liters_per_mililiter(self) -> float:
        """
        
        """
        if self.__pico_liters_per_mililiter != None:
            return self.__pico_liters_per_mililiter
        self.__pico_liters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.PicoLitersPerMililiter)
        return self.__pico_liters_per_mililiter

    
    @property
    def nano_liters_per_mililiter(self) -> float:
        """
        
        """
        if self.__nano_liters_per_mililiter != None:
            return self.__nano_liters_per_mililiter
        self.__nano_liters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.NanoLitersPerMililiter)
        return self.__nano_liters_per_mililiter

    
    @property
    def micro_liters_per_mililiter(self) -> float:
        """
        
        """
        if self.__micro_liters_per_mililiter != None:
            return self.__micro_liters_per_mililiter
        self.__micro_liters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.MicroLitersPerMililiter)
        return self.__micro_liters_per_mililiter

    
    @property
    def milli_liters_per_mililiter(self) -> float:
        """
        
        """
        if self.__milli_liters_per_mililiter != None:
            return self.__milli_liters_per_mililiter
        self.__milli_liters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.MilliLitersPerMililiter)
        return self.__milli_liters_per_mililiter

    
    @property
    def centi_liters_per_mililiter(self) -> float:
        """
        
        """
        if self.__centi_liters_per_mililiter != None:
            return self.__centi_liters_per_mililiter
        self.__centi_liters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.CentiLitersPerMililiter)
        return self.__centi_liters_per_mililiter

    
    @property
    def deci_liters_per_mililiter(self) -> float:
        """
        
        """
        if self.__deci_liters_per_mililiter != None:
            return self.__deci_liters_per_mililiter
        self.__deci_liters_per_mililiter = self.__convert_from_base(VolumeConcentrationUnits.DeciLitersPerMililiter)
        return self.__deci_liters_per_mililiter

    
    def to_string(self, unit: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction) -> string:
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
        
        if unit == VolumeConcentrationUnits.PicoLitersPerLiter:
            return f"""{self.pico_liters_per_liter} """
        
        if unit == VolumeConcentrationUnits.NanoLitersPerLiter:
            return f"""{self.nano_liters_per_liter} """
        
        if unit == VolumeConcentrationUnits.MicroLitersPerLiter:
            return f"""{self.micro_liters_per_liter} """
        
        if unit == VolumeConcentrationUnits.MilliLitersPerLiter:
            return f"""{self.milli_liters_per_liter} """
        
        if unit == VolumeConcentrationUnits.CentiLitersPerLiter:
            return f"""{self.centi_liters_per_liter} """
        
        if unit == VolumeConcentrationUnits.DeciLitersPerLiter:
            return f"""{self.deci_liters_per_liter} """
        
        if unit == VolumeConcentrationUnits.PicoLitersPerMililiter:
            return f"""{self.pico_liters_per_mililiter} """
        
        if unit == VolumeConcentrationUnits.NanoLitersPerMililiter:
            return f"""{self.nano_liters_per_mililiter} """
        
        if unit == VolumeConcentrationUnits.MicroLitersPerMililiter:
            return f"""{self.micro_liters_per_mililiter} """
        
        if unit == VolumeConcentrationUnits.MilliLitersPerMililiter:
            return f"""{self.milli_liters_per_mililiter} """
        
        if unit == VolumeConcentrationUnits.CentiLitersPerMililiter:
            return f"""{self.centi_liters_per_mililiter} """
        
        if unit == VolumeConcentrationUnits.DeciLitersPerMililiter:
            return f"""{self.deci_liters_per_mililiter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumeConcentrationUnits = VolumeConcentrationUnits.DecimalFraction) -> string:
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
        
        if unit_abbreviation == VolumeConcentrationUnits.PicoLitersPerLiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.NanoLitersPerLiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MicroLitersPerLiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MilliLitersPerLiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.CentiLitersPerLiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.DeciLitersPerLiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.PicoLitersPerMililiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.NanoLitersPerMililiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MicroLitersPerMililiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.MilliLitersPerMililiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.CentiLitersPerMililiter:
            return """"""
        
        if unit_abbreviation == VolumeConcentrationUnits.DeciLitersPerMililiter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for +: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return VolumeConcentration(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for *: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return VolumeConcentration(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for -: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return VolumeConcentration(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for /: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return VolumeConcentration(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for %: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return VolumeConcentration(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for **: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return VolumeConcentration(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for ==: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for <: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for >: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for <=: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, VolumeConcentration):
            raise TypeError("unsupported operand type(s) for >=: 'VolumeConcentration' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value