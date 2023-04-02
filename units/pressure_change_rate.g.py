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
        
        KiloPascalPerSecond = 'kilo_pascal_per_second'
        """
            
        """
        
        MegaPascalPerSecond = 'mega_pascal_per_second'
        """
            
        """
        
        KiloPascalPerMinute = 'kilo_pascal_per_minute'
        """
            
        """
        
        MegaPascalPerMinute = 'mega_pascal_per_minute'
        """
            
        """
        
        KiloPoundForcePerSquareInchPerSecond = 'kilo_pound_force_per_square_inch_per_second'
        """
            
        """
        
        MegaPoundForcePerSquareInchPerSecond = 'mega_pound_force_per_square_inch_per_second'
        """
            
        """
        
        KiloPoundForcePerSquareInchPerMinute = 'kilo_pound_force_per_square_inch_per_minute'
        """
            
        """
        
        MegaPoundForcePerSquareInchPerMinute = 'mega_pound_force_per_square_inch_per_minute'
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
        
        self.__kilo_pascals_per_second = None
        
        self.__mega_pascals_per_second = None
        
        self.__kilo_pascals_per_minute = None
        
        self.__mega_pascals_per_minute = None
        
        self.__kilo_pounds_force_per_square_inch_per_second = None
        
        self.__mega_pounds_force_per_square_inch_per_second = None
        
        self.__kilo_pounds_force_per_square_inch_per_minute = None
        
        self.__mega_pounds_force_per_square_inch_per_minute = None
        

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
        
        if from_unit == PressureChangeRateUnits.KiloPascalPerSecond:
            return ((value) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegaPascalPerSecond:
            return ((value) / 1000000.0)
        
        if from_unit == PressureChangeRateUnits.KiloPascalPerMinute:
            return ((value * 60) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegaPascalPerMinute:
            return ((value * 60) / 1000000.0)
        
        if from_unit == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerSecond:
            return ((value / 6.894757293168361e3) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerSecond:
            return ((value / 6.894757293168361e3) / 1000000.0)
        
        if from_unit == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerMinute:
            return ((value / 6.894757293168361e3 * 60) / 1000.0)
        
        if from_unit == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerMinute:
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
        
        if to_unit == PressureChangeRateUnits.KiloPascalPerSecond:
            return ((value) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegaPascalPerSecond:
            return ((value) * 1000000.0)
        
        if to_unit == PressureChangeRateUnits.KiloPascalPerMinute:
            return ((value / 60) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegaPascalPerMinute:
            return ((value / 60) * 1000000.0)
        
        if to_unit == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerSecond:
            return ((value * 6.894757293168361e3) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerSecond:
            return ((value * 6.894757293168361e3) * 1000000.0)
        
        if to_unit == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerMinute:
            return ((value * 6.894757293168361e3 / 60) * 1000.0)
        
        if to_unit == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerMinute:
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
    def from_kilo_pascals_per_second(kilo_pascals_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in kilo_pascals_per_second.

        

        :param meters: The PressureChangeRate value in kilo_pascals_per_second.
        :type kilo_pascals_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilo_pascals_per_second, PressureChangeRateUnits.KiloPascalPerSecond)

    
    @staticmethod
    def from_mega_pascals_per_second(mega_pascals_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in mega_pascals_per_second.

        

        :param meters: The PressureChangeRate value in mega_pascals_per_second.
        :type mega_pascals_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(mega_pascals_per_second, PressureChangeRateUnits.MegaPascalPerSecond)

    
    @staticmethod
    def from_kilo_pascals_per_minute(kilo_pascals_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in kilo_pascals_per_minute.

        

        :param meters: The PressureChangeRate value in kilo_pascals_per_minute.
        :type kilo_pascals_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilo_pascals_per_minute, PressureChangeRateUnits.KiloPascalPerMinute)

    
    @staticmethod
    def from_mega_pascals_per_minute(mega_pascals_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in mega_pascals_per_minute.

        

        :param meters: The PressureChangeRate value in mega_pascals_per_minute.
        :type mega_pascals_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(mega_pascals_per_minute, PressureChangeRateUnits.MegaPascalPerMinute)

    
    @staticmethod
    def from_kilo_pounds_force_per_square_inch_per_second(kilo_pounds_force_per_square_inch_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in kilo_pounds_force_per_square_inch_per_second.

        

        :param meters: The PressureChangeRate value in kilo_pounds_force_per_square_inch_per_second.
        :type kilo_pounds_force_per_square_inch_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilo_pounds_force_per_square_inch_per_second, PressureChangeRateUnits.KiloPoundForcePerSquareInchPerSecond)

    
    @staticmethod
    def from_mega_pounds_force_per_square_inch_per_second(mega_pounds_force_per_square_inch_per_second: float):
        """
        Create a new instance of PressureChangeRate from a value in mega_pounds_force_per_square_inch_per_second.

        

        :param meters: The PressureChangeRate value in mega_pounds_force_per_square_inch_per_second.
        :type mega_pounds_force_per_square_inch_per_second: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(mega_pounds_force_per_square_inch_per_second, PressureChangeRateUnits.MegaPoundForcePerSquareInchPerSecond)

    
    @staticmethod
    def from_kilo_pounds_force_per_square_inch_per_minute(kilo_pounds_force_per_square_inch_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in kilo_pounds_force_per_square_inch_per_minute.

        

        :param meters: The PressureChangeRate value in kilo_pounds_force_per_square_inch_per_minute.
        :type kilo_pounds_force_per_square_inch_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(kilo_pounds_force_per_square_inch_per_minute, PressureChangeRateUnits.KiloPoundForcePerSquareInchPerMinute)

    
    @staticmethod
    def from_mega_pounds_force_per_square_inch_per_minute(mega_pounds_force_per_square_inch_per_minute: float):
        """
        Create a new instance of PressureChangeRate from a value in mega_pounds_force_per_square_inch_per_minute.

        

        :param meters: The PressureChangeRate value in mega_pounds_force_per_square_inch_per_minute.
        :type mega_pounds_force_per_square_inch_per_minute: float
        :return: A new instance of PressureChangeRate.
        :rtype: PressureChangeRate
        """
        return PressureChangeRate(mega_pounds_force_per_square_inch_per_minute, PressureChangeRateUnits.MegaPoundForcePerSquareInchPerMinute)

    
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
    def kilo_pascals_per_second(self) -> float:
        """
        
        """
        if self.__kilo_pascals_per_second != None:
            return self.__kilo_pascals_per_second
        self.__kilo_pascals_per_second = self.__convert_from_base(PressureChangeRateUnits.KiloPascalPerSecond)
        return self.__kilo_pascals_per_second

    
    @property
    def mega_pascals_per_second(self) -> float:
        """
        
        """
        if self.__mega_pascals_per_second != None:
            return self.__mega_pascals_per_second
        self.__mega_pascals_per_second = self.__convert_from_base(PressureChangeRateUnits.MegaPascalPerSecond)
        return self.__mega_pascals_per_second

    
    @property
    def kilo_pascals_per_minute(self) -> float:
        """
        
        """
        if self.__kilo_pascals_per_minute != None:
            return self.__kilo_pascals_per_minute
        self.__kilo_pascals_per_minute = self.__convert_from_base(PressureChangeRateUnits.KiloPascalPerMinute)
        return self.__kilo_pascals_per_minute

    
    @property
    def mega_pascals_per_minute(self) -> float:
        """
        
        """
        if self.__mega_pascals_per_minute != None:
            return self.__mega_pascals_per_minute
        self.__mega_pascals_per_minute = self.__convert_from_base(PressureChangeRateUnits.MegaPascalPerMinute)
        return self.__mega_pascals_per_minute

    
    @property
    def kilo_pounds_force_per_square_inch_per_second(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_square_inch_per_second != None:
            return self.__kilo_pounds_force_per_square_inch_per_second
        self.__kilo_pounds_force_per_square_inch_per_second = self.__convert_from_base(PressureChangeRateUnits.KiloPoundForcePerSquareInchPerSecond)
        return self.__kilo_pounds_force_per_square_inch_per_second

    
    @property
    def mega_pounds_force_per_square_inch_per_second(self) -> float:
        """
        
        """
        if self.__mega_pounds_force_per_square_inch_per_second != None:
            return self.__mega_pounds_force_per_square_inch_per_second
        self.__mega_pounds_force_per_square_inch_per_second = self.__convert_from_base(PressureChangeRateUnits.MegaPoundForcePerSquareInchPerSecond)
        return self.__mega_pounds_force_per_square_inch_per_second

    
    @property
    def kilo_pounds_force_per_square_inch_per_minute(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force_per_square_inch_per_minute != None:
            return self.__kilo_pounds_force_per_square_inch_per_minute
        self.__kilo_pounds_force_per_square_inch_per_minute = self.__convert_from_base(PressureChangeRateUnits.KiloPoundForcePerSquareInchPerMinute)
        return self.__kilo_pounds_force_per_square_inch_per_minute

    
    @property
    def mega_pounds_force_per_square_inch_per_minute(self) -> float:
        """
        
        """
        if self.__mega_pounds_force_per_square_inch_per_minute != None:
            return self.__mega_pounds_force_per_square_inch_per_minute
        self.__mega_pounds_force_per_square_inch_per_minute = self.__convert_from_base(PressureChangeRateUnits.MegaPoundForcePerSquareInchPerMinute)
        return self.__mega_pounds_force_per_square_inch_per_minute

    
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
        
        if unit == PressureChangeRateUnits.KiloPascalPerSecond:
            return f"""{self.kilo_pascals_per_second} """
        
        if unit == PressureChangeRateUnits.MegaPascalPerSecond:
            return f"""{self.mega_pascals_per_second} """
        
        if unit == PressureChangeRateUnits.KiloPascalPerMinute:
            return f"""{self.kilo_pascals_per_minute} """
        
        if unit == PressureChangeRateUnits.MegaPascalPerMinute:
            return f"""{self.mega_pascals_per_minute} """
        
        if unit == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerSecond:
            return f"""{self.kilo_pounds_force_per_square_inch_per_second} """
        
        if unit == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerSecond:
            return f"""{self.mega_pounds_force_per_square_inch_per_second} """
        
        if unit == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerMinute:
            return f"""{self.kilo_pounds_force_per_square_inch_per_minute} """
        
        if unit == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerMinute:
            return f"""{self.mega_pounds_force_per_square_inch_per_minute} """
        
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
        
        if unit_abbreviation == PressureChangeRateUnits.KiloPascalPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegaPascalPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.KiloPascalPerMinute:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegaPascalPerMinute:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerSecond:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.KiloPoundForcePerSquareInchPerMinute:
            return """"""
        
        if unit_abbreviation == PressureChangeRateUnits.MegaPoundForcePerSquareInchPerMinute:
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