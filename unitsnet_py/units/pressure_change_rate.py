from enum import Enum
import math
import string


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
        

class PressureChangeRate:
    """
    Pressure change rate is the ratio of the pressure change to the time during which the change occurred (value of pressure changes per unit time).

    Args:
        value (float): The value.
        from_unit (PressureChangeRateUnits): The PressureChangeRate unit to create from, The default unit is PascalPerSecond
    """
    def __init__(self, value: float, from_unit: PressureChangeRateUnits = PressureChangeRateUnits.PascalPerSecond):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__pascals_per_second = None
        
        self.__pascals_per_minute = None
        
        self.__millimeters_of_mercury_per_second = None
        
        self.__atmospheres_per_second = None
        
        self.__pounds_force_per_square_inch_per_second = None
        
        self.__pounds_force_per_square_inch_per_minute = None
        
        self.__kilopascals_per_second = None
        
        self.__megapascals_per_second = None
        
        self.__kilopascals_per_minute = None
        
        self.__megapascals_per_minute = None
        
        self.__kilopounds_force_per_square_inch_per_second = None
        
        self.__megapounds_force_per_square_inch_per_second = None
        
        self.__kilopounds_force_per_square_inch_per_minute = None
        
        self.__megapounds_force_per_square_inch_per_minute = None
        

    def __convert_from_base(self, from_unit: PressureChangeRateUnits) -> float:
        value = self.__value
        
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
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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

    
    def to_string(self, unit: PressureChangeRateUnits = PressureChangeRateUnits.PascalPerSecond) -> string:
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
        
        if unit == PressureChangeRateUnits.KilopascalPerSecond:
            return f"""{self.kilopascals_per_second} """
        
        if unit == PressureChangeRateUnits.MegapascalPerSecond:
            return f"""{self.megapascals_per_second} """
        
        if unit == PressureChangeRateUnits.KilopascalPerMinute:
            return f"""{self.kilopascals_per_minute} """
        
        if unit == PressureChangeRateUnits.MegapascalPerMinute:
            return f"""{self.megapascals_per_minute} """
        
        if unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond:
            return f"""{self.kilopounds_force_per_square_inch_per_second} """
        
        if unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond:
            return f"""{self.megapounds_force_per_square_inch_per_second} """
        
        if unit == PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute:
            return f"""{self.kilopounds_force_per_square_inch_per_minute} """
        
        if unit == PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute:
            return f"""{self.megapounds_force_per_square_inch_per_minute} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: PressureChangeRateUnits = PressureChangeRateUnits.PascalPerSecond) -> string:
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
        
        if unit_abbreviation == PressureChangeRateUnits.KilopascalPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapascalPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.KilopascalPerMinute:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapascalPerMinute:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.KilopoundForcePerSquareInchPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapoundForcePerSquareInchPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.KilopoundForcePerSquareInchPerMinute:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegapoundForcePerSquareInchPerMinute:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for +: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return PressureChangeRate(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for *: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return PressureChangeRate(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for -: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return PressureChangeRate(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for /: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return PressureChangeRate(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for %: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return PressureChangeRate(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for **: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return PressureChangeRate(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for ==: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for <: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for >: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for <=: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, PressureChangeRate):
            raise TypeError("unsupported operand type(s) for >=: 'PressureChangeRate' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value