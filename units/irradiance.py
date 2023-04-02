from enum import Enum
import math
import string


class IrradianceUnits(Enum):
        """
            IrradianceUnits enumeration
        """
        
        WattPerSquareMeter = 'watt_per_square_meter'
        """
            
        """
        
        WattPerSquareCentimeter = 'watt_per_square_centimeter'
        """
            
        """
        
        PicoWattPerSquareMeter = 'pico_watt_per_square_meter'
        """
            
        """
        
        NanoWattPerSquareMeter = 'nano_watt_per_square_meter'
        """
            
        """
        
        MicroWattPerSquareMeter = 'micro_watt_per_square_meter'
        """
            
        """
        
        MilliWattPerSquareMeter = 'milli_watt_per_square_meter'
        """
            
        """
        
        KiloWattPerSquareMeter = 'kilo_watt_per_square_meter'
        """
            
        """
        
        MegaWattPerSquareMeter = 'mega_watt_per_square_meter'
        """
            
        """
        
        PicoWattPerSquareCentimeter = 'pico_watt_per_square_centimeter'
        """
            
        """
        
        NanoWattPerSquareCentimeter = 'nano_watt_per_square_centimeter'
        """
            
        """
        
        MicroWattPerSquareCentimeter = 'micro_watt_per_square_centimeter'
        """
            
        """
        
        MilliWattPerSquareCentimeter = 'milli_watt_per_square_centimeter'
        """
            
        """
        
        KiloWattPerSquareCentimeter = 'kilo_watt_per_square_centimeter'
        """
            
        """
        
        MegaWattPerSquareCentimeter = 'mega_watt_per_square_centimeter'
        """
            
        """
        

class Irradiance:
    """
    Irradiance is the intensity of ultraviolet (UV) or visible light incident on a surface.

    Args:
        value (float): The value.
        from_unit (IrradianceUnits): The Irradiance unit to create from, The default unit is WattPerSquareMeter
    """
    def __init__(self, value: float, from_unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_square_meter = None
        
        self.__watts_per_square_centimeter = None
        
        self.__pico_watts_per_square_meter = None
        
        self.__nano_watts_per_square_meter = None
        
        self.__micro_watts_per_square_meter = None
        
        self.__milli_watts_per_square_meter = None
        
        self.__kilo_watts_per_square_meter = None
        
        self.__mega_watts_per_square_meter = None
        
        self.__pico_watts_per_square_centimeter = None
        
        self.__nano_watts_per_square_centimeter = None
        
        self.__micro_watts_per_square_centimeter = None
        
        self.__milli_watts_per_square_centimeter = None
        
        self.__kilo_watts_per_square_centimeter = None
        
        self.__mega_watts_per_square_centimeter = None
        

    def __convert_from_base(self, from_unit: IrradianceUnits) -> float:
        value = self.__value
        
        if from_unit == IrradianceUnits.WattPerSquareMeter:
            return (value)
        
        if from_unit == IrradianceUnits.WattPerSquareCentimeter:
            return (value * 0.0001)
        
        if from_unit == IrradianceUnits.PicoWattPerSquareMeter:
            return ((value) / 1e-12)
        
        if from_unit == IrradianceUnits.NanoWattPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == IrradianceUnits.MicroWattPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == IrradianceUnits.MilliWattPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == IrradianceUnits.KiloWattPerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == IrradianceUnits.MegaWattPerSquareMeter:
            return ((value) / 1000000.0)
        
        if from_unit == IrradianceUnits.PicoWattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-12)
        
        if from_unit == IrradianceUnits.NanoWattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-09)
        
        if from_unit == IrradianceUnits.MicroWattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-06)
        
        if from_unit == IrradianceUnits.MilliWattPerSquareCentimeter:
            return ((value * 0.0001) / 0.001)
        
        if from_unit == IrradianceUnits.KiloWattPerSquareCentimeter:
            return ((value * 0.0001) / 1000.0)
        
        if from_unit == IrradianceUnits.MegaWattPerSquareCentimeter:
            return ((value * 0.0001) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IrradianceUnits) -> float:
        
        if to_unit == IrradianceUnits.WattPerSquareMeter:
            return (value)
        
        if to_unit == IrradianceUnits.WattPerSquareCentimeter:
            return (value * 10000)
        
        if to_unit == IrradianceUnits.PicoWattPerSquareMeter:
            return ((value) * 1e-12)
        
        if to_unit == IrradianceUnits.NanoWattPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == IrradianceUnits.MicroWattPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == IrradianceUnits.MilliWattPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == IrradianceUnits.KiloWattPerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == IrradianceUnits.MegaWattPerSquareMeter:
            return ((value) * 1000000.0)
        
        if to_unit == IrradianceUnits.PicoWattPerSquareCentimeter:
            return ((value * 10000) * 1e-12)
        
        if to_unit == IrradianceUnits.NanoWattPerSquareCentimeter:
            return ((value * 10000) * 1e-09)
        
        if to_unit == IrradianceUnits.MicroWattPerSquareCentimeter:
            return ((value * 10000) * 1e-06)
        
        if to_unit == IrradianceUnits.MilliWattPerSquareCentimeter:
            return ((value * 10000) * 0.001)
        
        if to_unit == IrradianceUnits.KiloWattPerSquareCentimeter:
            return ((value * 10000) * 1000.0)
        
        if to_unit == IrradianceUnits.MegaWattPerSquareCentimeter:
            return ((value * 10000) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_watts_per_square_meter(watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in watts_per_square_meter.

        

        :param meters: The Irradiance value in watts_per_square_meter.
        :type watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(watts_per_square_meter, IrradianceUnits.WattPerSquareMeter)

    
    @staticmethod
    def from_watts_per_square_centimeter(watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in watts_per_square_centimeter.

        

        :param meters: The Irradiance value in watts_per_square_centimeter.
        :type watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(watts_per_square_centimeter, IrradianceUnits.WattPerSquareCentimeter)

    
    @staticmethod
    def from_pico_watts_per_square_meter(pico_watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in pico_watts_per_square_meter.

        

        :param meters: The Irradiance value in pico_watts_per_square_meter.
        :type pico_watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(pico_watts_per_square_meter, IrradianceUnits.PicoWattPerSquareMeter)

    
    @staticmethod
    def from_nano_watts_per_square_meter(nano_watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in nano_watts_per_square_meter.

        

        :param meters: The Irradiance value in nano_watts_per_square_meter.
        :type nano_watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(nano_watts_per_square_meter, IrradianceUnits.NanoWattPerSquareMeter)

    
    @staticmethod
    def from_micro_watts_per_square_meter(micro_watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in micro_watts_per_square_meter.

        

        :param meters: The Irradiance value in micro_watts_per_square_meter.
        :type micro_watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(micro_watts_per_square_meter, IrradianceUnits.MicroWattPerSquareMeter)

    
    @staticmethod
    def from_milli_watts_per_square_meter(milli_watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in milli_watts_per_square_meter.

        

        :param meters: The Irradiance value in milli_watts_per_square_meter.
        :type milli_watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(milli_watts_per_square_meter, IrradianceUnits.MilliWattPerSquareMeter)

    
    @staticmethod
    def from_kilo_watts_per_square_meter(kilo_watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in kilo_watts_per_square_meter.

        

        :param meters: The Irradiance value in kilo_watts_per_square_meter.
        :type kilo_watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(kilo_watts_per_square_meter, IrradianceUnits.KiloWattPerSquareMeter)

    
    @staticmethod
    def from_mega_watts_per_square_meter(mega_watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in mega_watts_per_square_meter.

        

        :param meters: The Irradiance value in mega_watts_per_square_meter.
        :type mega_watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(mega_watts_per_square_meter, IrradianceUnits.MegaWattPerSquareMeter)

    
    @staticmethod
    def from_pico_watts_per_square_centimeter(pico_watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in pico_watts_per_square_centimeter.

        

        :param meters: The Irradiance value in pico_watts_per_square_centimeter.
        :type pico_watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(pico_watts_per_square_centimeter, IrradianceUnits.PicoWattPerSquareCentimeter)

    
    @staticmethod
    def from_nano_watts_per_square_centimeter(nano_watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in nano_watts_per_square_centimeter.

        

        :param meters: The Irradiance value in nano_watts_per_square_centimeter.
        :type nano_watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(nano_watts_per_square_centimeter, IrradianceUnits.NanoWattPerSquareCentimeter)

    
    @staticmethod
    def from_micro_watts_per_square_centimeter(micro_watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in micro_watts_per_square_centimeter.

        

        :param meters: The Irradiance value in micro_watts_per_square_centimeter.
        :type micro_watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(micro_watts_per_square_centimeter, IrradianceUnits.MicroWattPerSquareCentimeter)

    
    @staticmethod
    def from_milli_watts_per_square_centimeter(milli_watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in milli_watts_per_square_centimeter.

        

        :param meters: The Irradiance value in milli_watts_per_square_centimeter.
        :type milli_watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(milli_watts_per_square_centimeter, IrradianceUnits.MilliWattPerSquareCentimeter)

    
    @staticmethod
    def from_kilo_watts_per_square_centimeter(kilo_watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in kilo_watts_per_square_centimeter.

        

        :param meters: The Irradiance value in kilo_watts_per_square_centimeter.
        :type kilo_watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(kilo_watts_per_square_centimeter, IrradianceUnits.KiloWattPerSquareCentimeter)

    
    @staticmethod
    def from_mega_watts_per_square_centimeter(mega_watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in mega_watts_per_square_centimeter.

        

        :param meters: The Irradiance value in mega_watts_per_square_centimeter.
        :type mega_watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(mega_watts_per_square_centimeter, IrradianceUnits.MegaWattPerSquareCentimeter)

    
    @property
    def watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter != None:
            return self.__watts_per_square_meter
        self.__watts_per_square_meter = self.__convert_from_base(IrradianceUnits.WattPerSquareMeter)
        return self.__watts_per_square_meter

    
    @property
    def watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__watts_per_square_centimeter != None:
            return self.__watts_per_square_centimeter
        self.__watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.WattPerSquareCentimeter)
        return self.__watts_per_square_centimeter

    
    @property
    def pico_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__pico_watts_per_square_meter != None:
            return self.__pico_watts_per_square_meter
        self.__pico_watts_per_square_meter = self.__convert_from_base(IrradianceUnits.PicoWattPerSquareMeter)
        return self.__pico_watts_per_square_meter

    
    @property
    def nano_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__nano_watts_per_square_meter != None:
            return self.__nano_watts_per_square_meter
        self.__nano_watts_per_square_meter = self.__convert_from_base(IrradianceUnits.NanoWattPerSquareMeter)
        return self.__nano_watts_per_square_meter

    
    @property
    def micro_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__micro_watts_per_square_meter != None:
            return self.__micro_watts_per_square_meter
        self.__micro_watts_per_square_meter = self.__convert_from_base(IrradianceUnits.MicroWattPerSquareMeter)
        return self.__micro_watts_per_square_meter

    
    @property
    def milli_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_square_meter != None:
            return self.__milli_watts_per_square_meter
        self.__milli_watts_per_square_meter = self.__convert_from_base(IrradianceUnits.MilliWattPerSquareMeter)
        return self.__milli_watts_per_square_meter

    
    @property
    def kilo_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_square_meter != None:
            return self.__kilo_watts_per_square_meter
        self.__kilo_watts_per_square_meter = self.__convert_from_base(IrradianceUnits.KiloWattPerSquareMeter)
        return self.__kilo_watts_per_square_meter

    
    @property
    def mega_watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__mega_watts_per_square_meter != None:
            return self.__mega_watts_per_square_meter
        self.__mega_watts_per_square_meter = self.__convert_from_base(IrradianceUnits.MegaWattPerSquareMeter)
        return self.__mega_watts_per_square_meter

    
    @property
    def pico_watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__pico_watts_per_square_centimeter != None:
            return self.__pico_watts_per_square_centimeter
        self.__pico_watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.PicoWattPerSquareCentimeter)
        return self.__pico_watts_per_square_centimeter

    
    @property
    def nano_watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__nano_watts_per_square_centimeter != None:
            return self.__nano_watts_per_square_centimeter
        self.__nano_watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.NanoWattPerSquareCentimeter)
        return self.__nano_watts_per_square_centimeter

    
    @property
    def micro_watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__micro_watts_per_square_centimeter != None:
            return self.__micro_watts_per_square_centimeter
        self.__micro_watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MicroWattPerSquareCentimeter)
        return self.__micro_watts_per_square_centimeter

    
    @property
    def milli_watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__milli_watts_per_square_centimeter != None:
            return self.__milli_watts_per_square_centimeter
        self.__milli_watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MilliWattPerSquareCentimeter)
        return self.__milli_watts_per_square_centimeter

    
    @property
    def kilo_watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_watts_per_square_centimeter != None:
            return self.__kilo_watts_per_square_centimeter
        self.__kilo_watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.KiloWattPerSquareCentimeter)
        return self.__kilo_watts_per_square_centimeter

    
    @property
    def mega_watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__mega_watts_per_square_centimeter != None:
            return self.__mega_watts_per_square_centimeter
        self.__mega_watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MegaWattPerSquareCentimeter)
        return self.__mega_watts_per_square_centimeter

    
    def to_string(self, unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter) -> string:
        """
        Format the Irradiance to string.
        Note! the default format for Irradiance is WattPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == IrradianceUnits.WattPerSquareMeter:
            return f"""{self.watts_per_square_meter} W/m²"""
        
        if unit == IrradianceUnits.WattPerSquareCentimeter:
            return f"""{self.watts_per_square_centimeter} W/cm²"""
        
        if unit == IrradianceUnits.PicoWattPerSquareMeter:
            return f"""{self.pico_watts_per_square_meter} """
        
        if unit == IrradianceUnits.NanoWattPerSquareMeter:
            return f"""{self.nano_watts_per_square_meter} """
        
        if unit == IrradianceUnits.MicroWattPerSquareMeter:
            return f"""{self.micro_watts_per_square_meter} """
        
        if unit == IrradianceUnits.MilliWattPerSquareMeter:
            return f"""{self.milli_watts_per_square_meter} """
        
        if unit == IrradianceUnits.KiloWattPerSquareMeter:
            return f"""{self.kilo_watts_per_square_meter} """
        
        if unit == IrradianceUnits.MegaWattPerSquareMeter:
            return f"""{self.mega_watts_per_square_meter} """
        
        if unit == IrradianceUnits.PicoWattPerSquareCentimeter:
            return f"""{self.pico_watts_per_square_centimeter} """
        
        if unit == IrradianceUnits.NanoWattPerSquareCentimeter:
            return f"""{self.nano_watts_per_square_centimeter} """
        
        if unit == IrradianceUnits.MicroWattPerSquareCentimeter:
            return f"""{self.micro_watts_per_square_centimeter} """
        
        if unit == IrradianceUnits.MilliWattPerSquareCentimeter:
            return f"""{self.milli_watts_per_square_centimeter} """
        
        if unit == IrradianceUnits.KiloWattPerSquareCentimeter:
            return f"""{self.kilo_watts_per_square_centimeter} """
        
        if unit == IrradianceUnits.MegaWattPerSquareCentimeter:
            return f"""{self.mega_watts_per_square_centimeter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: IrradianceUnits = IrradianceUnits.WattPerSquareMeter) -> string:
        """
        Get Irradiance unit abbreviation.
        Note! the default abbreviation for Irradiance is WattPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IrradianceUnits.WattPerSquareMeter:
            return """W/m²"""
        
        if unit_abbreviation == IrradianceUnits.WattPerSquareCentimeter:
            return """W/cm²"""
        
        if unit_abbreviation == IrradianceUnits.PicoWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.NanoWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.MicroWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.MilliWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.KiloWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.MegaWattPerSquareMeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.PicoWattPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.NanoWattPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.MicroWattPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.MilliWattPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.KiloWattPerSquareCentimeter:
            return """"""
        
        if unit_abbreviation == IrradianceUnits.MegaWattPerSquareCentimeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for +: 'Irradiance' and '{}'".format(type(other).__name__))
        return Irradiance(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for *: 'Irradiance' and '{}'".format(type(other).__name__))
        return Irradiance(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for -: 'Irradiance' and '{}'".format(type(other).__name__))
        return Irradiance(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for /: 'Irradiance' and '{}'".format(type(other).__name__))
        return Irradiance(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for %: 'Irradiance' and '{}'".format(type(other).__name__))
        return Irradiance(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for **: 'Irradiance' and '{}'".format(type(other).__name__))
        return Irradiance(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for ==: 'Irradiance' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for <: 'Irradiance' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for >: 'Irradiance' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for <=: 'Irradiance' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Irradiance):
            raise TypeError("unsupported operand type(s) for >=: 'Irradiance' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value