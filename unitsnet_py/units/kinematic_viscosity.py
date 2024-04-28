from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class KinematicViscosityUnits(Enum):
        """
            KinematicViscosityUnits enumeration
        """
        
        SquareMeterPerSecond = 'SquareMeterPerSecond'
        """
            
        """
        
        Stokes = 'Stokes'
        """
            
        """
        
        SquareFootPerSecond = 'SquareFootPerSecond'
        """
            
        """
        
        Nanostokes = 'Nanostokes'
        """
            
        """
        
        Microstokes = 'Microstokes'
        """
            
        """
        
        Millistokes = 'Millistokes'
        """
            
        """
        
        Centistokes = 'Centistokes'
        """
            
        """
        
        Decistokes = 'Decistokes'
        """
            
        """
        
        Kilostokes = 'Kilostokes'
        """
            
        """
        

class KinematicViscosityDto:
    """
    A DTO representation of a KinematicViscosity

    Attributes:
        value (float): The value of the KinematicViscosity.
        unit (KinematicViscosityUnits): The specific unit that the KinematicViscosity value is representing.
    """

    def __init__(self, value: float, unit: KinematicViscosityUnits):
        """
        Create a new DTO representation of a KinematicViscosity

        Parameters:
            value (float): The value of the KinematicViscosity.
            unit (KinematicViscosityUnits): The specific unit that the KinematicViscosity value is representing.
        """
        self.value: float = value
        """
        The value of the KinematicViscosity
        """
        self.unit: KinematicViscosityUnits = unit
        """
        The specific unit that the KinematicViscosity value is representing
        """

    def to_json(self):
        """
        Get a KinematicViscosity DTO JSON object representing the current unit.

        :return: JSON object represents KinematicViscosity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterPerSecond"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of KinematicViscosity DTO from a json representation.

        :param data: The KinematicViscosity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterPerSecond"}
        :return: A new instance of KinematicViscosityDto.
        :rtype: KinematicViscosityDto
        """
        return KinematicViscosityDto(value=data["value"], unit=KinematicViscosityUnits(data["unit"]))


class KinematicViscosity(AbstractMeasure):
    """
    The viscosity of a fluid is a measure of its resistance to gradual deformation by shear stress or tensile stress.

    Args:
        value (float): The value.
        from_unit (KinematicViscosityUnits): The KinematicViscosity unit to create from, The default unit is SquareMeterPerSecond
    """
    def __init__(self, value: float, from_unit: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__square_meters_per_second = None
        
        self.__stokes = None
        
        self.__square_feet_per_second = None
        
        self.__nanostokes = None
        
        self.__microstokes = None
        
        self.__millistokes = None
        
        self.__centistokes = None
        
        self.__decistokes = None
        
        self.__kilostokes = None
        

    def convert(self, unit: KinematicViscosityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond) -> KinematicViscosityDto:
        """
        Get a new instance of KinematicViscosity DTO representing the current unit.

        :param hold_in_unit: The specific KinematicViscosity unit to store the KinematicViscosity value in the DTO representation.
        :type hold_in_unit: KinematicViscosityUnits
        :return: A new instance of KinematicViscosityDto.
        :rtype: KinematicViscosityDto
        """
        return KinematicViscosityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond):
        """
        Get a KinematicViscosity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific KinematicViscosity unit to store the KinematicViscosity value in the DTO representation.
        :type hold_in_unit: KinematicViscosityUnits
        :return: JSON object represents KinematicViscosity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SquareMeterPerSecond"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(kinematic_viscosity_dto: KinematicViscosityDto):
        """
        Obtain a new instance of KinematicViscosity from a DTO unit object.

        :param kinematic_viscosity_dto: The KinematicViscosity DTO representation.
        :type kinematic_viscosity_dto: KinematicViscosityDto
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(kinematic_viscosity_dto.value, kinematic_viscosity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of KinematicViscosity from a DTO unit json representation.

        :param data: The KinematicViscosity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SquareMeterPerSecond"}
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity.from_dto(KinematicViscosityDto.from_json(data))

    def __convert_from_base(self, from_unit: KinematicViscosityUnits) -> float:
        value = self._value
        
        if from_unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return (value)
        
        if from_unit == KinematicViscosityUnits.Stokes:
            return (value * 1e4)
        
        if from_unit == KinematicViscosityUnits.SquareFootPerSecond:
            return (value * 10.7639)
        
        if from_unit == KinematicViscosityUnits.Nanostokes:
            return ((value * 1e4) / 1e-09)
        
        if from_unit == KinematicViscosityUnits.Microstokes:
            return ((value * 1e4) / 1e-06)
        
        if from_unit == KinematicViscosityUnits.Millistokes:
            return ((value * 1e4) / 0.001)
        
        if from_unit == KinematicViscosityUnits.Centistokes:
            return ((value * 1e4) / 0.01)
        
        if from_unit == KinematicViscosityUnits.Decistokes:
            return ((value * 1e4) / 0.1)
        
        if from_unit == KinematicViscosityUnits.Kilostokes:
            return ((value * 1e4) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: KinematicViscosityUnits) -> float:
        
        if to_unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return (value)
        
        if to_unit == KinematicViscosityUnits.Stokes:
            return (value / 1e4)
        
        if to_unit == KinematicViscosityUnits.SquareFootPerSecond:
            return (value / 10.7639)
        
        if to_unit == KinematicViscosityUnits.Nanostokes:
            return ((value / 1e4) * 1e-09)
        
        if to_unit == KinematicViscosityUnits.Microstokes:
            return ((value / 1e4) * 1e-06)
        
        if to_unit == KinematicViscosityUnits.Millistokes:
            return ((value / 1e4) * 0.001)
        
        if to_unit == KinematicViscosityUnits.Centistokes:
            return ((value / 1e4) * 0.01)
        
        if to_unit == KinematicViscosityUnits.Decistokes:
            return ((value / 1e4) * 0.1)
        
        if to_unit == KinematicViscosityUnits.Kilostokes:
            return ((value / 1e4) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_square_meters_per_second(square_meters_per_second: float):
        """
        Create a new instance of KinematicViscosity from a value in square_meters_per_second.

        

        :param meters: The KinematicViscosity value in square_meters_per_second.
        :type square_meters_per_second: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(square_meters_per_second, KinematicViscosityUnits.SquareMeterPerSecond)

    
    @staticmethod
    def from_stokes(stokes: float):
        """
        Create a new instance of KinematicViscosity from a value in stokes.

        

        :param meters: The KinematicViscosity value in stokes.
        :type stokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(stokes, KinematicViscosityUnits.Stokes)

    
    @staticmethod
    def from_square_feet_per_second(square_feet_per_second: float):
        """
        Create a new instance of KinematicViscosity from a value in square_feet_per_second.

        

        :param meters: The KinematicViscosity value in square_feet_per_second.
        :type square_feet_per_second: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(square_feet_per_second, KinematicViscosityUnits.SquareFootPerSecond)

    
    @staticmethod
    def from_nanostokes(nanostokes: float):
        """
        Create a new instance of KinematicViscosity from a value in nanostokes.

        

        :param meters: The KinematicViscosity value in nanostokes.
        :type nanostokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(nanostokes, KinematicViscosityUnits.Nanostokes)

    
    @staticmethod
    def from_microstokes(microstokes: float):
        """
        Create a new instance of KinematicViscosity from a value in microstokes.

        

        :param meters: The KinematicViscosity value in microstokes.
        :type microstokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(microstokes, KinematicViscosityUnits.Microstokes)

    
    @staticmethod
    def from_millistokes(millistokes: float):
        """
        Create a new instance of KinematicViscosity from a value in millistokes.

        

        :param meters: The KinematicViscosity value in millistokes.
        :type millistokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(millistokes, KinematicViscosityUnits.Millistokes)

    
    @staticmethod
    def from_centistokes(centistokes: float):
        """
        Create a new instance of KinematicViscosity from a value in centistokes.

        

        :param meters: The KinematicViscosity value in centistokes.
        :type centistokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(centistokes, KinematicViscosityUnits.Centistokes)

    
    @staticmethod
    def from_decistokes(decistokes: float):
        """
        Create a new instance of KinematicViscosity from a value in decistokes.

        

        :param meters: The KinematicViscosity value in decistokes.
        :type decistokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(decistokes, KinematicViscosityUnits.Decistokes)

    
    @staticmethod
    def from_kilostokes(kilostokes: float):
        """
        Create a new instance of KinematicViscosity from a value in kilostokes.

        

        :param meters: The KinematicViscosity value in kilostokes.
        :type kilostokes: float
        :return: A new instance of KinematicViscosity.
        :rtype: KinematicViscosity
        """
        return KinematicViscosity(kilostokes, KinematicViscosityUnits.Kilostokes)

    
    @property
    def square_meters_per_second(self) -> float:
        """
        
        """
        if self.__square_meters_per_second != None:
            return self.__square_meters_per_second
        self.__square_meters_per_second = self.__convert_from_base(KinematicViscosityUnits.SquareMeterPerSecond)
        return self.__square_meters_per_second

    
    @property
    def stokes(self) -> float:
        """
        
        """
        if self.__stokes != None:
            return self.__stokes
        self.__stokes = self.__convert_from_base(KinematicViscosityUnits.Stokes)
        return self.__stokes

    
    @property
    def square_feet_per_second(self) -> float:
        """
        
        """
        if self.__square_feet_per_second != None:
            return self.__square_feet_per_second
        self.__square_feet_per_second = self.__convert_from_base(KinematicViscosityUnits.SquareFootPerSecond)
        return self.__square_feet_per_second

    
    @property
    def nanostokes(self) -> float:
        """
        
        """
        if self.__nanostokes != None:
            return self.__nanostokes
        self.__nanostokes = self.__convert_from_base(KinematicViscosityUnits.Nanostokes)
        return self.__nanostokes

    
    @property
    def microstokes(self) -> float:
        """
        
        """
        if self.__microstokes != None:
            return self.__microstokes
        self.__microstokes = self.__convert_from_base(KinematicViscosityUnits.Microstokes)
        return self.__microstokes

    
    @property
    def millistokes(self) -> float:
        """
        
        """
        if self.__millistokes != None:
            return self.__millistokes
        self.__millistokes = self.__convert_from_base(KinematicViscosityUnits.Millistokes)
        return self.__millistokes

    
    @property
    def centistokes(self) -> float:
        """
        
        """
        if self.__centistokes != None:
            return self.__centistokes
        self.__centistokes = self.__convert_from_base(KinematicViscosityUnits.Centistokes)
        return self.__centistokes

    
    @property
    def decistokes(self) -> float:
        """
        
        """
        if self.__decistokes != None:
            return self.__decistokes
        self.__decistokes = self.__convert_from_base(KinematicViscosityUnits.Decistokes)
        return self.__decistokes

    
    @property
    def kilostokes(self) -> float:
        """
        
        """
        if self.__kilostokes != None:
            return self.__kilostokes
        self.__kilostokes = self.__convert_from_base(KinematicViscosityUnits.Kilostokes)
        return self.__kilostokes

    
    def to_string(self, unit: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond, fractional_digits: int = None) -> str:
        """
        Format the KinematicViscosity to a string.
        
        Note: the default format for KinematicViscosity is SquareMeterPerSecond.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the KinematicViscosity. Default is 'SquareMeterPerSecond'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == KinematicViscosityUnits.SquareMeterPerSecond:
            return f"""{super()._truncate_fraction_digits(self.square_meters_per_second, fractional_digits)} m²/s"""
        
        if unit == KinematicViscosityUnits.Stokes:
            return f"""{super()._truncate_fraction_digits(self.stokes, fractional_digits)} St"""
        
        if unit == KinematicViscosityUnits.SquareFootPerSecond:
            return f"""{super()._truncate_fraction_digits(self.square_feet_per_second, fractional_digits)} ft²/s"""
        
        if unit == KinematicViscosityUnits.Nanostokes:
            return f"""{super()._truncate_fraction_digits(self.nanostokes, fractional_digits)} nSt"""
        
        if unit == KinematicViscosityUnits.Microstokes:
            return f"""{super()._truncate_fraction_digits(self.microstokes, fractional_digits)} μSt"""
        
        if unit == KinematicViscosityUnits.Millistokes:
            return f"""{super()._truncate_fraction_digits(self.millistokes, fractional_digits)} mSt"""
        
        if unit == KinematicViscosityUnits.Centistokes:
            return f"""{super()._truncate_fraction_digits(self.centistokes, fractional_digits)} cSt"""
        
        if unit == KinematicViscosityUnits.Decistokes:
            return f"""{super()._truncate_fraction_digits(self.decistokes, fractional_digits)} dSt"""
        
        if unit == KinematicViscosityUnits.Kilostokes:
            return f"""{super()._truncate_fraction_digits(self.kilostokes, fractional_digits)} kSt"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: KinematicViscosityUnits = KinematicViscosityUnits.SquareMeterPerSecond) -> str:
        """
        Get KinematicViscosity unit abbreviation.
        Note! the default abbreviation for KinematicViscosity is SquareMeterPerSecond.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == KinematicViscosityUnits.SquareMeterPerSecond:
            return """m²/s"""
        
        if unit_abbreviation == KinematicViscosityUnits.Stokes:
            return """St"""
        
        if unit_abbreviation == KinematicViscosityUnits.SquareFootPerSecond:
            return """ft²/s"""
        
        if unit_abbreviation == KinematicViscosityUnits.Nanostokes:
            return """nSt"""
        
        if unit_abbreviation == KinematicViscosityUnits.Microstokes:
            return """μSt"""
        
        if unit_abbreviation == KinematicViscosityUnits.Millistokes:
            return """mSt"""
        
        if unit_abbreviation == KinematicViscosityUnits.Centistokes:
            return """cSt"""
        
        if unit_abbreviation == KinematicViscosityUnits.Decistokes:
            return """dSt"""
        
        if unit_abbreviation == KinematicViscosityUnits.Kilostokes:
            return """kSt"""
        