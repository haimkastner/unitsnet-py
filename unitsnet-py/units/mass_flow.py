from enum import Enum
import math
import string


class MassFlowUnits(Enum):
        """
            MassFlowUnits enumeration
        """
        
        GramPerSecond = 'gram_per_second'
        """
            
        """
        
        GramPerDay = 'gram_per_day'
        """
            
        """
        
        GramPerHour = 'gram_per_hour'
        """
            
        """
        
        KilogramPerHour = 'kilogram_per_hour'
        """
            
        """
        
        KilogramPerMinute = 'kilogram_per_minute'
        """
            
        """
        
        TonnePerHour = 'tonne_per_hour'
        """
            
        """
        
        PoundPerDay = 'pound_per_day'
        """
            
        """
        
        PoundPerHour = 'pound_per_hour'
        """
            
        """
        
        PoundPerMinute = 'pound_per_minute'
        """
            
        """
        
        PoundPerSecond = 'pound_per_second'
        """
            
        """
        
        TonnePerDay = 'tonne_per_day'
        """
            
        """
        
        ShortTonPerHour = 'short_ton_per_hour'
        """
            
        """
        
        NanoGramPerSecond = 'nano_gram_per_second'
        """
            
        """
        
        MicroGramPerSecond = 'micro_gram_per_second'
        """
            
        """
        
        MilliGramPerSecond = 'milli_gram_per_second'
        """
            
        """
        
        CentiGramPerSecond = 'centi_gram_per_second'
        """
            
        """
        
        DeciGramPerSecond = 'deci_gram_per_second'
        """
            
        """
        
        DecaGramPerSecond = 'deca_gram_per_second'
        """
            
        """
        
        HectoGramPerSecond = 'hecto_gram_per_second'
        """
            
        """
        
        KiloGramPerSecond = 'kilo_gram_per_second'
        """
            
        """
        
        NanoGramPerDay = 'nano_gram_per_day'
        """
            
        """
        
        MicroGramPerDay = 'micro_gram_per_day'
        """
            
        """
        
        MilliGramPerDay = 'milli_gram_per_day'
        """
            
        """
        
        CentiGramPerDay = 'centi_gram_per_day'
        """
            
        """
        
        DeciGramPerDay = 'deci_gram_per_day'
        """
            
        """
        
        DecaGramPerDay = 'deca_gram_per_day'
        """
            
        """
        
        HectoGramPerDay = 'hecto_gram_per_day'
        """
            
        """
        
        KiloGramPerDay = 'kilo_gram_per_day'
        """
            
        """
        
        MegaGramPerDay = 'mega_gram_per_day'
        """
            
        """
        
        MegaPoundPerDay = 'mega_pound_per_day'
        """
            
        """
        
        MegaPoundPerHour = 'mega_pound_per_hour'
        """
            
        """
        
        MegaPoundPerMinute = 'mega_pound_per_minute'
        """
            
        """
        
        MegaPoundPerSecond = 'mega_pound_per_second'
        """
            
        """
        

class MassFlow:
    """
    Mass flow is the ratio of the mass change to the time during which the change occurred (value of mass changes per unit time).

    Args:
        value (float): The value.
        from_unit (MassFlowUnits): The MassFlow unit to create from, The default unit is GramPerSecond
    """
    def __init__(self, value: float, from_unit: MassFlowUnits = MassFlowUnits.GramPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__grams_per_second = None
        
        self.__grams_per_day = None
        
        self.__grams_per_hour = None
        
        self.__kilograms_per_hour = None
        
        self.__kilograms_per_minute = None
        
        self.__tonnes_per_hour = None
        
        self.__pounds_per_day = None
        
        self.__pounds_per_hour = None
        
        self.__pounds_per_minute = None
        
        self.__pounds_per_second = None
        
        self.__tonnes_per_day = None
        
        self.__short_tons_per_hour = None
        
        self.__nano_grams_per_second = None
        
        self.__micro_grams_per_second = None
        
        self.__milli_grams_per_second = None
        
        self.__centi_grams_per_second = None
        
        self.__deci_grams_per_second = None
        
        self.__deca_grams_per_second = None
        
        self.__hecto_grams_per_second = None
        
        self.__kilo_grams_per_second = None
        
        self.__nano_grams_per_day = None
        
        self.__micro_grams_per_day = None
        
        self.__milli_grams_per_day = None
        
        self.__centi_grams_per_day = None
        
        self.__deci_grams_per_day = None
        
        self.__deca_grams_per_day = None
        
        self.__hecto_grams_per_day = None
        
        self.__kilo_grams_per_day = None
        
        self.__mega_grams_per_day = None
        
        self.__mega_pounds_per_day = None
        
        self.__mega_pounds_per_hour = None
        
        self.__mega_pounds_per_minute = None
        
        self.__mega_pounds_per_second = None
        

    def __convert_from_base(self, from_unit: MassFlowUnits) -> float:
        value = self.__value
        
        if from_unit == MassFlowUnits.GramPerSecond:
            return (value)
        
        if from_unit == MassFlowUnits.GramPerDay:
            return (value * 86400)
        
        if from_unit == MassFlowUnits.GramPerHour:
            return (value * 3600)
        
        if from_unit == MassFlowUnits.KilogramPerHour:
            return (value * 3.6)
        
        if from_unit == MassFlowUnits.KilogramPerMinute:
            return (value * 0.06)
        
        if from_unit == MassFlowUnits.TonnePerHour:
            return (value * 3.6 / 1000)
        
        if from_unit == MassFlowUnits.PoundPerDay:
            return (value * 190.47936)
        
        if from_unit == MassFlowUnits.PoundPerHour:
            return (value * 7.93664)
        
        if from_unit == MassFlowUnits.PoundPerMinute:
            return (value * 0.132277)
        
        if from_unit == MassFlowUnits.PoundPerSecond:
            return (value / 453.59237)
        
        if from_unit == MassFlowUnits.TonnePerDay:
            return (value * 0.0864000)
        
        if from_unit == MassFlowUnits.ShortTonPerHour:
            return (value / 251.9957611)
        
        if from_unit == MassFlowUnits.NanoGramPerSecond:
            return ((value) / 1e-09)
        
        if from_unit == MassFlowUnits.MicroGramPerSecond:
            return ((value) / 1e-06)
        
        if from_unit == MassFlowUnits.MilliGramPerSecond:
            return ((value) / 0.001)
        
        if from_unit == MassFlowUnits.CentiGramPerSecond:
            return ((value) / 0.01)
        
        if from_unit == MassFlowUnits.DeciGramPerSecond:
            return ((value) / 0.1)
        
        if from_unit == MassFlowUnits.DecaGramPerSecond:
            return ((value) / 10.0)
        
        if from_unit == MassFlowUnits.HectoGramPerSecond:
            return ((value) / 100.0)
        
        if from_unit == MassFlowUnits.KiloGramPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == MassFlowUnits.NanoGramPerDay:
            return ((value * 86400) / 1e-09)
        
        if from_unit == MassFlowUnits.MicroGramPerDay:
            return ((value * 86400) / 1e-06)
        
        if from_unit == MassFlowUnits.MilliGramPerDay:
            return ((value * 86400) / 0.001)
        
        if from_unit == MassFlowUnits.CentiGramPerDay:
            return ((value * 86400) / 0.01)
        
        if from_unit == MassFlowUnits.DeciGramPerDay:
            return ((value * 86400) / 0.1)
        
        if from_unit == MassFlowUnits.DecaGramPerDay:
            return ((value * 86400) / 10.0)
        
        if from_unit == MassFlowUnits.HectoGramPerDay:
            return ((value * 86400) / 100.0)
        
        if from_unit == MassFlowUnits.KiloGramPerDay:
            return ((value * 86400) / 1000.0)
        
        if from_unit == MassFlowUnits.MegaGramPerDay:
            return ((value * 86400) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegaPoundPerDay:
            return ((value * 190.47936) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegaPoundPerHour:
            return ((value * 7.93664) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegaPoundPerMinute:
            return ((value * 0.132277) / 1000000.0)
        
        if from_unit == MassFlowUnits.MegaPoundPerSecond:
            return ((value / 453.59237) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassFlowUnits) -> float:
        
        if to_unit == MassFlowUnits.GramPerSecond:
            return (value)
        
        if to_unit == MassFlowUnits.GramPerDay:
            return (value / 86400)
        
        if to_unit == MassFlowUnits.GramPerHour:
            return (value / 3600)
        
        if to_unit == MassFlowUnits.KilogramPerHour:
            return (value / 3.6)
        
        if to_unit == MassFlowUnits.KilogramPerMinute:
            return (value / 0.06)
        
        if to_unit == MassFlowUnits.TonnePerHour:
            return (1000 * value / 3.6)
        
        if to_unit == MassFlowUnits.PoundPerDay:
            return (value / 190.47936)
        
        if to_unit == MassFlowUnits.PoundPerHour:
            return (value / 7.93664)
        
        if to_unit == MassFlowUnits.PoundPerMinute:
            return (value / 0.132277)
        
        if to_unit == MassFlowUnits.PoundPerSecond:
            return (value * 453.59237)
        
        if to_unit == MassFlowUnits.TonnePerDay:
            return (value / 0.0864000)
        
        if to_unit == MassFlowUnits.ShortTonPerHour:
            return (value * 251.9957611)
        
        if to_unit == MassFlowUnits.NanoGramPerSecond:
            return ((value) * 1e-09)
        
        if to_unit == MassFlowUnits.MicroGramPerSecond:
            return ((value) * 1e-06)
        
        if to_unit == MassFlowUnits.MilliGramPerSecond:
            return ((value) * 0.001)
        
        if to_unit == MassFlowUnits.CentiGramPerSecond:
            return ((value) * 0.01)
        
        if to_unit == MassFlowUnits.DeciGramPerSecond:
            return ((value) * 0.1)
        
        if to_unit == MassFlowUnits.DecaGramPerSecond:
            return ((value) * 10.0)
        
        if to_unit == MassFlowUnits.HectoGramPerSecond:
            return ((value) * 100.0)
        
        if to_unit == MassFlowUnits.KiloGramPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == MassFlowUnits.NanoGramPerDay:
            return ((value / 86400) * 1e-09)
        
        if to_unit == MassFlowUnits.MicroGramPerDay:
            return ((value / 86400) * 1e-06)
        
        if to_unit == MassFlowUnits.MilliGramPerDay:
            return ((value / 86400) * 0.001)
        
        if to_unit == MassFlowUnits.CentiGramPerDay:
            return ((value / 86400) * 0.01)
        
        if to_unit == MassFlowUnits.DeciGramPerDay:
            return ((value / 86400) * 0.1)
        
        if to_unit == MassFlowUnits.DecaGramPerDay:
            return ((value / 86400) * 10.0)
        
        if to_unit == MassFlowUnits.HectoGramPerDay:
            return ((value / 86400) * 100.0)
        
        if to_unit == MassFlowUnits.KiloGramPerDay:
            return ((value / 86400) * 1000.0)
        
        if to_unit == MassFlowUnits.MegaGramPerDay:
            return ((value / 86400) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegaPoundPerDay:
            return ((value / 190.47936) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegaPoundPerHour:
            return ((value / 7.93664) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegaPoundPerMinute:
            return ((value / 0.132277) * 1000000.0)
        
        if to_unit == MassFlowUnits.MegaPoundPerSecond:
            return ((value * 453.59237) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_grams_per_second(grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in grams_per_second.

        

        :param meters: The MassFlow value in grams_per_second.
        :type grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(grams_per_second, MassFlowUnits.GramPerSecond)

    
    @staticmethod
    def from_grams_per_day(grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in grams_per_day.

        

        :param meters: The MassFlow value in grams_per_day.
        :type grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(grams_per_day, MassFlowUnits.GramPerDay)

    
    @staticmethod
    def from_grams_per_hour(grams_per_hour: float):
        """
        Create a new instance of MassFlow from a value in grams_per_hour.

        

        :param meters: The MassFlow value in grams_per_hour.
        :type grams_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(grams_per_hour, MassFlowUnits.GramPerHour)

    
    @staticmethod
    def from_kilograms_per_hour(kilograms_per_hour: float):
        """
        Create a new instance of MassFlow from a value in kilograms_per_hour.

        

        :param meters: The MassFlow value in kilograms_per_hour.
        :type kilograms_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilograms_per_hour, MassFlowUnits.KilogramPerHour)

    
    @staticmethod
    def from_kilograms_per_minute(kilograms_per_minute: float):
        """
        Create a new instance of MassFlow from a value in kilograms_per_minute.

        

        :param meters: The MassFlow value in kilograms_per_minute.
        :type kilograms_per_minute: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilograms_per_minute, MassFlowUnits.KilogramPerMinute)

    
    @staticmethod
    def from_tonnes_per_hour(tonnes_per_hour: float):
        """
        Create a new instance of MassFlow from a value in tonnes_per_hour.

        

        :param meters: The MassFlow value in tonnes_per_hour.
        :type tonnes_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(tonnes_per_hour, MassFlowUnits.TonnePerHour)

    
    @staticmethod
    def from_pounds_per_day(pounds_per_day: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_day.

        

        :param meters: The MassFlow value in pounds_per_day.
        :type pounds_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_day, MassFlowUnits.PoundPerDay)

    
    @staticmethod
    def from_pounds_per_hour(pounds_per_hour: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_hour.

        

        :param meters: The MassFlow value in pounds_per_hour.
        :type pounds_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_hour, MassFlowUnits.PoundPerHour)

    
    @staticmethod
    def from_pounds_per_minute(pounds_per_minute: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_minute.

        

        :param meters: The MassFlow value in pounds_per_minute.
        :type pounds_per_minute: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_minute, MassFlowUnits.PoundPerMinute)

    
    @staticmethod
    def from_pounds_per_second(pounds_per_second: float):
        """
        Create a new instance of MassFlow from a value in pounds_per_second.

        

        :param meters: The MassFlow value in pounds_per_second.
        :type pounds_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(pounds_per_second, MassFlowUnits.PoundPerSecond)

    
    @staticmethod
    def from_tonnes_per_day(tonnes_per_day: float):
        """
        Create a new instance of MassFlow from a value in tonnes_per_day.

        

        :param meters: The MassFlow value in tonnes_per_day.
        :type tonnes_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(tonnes_per_day, MassFlowUnits.TonnePerDay)

    
    @staticmethod
    def from_short_tons_per_hour(short_tons_per_hour: float):
        """
        Create a new instance of MassFlow from a value in short_tons_per_hour.

        

        :param meters: The MassFlow value in short_tons_per_hour.
        :type short_tons_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(short_tons_per_hour, MassFlowUnits.ShortTonPerHour)

    
    @staticmethod
    def from_nano_grams_per_second(nano_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in nano_grams_per_second.

        

        :param meters: The MassFlow value in nano_grams_per_second.
        :type nano_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(nano_grams_per_second, MassFlowUnits.NanoGramPerSecond)

    
    @staticmethod
    def from_micro_grams_per_second(micro_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in micro_grams_per_second.

        

        :param meters: The MassFlow value in micro_grams_per_second.
        :type micro_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(micro_grams_per_second, MassFlowUnits.MicroGramPerSecond)

    
    @staticmethod
    def from_milli_grams_per_second(milli_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in milli_grams_per_second.

        

        :param meters: The MassFlow value in milli_grams_per_second.
        :type milli_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(milli_grams_per_second, MassFlowUnits.MilliGramPerSecond)

    
    @staticmethod
    def from_centi_grams_per_second(centi_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in centi_grams_per_second.

        

        :param meters: The MassFlow value in centi_grams_per_second.
        :type centi_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(centi_grams_per_second, MassFlowUnits.CentiGramPerSecond)

    
    @staticmethod
    def from_deci_grams_per_second(deci_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in deci_grams_per_second.

        

        :param meters: The MassFlow value in deci_grams_per_second.
        :type deci_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(deci_grams_per_second, MassFlowUnits.DeciGramPerSecond)

    
    @staticmethod
    def from_deca_grams_per_second(deca_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in deca_grams_per_second.

        

        :param meters: The MassFlow value in deca_grams_per_second.
        :type deca_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(deca_grams_per_second, MassFlowUnits.DecaGramPerSecond)

    
    @staticmethod
    def from_hecto_grams_per_second(hecto_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in hecto_grams_per_second.

        

        :param meters: The MassFlow value in hecto_grams_per_second.
        :type hecto_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(hecto_grams_per_second, MassFlowUnits.HectoGramPerSecond)

    
    @staticmethod
    def from_kilo_grams_per_second(kilo_grams_per_second: float):
        """
        Create a new instance of MassFlow from a value in kilo_grams_per_second.

        

        :param meters: The MassFlow value in kilo_grams_per_second.
        :type kilo_grams_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilo_grams_per_second, MassFlowUnits.KiloGramPerSecond)

    
    @staticmethod
    def from_nano_grams_per_day(nano_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in nano_grams_per_day.

        

        :param meters: The MassFlow value in nano_grams_per_day.
        :type nano_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(nano_grams_per_day, MassFlowUnits.NanoGramPerDay)

    
    @staticmethod
    def from_micro_grams_per_day(micro_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in micro_grams_per_day.

        

        :param meters: The MassFlow value in micro_grams_per_day.
        :type micro_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(micro_grams_per_day, MassFlowUnits.MicroGramPerDay)

    
    @staticmethod
    def from_milli_grams_per_day(milli_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in milli_grams_per_day.

        

        :param meters: The MassFlow value in milli_grams_per_day.
        :type milli_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(milli_grams_per_day, MassFlowUnits.MilliGramPerDay)

    
    @staticmethod
    def from_centi_grams_per_day(centi_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in centi_grams_per_day.

        

        :param meters: The MassFlow value in centi_grams_per_day.
        :type centi_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(centi_grams_per_day, MassFlowUnits.CentiGramPerDay)

    
    @staticmethod
    def from_deci_grams_per_day(deci_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in deci_grams_per_day.

        

        :param meters: The MassFlow value in deci_grams_per_day.
        :type deci_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(deci_grams_per_day, MassFlowUnits.DeciGramPerDay)

    
    @staticmethod
    def from_deca_grams_per_day(deca_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in deca_grams_per_day.

        

        :param meters: The MassFlow value in deca_grams_per_day.
        :type deca_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(deca_grams_per_day, MassFlowUnits.DecaGramPerDay)

    
    @staticmethod
    def from_hecto_grams_per_day(hecto_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in hecto_grams_per_day.

        

        :param meters: The MassFlow value in hecto_grams_per_day.
        :type hecto_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(hecto_grams_per_day, MassFlowUnits.HectoGramPerDay)

    
    @staticmethod
    def from_kilo_grams_per_day(kilo_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in kilo_grams_per_day.

        

        :param meters: The MassFlow value in kilo_grams_per_day.
        :type kilo_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(kilo_grams_per_day, MassFlowUnits.KiloGramPerDay)

    
    @staticmethod
    def from_mega_grams_per_day(mega_grams_per_day: float):
        """
        Create a new instance of MassFlow from a value in mega_grams_per_day.

        

        :param meters: The MassFlow value in mega_grams_per_day.
        :type mega_grams_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(mega_grams_per_day, MassFlowUnits.MegaGramPerDay)

    
    @staticmethod
    def from_mega_pounds_per_day(mega_pounds_per_day: float):
        """
        Create a new instance of MassFlow from a value in mega_pounds_per_day.

        

        :param meters: The MassFlow value in mega_pounds_per_day.
        :type mega_pounds_per_day: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(mega_pounds_per_day, MassFlowUnits.MegaPoundPerDay)

    
    @staticmethod
    def from_mega_pounds_per_hour(mega_pounds_per_hour: float):
        """
        Create a new instance of MassFlow from a value in mega_pounds_per_hour.

        

        :param meters: The MassFlow value in mega_pounds_per_hour.
        :type mega_pounds_per_hour: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(mega_pounds_per_hour, MassFlowUnits.MegaPoundPerHour)

    
    @staticmethod
    def from_mega_pounds_per_minute(mega_pounds_per_minute: float):
        """
        Create a new instance of MassFlow from a value in mega_pounds_per_minute.

        

        :param meters: The MassFlow value in mega_pounds_per_minute.
        :type mega_pounds_per_minute: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(mega_pounds_per_minute, MassFlowUnits.MegaPoundPerMinute)

    
    @staticmethod
    def from_mega_pounds_per_second(mega_pounds_per_second: float):
        """
        Create a new instance of MassFlow from a value in mega_pounds_per_second.

        

        :param meters: The MassFlow value in mega_pounds_per_second.
        :type mega_pounds_per_second: float
        :return: A new instance of MassFlow.
        :rtype: MassFlow
        """
        return MassFlow(mega_pounds_per_second, MassFlowUnits.MegaPoundPerSecond)

    
    @property
    def grams_per_second(self) -> float:
        """
        
        """
        if self.__grams_per_second != None:
            return self.__grams_per_second
        self.__grams_per_second = self.__convert_from_base(MassFlowUnits.GramPerSecond)
        return self.__grams_per_second

    
    @property
    def grams_per_day(self) -> float:
        """
        
        """
        if self.__grams_per_day != None:
            return self.__grams_per_day
        self.__grams_per_day = self.__convert_from_base(MassFlowUnits.GramPerDay)
        return self.__grams_per_day

    
    @property
    def grams_per_hour(self) -> float:
        """
        
        """
        if self.__grams_per_hour != None:
            return self.__grams_per_hour
        self.__grams_per_hour = self.__convert_from_base(MassFlowUnits.GramPerHour)
        return self.__grams_per_hour

    
    @property
    def kilograms_per_hour(self) -> float:
        """
        
        """
        if self.__kilograms_per_hour != None:
            return self.__kilograms_per_hour
        self.__kilograms_per_hour = self.__convert_from_base(MassFlowUnits.KilogramPerHour)
        return self.__kilograms_per_hour

    
    @property
    def kilograms_per_minute(self) -> float:
        """
        
        """
        if self.__kilograms_per_minute != None:
            return self.__kilograms_per_minute
        self.__kilograms_per_minute = self.__convert_from_base(MassFlowUnits.KilogramPerMinute)
        return self.__kilograms_per_minute

    
    @property
    def tonnes_per_hour(self) -> float:
        """
        
        """
        if self.__tonnes_per_hour != None:
            return self.__tonnes_per_hour
        self.__tonnes_per_hour = self.__convert_from_base(MassFlowUnits.TonnePerHour)
        return self.__tonnes_per_hour

    
    @property
    def pounds_per_day(self) -> float:
        """
        
        """
        if self.__pounds_per_day != None:
            return self.__pounds_per_day
        self.__pounds_per_day = self.__convert_from_base(MassFlowUnits.PoundPerDay)
        return self.__pounds_per_day

    
    @property
    def pounds_per_hour(self) -> float:
        """
        
        """
        if self.__pounds_per_hour != None:
            return self.__pounds_per_hour
        self.__pounds_per_hour = self.__convert_from_base(MassFlowUnits.PoundPerHour)
        return self.__pounds_per_hour

    
    @property
    def pounds_per_minute(self) -> float:
        """
        
        """
        if self.__pounds_per_minute != None:
            return self.__pounds_per_minute
        self.__pounds_per_minute = self.__convert_from_base(MassFlowUnits.PoundPerMinute)
        return self.__pounds_per_minute

    
    @property
    def pounds_per_second(self) -> float:
        """
        
        """
        if self.__pounds_per_second != None:
            return self.__pounds_per_second
        self.__pounds_per_second = self.__convert_from_base(MassFlowUnits.PoundPerSecond)
        return self.__pounds_per_second

    
    @property
    def tonnes_per_day(self) -> float:
        """
        
        """
        if self.__tonnes_per_day != None:
            return self.__tonnes_per_day
        self.__tonnes_per_day = self.__convert_from_base(MassFlowUnits.TonnePerDay)
        return self.__tonnes_per_day

    
    @property
    def short_tons_per_hour(self) -> float:
        """
        
        """
        if self.__short_tons_per_hour != None:
            return self.__short_tons_per_hour
        self.__short_tons_per_hour = self.__convert_from_base(MassFlowUnits.ShortTonPerHour)
        return self.__short_tons_per_hour

    
    @property
    def nano_grams_per_second(self) -> float:
        """
        
        """
        if self.__nano_grams_per_second != None:
            return self.__nano_grams_per_second
        self.__nano_grams_per_second = self.__convert_from_base(MassFlowUnits.NanoGramPerSecond)
        return self.__nano_grams_per_second

    
    @property
    def micro_grams_per_second(self) -> float:
        """
        
        """
        if self.__micro_grams_per_second != None:
            return self.__micro_grams_per_second
        self.__micro_grams_per_second = self.__convert_from_base(MassFlowUnits.MicroGramPerSecond)
        return self.__micro_grams_per_second

    
    @property
    def milli_grams_per_second(self) -> float:
        """
        
        """
        if self.__milli_grams_per_second != None:
            return self.__milli_grams_per_second
        self.__milli_grams_per_second = self.__convert_from_base(MassFlowUnits.MilliGramPerSecond)
        return self.__milli_grams_per_second

    
    @property
    def centi_grams_per_second(self) -> float:
        """
        
        """
        if self.__centi_grams_per_second != None:
            return self.__centi_grams_per_second
        self.__centi_grams_per_second = self.__convert_from_base(MassFlowUnits.CentiGramPerSecond)
        return self.__centi_grams_per_second

    
    @property
    def deci_grams_per_second(self) -> float:
        """
        
        """
        if self.__deci_grams_per_second != None:
            return self.__deci_grams_per_second
        self.__deci_grams_per_second = self.__convert_from_base(MassFlowUnits.DeciGramPerSecond)
        return self.__deci_grams_per_second

    
    @property
    def deca_grams_per_second(self) -> float:
        """
        
        """
        if self.__deca_grams_per_second != None:
            return self.__deca_grams_per_second
        self.__deca_grams_per_second = self.__convert_from_base(MassFlowUnits.DecaGramPerSecond)
        return self.__deca_grams_per_second

    
    @property
    def hecto_grams_per_second(self) -> float:
        """
        
        """
        if self.__hecto_grams_per_second != None:
            return self.__hecto_grams_per_second
        self.__hecto_grams_per_second = self.__convert_from_base(MassFlowUnits.HectoGramPerSecond)
        return self.__hecto_grams_per_second

    
    @property
    def kilo_grams_per_second(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_second != None:
            return self.__kilo_grams_per_second
        self.__kilo_grams_per_second = self.__convert_from_base(MassFlowUnits.KiloGramPerSecond)
        return self.__kilo_grams_per_second

    
    @property
    def nano_grams_per_day(self) -> float:
        """
        
        """
        if self.__nano_grams_per_day != None:
            return self.__nano_grams_per_day
        self.__nano_grams_per_day = self.__convert_from_base(MassFlowUnits.NanoGramPerDay)
        return self.__nano_grams_per_day

    
    @property
    def micro_grams_per_day(self) -> float:
        """
        
        """
        if self.__micro_grams_per_day != None:
            return self.__micro_grams_per_day
        self.__micro_grams_per_day = self.__convert_from_base(MassFlowUnits.MicroGramPerDay)
        return self.__micro_grams_per_day

    
    @property
    def milli_grams_per_day(self) -> float:
        """
        
        """
        if self.__milli_grams_per_day != None:
            return self.__milli_grams_per_day
        self.__milli_grams_per_day = self.__convert_from_base(MassFlowUnits.MilliGramPerDay)
        return self.__milli_grams_per_day

    
    @property
    def centi_grams_per_day(self) -> float:
        """
        
        """
        if self.__centi_grams_per_day != None:
            return self.__centi_grams_per_day
        self.__centi_grams_per_day = self.__convert_from_base(MassFlowUnits.CentiGramPerDay)
        return self.__centi_grams_per_day

    
    @property
    def deci_grams_per_day(self) -> float:
        """
        
        """
        if self.__deci_grams_per_day != None:
            return self.__deci_grams_per_day
        self.__deci_grams_per_day = self.__convert_from_base(MassFlowUnits.DeciGramPerDay)
        return self.__deci_grams_per_day

    
    @property
    def deca_grams_per_day(self) -> float:
        """
        
        """
        if self.__deca_grams_per_day != None:
            return self.__deca_grams_per_day
        self.__deca_grams_per_day = self.__convert_from_base(MassFlowUnits.DecaGramPerDay)
        return self.__deca_grams_per_day

    
    @property
    def hecto_grams_per_day(self) -> float:
        """
        
        """
        if self.__hecto_grams_per_day != None:
            return self.__hecto_grams_per_day
        self.__hecto_grams_per_day = self.__convert_from_base(MassFlowUnits.HectoGramPerDay)
        return self.__hecto_grams_per_day

    
    @property
    def kilo_grams_per_day(self) -> float:
        """
        
        """
        if self.__kilo_grams_per_day != None:
            return self.__kilo_grams_per_day
        self.__kilo_grams_per_day = self.__convert_from_base(MassFlowUnits.KiloGramPerDay)
        return self.__kilo_grams_per_day

    
    @property
    def mega_grams_per_day(self) -> float:
        """
        
        """
        if self.__mega_grams_per_day != None:
            return self.__mega_grams_per_day
        self.__mega_grams_per_day = self.__convert_from_base(MassFlowUnits.MegaGramPerDay)
        return self.__mega_grams_per_day

    
    @property
    def mega_pounds_per_day(self) -> float:
        """
        
        """
        if self.__mega_pounds_per_day != None:
            return self.__mega_pounds_per_day
        self.__mega_pounds_per_day = self.__convert_from_base(MassFlowUnits.MegaPoundPerDay)
        return self.__mega_pounds_per_day

    
    @property
    def mega_pounds_per_hour(self) -> float:
        """
        
        """
        if self.__mega_pounds_per_hour != None:
            return self.__mega_pounds_per_hour
        self.__mega_pounds_per_hour = self.__convert_from_base(MassFlowUnits.MegaPoundPerHour)
        return self.__mega_pounds_per_hour

    
    @property
    def mega_pounds_per_minute(self) -> float:
        """
        
        """
        if self.__mega_pounds_per_minute != None:
            return self.__mega_pounds_per_minute
        self.__mega_pounds_per_minute = self.__convert_from_base(MassFlowUnits.MegaPoundPerMinute)
        return self.__mega_pounds_per_minute

    
    @property
    def mega_pounds_per_second(self) -> float:
        """
        
        """
        if self.__mega_pounds_per_second != None:
            return self.__mega_pounds_per_second
        self.__mega_pounds_per_second = self.__convert_from_base(MassFlowUnits.MegaPoundPerSecond)
        return self.__mega_pounds_per_second

    
    def to_string(self, unit: MassFlowUnits = MassFlowUnits.GramPerSecond) -> string:
        """
        Format the MassFlow to string.
        Note! the default format for MassFlow is GramPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MassFlowUnits.GramPerSecond:
            return f"""{self.grams_per_second} g/s"""
        
        if unit == MassFlowUnits.GramPerDay:
            return f"""{self.grams_per_day} g/d"""
        
        if unit == MassFlowUnits.GramPerHour:
            return f"""{self.grams_per_hour} g/h"""
        
        if unit == MassFlowUnits.KilogramPerHour:
            return f"""{self.kilograms_per_hour} kg/h"""
        
        if unit == MassFlowUnits.KilogramPerMinute:
            return f"""{self.kilograms_per_minute} kg/min"""
        
        if unit == MassFlowUnits.TonnePerHour:
            return f"""{self.tonnes_per_hour} t/h"""
        
        if unit == MassFlowUnits.PoundPerDay:
            return f"""{self.pounds_per_day} lb/d"""
        
        if unit == MassFlowUnits.PoundPerHour:
            return f"""{self.pounds_per_hour} lb/h"""
        
        if unit == MassFlowUnits.PoundPerMinute:
            return f"""{self.pounds_per_minute} lb/min"""
        
        if unit == MassFlowUnits.PoundPerSecond:
            return f"""{self.pounds_per_second} lb/s"""
        
        if unit == MassFlowUnits.TonnePerDay:
            return f"""{self.tonnes_per_day} t/d"""
        
        if unit == MassFlowUnits.ShortTonPerHour:
            return f"""{self.short_tons_per_hour} short tn/h"""
        
        if unit == MassFlowUnits.NanoGramPerSecond:
            return f"""{self.nano_grams_per_second} """
        
        if unit == MassFlowUnits.MicroGramPerSecond:
            return f"""{self.micro_grams_per_second} """
        
        if unit == MassFlowUnits.MilliGramPerSecond:
            return f"""{self.milli_grams_per_second} """
        
        if unit == MassFlowUnits.CentiGramPerSecond:
            return f"""{self.centi_grams_per_second} """
        
        if unit == MassFlowUnits.DeciGramPerSecond:
            return f"""{self.deci_grams_per_second} """
        
        if unit == MassFlowUnits.DecaGramPerSecond:
            return f"""{self.deca_grams_per_second} """
        
        if unit == MassFlowUnits.HectoGramPerSecond:
            return f"""{self.hecto_grams_per_second} """
        
        if unit == MassFlowUnits.KiloGramPerSecond:
            return f"""{self.kilo_grams_per_second} """
        
        if unit == MassFlowUnits.NanoGramPerDay:
            return f"""{self.nano_grams_per_day} """
        
        if unit == MassFlowUnits.MicroGramPerDay:
            return f"""{self.micro_grams_per_day} """
        
        if unit == MassFlowUnits.MilliGramPerDay:
            return f"""{self.milli_grams_per_day} """
        
        if unit == MassFlowUnits.CentiGramPerDay:
            return f"""{self.centi_grams_per_day} """
        
        if unit == MassFlowUnits.DeciGramPerDay:
            return f"""{self.deci_grams_per_day} """
        
        if unit == MassFlowUnits.DecaGramPerDay:
            return f"""{self.deca_grams_per_day} """
        
        if unit == MassFlowUnits.HectoGramPerDay:
            return f"""{self.hecto_grams_per_day} """
        
        if unit == MassFlowUnits.KiloGramPerDay:
            return f"""{self.kilo_grams_per_day} """
        
        if unit == MassFlowUnits.MegaGramPerDay:
            return f"""{self.mega_grams_per_day} """
        
        if unit == MassFlowUnits.MegaPoundPerDay:
            return f"""{self.mega_pounds_per_day} """
        
        if unit == MassFlowUnits.MegaPoundPerHour:
            return f"""{self.mega_pounds_per_hour} """
        
        if unit == MassFlowUnits.MegaPoundPerMinute:
            return f"""{self.mega_pounds_per_minute} """
        
        if unit == MassFlowUnits.MegaPoundPerSecond:
            return f"""{self.mega_pounds_per_second} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassFlowUnits = MassFlowUnits.GramPerSecond) -> string:
        """
        Get MassFlow unit abbreviation.
        Note! the default abbreviation for MassFlow is GramPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassFlowUnits.GramPerSecond:
            return """g/s"""
        
        if unit_abbreviation == MassFlowUnits.GramPerDay:
            return """g/d"""
        
        if unit_abbreviation == MassFlowUnits.GramPerHour:
            return """g/h"""
        
        if unit_abbreviation == MassFlowUnits.KilogramPerHour:
            return """kg/h"""
        
        if unit_abbreviation == MassFlowUnits.KilogramPerMinute:
            return """kg/min"""
        
        if unit_abbreviation == MassFlowUnits.TonnePerHour:
            return """t/h"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerDay:
            return """lb/d"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerHour:
            return """lb/h"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerMinute:
            return """lb/min"""
        
        if unit_abbreviation == MassFlowUnits.PoundPerSecond:
            return """lb/s"""
        
        if unit_abbreviation == MassFlowUnits.TonnePerDay:
            return """t/d"""
        
        if unit_abbreviation == MassFlowUnits.ShortTonPerHour:
            return """short tn/h"""
        
        if unit_abbreviation == MassFlowUnits.NanoGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MicroGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MilliGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.CentiGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.DeciGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.DecaGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.HectoGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.KiloGramPerSecond:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.NanoGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MicroGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MilliGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.CentiGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.DeciGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.DecaGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.HectoGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.KiloGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MegaGramPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MegaPoundPerDay:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MegaPoundPerHour:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MegaPoundPerMinute:
            return """"""
        
        if unit_abbreviation == MassFlowUnits.MegaPoundPerSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for +: 'MassFlow' and '{}'".format(type(other).__name__))
        return MassFlow(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for *: 'MassFlow' and '{}'".format(type(other).__name__))
        return MassFlow(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for -: 'MassFlow' and '{}'".format(type(other).__name__))
        return MassFlow(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for /: 'MassFlow' and '{}'".format(type(other).__name__))
        return MassFlow(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for %: 'MassFlow' and '{}'".format(type(other).__name__))
        return MassFlow(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for **: 'MassFlow' and '{}'".format(type(other).__name__))
        return MassFlow(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for ==: 'MassFlow' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for <: 'MassFlow' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for >: 'MassFlow' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for <=: 'MassFlow' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, MassFlow):
            raise TypeError("unsupported operand type(s) for >=: 'MassFlow' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value