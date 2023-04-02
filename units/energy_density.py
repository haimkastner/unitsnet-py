from enum import Enum
import math
import string


class EnergyDensityUnits(Enum):
        """
            EnergyDensityUnits enumeration
        """
        
        JoulePerCubicMeter = 'joule_per_cubic_meter'
        """
            
        """
        
        WattHourPerCubicMeter = 'watt_hour_per_cubic_meter'
        """
            
        """
        
        KiloJoulePerCubicMeter = 'kilo_joule_per_cubic_meter'
        """
            
        """
        
        MegaJoulePerCubicMeter = 'mega_joule_per_cubic_meter'
        """
            
        """
        
        GigaJoulePerCubicMeter = 'giga_joule_per_cubic_meter'
        """
            
        """
        
        TeraJoulePerCubicMeter = 'tera_joule_per_cubic_meter'
        """
            
        """
        
        PetaJoulePerCubicMeter = 'peta_joule_per_cubic_meter'
        """
            
        """
        
        KiloWattHourPerCubicMeter = 'kilo_watt_hour_per_cubic_meter'
        """
            
        """
        
        MegaWattHourPerCubicMeter = 'mega_watt_hour_per_cubic_meter'
        """
            
        """
        
        GigaWattHourPerCubicMeter = 'giga_watt_hour_per_cubic_meter'
        """
            
        """
        
        TeraWattHourPerCubicMeter = 'tera_watt_hour_per_cubic_meter'
        """
            
        """
        
        PetaWattHourPerCubicMeter = 'peta_watt_hour_per_cubic_meter'
        """
            
        """
        

class EnergyDensity:
    """
    None

    Args:
        value (float): The value.
        from_unit (EnergyDensityUnits): The EnergyDensity unit to create from, The default unit is JoulePerCubicMeter
    """
    def __init__(self, value: float, from_unit: EnergyDensityUnits = EnergyDensityUnits.JoulePerCubicMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_cubic_meter = None
        
        self.__watt_hours_per_cubic_meter = None
        
        self.__kilo_joules_per_cubic_meter = None
        
        self.__mega_joules_per_cubic_meter = None
        
        self.__giga_joules_per_cubic_meter = None
        
        self.__tera_joules_per_cubic_meter = None
        
        self.__peta_joules_per_cubic_meter = None
        
        self.__kilo_watt_hours_per_cubic_meter = None
        
        self.__mega_watt_hours_per_cubic_meter = None
        
        self.__giga_watt_hours_per_cubic_meter = None
        
        self.__tera_watt_hours_per_cubic_meter = None
        
        self.__peta_watt_hours_per_cubic_meter = None
        

    def __convert_from_base(self, from_unit: EnergyDensityUnits) -> float:
        value = self.__value
        
        if from_unit == EnergyDensityUnits.JoulePerCubicMeter:
            return (value)
        
        if from_unit == EnergyDensityUnits.WattHourPerCubicMeter:
            return (value / 3.6e+3)
        
        if from_unit == EnergyDensityUnits.KiloJoulePerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == EnergyDensityUnits.MegaJoulePerCubicMeter:
            return ((value) / 1000000.0)
        
        if from_unit == EnergyDensityUnits.GigaJoulePerCubicMeter:
            return ((value) / 1000000000.0)
        
        if from_unit == EnergyDensityUnits.TeraJoulePerCubicMeter:
            return ((value) / 1000000000000.0)
        
        if from_unit == EnergyDensityUnits.PetaJoulePerCubicMeter:
            return ((value) / 1000000000000000.0)
        
        if from_unit == EnergyDensityUnits.KiloWattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000.0)
        
        if from_unit == EnergyDensityUnits.MegaWattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000.0)
        
        if from_unit == EnergyDensityUnits.GigaWattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000000.0)
        
        if from_unit == EnergyDensityUnits.TeraWattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000000000.0)
        
        if from_unit == EnergyDensityUnits.PetaWattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: EnergyDensityUnits) -> float:
        
        if to_unit == EnergyDensityUnits.JoulePerCubicMeter:
            return (value)
        
        if to_unit == EnergyDensityUnits.WattHourPerCubicMeter:
            return (value * 3.6e+3)
        
        if to_unit == EnergyDensityUnits.KiloJoulePerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == EnergyDensityUnits.MegaJoulePerCubicMeter:
            return ((value) * 1000000.0)
        
        if to_unit == EnergyDensityUnits.GigaJoulePerCubicMeter:
            return ((value) * 1000000000.0)
        
        if to_unit == EnergyDensityUnits.TeraJoulePerCubicMeter:
            return ((value) * 1000000000000.0)
        
        if to_unit == EnergyDensityUnits.PetaJoulePerCubicMeter:
            return ((value) * 1000000000000000.0)
        
        if to_unit == EnergyDensityUnits.KiloWattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000.0)
        
        if to_unit == EnergyDensityUnits.MegaWattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000.0)
        
        if to_unit == EnergyDensityUnits.GigaWattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000000.0)
        
        if to_unit == EnergyDensityUnits.TeraWattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000000000.0)
        
        if to_unit == EnergyDensityUnits.PetaWattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_joules_per_cubic_meter(joules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in joules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in joules_per_cubic_meter.
        :type joules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(joules_per_cubic_meter, EnergyDensityUnits.JoulePerCubicMeter)

    
    @staticmethod
    def from_watt_hours_per_cubic_meter(watt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in watt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in watt_hours_per_cubic_meter.
        :type watt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(watt_hours_per_cubic_meter, EnergyDensityUnits.WattHourPerCubicMeter)

    
    @staticmethod
    def from_kilo_joules_per_cubic_meter(kilo_joules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in kilo_joules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in kilo_joules_per_cubic_meter.
        :type kilo_joules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(kilo_joules_per_cubic_meter, EnergyDensityUnits.KiloJoulePerCubicMeter)

    
    @staticmethod
    def from_mega_joules_per_cubic_meter(mega_joules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in mega_joules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in mega_joules_per_cubic_meter.
        :type mega_joules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(mega_joules_per_cubic_meter, EnergyDensityUnits.MegaJoulePerCubicMeter)

    
    @staticmethod
    def from_giga_joules_per_cubic_meter(giga_joules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in giga_joules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in giga_joules_per_cubic_meter.
        :type giga_joules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(giga_joules_per_cubic_meter, EnergyDensityUnits.GigaJoulePerCubicMeter)

    
    @staticmethod
    def from_tera_joules_per_cubic_meter(tera_joules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in tera_joules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in tera_joules_per_cubic_meter.
        :type tera_joules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(tera_joules_per_cubic_meter, EnergyDensityUnits.TeraJoulePerCubicMeter)

    
    @staticmethod
    def from_peta_joules_per_cubic_meter(peta_joules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in peta_joules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in peta_joules_per_cubic_meter.
        :type peta_joules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(peta_joules_per_cubic_meter, EnergyDensityUnits.PetaJoulePerCubicMeter)

    
    @staticmethod
    def from_kilo_watt_hours_per_cubic_meter(kilo_watt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in kilo_watt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in kilo_watt_hours_per_cubic_meter.
        :type kilo_watt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(kilo_watt_hours_per_cubic_meter, EnergyDensityUnits.KiloWattHourPerCubicMeter)

    
    @staticmethod
    def from_mega_watt_hours_per_cubic_meter(mega_watt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in mega_watt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in mega_watt_hours_per_cubic_meter.
        :type mega_watt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(mega_watt_hours_per_cubic_meter, EnergyDensityUnits.MegaWattHourPerCubicMeter)

    
    @staticmethod
    def from_giga_watt_hours_per_cubic_meter(giga_watt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in giga_watt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in giga_watt_hours_per_cubic_meter.
        :type giga_watt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(giga_watt_hours_per_cubic_meter, EnergyDensityUnits.GigaWattHourPerCubicMeter)

    
    @staticmethod
    def from_tera_watt_hours_per_cubic_meter(tera_watt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in tera_watt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in tera_watt_hours_per_cubic_meter.
        :type tera_watt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(tera_watt_hours_per_cubic_meter, EnergyDensityUnits.TeraWattHourPerCubicMeter)

    
    @staticmethod
    def from_peta_watt_hours_per_cubic_meter(peta_watt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in peta_watt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in peta_watt_hours_per_cubic_meter.
        :type peta_watt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(peta_watt_hours_per_cubic_meter, EnergyDensityUnits.PetaWattHourPerCubicMeter)

    
    @property
    def joules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__joules_per_cubic_meter != None:
            return self.__joules_per_cubic_meter
        self.__joules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.JoulePerCubicMeter)
        return self.__joules_per_cubic_meter

    
    @property
    def watt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__watt_hours_per_cubic_meter != None:
            return self.__watt_hours_per_cubic_meter
        self.__watt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.WattHourPerCubicMeter)
        return self.__watt_hours_per_cubic_meter

    
    @property
    def kilo_joules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_cubic_meter != None:
            return self.__kilo_joules_per_cubic_meter
        self.__kilo_joules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.KiloJoulePerCubicMeter)
        return self.__kilo_joules_per_cubic_meter

    
    @property
    def mega_joules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__mega_joules_per_cubic_meter != None:
            return self.__mega_joules_per_cubic_meter
        self.__mega_joules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.MegaJoulePerCubicMeter)
        return self.__mega_joules_per_cubic_meter

    
    @property
    def giga_joules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__giga_joules_per_cubic_meter != None:
            return self.__giga_joules_per_cubic_meter
        self.__giga_joules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.GigaJoulePerCubicMeter)
        return self.__giga_joules_per_cubic_meter

    
    @property
    def tera_joules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__tera_joules_per_cubic_meter != None:
            return self.__tera_joules_per_cubic_meter
        self.__tera_joules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.TeraJoulePerCubicMeter)
        return self.__tera_joules_per_cubic_meter

    
    @property
    def peta_joules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__peta_joules_per_cubic_meter != None:
            return self.__peta_joules_per_cubic_meter
        self.__peta_joules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.PetaJoulePerCubicMeter)
        return self.__peta_joules_per_cubic_meter

    
    @property
    def kilo_watt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilo_watt_hours_per_cubic_meter != None:
            return self.__kilo_watt_hours_per_cubic_meter
        self.__kilo_watt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.KiloWattHourPerCubicMeter)
        return self.__kilo_watt_hours_per_cubic_meter

    
    @property
    def mega_watt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__mega_watt_hours_per_cubic_meter != None:
            return self.__mega_watt_hours_per_cubic_meter
        self.__mega_watt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.MegaWattHourPerCubicMeter)
        return self.__mega_watt_hours_per_cubic_meter

    
    @property
    def giga_watt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__giga_watt_hours_per_cubic_meter != None:
            return self.__giga_watt_hours_per_cubic_meter
        self.__giga_watt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.GigaWattHourPerCubicMeter)
        return self.__giga_watt_hours_per_cubic_meter

    
    @property
    def tera_watt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__tera_watt_hours_per_cubic_meter != None:
            return self.__tera_watt_hours_per_cubic_meter
        self.__tera_watt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.TeraWattHourPerCubicMeter)
        return self.__tera_watt_hours_per_cubic_meter

    
    @property
    def peta_watt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__peta_watt_hours_per_cubic_meter != None:
            return self.__peta_watt_hours_per_cubic_meter
        self.__peta_watt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.PetaWattHourPerCubicMeter)
        return self.__peta_watt_hours_per_cubic_meter

    
    def to_string(self, unit: EnergyDensityUnits = EnergyDensityUnits.JoulePerCubicMeter) -> string:
        """
        Format the EnergyDensity to string.
        Note! the default format for EnergyDensity is JoulePerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == EnergyDensityUnits.JoulePerCubicMeter:
            return f"""{self.joules_per_cubic_meter} J/m³"""
        
        if unit == EnergyDensityUnits.WattHourPerCubicMeter:
            return f"""{self.watt_hours_per_cubic_meter} Wh/m³"""
        
        if unit == EnergyDensityUnits.KiloJoulePerCubicMeter:
            return f"""{self.kilo_joules_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.MegaJoulePerCubicMeter:
            return f"""{self.mega_joules_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.GigaJoulePerCubicMeter:
            return f"""{self.giga_joules_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.TeraJoulePerCubicMeter:
            return f"""{self.tera_joules_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.PetaJoulePerCubicMeter:
            return f"""{self.peta_joules_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.KiloWattHourPerCubicMeter:
            return f"""{self.kilo_watt_hours_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.MegaWattHourPerCubicMeter:
            return f"""{self.mega_watt_hours_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.GigaWattHourPerCubicMeter:
            return f"""{self.giga_watt_hours_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.TeraWattHourPerCubicMeter:
            return f"""{self.tera_watt_hours_per_cubic_meter} """
        
        if unit == EnergyDensityUnits.PetaWattHourPerCubicMeter:
            return f"""{self.peta_watt_hours_per_cubic_meter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: EnergyDensityUnits = EnergyDensityUnits.JoulePerCubicMeter) -> string:
        """
        Get EnergyDensity unit abbreviation.
        Note! the default abbreviation for EnergyDensity is JoulePerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == EnergyDensityUnits.JoulePerCubicMeter:
            return """J/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.WattHourPerCubicMeter:
            return """Wh/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.KiloJoulePerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.MegaJoulePerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.GigaJoulePerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.TeraJoulePerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.PetaJoulePerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.KiloWattHourPerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.MegaWattHourPerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.GigaWattHourPerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.TeraWattHourPerCubicMeter:
            return """"""
        
        if unit_abbreviation == EnergyDensityUnits.PetaWattHourPerCubicMeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for +: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return EnergyDensity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for *: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return EnergyDensity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for -: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return EnergyDensity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for /: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return EnergyDensity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for %: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return EnergyDensity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for **: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return EnergyDensity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for ==: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for <: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for >: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for <=: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, EnergyDensity):
            raise TypeError("unsupported operand type(s) for >=: 'EnergyDensity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value