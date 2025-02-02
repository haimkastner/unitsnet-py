from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class FluidResistanceUnits(Enum):
        """
            FluidResistanceUnits enumeration
        """
        
        PascalSecondPerLiter = 'PascalSecondPerLiter'
        """
            
        """
        
        PascalMinutePerLiter = 'PascalMinutePerLiter'
        """
            
        """
        
        PascalSecondPerMilliliter = 'PascalSecondPerMilliliter'
        """
            
        """
        
        PascalMinutePerMilliliter = 'PascalMinutePerMilliliter'
        """
            
        """
        
        PascalSecondPerCubicMeter = 'PascalSecondPerCubicMeter'
        """
            
        """
        
        PascalMinutePerCubicMeter = 'PascalMinutePerCubicMeter'
        """
            
        """
        
        PascalSecondPerCubicCentimeter = 'PascalSecondPerCubicCentimeter'
        """
            
        """
        
        PascalMinutePerCubicCentimeter = 'PascalMinutePerCubicCentimeter'
        """
            
        """
        
        DyneSecondPerCentimeterToTheFifth = 'DyneSecondPerCentimeterToTheFifth'
        """
            
        """
        
        MillimeterMercurySecondPerLiter = 'MillimeterMercurySecondPerLiter'
        """
            
        """
        
        MillimeterMercuryMinutePerLiter = 'MillimeterMercuryMinutePerLiter'
        """
            
        """
        
        MillimeterMercurySecondPerMilliliter = 'MillimeterMercurySecondPerMilliliter'
        """
            
        """
        
        MillimeterMercuryMinutePerMilliliter = 'MillimeterMercuryMinutePerMilliliter'
        """
            
        """
        
        MillimeterMercurySecondPerCubicCentimeter = 'MillimeterMercurySecondPerCubicCentimeter'
        """
            
        """
        
        MillimeterMercuryMinutePerCubicCentimeter = 'MillimeterMercuryMinutePerCubicCentimeter'
        """
            
        """
        
        MillimeterMercurySecondPerCubicMeter = 'MillimeterMercurySecondPerCubicMeter'
        """
            
        """
        
        MillimeterMercuryMinutePerCubicMeter = 'MillimeterMercuryMinutePerCubicMeter'
        """
            
        """
        
        WoodUnit = 'WoodUnit'
        """
            
        """
        
        MegapascalSecondPerCubicMeter = 'MegapascalSecondPerCubicMeter'
        """
            
        """
        

class FluidResistanceDto:
    """
    A DTO representation of a FluidResistance

    Attributes:
        value (float): The value of the FluidResistance.
        unit (FluidResistanceUnits): The specific unit that the FluidResistance value is representing.
    """

    def __init__(self, value: float, unit: FluidResistanceUnits):
        """
        Create a new DTO representation of a FluidResistance

        Parameters:
            value (float): The value of the FluidResistance.
            unit (FluidResistanceUnits): The specific unit that the FluidResistance value is representing.
        """
        self.value: float = value
        """
        The value of the FluidResistance
        """
        self.unit: FluidResistanceUnits = unit
        """
        The specific unit that the FluidResistance value is representing
        """

    def to_json(self):
        """
        Get a FluidResistance DTO JSON object representing the current unit.

        :return: JSON object represents FluidResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "PascalSecondPerCubicMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of FluidResistance DTO from a json representation.

        :param data: The FluidResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "PascalSecondPerCubicMeter"}
        :return: A new instance of FluidResistanceDto.
        :rtype: FluidResistanceDto
        """
        return FluidResistanceDto(value=data["value"], unit=FluidResistanceUnits(data["unit"]))


class FluidResistance(AbstractMeasure):
    """
    Fluid Resistance is a force acting opposite to the relative motion of any object moving with respect to a surrounding fluid. Fluid Resistance is sometimes referred to as drag or fluid friction.

    Args:
        value (float): The value.
        from_unit (FluidResistanceUnits): The FluidResistance unit to create from, The default unit is PascalSecondPerCubicMeter
    """
    def __init__(self, value: float, from_unit: FluidResistanceUnits = FluidResistanceUnits.PascalSecondPerCubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__pascal_seconds_per_liter = None
        
        self.__pascal_minutes_per_liter = None
        
        self.__pascal_seconds_per_milliliter = None
        
        self.__pascal_minutes_per_milliliter = None
        
        self.__pascal_seconds_per_cubic_meter = None
        
        self.__pascal_minutes_per_cubic_meter = None
        
        self.__pascal_seconds_per_cubic_centimeter = None
        
        self.__pascal_minutes_per_cubic_centimeter = None
        
        self.__dyne_seconds_per_centimeter_to_the_fifth = None
        
        self.__millimeter_mercury_seconds_per_liter = None
        
        self.__millimeter_mercury_minutes_per_liter = None
        
        self.__millimeter_mercury_seconds_per_milliliter = None
        
        self.__millimeter_mercury_minutes_per_milliliter = None
        
        self.__millimeter_mercury_seconds_per_cubic_centimeter = None
        
        self.__millimeter_mercury_minutes_per_cubic_centimeter = None
        
        self.__millimeter_mercury_seconds_per_cubic_meter = None
        
        self.__millimeter_mercury_minutes_per_cubic_meter = None
        
        self.__wood_units = None
        
        self.__megapascal_seconds_per_cubic_meter = None
        

    def convert(self, unit: FluidResistanceUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: FluidResistanceUnits = FluidResistanceUnits.PascalSecondPerCubicMeter) -> FluidResistanceDto:
        """
        Get a new instance of FluidResistance DTO representing the current unit.

        :param hold_in_unit: The specific FluidResistance unit to store the FluidResistance value in the DTO representation.
        :type hold_in_unit: FluidResistanceUnits
        :return: A new instance of FluidResistanceDto.
        :rtype: FluidResistanceDto
        """
        return FluidResistanceDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: FluidResistanceUnits = FluidResistanceUnits.PascalSecondPerCubicMeter):
        """
        Get a FluidResistance DTO JSON object representing the current unit.

        :param hold_in_unit: The specific FluidResistance unit to store the FluidResistance value in the DTO representation.
        :type hold_in_unit: FluidResistanceUnits
        :return: JSON object represents FluidResistance DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "PascalSecondPerCubicMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(fluid_resistance_dto: FluidResistanceDto):
        """
        Obtain a new instance of FluidResistance from a DTO unit object.

        :param fluid_resistance_dto: The FluidResistance DTO representation.
        :type fluid_resistance_dto: FluidResistanceDto
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(fluid_resistance_dto.value, fluid_resistance_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of FluidResistance from a DTO unit json representation.

        :param data: The FluidResistance DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "PascalSecondPerCubicMeter"}
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance.from_dto(FluidResistanceDto.from_json(data))

    def __convert_from_base(self, from_unit: FluidResistanceUnits) -> float:
        value = self._value
        
        if from_unit == FluidResistanceUnits.PascalSecondPerLiter:
            return (value / 1e3)
        
        if from_unit == FluidResistanceUnits.PascalMinutePerLiter:
            return (value / 6e4)
        
        if from_unit == FluidResistanceUnits.PascalSecondPerMilliliter:
            return (value / 1e6)
        
        if from_unit == FluidResistanceUnits.PascalMinutePerMilliliter:
            return (value / 6e7)
        
        if from_unit == FluidResistanceUnits.PascalSecondPerCubicMeter:
            return (value)
        
        if from_unit == FluidResistanceUnits.PascalMinutePerCubicMeter:
            return (value / 60)
        
        if from_unit == FluidResistanceUnits.PascalSecondPerCubicCentimeter:
            return (value / 1e6)
        
        if from_unit == FluidResistanceUnits.PascalMinutePerCubicCentimeter:
            return (value / 6e7)
        
        if from_unit == FluidResistanceUnits.DyneSecondPerCentimeterToTheFifth:
            return (value / 1e5)
        
        if from_unit == FluidResistanceUnits.MillimeterMercurySecondPerLiter:
            return (value / 1.33322368e5)
        
        if from_unit == FluidResistanceUnits.MillimeterMercuryMinutePerLiter:
            return (value / 7.99934208e6)
        
        if from_unit == FluidResistanceUnits.MillimeterMercurySecondPerMilliliter:
            return (value / 1.33322368e8)
        
        if from_unit == FluidResistanceUnits.MillimeterMercuryMinutePerMilliliter:
            return (value / 7.99934208e9)
        
        if from_unit == FluidResistanceUnits.MillimeterMercurySecondPerCubicCentimeter:
            return (value / 1.33322368e8)
        
        if from_unit == FluidResistanceUnits.MillimeterMercuryMinutePerCubicCentimeter:
            return (value / 7.99934208e9)
        
        if from_unit == FluidResistanceUnits.MillimeterMercurySecondPerCubicMeter:
            return (value / 133.322368)
        
        if from_unit == FluidResistanceUnits.MillimeterMercuryMinutePerCubicMeter:
            return (value / 7.99934208e3)
        
        if from_unit == FluidResistanceUnits.WoodUnit:
            return (value / 7.99934208e6)
        
        if from_unit == FluidResistanceUnits.MegapascalSecondPerCubicMeter:
            return ((value) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: FluidResistanceUnits) -> float:
        
        if to_unit == FluidResistanceUnits.PascalSecondPerLiter:
            return (value * 1e3)
        
        if to_unit == FluidResistanceUnits.PascalMinutePerLiter:
            return (value * 6e4)
        
        if to_unit == FluidResistanceUnits.PascalSecondPerMilliliter:
            return (value * 1e6)
        
        if to_unit == FluidResistanceUnits.PascalMinutePerMilliliter:
            return (value * 6e7)
        
        if to_unit == FluidResistanceUnits.PascalSecondPerCubicMeter:
            return (value)
        
        if to_unit == FluidResistanceUnits.PascalMinutePerCubicMeter:
            return (value * 60)
        
        if to_unit == FluidResistanceUnits.PascalSecondPerCubicCentimeter:
            return (value * 1e6)
        
        if to_unit == FluidResistanceUnits.PascalMinutePerCubicCentimeter:
            return (value * 6e7)
        
        if to_unit == FluidResistanceUnits.DyneSecondPerCentimeterToTheFifth:
            return (value * 1e5)
        
        if to_unit == FluidResistanceUnits.MillimeterMercurySecondPerLiter:
            return (value * 1.33322368e5)
        
        if to_unit == FluidResistanceUnits.MillimeterMercuryMinutePerLiter:
            return (value * 7.99934208e6)
        
        if to_unit == FluidResistanceUnits.MillimeterMercurySecondPerMilliliter:
            return (value * 1.33322368e8)
        
        if to_unit == FluidResistanceUnits.MillimeterMercuryMinutePerMilliliter:
            return (value * 7.99934208e9)
        
        if to_unit == FluidResistanceUnits.MillimeterMercurySecondPerCubicCentimeter:
            return (value * 1.33322368e8)
        
        if to_unit == FluidResistanceUnits.MillimeterMercuryMinutePerCubicCentimeter:
            return (value * 7.99934208e9)
        
        if to_unit == FluidResistanceUnits.MillimeterMercurySecondPerCubicMeter:
            return (value * 133.322368)
        
        if to_unit == FluidResistanceUnits.MillimeterMercuryMinutePerCubicMeter:
            return (value * 7.99934208e3)
        
        if to_unit == FluidResistanceUnits.WoodUnit:
            return (value * 7.99934208e6)
        
        if to_unit == FluidResistanceUnits.MegapascalSecondPerCubicMeter:
            return ((value) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_pascal_seconds_per_liter(pascal_seconds_per_liter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_seconds_per_liter.

        

        :param meters: The FluidResistance value in pascal_seconds_per_liter.
        :type pascal_seconds_per_liter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_seconds_per_liter, FluidResistanceUnits.PascalSecondPerLiter)

    
    @staticmethod
    def from_pascal_minutes_per_liter(pascal_minutes_per_liter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_minutes_per_liter.

        

        :param meters: The FluidResistance value in pascal_minutes_per_liter.
        :type pascal_minutes_per_liter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_minutes_per_liter, FluidResistanceUnits.PascalMinutePerLiter)

    
    @staticmethod
    def from_pascal_seconds_per_milliliter(pascal_seconds_per_milliliter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_seconds_per_milliliter.

        

        :param meters: The FluidResistance value in pascal_seconds_per_milliliter.
        :type pascal_seconds_per_milliliter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_seconds_per_milliliter, FluidResistanceUnits.PascalSecondPerMilliliter)

    
    @staticmethod
    def from_pascal_minutes_per_milliliter(pascal_minutes_per_milliliter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_minutes_per_milliliter.

        

        :param meters: The FluidResistance value in pascal_minutes_per_milliliter.
        :type pascal_minutes_per_milliliter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_minutes_per_milliliter, FluidResistanceUnits.PascalMinutePerMilliliter)

    
    @staticmethod
    def from_pascal_seconds_per_cubic_meter(pascal_seconds_per_cubic_meter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_seconds_per_cubic_meter.

        

        :param meters: The FluidResistance value in pascal_seconds_per_cubic_meter.
        :type pascal_seconds_per_cubic_meter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_seconds_per_cubic_meter, FluidResistanceUnits.PascalSecondPerCubicMeter)

    
    @staticmethod
    def from_pascal_minutes_per_cubic_meter(pascal_minutes_per_cubic_meter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_minutes_per_cubic_meter.

        

        :param meters: The FluidResistance value in pascal_minutes_per_cubic_meter.
        :type pascal_minutes_per_cubic_meter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_minutes_per_cubic_meter, FluidResistanceUnits.PascalMinutePerCubicMeter)

    
    @staticmethod
    def from_pascal_seconds_per_cubic_centimeter(pascal_seconds_per_cubic_centimeter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_seconds_per_cubic_centimeter.

        

        :param meters: The FluidResistance value in pascal_seconds_per_cubic_centimeter.
        :type pascal_seconds_per_cubic_centimeter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_seconds_per_cubic_centimeter, FluidResistanceUnits.PascalSecondPerCubicCentimeter)

    
    @staticmethod
    def from_pascal_minutes_per_cubic_centimeter(pascal_minutes_per_cubic_centimeter: float):
        """
        Create a new instance of FluidResistance from a value in pascal_minutes_per_cubic_centimeter.

        

        :param meters: The FluidResistance value in pascal_minutes_per_cubic_centimeter.
        :type pascal_minutes_per_cubic_centimeter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(pascal_minutes_per_cubic_centimeter, FluidResistanceUnits.PascalMinutePerCubicCentimeter)

    
    @staticmethod
    def from_dyne_seconds_per_centimeter_to_the_fifth(dyne_seconds_per_centimeter_to_the_fifth: float):
        """
        Create a new instance of FluidResistance from a value in dyne_seconds_per_centimeter_to_the_fifth.

        

        :param meters: The FluidResistance value in dyne_seconds_per_centimeter_to_the_fifth.
        :type dyne_seconds_per_centimeter_to_the_fifth: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(dyne_seconds_per_centimeter_to_the_fifth, FluidResistanceUnits.DyneSecondPerCentimeterToTheFifth)

    
    @staticmethod
    def from_millimeter_mercury_seconds_per_liter(millimeter_mercury_seconds_per_liter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_seconds_per_liter.

        

        :param meters: The FluidResistance value in millimeter_mercury_seconds_per_liter.
        :type millimeter_mercury_seconds_per_liter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_seconds_per_liter, FluidResistanceUnits.MillimeterMercurySecondPerLiter)

    
    @staticmethod
    def from_millimeter_mercury_minutes_per_liter(millimeter_mercury_minutes_per_liter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_minutes_per_liter.

        

        :param meters: The FluidResistance value in millimeter_mercury_minutes_per_liter.
        :type millimeter_mercury_minutes_per_liter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_minutes_per_liter, FluidResistanceUnits.MillimeterMercuryMinutePerLiter)

    
    @staticmethod
    def from_millimeter_mercury_seconds_per_milliliter(millimeter_mercury_seconds_per_milliliter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_seconds_per_milliliter.

        

        :param meters: The FluidResistance value in millimeter_mercury_seconds_per_milliliter.
        :type millimeter_mercury_seconds_per_milliliter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_seconds_per_milliliter, FluidResistanceUnits.MillimeterMercurySecondPerMilliliter)

    
    @staticmethod
    def from_millimeter_mercury_minutes_per_milliliter(millimeter_mercury_minutes_per_milliliter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_minutes_per_milliliter.

        

        :param meters: The FluidResistance value in millimeter_mercury_minutes_per_milliliter.
        :type millimeter_mercury_minutes_per_milliliter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_minutes_per_milliliter, FluidResistanceUnits.MillimeterMercuryMinutePerMilliliter)

    
    @staticmethod
    def from_millimeter_mercury_seconds_per_cubic_centimeter(millimeter_mercury_seconds_per_cubic_centimeter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_seconds_per_cubic_centimeter.

        

        :param meters: The FluidResistance value in millimeter_mercury_seconds_per_cubic_centimeter.
        :type millimeter_mercury_seconds_per_cubic_centimeter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_seconds_per_cubic_centimeter, FluidResistanceUnits.MillimeterMercurySecondPerCubicCentimeter)

    
    @staticmethod
    def from_millimeter_mercury_minutes_per_cubic_centimeter(millimeter_mercury_minutes_per_cubic_centimeter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_minutes_per_cubic_centimeter.

        

        :param meters: The FluidResistance value in millimeter_mercury_minutes_per_cubic_centimeter.
        :type millimeter_mercury_minutes_per_cubic_centimeter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_minutes_per_cubic_centimeter, FluidResistanceUnits.MillimeterMercuryMinutePerCubicCentimeter)

    
    @staticmethod
    def from_millimeter_mercury_seconds_per_cubic_meter(millimeter_mercury_seconds_per_cubic_meter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_seconds_per_cubic_meter.

        

        :param meters: The FluidResistance value in millimeter_mercury_seconds_per_cubic_meter.
        :type millimeter_mercury_seconds_per_cubic_meter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_seconds_per_cubic_meter, FluidResistanceUnits.MillimeterMercurySecondPerCubicMeter)

    
    @staticmethod
    def from_millimeter_mercury_minutes_per_cubic_meter(millimeter_mercury_minutes_per_cubic_meter: float):
        """
        Create a new instance of FluidResistance from a value in millimeter_mercury_minutes_per_cubic_meter.

        

        :param meters: The FluidResistance value in millimeter_mercury_minutes_per_cubic_meter.
        :type millimeter_mercury_minutes_per_cubic_meter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(millimeter_mercury_minutes_per_cubic_meter, FluidResistanceUnits.MillimeterMercuryMinutePerCubicMeter)

    
    @staticmethod
    def from_wood_units(wood_units: float):
        """
        Create a new instance of FluidResistance from a value in wood_units.

        

        :param meters: The FluidResistance value in wood_units.
        :type wood_units: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(wood_units, FluidResistanceUnits.WoodUnit)

    
    @staticmethod
    def from_megapascal_seconds_per_cubic_meter(megapascal_seconds_per_cubic_meter: float):
        """
        Create a new instance of FluidResistance from a value in megapascal_seconds_per_cubic_meter.

        

        :param meters: The FluidResistance value in megapascal_seconds_per_cubic_meter.
        :type megapascal_seconds_per_cubic_meter: float
        :return: A new instance of FluidResistance.
        :rtype: FluidResistance
        """
        return FluidResistance(megapascal_seconds_per_cubic_meter, FluidResistanceUnits.MegapascalSecondPerCubicMeter)

    
    @property
    def pascal_seconds_per_liter(self) -> float:
        """
        
        """
        if self.__pascal_seconds_per_liter != None:
            return self.__pascal_seconds_per_liter
        self.__pascal_seconds_per_liter = self.__convert_from_base(FluidResistanceUnits.PascalSecondPerLiter)
        return self.__pascal_seconds_per_liter

    
    @property
    def pascal_minutes_per_liter(self) -> float:
        """
        
        """
        if self.__pascal_minutes_per_liter != None:
            return self.__pascal_minutes_per_liter
        self.__pascal_minutes_per_liter = self.__convert_from_base(FluidResistanceUnits.PascalMinutePerLiter)
        return self.__pascal_minutes_per_liter

    
    @property
    def pascal_seconds_per_milliliter(self) -> float:
        """
        
        """
        if self.__pascal_seconds_per_milliliter != None:
            return self.__pascal_seconds_per_milliliter
        self.__pascal_seconds_per_milliliter = self.__convert_from_base(FluidResistanceUnits.PascalSecondPerMilliliter)
        return self.__pascal_seconds_per_milliliter

    
    @property
    def pascal_minutes_per_milliliter(self) -> float:
        """
        
        """
        if self.__pascal_minutes_per_milliliter != None:
            return self.__pascal_minutes_per_milliliter
        self.__pascal_minutes_per_milliliter = self.__convert_from_base(FluidResistanceUnits.PascalMinutePerMilliliter)
        return self.__pascal_minutes_per_milliliter

    
    @property
    def pascal_seconds_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__pascal_seconds_per_cubic_meter != None:
            return self.__pascal_seconds_per_cubic_meter
        self.__pascal_seconds_per_cubic_meter = self.__convert_from_base(FluidResistanceUnits.PascalSecondPerCubicMeter)
        return self.__pascal_seconds_per_cubic_meter

    
    @property
    def pascal_minutes_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__pascal_minutes_per_cubic_meter != None:
            return self.__pascal_minutes_per_cubic_meter
        self.__pascal_minutes_per_cubic_meter = self.__convert_from_base(FluidResistanceUnits.PascalMinutePerCubicMeter)
        return self.__pascal_minutes_per_cubic_meter

    
    @property
    def pascal_seconds_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__pascal_seconds_per_cubic_centimeter != None:
            return self.__pascal_seconds_per_cubic_centimeter
        self.__pascal_seconds_per_cubic_centimeter = self.__convert_from_base(FluidResistanceUnits.PascalSecondPerCubicCentimeter)
        return self.__pascal_seconds_per_cubic_centimeter

    
    @property
    def pascal_minutes_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__pascal_minutes_per_cubic_centimeter != None:
            return self.__pascal_minutes_per_cubic_centimeter
        self.__pascal_minutes_per_cubic_centimeter = self.__convert_from_base(FluidResistanceUnits.PascalMinutePerCubicCentimeter)
        return self.__pascal_minutes_per_cubic_centimeter

    
    @property
    def dyne_seconds_per_centimeter_to_the_fifth(self) -> float:
        """
        
        """
        if self.__dyne_seconds_per_centimeter_to_the_fifth != None:
            return self.__dyne_seconds_per_centimeter_to_the_fifth
        self.__dyne_seconds_per_centimeter_to_the_fifth = self.__convert_from_base(FluidResistanceUnits.DyneSecondPerCentimeterToTheFifth)
        return self.__dyne_seconds_per_centimeter_to_the_fifth

    
    @property
    def millimeter_mercury_seconds_per_liter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_seconds_per_liter != None:
            return self.__millimeter_mercury_seconds_per_liter
        self.__millimeter_mercury_seconds_per_liter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercurySecondPerLiter)
        return self.__millimeter_mercury_seconds_per_liter

    
    @property
    def millimeter_mercury_minutes_per_liter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_minutes_per_liter != None:
            return self.__millimeter_mercury_minutes_per_liter
        self.__millimeter_mercury_minutes_per_liter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercuryMinutePerLiter)
        return self.__millimeter_mercury_minutes_per_liter

    
    @property
    def millimeter_mercury_seconds_per_milliliter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_seconds_per_milliliter != None:
            return self.__millimeter_mercury_seconds_per_milliliter
        self.__millimeter_mercury_seconds_per_milliliter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercurySecondPerMilliliter)
        return self.__millimeter_mercury_seconds_per_milliliter

    
    @property
    def millimeter_mercury_minutes_per_milliliter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_minutes_per_milliliter != None:
            return self.__millimeter_mercury_minutes_per_milliliter
        self.__millimeter_mercury_minutes_per_milliliter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercuryMinutePerMilliliter)
        return self.__millimeter_mercury_minutes_per_milliliter

    
    @property
    def millimeter_mercury_seconds_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_seconds_per_cubic_centimeter != None:
            return self.__millimeter_mercury_seconds_per_cubic_centimeter
        self.__millimeter_mercury_seconds_per_cubic_centimeter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercurySecondPerCubicCentimeter)
        return self.__millimeter_mercury_seconds_per_cubic_centimeter

    
    @property
    def millimeter_mercury_minutes_per_cubic_centimeter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_minutes_per_cubic_centimeter != None:
            return self.__millimeter_mercury_minutes_per_cubic_centimeter
        self.__millimeter_mercury_minutes_per_cubic_centimeter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercuryMinutePerCubicCentimeter)
        return self.__millimeter_mercury_minutes_per_cubic_centimeter

    
    @property
    def millimeter_mercury_seconds_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_seconds_per_cubic_meter != None:
            return self.__millimeter_mercury_seconds_per_cubic_meter
        self.__millimeter_mercury_seconds_per_cubic_meter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercurySecondPerCubicMeter)
        return self.__millimeter_mercury_seconds_per_cubic_meter

    
    @property
    def millimeter_mercury_minutes_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__millimeter_mercury_minutes_per_cubic_meter != None:
            return self.__millimeter_mercury_minutes_per_cubic_meter
        self.__millimeter_mercury_minutes_per_cubic_meter = self.__convert_from_base(FluidResistanceUnits.MillimeterMercuryMinutePerCubicMeter)
        return self.__millimeter_mercury_minutes_per_cubic_meter

    
    @property
    def wood_units(self) -> float:
        """
        
        """
        if self.__wood_units != None:
            return self.__wood_units
        self.__wood_units = self.__convert_from_base(FluidResistanceUnits.WoodUnit)
        return self.__wood_units

    
    @property
    def megapascal_seconds_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__megapascal_seconds_per_cubic_meter != None:
            return self.__megapascal_seconds_per_cubic_meter
        self.__megapascal_seconds_per_cubic_meter = self.__convert_from_base(FluidResistanceUnits.MegapascalSecondPerCubicMeter)
        return self.__megapascal_seconds_per_cubic_meter

    
    def to_string(self, unit: FluidResistanceUnits = FluidResistanceUnits.PascalSecondPerCubicMeter, fractional_digits: int = None) -> str:
        """
        Format the FluidResistance to a string.
        
        Note: the default format for FluidResistance is PascalSecondPerCubicMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the FluidResistance. Default is 'PascalSecondPerCubicMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == FluidResistanceUnits.PascalSecondPerLiter:
            return f"""{super()._truncate_fraction_digits(self.pascal_seconds_per_liter, fractional_digits)} Pa·s/l"""
        
        if unit == FluidResistanceUnits.PascalMinutePerLiter:
            return f"""{super()._truncate_fraction_digits(self.pascal_minutes_per_liter, fractional_digits)} Pa·min/l"""
        
        if unit == FluidResistanceUnits.PascalSecondPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.pascal_seconds_per_milliliter, fractional_digits)} Pa·s/ml"""
        
        if unit == FluidResistanceUnits.PascalMinutePerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.pascal_minutes_per_milliliter, fractional_digits)} Pa·min/ml"""
        
        if unit == FluidResistanceUnits.PascalSecondPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.pascal_seconds_per_cubic_meter, fractional_digits)} Pa·s/m³"""
        
        if unit == FluidResistanceUnits.PascalMinutePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.pascal_minutes_per_cubic_meter, fractional_digits)} Pa·min/m³"""
        
        if unit == FluidResistanceUnits.PascalSecondPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.pascal_seconds_per_cubic_centimeter, fractional_digits)} Pa·s/cm³"""
        
        if unit == FluidResistanceUnits.PascalMinutePerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.pascal_minutes_per_cubic_centimeter, fractional_digits)} Pa·min/cm³"""
        
        if unit == FluidResistanceUnits.DyneSecondPerCentimeterToTheFifth:
            return f"""{super()._truncate_fraction_digits(self.dyne_seconds_per_centimeter_to_the_fifth, fractional_digits)} dyn·s/cm⁵"""
        
        if unit == FluidResistanceUnits.MillimeterMercurySecondPerLiter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_seconds_per_liter, fractional_digits)} mmHg·s/l"""
        
        if unit == FluidResistanceUnits.MillimeterMercuryMinutePerLiter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_minutes_per_liter, fractional_digits)} mmHg·min/l"""
        
        if unit == FluidResistanceUnits.MillimeterMercurySecondPerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_seconds_per_milliliter, fractional_digits)} mmHg·s/ml"""
        
        if unit == FluidResistanceUnits.MillimeterMercuryMinutePerMilliliter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_minutes_per_milliliter, fractional_digits)} mmHg·min/ml"""
        
        if unit == FluidResistanceUnits.MillimeterMercurySecondPerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_seconds_per_cubic_centimeter, fractional_digits)} mmHg·s/cm³"""
        
        if unit == FluidResistanceUnits.MillimeterMercuryMinutePerCubicCentimeter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_minutes_per_cubic_centimeter, fractional_digits)} mmHg·min/cm³"""
        
        if unit == FluidResistanceUnits.MillimeterMercurySecondPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_seconds_per_cubic_meter, fractional_digits)} mmHg·s/m³"""
        
        if unit == FluidResistanceUnits.MillimeterMercuryMinutePerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.millimeter_mercury_minutes_per_cubic_meter, fractional_digits)} mmHg·min/m³"""
        
        if unit == FluidResistanceUnits.WoodUnit:
            return f"""{super()._truncate_fraction_digits(self.wood_units, fractional_digits)} WU"""
        
        if unit == FluidResistanceUnits.MegapascalSecondPerCubicMeter:
            return f"""{super()._truncate_fraction_digits(self.megapascal_seconds_per_cubic_meter, fractional_digits)} MPa·s/m³"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: FluidResistanceUnits = FluidResistanceUnits.PascalSecondPerCubicMeter) -> str:
        """
        Get FluidResistance unit abbreviation.
        Note! the default abbreviation for FluidResistance is PascalSecondPerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == FluidResistanceUnits.PascalSecondPerLiter:
            return """Pa·s/l"""
        
        if unit_abbreviation == FluidResistanceUnits.PascalMinutePerLiter:
            return """Pa·min/l"""
        
        if unit_abbreviation == FluidResistanceUnits.PascalSecondPerMilliliter:
            return """Pa·s/ml"""
        
        if unit_abbreviation == FluidResistanceUnits.PascalMinutePerMilliliter:
            return """Pa·min/ml"""
        
        if unit_abbreviation == FluidResistanceUnits.PascalSecondPerCubicMeter:
            return """Pa·s/m³"""
        
        if unit_abbreviation == FluidResistanceUnits.PascalMinutePerCubicMeter:
            return """Pa·min/m³"""
        
        if unit_abbreviation == FluidResistanceUnits.PascalSecondPerCubicCentimeter:
            return """Pa·s/cm³"""
        
        if unit_abbreviation == FluidResistanceUnits.PascalMinutePerCubicCentimeter:
            return """Pa·min/cm³"""
        
        if unit_abbreviation == FluidResistanceUnits.DyneSecondPerCentimeterToTheFifth:
            return """dyn·s/cm⁵"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercurySecondPerLiter:
            return """mmHg·s/l"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercuryMinutePerLiter:
            return """mmHg·min/l"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercurySecondPerMilliliter:
            return """mmHg·s/ml"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercuryMinutePerMilliliter:
            return """mmHg·min/ml"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercurySecondPerCubicCentimeter:
            return """mmHg·s/cm³"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercuryMinutePerCubicCentimeter:
            return """mmHg·min/cm³"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercurySecondPerCubicMeter:
            return """mmHg·s/m³"""
        
        if unit_abbreviation == FluidResistanceUnits.MillimeterMercuryMinutePerCubicMeter:
            return """mmHg·min/m³"""
        
        if unit_abbreviation == FluidResistanceUnits.WoodUnit:
            return """WU"""
        
        if unit_abbreviation == FluidResistanceUnits.MegapascalSecondPerCubicMeter:
            return """MPa·s/m³"""
        