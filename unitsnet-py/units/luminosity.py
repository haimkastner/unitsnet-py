from enum import Enum
import math
import string


class LuminosityUnits(Enum):
        """
            LuminosityUnits enumeration
        """
        
        Watt = 'watt'
        """
            
        """
        
        SolarLuminosity = 'solar_luminosity'
        """
            
        """
        
        FemtoWatt = 'femto_watt'
        """
            
        """
        
        PicoWatt = 'pico_watt'
        """
            
        """
        
        NanoWatt = 'nano_watt'
        """
            
        """
        
        MicroWatt = 'micro_watt'
        """
            
        """
        
        MilliWatt = 'milli_watt'
        """
            
        """
        
        DeciWatt = 'deci_watt'
        """
            
        """
        
        DecaWatt = 'deca_watt'
        """
            
        """
        
        KiloWatt = 'kilo_watt'
        """
            
        """
        
        MegaWatt = 'mega_watt'
        """
            
        """
        
        GigaWatt = 'giga_watt'
        """
            
        """
        
        TeraWatt = 'tera_watt'
        """
            
        """
        
        PetaWatt = 'peta_watt'
        """
            
        """
        

class Luminosity:
    """
    Luminosity is an absolute measure of radiated electromagnetic power (light), the radiant power emitted by a light-emitting object.

    Args:
        value (float): The value.
        from_unit (LuminosityUnits): The Luminosity unit to create from, The default unit is Watt
    """
    def __init__(self, value: float, from_unit: LuminosityUnits = LuminosityUnits.Watt):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__watts = None
        
        self.__solar_luminosities = None
        
        self.__femto_watts = None
        
        self.__pico_watts = None
        
        self.__nano_watts = None
        
        self.__micro_watts = None
        
        self.__milli_watts = None
        
        self.__deci_watts = None
        
        self.__deca_watts = None
        
        self.__kilo_watts = None
        
        self.__mega_watts = None
        
        self.__giga_watts = None
        
        self.__tera_watts = None
        
        self.__peta_watts = None
        

    def __convert_from_base(self, from_unit: LuminosityUnits) -> float:
        value = self.__value
        
        if from_unit == LuminosityUnits.Watt:
            return (value)
        
        if from_unit == LuminosityUnits.SolarLuminosity:
            return (value / 3.846e26)
        
        if from_unit == LuminosityUnits.FemtoWatt:
            return ((value) / 1e-15)
        
        if from_unit == LuminosityUnits.PicoWatt:
            return ((value) / 1e-12)
        
        if from_unit == LuminosityUnits.NanoWatt:
            return ((value) / 1e-09)
        
        if from_unit == LuminosityUnits.MicroWatt:
            return ((value) / 1e-06)
        
        if from_unit == LuminosityUnits.MilliWatt:
            return ((value) / 0.001)
        
        if from_unit == LuminosityUnits.DeciWatt:
            return ((value) / 0.1)
        
        if from_unit == LuminosityUnits.DecaWatt:
            return ((value) / 10.0)
        
        if from_unit == LuminosityUnits.KiloWatt:
            return ((value) / 1000.0)
        
        if from_unit == LuminosityUnits.MegaWatt:
            return ((value) / 1000000.0)
        
        if from_unit == LuminosityUnits.GigaWatt:
            return ((value) / 1000000000.0)
        
        if from_unit == LuminosityUnits.TeraWatt:
            return ((value) / 1000000000000.0)
        
        if from_unit == LuminosityUnits.PetaWatt:
            return ((value) / 1000000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LuminosityUnits) -> float:
        
        if to_unit == LuminosityUnits.Watt:
            return (value)
        
        if to_unit == LuminosityUnits.SolarLuminosity:
            return (value * 3.846e26)
        
        if to_unit == LuminosityUnits.FemtoWatt:
            return ((value) * 1e-15)
        
        if to_unit == LuminosityUnits.PicoWatt:
            return ((value) * 1e-12)
        
        if to_unit == LuminosityUnits.NanoWatt:
            return ((value) * 1e-09)
        
        if to_unit == LuminosityUnits.MicroWatt:
            return ((value) * 1e-06)
        
        if to_unit == LuminosityUnits.MilliWatt:
            return ((value) * 0.001)
        
        if to_unit == LuminosityUnits.DeciWatt:
            return ((value) * 0.1)
        
        if to_unit == LuminosityUnits.DecaWatt:
            return ((value) * 10.0)
        
        if to_unit == LuminosityUnits.KiloWatt:
            return ((value) * 1000.0)
        
        if to_unit == LuminosityUnits.MegaWatt:
            return ((value) * 1000000.0)
        
        if to_unit == LuminosityUnits.GigaWatt:
            return ((value) * 1000000000.0)
        
        if to_unit == LuminosityUnits.TeraWatt:
            return ((value) * 1000000000000.0)
        
        if to_unit == LuminosityUnits.PetaWatt:
            return ((value) * 1000000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_watts(watts: float):
        """
        Create a new instance of Luminosity from a value in watts.

        

        :param meters: The Luminosity value in watts.
        :type watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(watts, LuminosityUnits.Watt)

    
    @staticmethod
    def from_solar_luminosities(solar_luminosities: float):
        """
        Create a new instance of Luminosity from a value in solar_luminosities.

        

        :param meters: The Luminosity value in solar_luminosities.
        :type solar_luminosities: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(solar_luminosities, LuminosityUnits.SolarLuminosity)

    
    @staticmethod
    def from_femto_watts(femto_watts: float):
        """
        Create a new instance of Luminosity from a value in femto_watts.

        

        :param meters: The Luminosity value in femto_watts.
        :type femto_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(femto_watts, LuminosityUnits.FemtoWatt)

    
    @staticmethod
    def from_pico_watts(pico_watts: float):
        """
        Create a new instance of Luminosity from a value in pico_watts.

        

        :param meters: The Luminosity value in pico_watts.
        :type pico_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(pico_watts, LuminosityUnits.PicoWatt)

    
    @staticmethod
    def from_nano_watts(nano_watts: float):
        """
        Create a new instance of Luminosity from a value in nano_watts.

        

        :param meters: The Luminosity value in nano_watts.
        :type nano_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(nano_watts, LuminosityUnits.NanoWatt)

    
    @staticmethod
    def from_micro_watts(micro_watts: float):
        """
        Create a new instance of Luminosity from a value in micro_watts.

        

        :param meters: The Luminosity value in micro_watts.
        :type micro_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(micro_watts, LuminosityUnits.MicroWatt)

    
    @staticmethod
    def from_milli_watts(milli_watts: float):
        """
        Create a new instance of Luminosity from a value in milli_watts.

        

        :param meters: The Luminosity value in milli_watts.
        :type milli_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(milli_watts, LuminosityUnits.MilliWatt)

    
    @staticmethod
    def from_deci_watts(deci_watts: float):
        """
        Create a new instance of Luminosity from a value in deci_watts.

        

        :param meters: The Luminosity value in deci_watts.
        :type deci_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(deci_watts, LuminosityUnits.DeciWatt)

    
    @staticmethod
    def from_deca_watts(deca_watts: float):
        """
        Create a new instance of Luminosity from a value in deca_watts.

        

        :param meters: The Luminosity value in deca_watts.
        :type deca_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(deca_watts, LuminosityUnits.DecaWatt)

    
    @staticmethod
    def from_kilo_watts(kilo_watts: float):
        """
        Create a new instance of Luminosity from a value in kilo_watts.

        

        :param meters: The Luminosity value in kilo_watts.
        :type kilo_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(kilo_watts, LuminosityUnits.KiloWatt)

    
    @staticmethod
    def from_mega_watts(mega_watts: float):
        """
        Create a new instance of Luminosity from a value in mega_watts.

        

        :param meters: The Luminosity value in mega_watts.
        :type mega_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(mega_watts, LuminosityUnits.MegaWatt)

    
    @staticmethod
    def from_giga_watts(giga_watts: float):
        """
        Create a new instance of Luminosity from a value in giga_watts.

        

        :param meters: The Luminosity value in giga_watts.
        :type giga_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(giga_watts, LuminosityUnits.GigaWatt)

    
    @staticmethod
    def from_tera_watts(tera_watts: float):
        """
        Create a new instance of Luminosity from a value in tera_watts.

        

        :param meters: The Luminosity value in tera_watts.
        :type tera_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(tera_watts, LuminosityUnits.TeraWatt)

    
    @staticmethod
    def from_peta_watts(peta_watts: float):
        """
        Create a new instance of Luminosity from a value in peta_watts.

        

        :param meters: The Luminosity value in peta_watts.
        :type peta_watts: float
        :return: A new instance of Luminosity.
        :rtype: Luminosity
        """
        return Luminosity(peta_watts, LuminosityUnits.PetaWatt)

    
    @property
    def watts(self) -> float:
        """
        
        """
        if self.__watts != None:
            return self.__watts
        self.__watts = self.__convert_from_base(LuminosityUnits.Watt)
        return self.__watts

    
    @property
    def solar_luminosities(self) -> float:
        """
        
        """
        if self.__solar_luminosities != None:
            return self.__solar_luminosities
        self.__solar_luminosities = self.__convert_from_base(LuminosityUnits.SolarLuminosity)
        return self.__solar_luminosities

    
    @property
    def femto_watts(self) -> float:
        """
        
        """
        if self.__femto_watts != None:
            return self.__femto_watts
        self.__femto_watts = self.__convert_from_base(LuminosityUnits.FemtoWatt)
        return self.__femto_watts

    
    @property
    def pico_watts(self) -> float:
        """
        
        """
        if self.__pico_watts != None:
            return self.__pico_watts
        self.__pico_watts = self.__convert_from_base(LuminosityUnits.PicoWatt)
        return self.__pico_watts

    
    @property
    def nano_watts(self) -> float:
        """
        
        """
        if self.__nano_watts != None:
            return self.__nano_watts
        self.__nano_watts = self.__convert_from_base(LuminosityUnits.NanoWatt)
        return self.__nano_watts

    
    @property
    def micro_watts(self) -> float:
        """
        
        """
        if self.__micro_watts != None:
            return self.__micro_watts
        self.__micro_watts = self.__convert_from_base(LuminosityUnits.MicroWatt)
        return self.__micro_watts

    
    @property
    def milli_watts(self) -> float:
        """
        
        """
        if self.__milli_watts != None:
            return self.__milli_watts
        self.__milli_watts = self.__convert_from_base(LuminosityUnits.MilliWatt)
        return self.__milli_watts

    
    @property
    def deci_watts(self) -> float:
        """
        
        """
        if self.__deci_watts != None:
            return self.__deci_watts
        self.__deci_watts = self.__convert_from_base(LuminosityUnits.DeciWatt)
        return self.__deci_watts

    
    @property
    def deca_watts(self) -> float:
        """
        
        """
        if self.__deca_watts != None:
            return self.__deca_watts
        self.__deca_watts = self.__convert_from_base(LuminosityUnits.DecaWatt)
        return self.__deca_watts

    
    @property
    def kilo_watts(self) -> float:
        """
        
        """
        if self.__kilo_watts != None:
            return self.__kilo_watts
        self.__kilo_watts = self.__convert_from_base(LuminosityUnits.KiloWatt)
        return self.__kilo_watts

    
    @property
    def mega_watts(self) -> float:
        """
        
        """
        if self.__mega_watts != None:
            return self.__mega_watts
        self.__mega_watts = self.__convert_from_base(LuminosityUnits.MegaWatt)
        return self.__mega_watts

    
    @property
    def giga_watts(self) -> float:
        """
        
        """
        if self.__giga_watts != None:
            return self.__giga_watts
        self.__giga_watts = self.__convert_from_base(LuminosityUnits.GigaWatt)
        return self.__giga_watts

    
    @property
    def tera_watts(self) -> float:
        """
        
        """
        if self.__tera_watts != None:
            return self.__tera_watts
        self.__tera_watts = self.__convert_from_base(LuminosityUnits.TeraWatt)
        return self.__tera_watts

    
    @property
    def peta_watts(self) -> float:
        """
        
        """
        if self.__peta_watts != None:
            return self.__peta_watts
        self.__peta_watts = self.__convert_from_base(LuminosityUnits.PetaWatt)
        return self.__peta_watts

    
    def to_string(self, unit: LuminosityUnits = LuminosityUnits.Watt) -> string:
        """
        Format the Luminosity to string.
        Note! the default format for Luminosity is Watt.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LuminosityUnits.Watt:
            return f"""{self.watts} W"""
        
        if unit == LuminosityUnits.SolarLuminosity:
            return f"""{self.solar_luminosities} L⊙"""
        
        if unit == LuminosityUnits.FemtoWatt:
            return f"""{self.femto_watts} """
        
        if unit == LuminosityUnits.PicoWatt:
            return f"""{self.pico_watts} """
        
        if unit == LuminosityUnits.NanoWatt:
            return f"""{self.nano_watts} """
        
        if unit == LuminosityUnits.MicroWatt:
            return f"""{self.micro_watts} """
        
        if unit == LuminosityUnits.MilliWatt:
            return f"""{self.milli_watts} """
        
        if unit == LuminosityUnits.DeciWatt:
            return f"""{self.deci_watts} """
        
        if unit == LuminosityUnits.DecaWatt:
            return f"""{self.deca_watts} """
        
        if unit == LuminosityUnits.KiloWatt:
            return f"""{self.kilo_watts} """
        
        if unit == LuminosityUnits.MegaWatt:
            return f"""{self.mega_watts} """
        
        if unit == LuminosityUnits.GigaWatt:
            return f"""{self.giga_watts} """
        
        if unit == LuminosityUnits.TeraWatt:
            return f"""{self.tera_watts} """
        
        if unit == LuminosityUnits.PetaWatt:
            return f"""{self.peta_watts} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: LuminosityUnits = LuminosityUnits.Watt) -> string:
        """
        Get Luminosity unit abbreviation.
        Note! the default abbreviation for Luminosity is Watt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LuminosityUnits.Watt:
            return """W"""
        
        if unit_abbreviation == LuminosityUnits.SolarLuminosity:
            return """L⊙"""
        
        if unit_abbreviation == LuminosityUnits.FemtoWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.PicoWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.NanoWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.MicroWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.MilliWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.DeciWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.DecaWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.KiloWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.MegaWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.GigaWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.TeraWatt:
            return """"""
        
        if unit_abbreviation == LuminosityUnits.PetaWatt:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for +: 'Luminosity' and '{}'".format(type(other).__name__))
        return Luminosity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for *: 'Luminosity' and '{}'".format(type(other).__name__))
        return Luminosity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for -: 'Luminosity' and '{}'".format(type(other).__name__))
        return Luminosity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for /: 'Luminosity' and '{}'".format(type(other).__name__))
        return Luminosity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for %: 'Luminosity' and '{}'".format(type(other).__name__))
        return Luminosity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for **: 'Luminosity' and '{}'".format(type(other).__name__))
        return Luminosity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for ==: 'Luminosity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for <: 'Luminosity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for >: 'Luminosity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for <=: 'Luminosity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Luminosity):
            raise TypeError("unsupported operand type(s) for >=: 'Luminosity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value