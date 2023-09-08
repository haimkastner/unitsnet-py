from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricSurfaceChargeDensityUnits(Enum):
        """
            ElectricSurfaceChargeDensityUnits enumeration
        """
        
        CoulombPerSquareMeter = 'coulomb_per_square_meter'
        """
            
        """
        
        CoulombPerSquareCentimeter = 'coulomb_per_square_centimeter'
        """
            
        """
        
        CoulombPerSquareInch = 'coulomb_per_square_inch'
        """
            
        """
        

class ElectricSurfaceChargeDensity(AbstractMeasure):
    """
    In electromagnetism, surface charge density is a measure of the amount of electric charge per surface area.

    Args:
        value (float): The value.
        from_unit (ElectricSurfaceChargeDensityUnits): The ElectricSurfaceChargeDensity unit to create from, The default unit is CoulombPerSquareMeter
    """
    def __init__(self, value: float, from_unit: ElectricSurfaceChargeDensityUnits = ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__coulombs_per_square_meter = None
        
        self.__coulombs_per_square_centimeter = None
        
        self.__coulombs_per_square_inch = None
        

    def convert(self, unit: ElectricSurfaceChargeDensityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ElectricSurfaceChargeDensityUnits) -> float:
        value = self._value
        
        if from_unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter:
            return (value)
        
        if from_unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareCentimeter:
            return (value / 1.0e4)
        
        if from_unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareInch:
            return (value / 1.5500031000062000e3)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricSurfaceChargeDensityUnits) -> float:
        
        if to_unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter:
            return (value)
        
        if to_unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareCentimeter:
            return (value * 1.0e4)
        
        if to_unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareInch:
            return (value * 1.5500031000062000e3)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_coulombs_per_square_meter(coulombs_per_square_meter: float):
        """
        Create a new instance of ElectricSurfaceChargeDensity from a value in coulombs_per_square_meter.

        

        :param meters: The ElectricSurfaceChargeDensity value in coulombs_per_square_meter.
        :type coulombs_per_square_meter: float
        :return: A new instance of ElectricSurfaceChargeDensity.
        :rtype: ElectricSurfaceChargeDensity
        """
        return ElectricSurfaceChargeDensity(coulombs_per_square_meter, ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter)

    
    @staticmethod
    def from_coulombs_per_square_centimeter(coulombs_per_square_centimeter: float):
        """
        Create a new instance of ElectricSurfaceChargeDensity from a value in coulombs_per_square_centimeter.

        

        :param meters: The ElectricSurfaceChargeDensity value in coulombs_per_square_centimeter.
        :type coulombs_per_square_centimeter: float
        :return: A new instance of ElectricSurfaceChargeDensity.
        :rtype: ElectricSurfaceChargeDensity
        """
        return ElectricSurfaceChargeDensity(coulombs_per_square_centimeter, ElectricSurfaceChargeDensityUnits.CoulombPerSquareCentimeter)

    
    @staticmethod
    def from_coulombs_per_square_inch(coulombs_per_square_inch: float):
        """
        Create a new instance of ElectricSurfaceChargeDensity from a value in coulombs_per_square_inch.

        

        :param meters: The ElectricSurfaceChargeDensity value in coulombs_per_square_inch.
        :type coulombs_per_square_inch: float
        :return: A new instance of ElectricSurfaceChargeDensity.
        :rtype: ElectricSurfaceChargeDensity
        """
        return ElectricSurfaceChargeDensity(coulombs_per_square_inch, ElectricSurfaceChargeDensityUnits.CoulombPerSquareInch)

    
    @property
    def coulombs_per_square_meter(self) -> float:
        """
        
        """
        if self.__coulombs_per_square_meter != None:
            return self.__coulombs_per_square_meter
        self.__coulombs_per_square_meter = self.__convert_from_base(ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter)
        return self.__coulombs_per_square_meter

    
    @property
    def coulombs_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__coulombs_per_square_centimeter != None:
            return self.__coulombs_per_square_centimeter
        self.__coulombs_per_square_centimeter = self.__convert_from_base(ElectricSurfaceChargeDensityUnits.CoulombPerSquareCentimeter)
        return self.__coulombs_per_square_centimeter

    
    @property
    def coulombs_per_square_inch(self) -> float:
        """
        
        """
        if self.__coulombs_per_square_inch != None:
            return self.__coulombs_per_square_inch
        self.__coulombs_per_square_inch = self.__convert_from_base(ElectricSurfaceChargeDensityUnits.CoulombPerSquareInch)
        return self.__coulombs_per_square_inch

    
    def to_string(self, unit: ElectricSurfaceChargeDensityUnits = ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter) -> str:
        """
        Format the ElectricSurfaceChargeDensity to string.
        Note! the default format for ElectricSurfaceChargeDensity is CoulombPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter:
            return f"""{self.coulombs_per_square_meter} C/m²"""
        
        if unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareCentimeter:
            return f"""{self.coulombs_per_square_centimeter} C/cm²"""
        
        if unit == ElectricSurfaceChargeDensityUnits.CoulombPerSquareInch:
            return f"""{self.coulombs_per_square_inch} C/in²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricSurfaceChargeDensityUnits = ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter) -> str:
        """
        Get ElectricSurfaceChargeDensity unit abbreviation.
        Note! the default abbreviation for ElectricSurfaceChargeDensity is CoulombPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricSurfaceChargeDensityUnits.CoulombPerSquareMeter:
            return """C/m²"""
        
        if unit_abbreviation == ElectricSurfaceChargeDensityUnits.CoulombPerSquareCentimeter:
            return """C/cm²"""
        
        if unit_abbreviation == ElectricSurfaceChargeDensityUnits.CoulombPerSquareInch:
            return """C/in²"""
        