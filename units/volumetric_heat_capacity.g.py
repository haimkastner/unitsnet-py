from enum import Enum
import math
import string


class VolumetricHeatCapacityUnits(Enum):
        """
            VolumetricHeatCapacityUnits enumeration
        """
        
        JoulePerCubicMeterKelvin = 'joule_per_cubic_meter_kelvin'
        """
            
        """
        
        JoulePerCubicMeterDegreeCelsius = 'joule_per_cubic_meter_degree_celsius'
        """
            
        """
        
        CaloriePerCubicCentimeterDegreeCelsius = 'calorie_per_cubic_centimeter_degree_celsius'
        """
            
        """
        
        BtuPerCubicFootDegreeFahrenheit = 'btu_per_cubic_foot_degree_fahrenheit'
        """
            
        """
        
        KiloJoulePerCubicMeterKelvin = 'kilo_joule_per_cubic_meter_kelvin'
        """
            
        """
        
        MegaJoulePerCubicMeterKelvin = 'mega_joule_per_cubic_meter_kelvin'
        """
            
        """
        
        KiloJoulePerCubicMeterDegreeCelsius = 'kilo_joule_per_cubic_meter_degree_celsius'
        """
            
        """
        
        MegaJoulePerCubicMeterDegreeCelsius = 'mega_joule_per_cubic_meter_degree_celsius'
        """
            
        """
        
        KiloCaloriePerCubicCentimeterDegreeCelsius = 'kilo_calorie_per_cubic_centimeter_degree_celsius'
        """
            
        """
        
    
class VolumetricHeatCapacity:
    """
    The volumetric heat capacity is the amount of energy that must be added, in the form of heat, to one unit of volume of the material in order to cause an increase of one unit in its temperature.

    Args:
        value (float): The value.
        from_unit (VolumetricHeatCapacityUnits): The VolumetricHeatCapacity unit to create from, The default unit is JoulePerCubicMeterKelvin
    """
    def __init__(self, value: float, from_unit: VolumetricHeatCapacityUnits = VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_cubic_meter_kelvin = None
        
        self.__joules_per_cubic_meter_degree_celsius = None
        
        self.__calories_per_cubic_centimeter_degree_celsius = None
        
        self.__btus_per_cubic_foot_degree_fahrenheit = None
        
        self.__kilo_joules_per_cubic_meter_kelvin = None
        
        self.__mega_joules_per_cubic_meter_kelvin = None
        
        self.__kilo_joules_per_cubic_meter_degree_celsius = None
        
        self.__mega_joules_per_cubic_meter_degree_celsius = None
        
        self.__kilo_calories_per_cubic_centimeter_degree_celsius = None
        

    def __convert_from_base(self, from_unit: VolumetricHeatCapacityUnits) -> float:
        value = self.__value
        
        if from_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return (value)
        
        if from_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return (value)
        
        if from_unit == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return (value * 2.388459e-7)
        
        if from_unit == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return (value * 1.4910660e-5)
        
        if from_unit == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterKelvin:
            return ((value) / 1000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterKelvin:
            return ((value) / 1000000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterDegreeCelsius:
            return ((value) / 1000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterDegreeCelsius:
            return ((value) / 1000000.0)
        
        if from_unit == VolumetricHeatCapacityUnits.KiloCaloriePerCubicCentimeterDegreeCelsius:
            return ((value * 2.388459e-7) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: VolumetricHeatCapacityUnits) -> float:
        
        if to_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return (value)
        
        if to_unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return (value)
        
        if to_unit == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return (value / 2.388459e-7)
        
        if to_unit == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return (value / 1.4910660e-5)
        
        if to_unit == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterKelvin:
            return ((value) * 1000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterKelvin:
            return ((value) * 1000000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterDegreeCelsius:
            return ((value) * 1000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterDegreeCelsius:
            return ((value) * 1000000.0)
        
        if to_unit == VolumetricHeatCapacityUnits.KiloCaloriePerCubicCentimeterDegreeCelsius:
            return ((value / 2.388459e-7) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_joules_per_cubic_meter_kelvin(joules_per_cubic_meter_kelvin: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in joules_per_cubic_meter_kelvin.

        

        :param meters: The VolumetricHeatCapacity value in joules_per_cubic_meter_kelvin.
        :type joules_per_cubic_meter_kelvin: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(joules_per_cubic_meter_kelvin, VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin)

    
    @staticmethod
    def from_joules_per_cubic_meter_degree_celsius(joules_per_cubic_meter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in joules_per_cubic_meter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in joules_per_cubic_meter_degree_celsius.
        :type joules_per_cubic_meter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(joules_per_cubic_meter_degree_celsius, VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius)

    
    @staticmethod
    def from_calories_per_cubic_centimeter_degree_celsius(calories_per_cubic_centimeter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in calories_per_cubic_centimeter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in calories_per_cubic_centimeter_degree_celsius.
        :type calories_per_cubic_centimeter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(calories_per_cubic_centimeter_degree_celsius, VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius)

    
    @staticmethod
    def from_btus_per_cubic_foot_degree_fahrenheit(btus_per_cubic_foot_degree_fahrenheit: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in btus_per_cubic_foot_degree_fahrenheit.

        

        :param meters: The VolumetricHeatCapacity value in btus_per_cubic_foot_degree_fahrenheit.
        :type btus_per_cubic_foot_degree_fahrenheit: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(btus_per_cubic_foot_degree_fahrenheit, VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit)

    
    @staticmethod
    def from_kilo_joules_per_cubic_meter_kelvin(kilo_joules_per_cubic_meter_kelvin: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in kilo_joules_per_cubic_meter_kelvin.

        

        :param meters: The VolumetricHeatCapacity value in kilo_joules_per_cubic_meter_kelvin.
        :type kilo_joules_per_cubic_meter_kelvin: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(kilo_joules_per_cubic_meter_kelvin, VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterKelvin)

    
    @staticmethod
    def from_mega_joules_per_cubic_meter_kelvin(mega_joules_per_cubic_meter_kelvin: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in mega_joules_per_cubic_meter_kelvin.

        

        :param meters: The VolumetricHeatCapacity value in mega_joules_per_cubic_meter_kelvin.
        :type mega_joules_per_cubic_meter_kelvin: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(mega_joules_per_cubic_meter_kelvin, VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterKelvin)

    
    @staticmethod
    def from_kilo_joules_per_cubic_meter_degree_celsius(kilo_joules_per_cubic_meter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in kilo_joules_per_cubic_meter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in kilo_joules_per_cubic_meter_degree_celsius.
        :type kilo_joules_per_cubic_meter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(kilo_joules_per_cubic_meter_degree_celsius, VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterDegreeCelsius)

    
    @staticmethod
    def from_mega_joules_per_cubic_meter_degree_celsius(mega_joules_per_cubic_meter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in mega_joules_per_cubic_meter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in mega_joules_per_cubic_meter_degree_celsius.
        :type mega_joules_per_cubic_meter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(mega_joules_per_cubic_meter_degree_celsius, VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterDegreeCelsius)

    
    @staticmethod
    def from_kilo_calories_per_cubic_centimeter_degree_celsius(kilo_calories_per_cubic_centimeter_degree_celsius: float):
        """
        Create a new instance of VolumetricHeatCapacity from a value in kilo_calories_per_cubic_centimeter_degree_celsius.

        

        :param meters: The VolumetricHeatCapacity value in kilo_calories_per_cubic_centimeter_degree_celsius.
        :type kilo_calories_per_cubic_centimeter_degree_celsius: float
        :return: A new instance of VolumetricHeatCapacity.
        :rtype: VolumetricHeatCapacity
        """
        return VolumetricHeatCapacity(kilo_calories_per_cubic_centimeter_degree_celsius, VolumetricHeatCapacityUnits.KiloCaloriePerCubicCentimeterDegreeCelsius)

    
    @property
    def joules_per_cubic_meter_kelvin(self) -> float:
        """
        
        """
        if self.__joules_per_cubic_meter_kelvin != None:
            return self.__joules_per_cubic_meter_kelvin
        self.__joules_per_cubic_meter_kelvin = self.__convert_from_base(VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin)
        return self.__joules_per_cubic_meter_kelvin

    
    @property
    def joules_per_cubic_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__joules_per_cubic_meter_degree_celsius != None:
            return self.__joules_per_cubic_meter_degree_celsius
        self.__joules_per_cubic_meter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius)
        return self.__joules_per_cubic_meter_degree_celsius

    
    @property
    def calories_per_cubic_centimeter_degree_celsius(self) -> float:
        """
        
        """
        if self.__calories_per_cubic_centimeter_degree_celsius != None:
            return self.__calories_per_cubic_centimeter_degree_celsius
        self.__calories_per_cubic_centimeter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius)
        return self.__calories_per_cubic_centimeter_degree_celsius

    
    @property
    def btus_per_cubic_foot_degree_fahrenheit(self) -> float:
        """
        
        """
        if self.__btus_per_cubic_foot_degree_fahrenheit != None:
            return self.__btus_per_cubic_foot_degree_fahrenheit
        self.__btus_per_cubic_foot_degree_fahrenheit = self.__convert_from_base(VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit)
        return self.__btus_per_cubic_foot_degree_fahrenheit

    
    @property
    def kilo_joules_per_cubic_meter_kelvin(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_cubic_meter_kelvin != None:
            return self.__kilo_joules_per_cubic_meter_kelvin
        self.__kilo_joules_per_cubic_meter_kelvin = self.__convert_from_base(VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterKelvin)
        return self.__kilo_joules_per_cubic_meter_kelvin

    
    @property
    def mega_joules_per_cubic_meter_kelvin(self) -> float:
        """
        
        """
        if self.__mega_joules_per_cubic_meter_kelvin != None:
            return self.__mega_joules_per_cubic_meter_kelvin
        self.__mega_joules_per_cubic_meter_kelvin = self.__convert_from_base(VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterKelvin)
        return self.__mega_joules_per_cubic_meter_kelvin

    
    @property
    def kilo_joules_per_cubic_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_cubic_meter_degree_celsius != None:
            return self.__kilo_joules_per_cubic_meter_degree_celsius
        self.__kilo_joules_per_cubic_meter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterDegreeCelsius)
        return self.__kilo_joules_per_cubic_meter_degree_celsius

    
    @property
    def mega_joules_per_cubic_meter_degree_celsius(self) -> float:
        """
        
        """
        if self.__mega_joules_per_cubic_meter_degree_celsius != None:
            return self.__mega_joules_per_cubic_meter_degree_celsius
        self.__mega_joules_per_cubic_meter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterDegreeCelsius)
        return self.__mega_joules_per_cubic_meter_degree_celsius

    
    @property
    def kilo_calories_per_cubic_centimeter_degree_celsius(self) -> float:
        """
        
        """
        if self.__kilo_calories_per_cubic_centimeter_degree_celsius != None:
            return self.__kilo_calories_per_cubic_centimeter_degree_celsius
        self.__kilo_calories_per_cubic_centimeter_degree_celsius = self.__convert_from_base(VolumetricHeatCapacityUnits.KiloCaloriePerCubicCentimeterDegreeCelsius)
        return self.__kilo_calories_per_cubic_centimeter_degree_celsius

    
    def to_string(self, unit: VolumetricHeatCapacityUnits = VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin) -> string:
        """
        Format the VolumetricHeatCapacity to string.
        Note! the default format for VolumetricHeatCapacity is JoulePerCubicMeterKelvin.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return f"""{self.joules_per_cubic_meter_kelvin} J/m³·K"""
        
        if unit == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return f"""{self.joules_per_cubic_meter_degree_celsius} J/m³·°C"""
        
        if unit == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return f"""{self.calories_per_cubic_centimeter_degree_celsius} cal/cm³·°C"""
        
        if unit == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return f"""{self.btus_per_cubic_foot_degree_fahrenheit} BTU/ft³·°F"""
        
        if unit == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterKelvin:
            return f"""{self.kilo_joules_per_cubic_meter_kelvin} """
        
        if unit == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterKelvin:
            return f"""{self.mega_joules_per_cubic_meter_kelvin} """
        
        if unit == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterDegreeCelsius:
            return f"""{self.kilo_joules_per_cubic_meter_degree_celsius} """
        
        if unit == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterDegreeCelsius:
            return f"""{self.mega_joules_per_cubic_meter_degree_celsius} """
        
        if unit == VolumetricHeatCapacityUnits.KiloCaloriePerCubicCentimeterDegreeCelsius:
            return f"""{self.kilo_calories_per_cubic_centimeter_degree_celsius} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: VolumetricHeatCapacityUnits = VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin) -> string:
        """
        Get VolumetricHeatCapacity unit abbreviation.
        Note! the default abbreviation for VolumetricHeatCapacity is JoulePerCubicMeterKelvin.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.JoulePerCubicMeterKelvin:
            return """J/m³·K"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.JoulePerCubicMeterDegreeCelsius:
            return """J/m³·°C"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.CaloriePerCubicCentimeterDegreeCelsius:
            return """cal/cm³·°C"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.BtuPerCubicFootDegreeFahrenheit:
            return """BTU/ft³·°F"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterKelvin:
            return """"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterKelvin:
            return """"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.KiloJoulePerCubicMeterDegreeCelsius:
            return """"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.MegaJoulePerCubicMeterDegreeCelsius:
            return """"""
        
        if unit_abbreviation == VolumetricHeatCapacityUnits.KiloCaloriePerCubicCentimeterDegreeCelsius:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for +: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return VolumetricHeatCapacity(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for *: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return VolumetricHeatCapacity(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for -: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return VolumetricHeatCapacity(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for /: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return VolumetricHeatCapacity(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for %: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return VolumetricHeatCapacity(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for **: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return VolumetricHeatCapacity(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for ==: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for <: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for >: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for <=: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, VolumetricHeatCapacity):
            raise TypeError("unsupported operand type(s) for >=: 'VolumetricHeatCapacity' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value