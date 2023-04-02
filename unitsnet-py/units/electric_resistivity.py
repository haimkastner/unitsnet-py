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
        
        PicoohmMeter = 'picoohm_meter'
        """
            
        """
        
        NanoohmMeter = 'nanoohm_meter'
        """
            
        """
        
        MicroohmMeter = 'microohm_meter'
        """
            
        """
        
        MilliohmMeter = 'milliohm_meter'
        """
            
        """
        
        KiloohmMeter = 'kiloohm_meter'
        """
            
        """
        
        MegaohmMeter = 'megaohm_meter'
        """
            
        """
        
        PicoohmCentimeter = 'picoohm_centimeter'
        """
            
        """
        
        NanoohmCentimeter = 'nanoohm_centimeter'
        """
            
        """
        
        MicroohmCentimeter = 'microohm_centimeter'
        """
            
        """
        
        MilliohmCentimeter = 'milliohm_centimeter'
        """
            
        """
        
        KiloohmCentimeter = 'kiloohm_centimeter'
        """
            
        """
        
        MegaohmCentimeter = 'megaohm_centimeter'
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
        
        self.__picoohm_meters = None
        
        self.__nanoohm_meters = None
        
        self.__microohm_meters = None
        
        self.__milliohm_meters = None
        
        self.__kiloohm_meters = None
        
        self.__megaohm_meters = None
        
        self.__picoohms_centimeter = None
        
        self.__nanoohms_centimeter = None
        
        self.__microohms_centimeter = None
        
        self.__milliohms_centimeter = None
        
        self.__kiloohms_centimeter = None
        
        self.__megaohms_centimeter = None
        

    def __convert_from_base(self, from_unit: ElectricResistivityUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricResistivityUnits.OhmMeter:
            return (value)
        
        if from_unit == ElectricResistivityUnits.OhmCentimeter:
            return (value * 100)
        
        if from_unit == ElectricResistivityUnits.PicoohmMeter:
            return ((value) / 1e-12)
        
        if from_unit == ElectricResistivityUnits.NanoohmMeter:
            return ((value) / 1e-09)
        
        if from_unit == ElectricResistivityUnits.MicroohmMeter:
            return ((value) / 1e-06)
        
        if from_unit == ElectricResistivityUnits.MilliohmMeter:
            return ((value) / 0.001)
        
        if from_unit == ElectricResistivityUnits.KiloohmMeter:
            return ((value) / 1000.0)
        
        if from_unit == ElectricResistivityUnits.MegaohmMeter:
            return ((value) / 1000000.0)
        
        if from_unit == ElectricResistivityUnits.PicoohmCentimeter:
            return ((value * 100) / 1e-12)
        
        if from_unit == ElectricResistivityUnits.NanoohmCentimeter:
            return ((value * 100) / 1e-09)
        
        if from_unit == ElectricResistivityUnits.MicroohmCentimeter:
            return ((value * 100) / 1e-06)
        
        if from_unit == ElectricResistivityUnits.MilliohmCentimeter:
            return ((value * 100) / 0.001)
        
        if from_unit == ElectricResistivityUnits.KiloohmCentimeter:
            return ((value * 100) / 1000.0)
        
        if from_unit == ElectricResistivityUnits.MegaohmCentimeter:
            return ((value * 100) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricResistivityUnits) -> float:
        
        if to_unit == ElectricResistivityUnits.OhmMeter:
            return (value)
        
        if to_unit == ElectricResistivityUnits.OhmCentimeter:
            return (value / 100)
        
        if to_unit == ElectricResistivityUnits.PicoohmMeter:
            return ((value) * 1e-12)
        
        if to_unit == ElectricResistivityUnits.NanoohmMeter:
            return ((value) * 1e-09)
        
        if to_unit == ElectricResistivityUnits.MicroohmMeter:
            return ((value) * 1e-06)
        
        if to_unit == ElectricResistivityUnits.MilliohmMeter:
            return ((value) * 0.001)
        
        if to_unit == ElectricResistivityUnits.KiloohmMeter:
            return ((value) * 1000.0)
        
        if to_unit == ElectricResistivityUnits.MegaohmMeter:
            return ((value) * 1000000.0)
        
        if to_unit == ElectricResistivityUnits.PicoohmCentimeter:
            return ((value / 100) * 1e-12)
        
        if to_unit == ElectricResistivityUnits.NanoohmCentimeter:
            return ((value / 100) * 1e-09)
        
        if to_unit == ElectricResistivityUnits.MicroohmCentimeter:
            return ((value / 100) * 1e-06)
        
        if to_unit == ElectricResistivityUnits.MilliohmCentimeter:
            return ((value / 100) * 0.001)
        
        if to_unit == ElectricResistivityUnits.KiloohmCentimeter:
            return ((value / 100) * 1000.0)
        
        if to_unit == ElectricResistivityUnits.MegaohmCentimeter:
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
    def from_picoohm_meters(picoohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in picoohm_meters.

        

        :param meters: The ElectricResistivity value in picoohm_meters.
        :type picoohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(picoohm_meters, ElectricResistivityUnits.PicoohmMeter)

    
    @staticmethod
    def from_nanoohm_meters(nanoohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in nanoohm_meters.

        

        :param meters: The ElectricResistivity value in nanoohm_meters.
        :type nanoohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(nanoohm_meters, ElectricResistivityUnits.NanoohmMeter)

    
    @staticmethod
    def from_microohm_meters(microohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in microohm_meters.

        

        :param meters: The ElectricResistivity value in microohm_meters.
        :type microohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(microohm_meters, ElectricResistivityUnits.MicroohmMeter)

    
    @staticmethod
    def from_milliohm_meters(milliohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in milliohm_meters.

        

        :param meters: The ElectricResistivity value in milliohm_meters.
        :type milliohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(milliohm_meters, ElectricResistivityUnits.MilliohmMeter)

    
    @staticmethod
    def from_kiloohm_meters(kiloohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in kiloohm_meters.

        

        :param meters: The ElectricResistivity value in kiloohm_meters.
        :type kiloohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(kiloohm_meters, ElectricResistivityUnits.KiloohmMeter)

    
    @staticmethod
    def from_megaohm_meters(megaohm_meters: float):
        """
        Create a new instance of ElectricResistivity from a value in megaohm_meters.

        

        :param meters: The ElectricResistivity value in megaohm_meters.
        :type megaohm_meters: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(megaohm_meters, ElectricResistivityUnits.MegaohmMeter)

    
    @staticmethod
    def from_picoohms_centimeter(picoohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in picoohms_centimeter.

        

        :param meters: The ElectricResistivity value in picoohms_centimeter.
        :type picoohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(picoohms_centimeter, ElectricResistivityUnits.PicoohmCentimeter)

    
    @staticmethod
    def from_nanoohms_centimeter(nanoohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in nanoohms_centimeter.

        

        :param meters: The ElectricResistivity value in nanoohms_centimeter.
        :type nanoohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(nanoohms_centimeter, ElectricResistivityUnits.NanoohmCentimeter)

    
    @staticmethod
    def from_microohms_centimeter(microohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in microohms_centimeter.

        

        :param meters: The ElectricResistivity value in microohms_centimeter.
        :type microohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(microohms_centimeter, ElectricResistivityUnits.MicroohmCentimeter)

    
    @staticmethod
    def from_milliohms_centimeter(milliohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in milliohms_centimeter.

        

        :param meters: The ElectricResistivity value in milliohms_centimeter.
        :type milliohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(milliohms_centimeter, ElectricResistivityUnits.MilliohmCentimeter)

    
    @staticmethod
    def from_kiloohms_centimeter(kiloohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in kiloohms_centimeter.

        

        :param meters: The ElectricResistivity value in kiloohms_centimeter.
        :type kiloohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(kiloohms_centimeter, ElectricResistivityUnits.KiloohmCentimeter)

    
    @staticmethod
    def from_megaohms_centimeter(megaohms_centimeter: float):
        """
        Create a new instance of ElectricResistivity from a value in megaohms_centimeter.

        

        :param meters: The ElectricResistivity value in megaohms_centimeter.
        :type megaohms_centimeter: float
        :return: A new instance of ElectricResistivity.
        :rtype: ElectricResistivity
        """
        return ElectricResistivity(megaohms_centimeter, ElectricResistivityUnits.MegaohmCentimeter)

    
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
    def picoohm_meters(self) -> float:
        """
        
        """
        if self.__picoohm_meters != None:
            return self.__picoohm_meters
        self.__picoohm_meters = self.__convert_from_base(ElectricResistivityUnits.PicoohmMeter)
        return self.__picoohm_meters

    
    @property
    def nanoohm_meters(self) -> float:
        """
        
        """
        if self.__nanoohm_meters != None:
            return self.__nanoohm_meters
        self.__nanoohm_meters = self.__convert_from_base(ElectricResistivityUnits.NanoohmMeter)
        return self.__nanoohm_meters

    
    @property
    def microohm_meters(self) -> float:
        """
        
        """
        if self.__microohm_meters != None:
            return self.__microohm_meters
        self.__microohm_meters = self.__convert_from_base(ElectricResistivityUnits.MicroohmMeter)
        return self.__microohm_meters

    
    @property
    def milliohm_meters(self) -> float:
        """
        
        """
        if self.__milliohm_meters != None:
            return self.__milliohm_meters
        self.__milliohm_meters = self.__convert_from_base(ElectricResistivityUnits.MilliohmMeter)
        return self.__milliohm_meters

    
    @property
    def kiloohm_meters(self) -> float:
        """
        
        """
        if self.__kiloohm_meters != None:
            return self.__kiloohm_meters
        self.__kiloohm_meters = self.__convert_from_base(ElectricResistivityUnits.KiloohmMeter)
        return self.__kiloohm_meters

    
    @property
    def megaohm_meters(self) -> float:
        """
        
        """
        if self.__megaohm_meters != None:
            return self.__megaohm_meters
        self.__megaohm_meters = self.__convert_from_base(ElectricResistivityUnits.MegaohmMeter)
        return self.__megaohm_meters

    
    @property
    def picoohms_centimeter(self) -> float:
        """
        
        """
        if self.__picoohms_centimeter != None:
            return self.__picoohms_centimeter
        self.__picoohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.PicoohmCentimeter)
        return self.__picoohms_centimeter

    
    @property
    def nanoohms_centimeter(self) -> float:
        """
        
        """
        if self.__nanoohms_centimeter != None:
            return self.__nanoohms_centimeter
        self.__nanoohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.NanoohmCentimeter)
        return self.__nanoohms_centimeter

    
    @property
    def microohms_centimeter(self) -> float:
        """
        
        """
        if self.__microohms_centimeter != None:
            return self.__microohms_centimeter
        self.__microohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MicroohmCentimeter)
        return self.__microohms_centimeter

    
    @property
    def milliohms_centimeter(self) -> float:
        """
        
        """
        if self.__milliohms_centimeter != None:
            return self.__milliohms_centimeter
        self.__milliohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MilliohmCentimeter)
        return self.__milliohms_centimeter

    
    @property
    def kiloohms_centimeter(self) -> float:
        """
        
        """
        if self.__kiloohms_centimeter != None:
            return self.__kiloohms_centimeter
        self.__kiloohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.KiloohmCentimeter)
        return self.__kiloohms_centimeter

    
    @property
    def megaohms_centimeter(self) -> float:
        """
        
        """
        if self.__megaohms_centimeter != None:
            return self.__megaohms_centimeter
        self.__megaohms_centimeter = self.__convert_from_base(ElectricResistivityUnits.MegaohmCentimeter)
        return self.__megaohms_centimeter

    
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
        
        if unit == ElectricResistivityUnits.PicoohmMeter:
            return f"""{self.picoohm_meters} """
        
        if unit == ElectricResistivityUnits.NanoohmMeter:
            return f"""{self.nanoohm_meters} """
        
        if unit == ElectricResistivityUnits.MicroohmMeter:
            return f"""{self.microohm_meters} """
        
        if unit == ElectricResistivityUnits.MilliohmMeter:
            return f"""{self.milliohm_meters} """
        
        if unit == ElectricResistivityUnits.KiloohmMeter:
            return f"""{self.kiloohm_meters} """
        
        if unit == ElectricResistivityUnits.MegaohmMeter:
            return f"""{self.megaohm_meters} """
        
        if unit == ElectricResistivityUnits.PicoohmCentimeter:
            return f"""{self.picoohms_centimeter} """
        
        if unit == ElectricResistivityUnits.NanoohmCentimeter:
            return f"""{self.nanoohms_centimeter} """
        
        if unit == ElectricResistivityUnits.MicroohmCentimeter:
            return f"""{self.microohms_centimeter} """
        
        if unit == ElectricResistivityUnits.MilliohmCentimeter:
            return f"""{self.milliohms_centimeter} """
        
        if unit == ElectricResistivityUnits.KiloohmCentimeter:
            return f"""{self.kiloohms_centimeter} """
        
        if unit == ElectricResistivityUnits.MegaohmCentimeter:
            return f"""{self.megaohms_centimeter} """
        
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
        
        if unit_abbreviation == ElectricResistivityUnits.PicoohmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.NanoohmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MicroohmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MilliohmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.KiloohmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MegaohmMeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.PicoohmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.NanoohmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MicroohmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MilliohmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.KiloohmCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricResistivityUnits.MegaohmCentimeter:
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