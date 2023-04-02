from enum import Enum
import math
import string


class ElectricResistivityUnits(Enum):
        """
            ElectricResistivityUnits enumeration
        """
        
        OhmMeter = 'ohm_meter'
        """
            
        """
        
        OhmCentimeter = 'ohm_centimeter'
        """
            
        """
        
        PicoOhmMeter = 'pico_ohm_meter'
        """
            
        """
        
        NanoOhmMeter = 'nano_ohm_meter'
        """
            
        """
        
        MicroOhmMeter = 'micro_ohm_meter'
        """
            
        """
        
        MilliOhmMeter = 'milli_ohm_meter'
        """
            
        """
        
        KiloOhmMeter = 'kilo_ohm_meter'
        """
            
        """
        
        MegaOhmMeter = 'mega_ohm_meter'
        """
            
        """
        
        PicoOhmCentimeter = 'pico_ohm_centimeter'
        """
            
        """
        
        NanoOhmCentimeter = 'nano_ohm_centimeter'
        """
            
        """
        
        MicroOhmCentimeter = 'micro_ohm_centimeter'
        """
            
        """
        
        MilliOhmCentimeter = 'milli_ohm_centimeter'
        """
            
        """
        
        KiloOhmCentimeter = 'kilo_ohm_centimeter'
        """
            
        """
        
        MegaOhmCentimeter = 'mega_ohm_centimeter'
        """
            
        """
        
    
class ElectricResistivity:
    """
    Electrical resistivity (also known as resistivity, specific electrical resistance, or volume resistivity) is a fundamental property that quantifies how strongly a given material opposes the flow of electric current.

    Args:
        value (float): The value.
        from_unit (ElectricResistivityUnits): The ElectricResistivity unit to create from, The default unit is OhmMeter
    """
    def __init__(self, value: float, from_unit: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__ohm_meters = None
        
        self.__ohms_centimeter = None
        
        self.__pico_ohm_meters = None
        
        self.__nano_ohm_meters = None
        
        self.__micro_ohm_meters = None
        
        self.__milli_ohm_meters = None
        
        self.__kilo_ohm_meters = None
        
        self.__mega_ohm_meters = None
        
        self.__pico_ohms_centimeter = None
        
        self.__nano_ohms_centimeter = None
        
        self.__micro_ohms_centimeter = None
        
        self.__milli_ohms_centimeter = None
        
        self.__kilo_ohms_centimeter = None
        
        self.__mega_ohms_centimeter = None
        

    def __convert_from_base(self, from_unit: ElectricResistivityUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricResistivityUnits.OhmMeter:
            return (value)
        
        if from_unit == ElectricResistivityUnits.OhmCentimeter:
            return (value * 100)
        
        if from_unit == ElectricResistivityUnits.PicoOhmMeter:
            return ((value) / 1e-12)
        
        if from_unit == ElectricResistivityUnits.NanoOhmMeter:
            return ((value) / 1e-09)
        
        if from_unit == ElectricResistivityUnits.MicroOhmMeter:
            return ((value) / 1e-06)
        
        if from_unit == ElectricResistivityUnits.MilliOhmMeter:
            return ((value) / 0.001)
        
        if from_unit == ElectricResistivityUnits.KiloOhmMeter:
            return ((value) / 1000.0)
        
        if from_unit == ElectricResistivityUnits.MegaOhmMeter:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricResistivityUnits.PicoOhmCentimeter:
            return ((value * 100) / 1e-12)
        
        if from_unit == ElectricResistivityUnits.NanoOhmCentimeter:
            return ((value * 100) / 1e-09)
        
        if from_unit == ElectricResistivityUnits.MicroOhmCentimeter:
            return ((value * 100) / 1e-06)
        
        if from_unit == ElectricResistivityUnits.MilliOhmCentimeter:
            return ((value * 100) / 0.001)
        
        if from_unit == ElectricResistivityUnits.KiloOhmCentimeter:
            return ((value * 100) / 1000.0)
        
        if from_unit == ElectricResistivityUnits.MegaOhmCentimeter:
            return ((value * 100) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricResistivityUnits) -> float:
        
        if to_unit == ElectricResistivityUnits.OhmMeter:
            return (value)
        
        if to_unit == ElectricResistivityUnits.OhmCentimeter:
            return (value / 100)
        
        if to_unit == ElectricResistivityUnits.PicoOhmMeter:
            return ((value) * 1e-12)
        
        if to_unit == ElectricResistivityUnits.NanoOhmMeter:
            return ((value) * 1e-09)
        
        if to_unit == ElectricResistivityUnits.MicroOhmMeter:
            return ((value) * 1e-06)
        
        if to_unit == ElectricResistivityUnits.MilliOhmMeter:
            return ((value) * 0.001)
        
        if to_unit == ElectricResistivityUnits.KiloOhmMeter:
            return ((value) * 1000.0)
        
        if to_unit == ElectricResistivityUnits.MegaOhmMeter:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricResistivityUnits.PicoOhmCentimeter:
            return ((value / 100) * 1e-12)
        
        if to_unit == ElectricResistivityUnits.NanoOhmCentimeter:
            return ((value / 100) * 1e-09)
        
        if to_unit == ElectricResistivityUnits.MicroOhmCentimeter:
            return ((value / 100) * 1e-06)
        
        if to_unit == ElectricResistivityUnits.MilliOhmCentimeter:
            return ((value / 100) * 0.001)
        
        if to_unit == ElectricResistivityUnits.KiloOhmCentimeter:
            return ((value / 100) * 1000.0)
        
        if to_unit == ElectricResistivityUnits.MegaOhmCentimeter:
            return ((value / 100) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_ohm_meters(ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in ohm_meters.

        

        :param meters: The ElectricResistivity value in ohm_meters.
        :type ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(ohm_meters, ElectricResistivityUnits.OhmMeter)

    
    @staticmethod
    def from_ohms_centimeter(ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in ohms_centimeter.

        

        :param meters: The ElectricResistivity value in ohms_centimeter.
        :type ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(ohms_centimeter, ElectricResistivityUnits.OhmCentimeter)

    
    @staticmethod
    def from_pico_ohm_meters(pico_ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in pico_ohm_meters.

        

        :param meters: The ElectricResistivity value in pico_ohm_meters.
        :type pico_ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(pico_ohm_meters, ElectricResistivityUnits.PicoOhmMeter)

    
    @staticmethod
    def from_nano_ohm_meters(nano_ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in nano_ohm_meters.

        

        :param meters: The ElectricResistivity value in nano_ohm_meters.
        :type nano_ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(nano_ohm_meters, ElectricResistivityUnits.NanoOhmMeter)

    
    @staticmethod
    def from_micro_ohm_meters(micro_ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in micro_ohm_meters.

        

        :param meters: The ElectricResistivity value in micro_ohm_meters.
        :type micro_ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(micro_ohm_meters, ElectricResistivityUnits.MicroOhmMeter)

    
    @staticmethod
    def from_milli_ohm_meters(milli_ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in milli_ohm_meters.

        

        :param meters: The ElectricResistivity value in milli_ohm_meters.
        :type milli_ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(milli_ohm_meters, ElectricResistivityUnits.MilliOhmMeter)

    
    @staticmethod
    def from_kilo_ohm_meters(kilo_ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in kilo_ohm_meters.

        

        :param meters: The ElectricResistivity value in kilo_ohm_meters.
        :type kilo_ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(kilo_ohm_meters, ElectricResistivityUnits.KiloOhmMeter)

    
    @staticmethod
    def from_mega_ohm_meters(mega_ohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in mega_ohm_meters.

        

        :param meters: The ElectricResistivity value in mega_ohm_meters.
        :type mega_ohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(mega_ohm_meters, ElectricResistivityUnits.MegaOhmMeter)

    
    @staticmethod
    def from_pico_ohms_centimeter(pico_ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in pico_ohms_centimeter.

        

        :param meters: The ElectricResistivity value in pico_ohms_centimeter.
        :type pico_ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(pico_ohms_centimeter, ElectricResistivityUnits.PicoOhmCentimeter)

    
    @staticmethod
    def from_nano_ohms_centimeter(nano_ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in nano_ohms_centimeter.

        

        :param meters: The ElectricResistivity value in nano_ohms_centimeter.
        :type nano_ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(nano_ohms_centimeter, ElectricResistivityUnits.NanoOhmCentimeter)

    
    @staticmethod
    def from_micro_ohms_centimeter(micro_ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in micro_ohms_centimeter.

        

        :param meters: The ElectricResistivity value in micro_ohms_centimeter.
        :type micro_ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(micro_ohms_centimeter, ElectricResistivityUnits.MicroOhmCentimeter)

    
    @staticmethod
    def from_milli_ohms_centimeter(milli_ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in milli_ohms_centimeter.

        

        :param meters: The ElectricResistivity value in milli_ohms_centimeter.
        :type milli_ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(milli_ohms_centimeter, ElectricResistivityUnits.MilliOhmCentimeter)

    
    @staticmethod
    def from_kilo_ohms_centimeter(kilo_ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in kilo_ohms_centimeter.

        

        :param meters: The ElectricResistivity value in kilo_ohms_centimeter.
        :type kilo_ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(kilo_ohms_centimeter, ElectricResistivityUnits.KiloOhmCentimeter)

    
    @staticmethod
    def from_mega_ohms_centimeter(mega_ohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in mega_ohms_centimeter.

        

        :param meters: The ElectricResistivity value in mega_ohms_centimeter.
        :type mega_ohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(mega_ohms_centimeter, ElectricResistivityUnits.MegaOhmCentimeter)

    
    @property
    def ohm_meters(self) -> float:
        """
        
        """
        if self.__ohm_meters != None:
            return self.__ohm_meters
        self.__ohm_meters = self.__convert_from_base(ElectricResistivityUnits.OhmMeter)
        return self.__ohm_meters

    
    @property
    def ohms_centimeter(self) -> float:
        """
        
        """
        if self.__ohms_centimeter != None:
            return self.__ohms_centimeter
        self.__ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.OhmCentimeter)
        return self.__ohms_centimeter

    
    @property
    def pico_ohm_meters(self) -> float:
        """
        
        """
        if self.__pico_ohm_meters != None:
            return self.__pico_ohm_meters
        self.__pico_ohm_meters = self.__convert_from_base(ElectricResistivityUnits.PicoOhmMeter)
        return self.__pico_ohm_meters

    
    @property
    def nano_ohm_meters(self) -> float:
        """
        
        """
        if self.__nano_ohm_meters != None:
            return self.__nano_ohm_meters
        self.__nano_ohm_meters = self.__convert_from_base(ElectricResistivityUnits.NanoOhmMeter)
        return self.__nano_ohm_meters

    
    @property
    def micro_ohm_meters(self) -> float:
        """
        
        """
        if self.__micro_ohm_meters != None:
            return self.__micro_ohm_meters
        self.__micro_ohm_meters = self.__convert_from_base(ElectricResistivityUnits.MicroOhmMeter)
        return self.__micro_ohm_meters

    
    @property
    def milli_ohm_meters(self) -> float:
        """
        
        """
        if self.__milli_ohm_meters != None:
            return self.__milli_ohm_meters
        self.__milli_ohm_meters = self.__convert_from_base(ElectricResistivityUnits.MilliOhmMeter)
        return self.__milli_ohm_meters

    
    @property
    def kilo_ohm_meters(self) -> float:
        """
        
        """
        if self.__kilo_ohm_meters != None:
            return self.__kilo_ohm_meters
        self.__kilo_ohm_meters = self.__convert_from_base(ElectricResistivityUnits.KiloOhmMeter)
        return self.__kilo_ohm_meters

    
    @property
    def mega_ohm_meters(self) -> float:
        """
        
        """
        if self.__mega_ohm_meters != None:
            return self.__mega_ohm_meters
        self.__mega_ohm_meters = self.__convert_from_base(ElectricResistivityUnits.MegaOhmMeter)
        return self.__mega_ohm_meters

    
    @property
    def pico_ohms_centimeter(self) -> float:
        """
        
        """
        if self.__pico_ohms_centimeter != None:
            return self.__pico_ohms_centimeter
        self.__pico_ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.PicoOhmCentimeter)
        return self.__pico_ohms_centimeter

    
    @property
    def nano_ohms_centimeter(self) -> float:
        """
        
        """
        if self.__nano_ohms_centimeter != None:
            return self.__nano_ohms_centimeter
        self.__nano_ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.NanoOhmCentimeter)
        return self.__nano_ohms_centimeter

    
    @property
    def micro_ohms_centimeter(self) -> float:
        """
        
        """
        if self.__micro_ohms_centimeter != None:
            return self.__micro_ohms_centimeter
        self.__micro_ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MicroOhmCentimeter)
        return self.__micro_ohms_centimeter

    
    @property
    def milli_ohms_centimeter(self) -> float:
        """
        
        """
        if self.__milli_ohms_centimeter != None:
            return self.__milli_ohms_centimeter
        self.__milli_ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MilliOhmCentimeter)
        return self.__milli_ohms_centimeter

    
    @property
    def kilo_ohms_centimeter(self) -> float:
        """
        
        """
        if self.__kilo_ohms_centimeter != None:
            return self.__kilo_ohms_centimeter
        self.__kilo_ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.KiloOhmCentimeter)
        return self.__kilo_ohms_centimeter

    
    @property
    def mega_ohms_centimeter(self) -> float:
        """
        
        """
        if self.__mega_ohms_centimeter != None:
            return self.__mega_ohms_centimeter
        self.__mega_ohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MegaOhmCentimeter)
        return self.__mega_ohms_centimeter

    
    def to_string(self, unit: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter) -> string:
        """
        Format the ElectricResistivity to string.
        Note! the default format for ElectricResistivity is OhmMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricResistivityUnits.OhmMeter:
            return f"""{self.ohm_meters} Ω·m"""
        
        if unit == ElectricResistivityUnits.OhmCentimeter:
            return f"""{self.ohms_centimeter} Ω·cm"""
        
        if unit == ElectricResistivityUnits.PicoOhmMeter:
            return f"""{self.pico_ohm_meters} """
        
        if unit == ElectricResistivityUnits.NanoOhmMeter:
            return f"""{self.nano_ohm_meters} """
        
        if unit == ElectricResistivityUnits.MicroOhmMeter:
            return f"""{self.micro_ohm_meters} """
        
        if unit == ElectricResistivityUnits.MilliOhmMeter:
            return f"""{self.milli_ohm_meters} """
        
        if unit == ElectricResistivityUnits.KiloOhmMeter:
            return f"""{self.kilo_ohm_meters} """
        
        if unit == ElectricResistivityUnits.MegaOhmMeter:
            return f"""{self.mega_ohm_meters} """
        
        if unit == ElectricResistivityUnits.PicoOhmCentimeter:
            return f"""{self.pico_ohms_centimeter} """
        
        if unit == ElectricResistivityUnits.NanoOhmCentimeter:
            return f"""{self.nano_ohms_centimeter} """
        
        if unit == ElectricResistivityUnits.MicroOhmCentimeter:
            return f"""{self.micro_ohms_centimeter} """
        
        if unit == ElectricResistivityUnits.MilliOhmCentimeter:
            return f"""{self.milli_ohms_centimeter} """
        
        if unit == ElectricResistivityUnits.KiloOhmCentimeter:
            return f"""{self.kilo_ohms_centimeter} """
        
        if unit == ElectricResistivityUnits.MegaOhmCentimeter:
            return f"""{self.mega_ohms_centimeter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricResistivityUnits = ElectricResistivityUnits.OhmMeter) -> string:
        """
        Get ElectricResistivity unit abbreviation.
        Note! the default abbreviation for ElectricResistivity is OhmMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricResistivityUnits.OhmMeter:
            return """Ω·m"""
        
        if unit_abbreviation == ElectricResistivityUnits.OhmCentimeter:
            return """Ω·cm"""
        
        if unit_abbreviation == ElectricResistivityUnits.PicoOhmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.NanoOhmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MicroOhmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MilliOhmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.KiloOhmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MegaOhmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.PicoOhmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.NanoOhmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MicroOhmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MilliOhmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.KiloOhmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MegaOhmCentimeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for +: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return ElectricResistivity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for *: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return ElectricResistivity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for -: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return ElectricResistivity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for /: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return ElectricResistivity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for %: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return ElectricResistivity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for **: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return ElectricResistivity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for <: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for >: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricResistivity):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricResistivity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value