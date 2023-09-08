from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class PressureChangeRateUnits(Enum):
        """
            PressureChangeRateUnits enumeration
        """
        
        PascalPerSecond = 'pascal_per_second'
        """
            
        """
        
        PascalPerMinute = 'pascal_per_minute'
        """
            
        """
        
        MillimeterOfMercuryPerSecond = 'millimeter_of_mercury_per_second'
        """
            
        """
        
        AtmospherePerSecond = 'atmosphere_per_second'
        """
            
        """
        
        PoundForcePerSquareInchPerSecond = 'pound_force_per_square_inch_per_second'
        """
            
        """
        
        PoundForcePerSquareInchPerMinute = 'pound_force_per_square_inch_per_minute'
        """
            
        """
        
        BarPerSecond = 'bar_per_second'
        """
            
        """
        
        BarPerMinute = 'bar_per_minute'
        """
            
        """
        
        KilopascalPerSecond = 'kilopascal_per_second'
        """
            
        """
        
        MegapascalPerSecond = 'megapascal_per_second'
        """
            
        """
        
        KilopascalPerMinute = 'kilopascal_per_minute'
        """
            
        """
        
        MegapascalPerMinute = 'megapascal_per_minute'
        """
            
        """
        
        KilopoundForcePerSquareInchPerSecond = 'kilopound_force_per_square_inch_per_second'
        """
            
        """
        
        MegapoundForcePerSquareInchPerSecond = 'megapound_force_per_square_inch_per_second'
        """
            
        """
        
        KilopoundForcePerSquareInchPerMinute = 'kilopound_force_per_square_inch_per_minute'
        """
            
        """
        
        MegapoundForcePerSquareInchPerMinute = 'megapound_force_per_square_inch_per_minute'
        """
            
        """
        
        MillibarPerSecond = 'millibar_per_second'
        """
            
        """
        
        MillibarPerMinute = 'millibar_per_minute'
        """
            
        """
        

class PressureChangeRate(AbstractMeasure):
    """
    Pressure change rate is the ratio of the pressure change to the time during which the change occurred (value of pressure changes per unit time).

    Args:
        value (float): The value.
        from_unit (PressureChangeRateUnits): The PressureChangeRate unit to create from, The default unit is PascalPerSecond
    """
    def __init__(self, value: float, from_unit: PressureChangeRateUnits = PressureChangeRateUnits.PascalPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__pascals_per_second = None
        
        self.__pascals_per_minute = None
        
        self.__millimeters_of_mercury_per_second = None
        
        self.__atmospheres_per_second = None
        
        self.__pounds_force_per_square_inch_per_second = None
        
        self.__pounds_force_per_square_inch_per_minute = None
        
        self.__bars_per_second = None
        
        self.__bars_per_minute = None
        
        self.__kilopascals_per_second = None
        
        self.__megapascals_per_second = None
        
        self.__kilopascals_per_minute = None
        
        self.__megapascals_per_minute = None
        
        self.__kilopounds_force_per_square_inch_per_second = None
        
        self.__megapounds_force_per_square_inch_per_second = None
        
        self.__kilopounds_force_per_square_inch_per_minute = None
        
        self.__megapounds_force_per_square_inch_per_minute = None
        
        self.__millibars_per_second = None
        
        self.__millibars_per_minute = None
        

    def convert(self, unit: PressureChangeRateUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: PressureChangeRateUnits) -> float:
        value = self._value
        
        if from_unit == PressureChangeRateUnits.PascalPerSecond:
            return (value)
        
        if from_unit == PressureChangeRateUnits.PascalPerMinute:
            return (value * 60)
        
        if from_unit == PressureChangeRateUnits.MillimeterOfMercuryPerSecond:
            return (value / 133.322)
        
        if from_unit == PressureChangeRateUnits.AtmospherePerSecond:
            return (value / (1.01325 * 1e5))
        
        if from_unit == PressureChangeRateUnits.PoundForcePerSquareInchPerSecond:
            return (value / 6.894757293168361e3)
        
        if from_unit == PressureChangeRateUnits.PoundForcePerSquareInchPerMinute:
            return (value / 6.894757293168361e3 * 60)
        
        if from_unit == PressureChangeRateUnits.BarPerSecond:
            return (value / 1e5)
        
        if from_unit == PressureChangeRateUnits.BarPerMinute:
            return (value / 1e5 * 60)
        
        if from_unit == PressureChangeRateUnits.KilopascalPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegapascalPerSecond:
            return ((value) / 1000000.0)
        
        if from_unit == PressureChangeRateUnits.KilopascalPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegapascalPerMinute:
            return ((value * 60) / 1000000.0)
        
        if from_unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond:
            return ((value / 6.894757293168361e3) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond:
            return ((value / 6.894757293168361e3) / 1000000.0)
        
        if from_unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute:
            return ((value / 6.894757293168361e3 * 60) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute:
            return ((value / 6.894757293168361e3 * 60) / 1000000.0)
        
        if from_unit == PressureChangeRateUnits.MillibarPerSecond:
            return ((value / 1e5) / 0.001)
        
        if from_unit == PressureChangeRateUnits.MillibarPerMinute:
            return ((value / 1e5 * 60) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PressureChangeRateUnits) -> float:
        
        if to_unit == PressureChangeRateUnits.PascalPerSecond:
            return (value)
        
        if to_unit == PressureChangeRateUnits.PascalPerMinute:
            return (value / 60)
        
        if to_unit == PressureChangeRateUnits.MillimeterOfMercuryPerSecond:
            return (value * 133.322)
        
        if to_unit == PressureChangeRateUnits.AtmospherePerSecond:
            return (value * 1.01325 * 1e5)
        
        if to_unit == PressureChangeRateUnits.PoundForcePerSquareInchPerSecond:
            return (value * 6.894757293168361e3)
        
        if to_unit == PressureChangeRateUnits.PoundForcePerSquareInchPerMinute:
            return (value * 6.894757293168361e3 / 60)
        
        if to_unit == PressureChangeRateUnits.BarPerSecond:
            return (value * 1e5)
        
        if to_unit == PressureChangeRateUnits.BarPerMinute:
            return (value * 1e5 / 60)
        
        if to_unit == PressureChangeRateUnits.KilopascalPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegapascalPerSecond:
            return ((value) * 1000000.0)
        
        if to_unit == PressureChangeRateUnits.KilopascalPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegapascalPerMinute:
            return ((value / 60) * 1000000.0)
        
        if to_unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond:
            return ((value * 6.894757293168361e3) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond:
            return ((value * 6.894757293168361e3) * 1000000.0)
        
        if to_unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute:
            return ((value * 6.894757293168361e3 / 60) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute:
            return ((value * 6.894757293168361e3 / 60) * 1000000.0)
        
        if to_unit == PressureChangeRateUnits.MillibarPerSecond:
            return ((value * 1e5) * 0.001)
        
        if to_unit == PressureChangeRateUnits.MillibarPerMinute:
            return ((value * 1e5 / 60) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_pascals_per_second(pascals_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in pascals_per_second.

        

        :param meters: The PressureChangeRate value in pascals_per_second.
        :type pascals_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(pascals_per_second, PressureChangeRateUnits.PascalPerSecond)

    
    @staticmethod
    def from_pascals_per_minute(pascals_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in pascals_per_minute.

        

        :param meters: The PressureChangeRate value in pascals_per_minute.
        :type pascals_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(pascals_per_minute, PressureChangeRateUnits.PascalPerMinute)

    
    @staticmethod
    def from_millimeters_of_mercury_per_second(millimeters_of_mercury_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in millimeters_of_mercury_per_second.

        

        :param meters: The PressureChangeRate value in millimeters_of_mercury_per_second.
        :type millimeters_of_mercury_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(millimeters_of_mercury_per_second, PressureChangeRateUnits.MillimeterOfMercuryPerSecond)

    
    @staticmethod
    def from_atmospheres_per_second(atmospheres_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in atmospheres_per_second.

        

        :param meters: The PressureChangeRate value in atmospheres_per_second.
        :type atmospheres_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(atmospheres_per_second, PressureChangeRateUnits.AtmospherePerSecond)

    
    @staticmethod
    def from_pounds_force_per_square_inch_per_second(pounds_force_per_square_inch_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in pounds_force_per_square_inch_per_second.

        

        :param meters: The PressureChangeRate value in pounds_force_per_square_inch_per_second.
        :type pounds_force_per_square_inch_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(pounds_force_per_square_inch_per_second, PressureChangeRateUnits.PoundForcePerSquareInchPerSecond)

    
    @staticmethod
    def from_pounds_force_per_square_inch_per_minute(pounds_force_per_square_inch_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in pounds_force_per_square_inch_per_minute.

        

        :param meters: The PressureChangeRate value in pounds_force_per_square_inch_per_minute.
        :type pounds_force_per_square_inch_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(pounds_force_per_square_inch_per_minute, PressureChangeRateUnits.PoundForcePerSquareInchPerMinute)

    
    @staticmethod
    def from_bars_per_second(bars_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in bars_per_second.

        

        :param meters: The PressureChangeRate value in bars_per_second.
        :type bars_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(bars_per_second, PressureChangeRateUnits.BarPerSecond)

    
    @staticmethod
    def from_bars_per_minute(bars_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in bars_per_minute.

        

        :param meters: The PressureChangeRate value in bars_per_minute.
        :type bars_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(bars_per_minute, PressureChangeRateUnits.BarPerMinute)

    
    @staticmethod
    def from_kilopascals_per_second(kilopascals_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in kilopascals_per_second.

        

        :param meters: The PressureChangeRate value in kilopascals_per_second.
        :type kilopascals_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilopascals_per_second, PressureChangeRateUnits.KilopascalPerSecond)

    
    @staticmethod
    def from_megapascals_per_second(megapascals_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in megapascals_per_second.

        

        :param meters: The PressureChangeRate value in megapascals_per_second.
        :type megapascals_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(megapascals_per_second, PressureChangeRateUnits.MegapascalPerSecond)

    
    @staticmethod
    def from_kilopascals_per_minute(kilopascals_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in kilopascals_per_minute.

        

        :param meters: The PressureChangeRate value in kilopascals_per_minute.
        :type kilopascals_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilopascals_per_minute, PressureChangeRateUnits.KilopascalPerMinute)

    
    @staticmethod
    def from_megapascals_per_minute(megapascals_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in megapascals_per_minute.

        

        :param meters: The PressureChangeRate value in megapascals_per_minute.
        :type megapascals_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(megapascals_per_minute, PressureChangeRateUnits.MegapascalPerMinute)

    
    @staticmethod
    def from_kilopounds_force_per_square_inch_per_second(kilopounds_force_per_square_inch_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in kilopounds_force_per_square_inch_per_second.

        

        :param meters: The PressureChangeRate value in kilopounds_force_per_square_inch_per_second.
        :type kilopounds_force_per_square_inch_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilopounds_force_per_square_inch_per_second, PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond)

    
    @staticmethod
    def from_megapounds_force_per_square_inch_per_second(megapounds_force_per_square_inch_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in megapounds_force_per_square_inch_per_second.

        

        :param meters: The PressureChangeRate value in megapounds_force_per_square_inch_per_second.
        :type megapounds_force_per_square_inch_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(megapounds_force_per_square_inch_per_second, PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond)

    
    @staticmethod
    def from_kilopounds_force_per_square_inch_per_minute(kilopounds_force_per_square_inch_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in kilopounds_force_per_square_inch_per_minute.

        

        :param meters: The PressureChangeRate value in kilopounds_force_per_square_inch_per_minute.
        :type kilopounds_force_per_square_inch_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilopounds_force_per_square_inch_per_minute, PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute)

    
    @staticmethod
    def from_megapounds_force_per_square_inch_per_minute(megapounds_force_per_square_inch_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in megapounds_force_per_square_inch_per_minute.

        

        :param meters: The PressureChangeRate value in megapounds_force_per_square_inch_per_minute.
        :type megapounds_force_per_square_inch_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(megapounds_force_per_square_inch_per_minute, PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute)

    
    @staticmethod
    def from_millibars_per_second(millibars_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in millibars_per_second.

        

        :param meters: The PressureChangeRate value in millibars_per_second.
        :type millibars_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(millibars_per_second, PressureChangeRateUnits.MillibarPerSecond)

    
    @staticmethod
    def from_millibars_per_minute(millibars_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in millibars_per_minute.

        

        :param meters: The PressureChangeRate value in millibars_per_minute.
        :type millibars_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(millibars_per_minute, PressureChangeRateUnits.MillibarPerMinute)

    
    @property
    def pascals_per_second(self) -> float:
        """
        
        """
        if self.__pascals_per_second != None:
            return self.__pascals_per_second
        self.__pascals_per_second = self.__convert_from_base(PressureChangeRateUnits.PascalPerSecond)
        return self.__pascals_per_second

    
    @property
    def pascals_per_minute(self) -> float:
        """
        
        """
        if self.__pascals_per_minute != None:
            return self.__pascals_per_minute
        self.__pascals_per_minute = self.__convert_from_base(PressureChangeRateUnits.PascalPerMinute)
        return self.__pascals_per_minute

    
    @property
    def millimeters_of_mercury_per_second(self) -> float:
        """
        
        """
        if self.__millimeters_of_mercury_per_second != None:
            return self.__millimeters_of_mercury_per_second
        self.__millimeters_of_mercury_per_second = self.__convert_from_base(PressureChangeRateUnits.MillimeterOfMercuryPerSecond)
        return self.__millimeters_of_mercury_per_second

    
    @property
    def atmospheres_per_second(self) -> float:
        """
        
        """
        if self.__atmospheres_per_second != None:
            return self.__atmospheres_per_second
        self.__atmospheres_per_second = self.__convert_from_base(PressureChangeRateUnits.AtmospherePerSecond)
        return self.__atmospheres_per_second

    
    @property
    def pounds_force_per_square_inch_per_second(self) -> float:
        """
        
        """
        if self.__pounds_force_per_square_inch_per_second != None:
            return self.__pounds_force_per_square_inch_per_second
        self.__pounds_force_per_square_inch_per_second = self.__convert_from_base(PressureChangeRateUnits.PoundForcePerSquareInchPerSecond)
        return self.__pounds_force_per_square_inch_per_second

    
    @property
    def pounds_force_per_square_inch_per_minute(self) -> float:
        """
        
        """
        if self.__pounds_force_per_square_inch_per_minute != None:
            return self.__pounds_force_per_square_inch_per_minute
        self.__pounds_force_per_square_inch_per_minute = self.__convert_from_base(PressureChangeRateUnits.PoundForcePerSquareInchPerMinute)
        return self.__pounds_force_per_square_inch_per_minute

    
    @property
    def bars_per_second(self) -> float:
        """
        
        """
        if self.__bars_per_second != None:
            return self.__bars_per_second
        self.__bars_per_second = self.__convert_from_base(PressureChangeRateUnits.BarPerSecond)
        return self.__bars_per_second

    
    @property
    def bars_per_minute(self) -> float:
        """
        
        """
        if self.__bars_per_minute != None:
            return self.__bars_per_minute
        self.__bars_per_minute = self.__convert_from_base(PressureChangeRateUnits.BarPerMinute)
        return self.__bars_per_minute

    
    @property
    def kilopascals_per_second(self) -> float:
        """
        
        """
        if self.__kilopascals_per_second != None:
            return self.__kilopascals_per_second
        self.__kilopascals_per_second = self.__convert_from_base(PressureChangeRateUnits.KilopascalPerSecond)
        return self.__kilopascals_per_second

    
    @property
    def megapascals_per_second(self) -> float:
        """
        
        """
        if self.__megapascals_per_second != None:
            return self.__megapascals_per_second
        self.__megapascals_per_second = self.__convert_from_base(PressureChangeRateUnits.MegapascalPerSecond)
        return self.__megapascals_per_second

    
    @property
    def kilopascals_per_minute(self) -> float:
        """
        
        """
        if self.__kilopascals_per_minute != None:
            return self.__kilopascals_per_minute
        self.__kilopascals_per_minute = self.__convert_from_base(PressureChangeRateUnits.KilopascalPerMinute)
        return self.__kilopascals_per_minute

    
    @property
    def megapascals_per_minute(self) -> float:
        """
        
        """
        if self.__megapascals_per_minute != None:
            return self.__megapascals_per_minute
        self.__megapascals_per_minute = self.__convert_from_base(PressureChangeRateUnits.MegapascalPerMinute)
        return self.__megapascals_per_minute

    
    @property
    def kilopounds_force_per_square_inch_per_second(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_square_inch_per_second != None:
            return self.__kilopounds_force_per_square_inch_per_second
        self.__kilopounds_force_per_square_inch_per_second = self.__convert_from_base(PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond)
        return self.__kilopounds_force_per_square_inch_per_second

    
    @property
    def megapounds_force_per_square_inch_per_second(self) -> float:
        """
        
        """
        if self.__megapounds_force_per_square_inch_per_second != None:
            return self.__megapounds_force_per_square_inch_per_second
        self.__megapounds_force_per_square_inch_per_second = self.__convert_from_base(PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond)
        return self.__megapounds_force_per_square_inch_per_second

    
    @property
    def kilopounds_force_per_square_inch_per_minute(self) -> float:
        """
        
        """
        if self.__kilopounds_force_per_square_inch_per_minute != None:
            return self.__kilopounds_force_per_square_inch_per_minute
        self.__kilopounds_force_per_square_inch_per_minute = self.__convert_from_base(PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute)
        return self.__kilopounds_force_per_square_inch_per_minute

    
    @property
    def megapounds_force_per_square_inch_per_minute(self) -> float:
        """
        
        """
        if self.__megapounds_force_per_square_inch_per_minute != None:
            return self.__megapounds_force_per_square_inch_per_minute
        self.__megapounds_force_per_square_inch_per_minute = self.__convert_from_base(PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute)
        return self.__megapounds_force_per_square_inch_per_minute

    
    @property
    def millibars_per_second(self) -> float:
        """
        
        """
        if self.__millibars_per_second != None:
            return self.__millibars_per_second
        self.__millibars_per_second = self.__convert_from_base(PressureChangeRateUnits.MillibarPerSecond)
        return self.__millibars_per_second

    
    @property
    def millibars_per_minute(self) -> float:
        """
        
        """
        if self.__millibars_per_minute != None:
            return self.__millibars_per_minute
        self.__millibars_per_minute = self.__convert_from_base(PressureChangeRateUnits.MillibarPerMinute)
        return self.__millibars_per_minute

    
    def to_string(self, unit: PressureChangeRateUnits = PressureChangeRateUnits.PascalPerSecond) -> str:
        """
        Format the PressureChangeRate to string.
        Note! the default format for PressureChangeRate is PascalPerSecond.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PressureChangeRateUnits.PascalPerSecond:
            return f"""{self.pascals_per_second} Pa/s"""
        
        if unit == PressureChangeRateUnits.PascalPerMinute:
            return f"""{self.pascals_per_minute} Pa/min"""
        
        if unit == PressureChangeRateUnits.MillimeterOfMercuryPerSecond:
            return f"""{self.millimeters_of_mercury_per_second} mmHg/s"""
        
        if unit == PressureChangeRateUnits.AtmospherePerSecond:
            return f"""{self.atmospheres_per_second} atm/s"""
        
        if unit == PressureChangeRateUnits.PoundForcePerSquareInchPerSecond:
            return f"""{self.pounds_force_per_square_inch_per_second} psi/s"""
        
        if unit == PressureChangeRateUnits.PoundForcePerSquareInchPerMinute:
            return f"""{self.pounds_force_per_square_inch_per_minute} psi/min"""
        
        if unit == PressureChangeRateUnits.BarPerSecond:
            return f"""{self.bars_per_second} bar/s"""
        
        if unit == PressureChangeRateUnits.BarPerMinute:
            return f"""{self.bars_per_minute} bar/min"""
        
        if unit == PressureChangeRateUnits.KilopascalPerSecond:
            return f"""{self.kilopascals_per_second} kPa/s"""
        
        if unit == PressureChangeRateUnits.MegapascalPerSecond:
            return f"""{self.megapascals_per_second} MPa/s"""
        
        if unit == PressureChangeRateUnits.KilopascalPerMinute:
            return f"""{self.kilopascals_per_minute} kPa/min"""
        
        if unit == PressureChangeRateUnits.MegapascalPerMinute:
            return f"""{self.megapascals_per_minute} MPa/min"""
        
        if unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond:
            return f"""{self.kilopounds_force_per_square_inch_per_second} kpsi/s"""
        
        if unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond:
            return f"""{self.megapounds_force_per_square_inch_per_second} Mpsi/s"""
        
        if unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute:
            return f"""{self.kilopounds_force_per_square_inch_per_minute} kpsi/min"""
        
        if unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute:
            return f"""{self.megapounds_force_per_square_inch_per_minute} Mpsi/min"""
        
        if unit == PressureChangeRateUnits.MillibarPerSecond:
            return f"""{self.millibars_per_second} mbar/s"""
        
        if unit == PressureChangeRateUnits.MillibarPerMinute:
            return f"""{self.millibars_per_minute} mbar/min"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PressureChangeRateUnits = PressureChangeRateUnits.PascalPerSecond) -> str:
        """
        Get PressureChangeRate unit abbreviation.
        Note! the default abbreviation for PressureChangeRate is PascalPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PressureChangeRateUnits.PascalPerSecond:
            return """Pa/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.PascalPerMinute:
            return """Pa/min"""
        
        if unit_abbreviation == PressureChangeRateUnits.MillimeterOfMercuryPerSecond:
            return """mmHg/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.AtmospherePerSecond:
            return """atm/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.PoundForcePerSquareInchPerSecond:
            return """psi/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.PoundForcePerSquareInchPerMinute:
            return """psi/min"""
        
        if unit_abbreviation == PressureChangeRateUnits.BarPerSecond:
            return """bar/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.BarPerMinute:
            return """bar/min"""
        
        if unit_abbreviation == PressureChangeRateUnits.KilopascalPerSecond:
            return """kPa/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapascalPerSecond:
            return """MPa/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.KilopascalPerMinute:
            return """kPa/min"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapascalPerMinute:
            return """MPa/min"""
        
        if unit_abbreviation == PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond:
            return """kpsi/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond:
            return """Mpsi/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute:
            return """kpsi/min"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute:
            return """Mpsi/min"""
        
        if unit_abbreviation == PressureChangeRateUnits.MillibarPerSecond:
            return """mbar/s"""
        
        if unit_abbreviation == PressureChangeRateUnits.MillibarPerMinute:
            return """mbar/min"""
        