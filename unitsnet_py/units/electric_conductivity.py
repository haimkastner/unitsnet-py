from enum import Enum
import math
import string


class ElectricConductivityUnits(Enum):
        """
            ElectricConductivityUnits enumeration
        """
        
        SiemensPerMeter = 'siemens_per_meter'
        """
            
        """
        
        SiemensPerInch = 'siemens_per_inch'
        """
            
        """
        
        SiemensPerFoot = 'siemens_per_foot'
        """
            
        """
        
        SiemensPerCentimeter = 'siemens_per_centimeter'
        """
            
        """
        
        MicrosiemensPerCentimeter = 'microsiemens_per_centimeter'
        """
            
        """
        
        MillisiemensPerCentimeter = 'millisiemens_per_centimeter'
        """
            
        """
        

class ElectricConductivity:
    """
    Electrical conductivity or specific conductance is the reciprocal of electrical resistivity, and measures a material's ability to conduct an electric current.

    Args:
        value (float): The value.
        from_unit (ElectricConductivityUnits): The ElectricConductivity unit to create from, The default unit is SiemensPerMeter
    """
    def __init__(self, value: float, from_unit: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__siemens_per_meter = None
        
        self.__siemens_per_inch = None
        
        self.__siemens_per_foot = None
        
        self.__siemens_per_centimeter = None
        
        self.__microsiemens_per_centimeter = None
        
        self.__millisiemens_per_centimeter = None
        

    def __convert_from_base(self, from_unit: ElectricConductivityUnits) -> float:
        value = self.__value
        
        if from_unit == ElectricConductivityUnits.SiemensPerMeter:
            return (value)
        
        if from_unit == ElectricConductivityUnits.SiemensPerInch:
            return (value / 3.937007874015748e1)
        
        if from_unit == ElectricConductivityUnits.SiemensPerFoot:
            return (value / 3.2808398950131234)
        
        if from_unit == ElectricConductivityUnits.SiemensPerCentimeter:
            return (value / 1e2)
        
        if from_unit == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return ((value / 1e2) / 1e-06)
        
        if from_unit == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return ((value / 1e2) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricConductivityUnits) -> float:
        
        if to_unit == ElectricConductivityUnits.SiemensPerMeter:
            return (value)
        
        if to_unit == ElectricConductivityUnits.SiemensPerInch:
            return (value * 3.937007874015748e1)
        
        if to_unit == ElectricConductivityUnits.SiemensPerFoot:
            return (value * 3.2808398950131234)
        
        if to_unit == ElectricConductivityUnits.SiemensPerCentimeter:
            return (value * 1e2)
        
        if to_unit == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return ((value * 1e2) * 1e-06)
        
        if to_unit == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return ((value * 1e2) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_siemens_per_meter(siemens_per_meter: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_meter.

        

        :param meters: The ElectricConductivity value in siemens_per_meter.
        :type siemens_per_meter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_meter, ElectricConductivityUnits.SiemensPerMeter)

    
    @staticmethod
    def from_siemens_per_inch(siemens_per_inch: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_inch.

        

        :param meters: The ElectricConductivity value in siemens_per_inch.
        :type siemens_per_inch: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_inch, ElectricConductivityUnits.SiemensPerInch)

    
    @staticmethod
    def from_siemens_per_foot(siemens_per_foot: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_foot.

        

        :param meters: The ElectricConductivity value in siemens_per_foot.
        :type siemens_per_foot: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_foot, ElectricConductivityUnits.SiemensPerFoot)

    
    @staticmethod
    def from_siemens_per_centimeter(siemens_per_centimeter: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_centimeter.

        

        :param meters: The ElectricConductivity value in siemens_per_centimeter.
        :type siemens_per_centimeter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_centimeter, ElectricConductivityUnits.SiemensPerCentimeter)

    
    @staticmethod
    def from_microsiemens_per_centimeter(microsiemens_per_centimeter: float):
        """
        Create a new instance of ElectricConductivity from a value in microsiemens_per_centimeter.

        

        :param meters: The ElectricConductivity value in microsiemens_per_centimeter.
        :type microsiemens_per_centimeter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(microsiemens_per_centimeter, ElectricConductivityUnits.MicrosiemensPerCentimeter)

    
    @staticmethod
    def from_millisiemens_per_centimeter(millisiemens_per_centimeter: float):
        """
        Create a new instance of ElectricConductivity from a value in millisiemens_per_centimeter.

        

        :param meters: The ElectricConductivity value in millisiemens_per_centimeter.
        :type millisiemens_per_centimeter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(millisiemens_per_centimeter, ElectricConductivityUnits.MillisiemensPerCentimeter)

    
    @property
    def siemens_per_meter(self) -> float:
        """
        
        """
        if self.__siemens_per_meter != None:
            return self.__siemens_per_meter
        self.__siemens_per_meter = self.__convert_from_base(ElectricConductivityUnits.SiemensPerMeter)
        return self.__siemens_per_meter

    
    @property
    def siemens_per_inch(self) -> float:
        """
        
        """
        if self.__siemens_per_inch != None:
            return self.__siemens_per_inch
        self.__siemens_per_inch = self.__convert_from_base(ElectricConductivityUnits.SiemensPerInch)
        return self.__siemens_per_inch

    
    @property
    def siemens_per_foot(self) -> float:
        """
        
        """
        if self.__siemens_per_foot != None:
            return self.__siemens_per_foot
        self.__siemens_per_foot = self.__convert_from_base(ElectricConductivityUnits.SiemensPerFoot)
        return self.__siemens_per_foot

    
    @property
    def siemens_per_centimeter(self) -> float:
        """
        
        """
        if self.__siemens_per_centimeter != None:
            return self.__siemens_per_centimeter
        self.__siemens_per_centimeter = self.__convert_from_base(ElectricConductivityUnits.SiemensPerCentimeter)
        return self.__siemens_per_centimeter

    
    @property
    def microsiemens_per_centimeter(self) -> float:
        """
        
        """
        if self.__microsiemens_per_centimeter != None:
            return self.__microsiemens_per_centimeter
        self.__microsiemens_per_centimeter = self.__convert_from_base(ElectricConductivityUnits.MicrosiemensPerCentimeter)
        return self.__microsiemens_per_centimeter

    
    @property
    def millisiemens_per_centimeter(self) -> float:
        """
        
        """
        if self.__millisiemens_per_centimeter != None:
            return self.__millisiemens_per_centimeter
        self.__millisiemens_per_centimeter = self.__convert_from_base(ElectricConductivityUnits.MillisiemensPerCentimeter)
        return self.__millisiemens_per_centimeter

    
    def to_string(self, unit: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter) -> string:
        """
        Format the ElectricConductivity to string.
        Note! the default format for ElectricConductivity is SiemensPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricConductivityUnits.SiemensPerMeter:
            return f"""{self.siemens_per_meter} S/m"""
        
        if unit == ElectricConductivityUnits.SiemensPerInch:
            return f"""{self.siemens_per_inch} S/in"""
        
        if unit == ElectricConductivityUnits.SiemensPerFoot:
            return f"""{self.siemens_per_foot} S/ft"""
        
        if unit == ElectricConductivityUnits.SiemensPerCentimeter:
            return f"""{self.siemens_per_centimeter} S/cm"""
        
        if unit == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return f"""{self.microsiemens_per_centimeter} """
        
        if unit == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return f"""{self.millisiemens_per_centimeter} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter) -> string:
        """
        Get ElectricConductivity unit abbreviation.
        Note! the default abbreviation for ElectricConductivity is SiemensPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerMeter:
            return """S/m"""
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerInch:
            return """S/in"""
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerFoot:
            return """S/ft"""
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerCentimeter:
            return """S/cm"""
        
        if unit_abbreviation == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return """"""
        
        if unit_abbreviation == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for +: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return ElectricConductivity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for *: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return ElectricConductivity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for -: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return ElectricConductivity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for /: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return ElectricConductivity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for %: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return ElectricConductivity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for **: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return ElectricConductivity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for ==: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for <: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for >: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for <=: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, ElectricConductivity):
            raise TypeError("unsupported operand type(s) for >=: 'ElectricConductivity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value