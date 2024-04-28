from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RotationalStiffnessUnits(Enum):
        """
            RotationalStiffnessUnits enumeration
        """
        
        NewtonMeterPerRadian = 'NewtonMeterPerRadian'
        """
            
        """
        
        PoundForceFootPerDegrees = 'PoundForceFootPerDegrees'
        """
            
        """
        
        KilopoundForceFootPerDegrees = 'KilopoundForceFootPerDegrees'
        """
            
        """
        
        NewtonMillimeterPerDegree = 'NewtonMillimeterPerDegree'
        """
            
        """
        
        NewtonMeterPerDegree = 'NewtonMeterPerDegree'
        """
            
        """
        
        NewtonMillimeterPerRadian = 'NewtonMillimeterPerRadian'
        """
            
        """
        
        PoundForceFeetPerRadian = 'PoundForceFeetPerRadian'
        """
            
        """
        
        KilonewtonMeterPerRadian = 'KilonewtonMeterPerRadian'
        """
            
        """
        
        MeganewtonMeterPerRadian = 'MeganewtonMeterPerRadian'
        """
            
        """
        
        NanonewtonMillimeterPerDegree = 'NanonewtonMillimeterPerDegree'
        """
            
        """
        
        MicronewtonMillimeterPerDegree = 'MicronewtonMillimeterPerDegree'
        """
            
        """
        
        MillinewtonMillimeterPerDegree = 'MillinewtonMillimeterPerDegree'
        """
            
        """
        
        CentinewtonMillimeterPerDegree = 'CentinewtonMillimeterPerDegree'
        """
            
        """
        
        DecinewtonMillimeterPerDegree = 'DecinewtonMillimeterPerDegree'
        """
            
        """
        
        DecanewtonMillimeterPerDegree = 'DecanewtonMillimeterPerDegree'
        """
            
        """
        
        KilonewtonMillimeterPerDegree = 'KilonewtonMillimeterPerDegree'
        """
            
        """
        
        MeganewtonMillimeterPerDegree = 'MeganewtonMillimeterPerDegree'
        """
            
        """
        
        NanonewtonMeterPerDegree = 'NanonewtonMeterPerDegree'
        """
            
        """
        
        MicronewtonMeterPerDegree = 'MicronewtonMeterPerDegree'
        """
            
        """
        
        MillinewtonMeterPerDegree = 'MillinewtonMeterPerDegree'
        """
            
        """
        
        CentinewtonMeterPerDegree = 'CentinewtonMeterPerDegree'
        """
            
        """
        
        DecinewtonMeterPerDegree = 'DecinewtonMeterPerDegree'
        """
            
        """
        
        DecanewtonMeterPerDegree = 'DecanewtonMeterPerDegree'
        """
            
        """
        
        KilonewtonMeterPerDegree = 'KilonewtonMeterPerDegree'
        """
            
        """
        
        MeganewtonMeterPerDegree = 'MeganewtonMeterPerDegree'
        """
            
        """
        
        NanonewtonMillimeterPerRadian = 'NanonewtonMillimeterPerRadian'
        """
            
        """
        
        MicronewtonMillimeterPerRadian = 'MicronewtonMillimeterPerRadian'
        """
            
        """
        
        MillinewtonMillimeterPerRadian = 'MillinewtonMillimeterPerRadian'
        """
            
        """
        
        CentinewtonMillimeterPerRadian = 'CentinewtonMillimeterPerRadian'
        """
            
        """
        
        DecinewtonMillimeterPerRadian = 'DecinewtonMillimeterPerRadian'
        """
            
        """
        
        DecanewtonMillimeterPerRadian = 'DecanewtonMillimeterPerRadian'
        """
            
        """
        
        KilonewtonMillimeterPerRadian = 'KilonewtonMillimeterPerRadian'
        """
            
        """
        
        MeganewtonMillimeterPerRadian = 'MeganewtonMillimeterPerRadian'
        """
            
        """
        

class RotationalStiffnessDto:
    """
    A DTO representation of a RotationalStiffness

    Attributes:
        value (float): The value of the RotationalStiffness.
        unit (RotationalStiffnessUnits): The specific unit that the RotationalStiffness value is representing.
    """

    def __init__(self, value: float, unit: RotationalStiffnessUnits):
        """
        Create a new DTO representation of a RotationalStiffness

        Parameters:
            value (float): The value of the RotationalStiffness.
            unit (RotationalStiffnessUnits): The specific unit that the RotationalStiffness value is representing.
        """
        self.value: float = value
        """
        The value of the RotationalStiffness
        """
        self.unit: RotationalStiffnessUnits = unit
        """
        The specific unit that the RotationalStiffness value is representing
        """

    def to_json(self):
        """
        Get a RotationalStiffness DTO JSON object representing the current unit.

        :return: JSON object represents RotationalStiffness DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonMeterPerRadian"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of RotationalStiffness DTO from a json representation.

        :param data: The RotationalStiffness DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonMeterPerRadian"}
        :return: A new instance of RotationalStiffnessDto.
        :rtype: RotationalStiffnessDto
        """
        return RotationalStiffnessDto(value=data["value"], unit=RotationalStiffnessUnits(data["unit"]))


class RotationalStiffness(AbstractMeasure):
    """
    https://en.wikipedia.org/wiki/Stiffness#Rotational_stiffness

    Args:
        value (float): The value.
        from_unit (RotationalStiffnessUnits): The RotationalStiffness unit to create from, The default unit is NewtonMeterPerRadian
    """
    def __init__(self, value: float, from_unit: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__newton_meters_per_radian = None
        
        self.__pound_force_feet_per_degrees = None
        
        self.__kilopound_force_feet_per_degrees = None
        
        self.__newton_millimeters_per_degree = None
        
        self.__newton_meters_per_degree = None
        
        self.__newton_millimeters_per_radian = None
        
        self.__pound_force_feet_per_radian = None
        
        self.__kilonewton_meters_per_radian = None
        
        self.__meganewton_meters_per_radian = None
        
        self.__nanonewton_millimeters_per_degree = None
        
        self.__micronewton_millimeters_per_degree = None
        
        self.__millinewton_millimeters_per_degree = None
        
        self.__centinewton_millimeters_per_degree = None
        
        self.__decinewton_millimeters_per_degree = None
        
        self.__decanewton_millimeters_per_degree = None
        
        self.__kilonewton_millimeters_per_degree = None
        
        self.__meganewton_millimeters_per_degree = None
        
        self.__nanonewton_meters_per_degree = None
        
        self.__micronewton_meters_per_degree = None
        
        self.__millinewton_meters_per_degree = None
        
        self.__centinewton_meters_per_degree = None
        
        self.__decinewton_meters_per_degree = None
        
        self.__decanewton_meters_per_degree = None
        
        self.__kilonewton_meters_per_degree = None
        
        self.__meganewton_meters_per_degree = None
        
        self.__nanonewton_millimeters_per_radian = None
        
        self.__micronewton_millimeters_per_radian = None
        
        self.__millinewton_millimeters_per_radian = None
        
        self.__centinewton_millimeters_per_radian = None
        
        self.__decinewton_millimeters_per_radian = None
        
        self.__decanewton_millimeters_per_radian = None
        
        self.__kilonewton_millimeters_per_radian = None
        
        self.__meganewton_millimeters_per_radian = None
        

    def convert(self, unit: RotationalStiffnessUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian) -> RotationalStiffnessDto:
        """
        Get a new instance of RotationalStiffness DTO representing the current unit.

        :param hold_in_unit: The specific RotationalStiffness unit to store the RotationalStiffness value in the DTO representation.
        :type hold_in_unit: RotationalStiffnessUnits
        :return: A new instance of RotationalStiffnessDto.
        :rtype: RotationalStiffnessDto
        """
        return RotationalStiffnessDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian):
        """
        Get a RotationalStiffness DTO JSON object representing the current unit.

        :param hold_in_unit: The specific RotationalStiffness unit to store the RotationalStiffness value in the DTO representation.
        :type hold_in_unit: RotationalStiffnessUnits
        :return: JSON object represents RotationalStiffness DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "NewtonMeterPerRadian"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(rotational_stiffness_dto: RotationalStiffnessDto):
        """
        Obtain a new instance of RotationalStiffness from a DTO unit object.

        :param rotational_stiffness_dto: The RotationalStiffness DTO representation.
        :type rotational_stiffness_dto: RotationalStiffnessDto
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(rotational_stiffness_dto.value, rotational_stiffness_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of RotationalStiffness from a DTO unit json representation.

        :param data: The RotationalStiffness DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "NewtonMeterPerRadian"}
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness.from_dto(RotationalStiffnessDto.from_json(data))

    def __convert_from_base(self, from_unit: RotationalStiffnessUnits) -> float:
        value = self._value
        
        if from_unit == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return (value)
        
        if from_unit == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return (value / 77.6826)
        
        if from_unit == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return (value / 77682.6)
        
        if from_unit == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return (value / 180 * math.pi * 1000)
        
        if from_unit == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return (value / (180 / math.pi))
        
        if from_unit == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return (value * 1000)
        
        if from_unit == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return (value / 1.3558179483314)
        
        if from_unit == RotationalStiffnessUnits.KilonewtonMeterPerRadian:
            return ((value) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MeganewtonMeterPerRadian:
            return ((value) / 1000000.0)
        
        if from_unit == RotationalStiffnessUnits.NanonewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1e-09)
        
        if from_unit == RotationalStiffnessUnits.MicronewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1e-06)
        
        if from_unit == RotationalStiffnessUnits.MillinewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 0.001)
        
        if from_unit == RotationalStiffnessUnits.CentinewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 0.01)
        
        if from_unit == RotationalStiffnessUnits.DecinewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 0.1)
        
        if from_unit == RotationalStiffnessUnits.DecanewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 10.0)
        
        if from_unit == RotationalStiffnessUnits.KilonewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MeganewtonMillimeterPerDegree:
            return ((value / 180 * math.pi * 1000) / 1000000.0)
        
        if from_unit == RotationalStiffnessUnits.NanonewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1e-09)
        
        if from_unit == RotationalStiffnessUnits.MicronewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1e-06)
        
        if from_unit == RotationalStiffnessUnits.MillinewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 0.001)
        
        if from_unit == RotationalStiffnessUnits.CentinewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 0.01)
        
        if from_unit == RotationalStiffnessUnits.DecinewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 0.1)
        
        if from_unit == RotationalStiffnessUnits.DecanewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 10.0)
        
        if from_unit == RotationalStiffnessUnits.KilonewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MeganewtonMeterPerDegree:
            return ((value / (180 / math.pi)) / 1000000.0)
        
        if from_unit == RotationalStiffnessUnits.NanonewtonMillimeterPerRadian:
            return ((value * 1000) / 1e-09)
        
        if from_unit == RotationalStiffnessUnits.MicronewtonMillimeterPerRadian:
            return ((value * 1000) / 1e-06)
        
        if from_unit == RotationalStiffnessUnits.MillinewtonMillimeterPerRadian:
            return ((value * 1000) / 0.001)
        
        if from_unit == RotationalStiffnessUnits.CentinewtonMillimeterPerRadian:
            return ((value * 1000) / 0.01)
        
        if from_unit == RotationalStiffnessUnits.DecinewtonMillimeterPerRadian:
            return ((value * 1000) / 0.1)
        
        if from_unit == RotationalStiffnessUnits.DecanewtonMillimeterPerRadian:
            return ((value * 1000) / 10.0)
        
        if from_unit == RotationalStiffnessUnits.KilonewtonMillimeterPerRadian:
            return ((value * 1000) / 1000.0)
        
        if from_unit == RotationalStiffnessUnits.MeganewtonMillimeterPerRadian:
            return ((value * 1000) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RotationalStiffnessUnits) -> float:
        
        if to_unit == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return (value)
        
        if to_unit == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return (value * 77.6826)
        
        if to_unit == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return (value * 77682.6)
        
        if to_unit == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return (value * 180 / math.pi * 0.001)
        
        if to_unit == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return (value * (180 / math.pi))
        
        if to_unit == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return (value * 0.001)
        
        if to_unit == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return (value * 1.3558179483314)
        
        if to_unit == RotationalStiffnessUnits.KilonewtonMeterPerRadian:
            return ((value) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MeganewtonMeterPerRadian:
            return ((value) * 1000000.0)
        
        if to_unit == RotationalStiffnessUnits.NanonewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1e-09)
        
        if to_unit == RotationalStiffnessUnits.MicronewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1e-06)
        
        if to_unit == RotationalStiffnessUnits.MillinewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 0.001)
        
        if to_unit == RotationalStiffnessUnits.CentinewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 0.01)
        
        if to_unit == RotationalStiffnessUnits.DecinewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 0.1)
        
        if to_unit == RotationalStiffnessUnits.DecanewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 10.0)
        
        if to_unit == RotationalStiffnessUnits.KilonewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MeganewtonMillimeterPerDegree:
            return ((value * 180 / math.pi * 0.001) * 1000000.0)
        
        if to_unit == RotationalStiffnessUnits.NanonewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1e-09)
        
        if to_unit == RotationalStiffnessUnits.MicronewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1e-06)
        
        if to_unit == RotationalStiffnessUnits.MillinewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 0.001)
        
        if to_unit == RotationalStiffnessUnits.CentinewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 0.01)
        
        if to_unit == RotationalStiffnessUnits.DecinewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 0.1)
        
        if to_unit == RotationalStiffnessUnits.DecanewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 10.0)
        
        if to_unit == RotationalStiffnessUnits.KilonewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MeganewtonMeterPerDegree:
            return ((value * (180 / math.pi)) * 1000000.0)
        
        if to_unit == RotationalStiffnessUnits.NanonewtonMillimeterPerRadian:
            return ((value * 0.001) * 1e-09)
        
        if to_unit == RotationalStiffnessUnits.MicronewtonMillimeterPerRadian:
            return ((value * 0.001) * 1e-06)
        
        if to_unit == RotationalStiffnessUnits.MillinewtonMillimeterPerRadian:
            return ((value * 0.001) * 0.001)
        
        if to_unit == RotationalStiffnessUnits.CentinewtonMillimeterPerRadian:
            return ((value * 0.001) * 0.01)
        
        if to_unit == RotationalStiffnessUnits.DecinewtonMillimeterPerRadian:
            return ((value * 0.001) * 0.1)
        
        if to_unit == RotationalStiffnessUnits.DecanewtonMillimeterPerRadian:
            return ((value * 0.001) * 10.0)
        
        if to_unit == RotationalStiffnessUnits.KilonewtonMillimeterPerRadian:
            return ((value * 0.001) * 1000.0)
        
        if to_unit == RotationalStiffnessUnits.MeganewtonMillimeterPerRadian:
            return ((value * 0.001) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_newton_meters_per_radian(newton_meters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_meters_per_radian.

        

        :param meters: The RotationalStiffness value in newton_meters_per_radian.
        :type newton_meters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_meters_per_radian, RotationalStiffnessUnits.NewtonMeterPerRadian)

    
    @staticmethod
    def from_pound_force_feet_per_degrees(pound_force_feet_per_degrees: float):
        """
        Create a new instance of RotationalStiffness from a value in pound_force_feet_per_degrees.

        

        :param meters: The RotationalStiffness value in pound_force_feet_per_degrees.
        :type pound_force_feet_per_degrees: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(pound_force_feet_per_degrees, RotationalStiffnessUnits.PoundForceFootPerDegrees)

    
    @staticmethod
    def from_kilopound_force_feet_per_degrees(kilopound_force_feet_per_degrees: float):
        """
        Create a new instance of RotationalStiffness from a value in kilopound_force_feet_per_degrees.

        

        :param meters: The RotationalStiffness value in kilopound_force_feet_per_degrees.
        :type kilopound_force_feet_per_degrees: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilopound_force_feet_per_degrees, RotationalStiffnessUnits.KilopoundForceFootPerDegrees)

    
    @staticmethod
    def from_newton_millimeters_per_degree(newton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in newton_millimeters_per_degree.
        :type newton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_millimeters_per_degree, RotationalStiffnessUnits.NewtonMillimeterPerDegree)

    
    @staticmethod
    def from_newton_meters_per_degree(newton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in newton_meters_per_degree.
        :type newton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_meters_per_degree, RotationalStiffnessUnits.NewtonMeterPerDegree)

    
    @staticmethod
    def from_newton_millimeters_per_radian(newton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in newton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in newton_millimeters_per_radian.
        :type newton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(newton_millimeters_per_radian, RotationalStiffnessUnits.NewtonMillimeterPerRadian)

    
    @staticmethod
    def from_pound_force_feet_per_radian(pound_force_feet_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in pound_force_feet_per_radian.

        

        :param meters: The RotationalStiffness value in pound_force_feet_per_radian.
        :type pound_force_feet_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(pound_force_feet_per_radian, RotationalStiffnessUnits.PoundForceFeetPerRadian)

    
    @staticmethod
    def from_kilonewton_meters_per_radian(kilonewton_meters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in kilonewton_meters_per_radian.

        

        :param meters: The RotationalStiffness value in kilonewton_meters_per_radian.
        :type kilonewton_meters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilonewton_meters_per_radian, RotationalStiffnessUnits.KilonewtonMeterPerRadian)

    
    @staticmethod
    def from_meganewton_meters_per_radian(meganewton_meters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in meganewton_meters_per_radian.

        

        :param meters: The RotationalStiffness value in meganewton_meters_per_radian.
        :type meganewton_meters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(meganewton_meters_per_radian, RotationalStiffnessUnits.MeganewtonMeterPerRadian)

    
    @staticmethod
    def from_nanonewton_millimeters_per_degree(nanonewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in nanonewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in nanonewton_millimeters_per_degree.
        :type nanonewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(nanonewton_millimeters_per_degree, RotationalStiffnessUnits.NanonewtonMillimeterPerDegree)

    
    @staticmethod
    def from_micronewton_millimeters_per_degree(micronewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in micronewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in micronewton_millimeters_per_degree.
        :type micronewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(micronewton_millimeters_per_degree, RotationalStiffnessUnits.MicronewtonMillimeterPerDegree)

    
    @staticmethod
    def from_millinewton_millimeters_per_degree(millinewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in millinewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in millinewton_millimeters_per_degree.
        :type millinewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(millinewton_millimeters_per_degree, RotationalStiffnessUnits.MillinewtonMillimeterPerDegree)

    
    @staticmethod
    def from_centinewton_millimeters_per_degree(centinewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in centinewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in centinewton_millimeters_per_degree.
        :type centinewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(centinewton_millimeters_per_degree, RotationalStiffnessUnits.CentinewtonMillimeterPerDegree)

    
    @staticmethod
    def from_decinewton_millimeters_per_degree(decinewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in decinewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in decinewton_millimeters_per_degree.
        :type decinewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(decinewton_millimeters_per_degree, RotationalStiffnessUnits.DecinewtonMillimeterPerDegree)

    
    @staticmethod
    def from_decanewton_millimeters_per_degree(decanewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in decanewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in decanewton_millimeters_per_degree.
        :type decanewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(decanewton_millimeters_per_degree, RotationalStiffnessUnits.DecanewtonMillimeterPerDegree)

    
    @staticmethod
    def from_kilonewton_millimeters_per_degree(kilonewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in kilonewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in kilonewton_millimeters_per_degree.
        :type kilonewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilonewton_millimeters_per_degree, RotationalStiffnessUnits.KilonewtonMillimeterPerDegree)

    
    @staticmethod
    def from_meganewton_millimeters_per_degree(meganewton_millimeters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in meganewton_millimeters_per_degree.

        

        :param meters: The RotationalStiffness value in meganewton_millimeters_per_degree.
        :type meganewton_millimeters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(meganewton_millimeters_per_degree, RotationalStiffnessUnits.MeganewtonMillimeterPerDegree)

    
    @staticmethod
    def from_nanonewton_meters_per_degree(nanonewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in nanonewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in nanonewton_meters_per_degree.
        :type nanonewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(nanonewton_meters_per_degree, RotationalStiffnessUnits.NanonewtonMeterPerDegree)

    
    @staticmethod
    def from_micronewton_meters_per_degree(micronewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in micronewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in micronewton_meters_per_degree.
        :type micronewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(micronewton_meters_per_degree, RotationalStiffnessUnits.MicronewtonMeterPerDegree)

    
    @staticmethod
    def from_millinewton_meters_per_degree(millinewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in millinewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in millinewton_meters_per_degree.
        :type millinewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(millinewton_meters_per_degree, RotationalStiffnessUnits.MillinewtonMeterPerDegree)

    
    @staticmethod
    def from_centinewton_meters_per_degree(centinewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in centinewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in centinewton_meters_per_degree.
        :type centinewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(centinewton_meters_per_degree, RotationalStiffnessUnits.CentinewtonMeterPerDegree)

    
    @staticmethod
    def from_decinewton_meters_per_degree(decinewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in decinewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in decinewton_meters_per_degree.
        :type decinewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(decinewton_meters_per_degree, RotationalStiffnessUnits.DecinewtonMeterPerDegree)

    
    @staticmethod
    def from_decanewton_meters_per_degree(decanewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in decanewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in decanewton_meters_per_degree.
        :type decanewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(decanewton_meters_per_degree, RotationalStiffnessUnits.DecanewtonMeterPerDegree)

    
    @staticmethod
    def from_kilonewton_meters_per_degree(kilonewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in kilonewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in kilonewton_meters_per_degree.
        :type kilonewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilonewton_meters_per_degree, RotationalStiffnessUnits.KilonewtonMeterPerDegree)

    
    @staticmethod
    def from_meganewton_meters_per_degree(meganewton_meters_per_degree: float):
        """
        Create a new instance of RotationalStiffness from a value in meganewton_meters_per_degree.

        

        :param meters: The RotationalStiffness value in meganewton_meters_per_degree.
        :type meganewton_meters_per_degree: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(meganewton_meters_per_degree, RotationalStiffnessUnits.MeganewtonMeterPerDegree)

    
    @staticmethod
    def from_nanonewton_millimeters_per_radian(nanonewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in nanonewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in nanonewton_millimeters_per_radian.
        :type nanonewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(nanonewton_millimeters_per_radian, RotationalStiffnessUnits.NanonewtonMillimeterPerRadian)

    
    @staticmethod
    def from_micronewton_millimeters_per_radian(micronewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in micronewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in micronewton_millimeters_per_radian.
        :type micronewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(micronewton_millimeters_per_radian, RotationalStiffnessUnits.MicronewtonMillimeterPerRadian)

    
    @staticmethod
    def from_millinewton_millimeters_per_radian(millinewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in millinewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in millinewton_millimeters_per_radian.
        :type millinewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(millinewton_millimeters_per_radian, RotationalStiffnessUnits.MillinewtonMillimeterPerRadian)

    
    @staticmethod
    def from_centinewton_millimeters_per_radian(centinewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in centinewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in centinewton_millimeters_per_radian.
        :type centinewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(centinewton_millimeters_per_radian, RotationalStiffnessUnits.CentinewtonMillimeterPerRadian)

    
    @staticmethod
    def from_decinewton_millimeters_per_radian(decinewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in decinewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in decinewton_millimeters_per_radian.
        :type decinewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(decinewton_millimeters_per_radian, RotationalStiffnessUnits.DecinewtonMillimeterPerRadian)

    
    @staticmethod
    def from_decanewton_millimeters_per_radian(decanewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in decanewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in decanewton_millimeters_per_radian.
        :type decanewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(decanewton_millimeters_per_radian, RotationalStiffnessUnits.DecanewtonMillimeterPerRadian)

    
    @staticmethod
    def from_kilonewton_millimeters_per_radian(kilonewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in kilonewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in kilonewton_millimeters_per_radian.
        :type kilonewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(kilonewton_millimeters_per_radian, RotationalStiffnessUnits.KilonewtonMillimeterPerRadian)

    
    @staticmethod
    def from_meganewton_millimeters_per_radian(meganewton_millimeters_per_radian: float):
        """
        Create a new instance of RotationalStiffness from a value in meganewton_millimeters_per_radian.

        

        :param meters: The RotationalStiffness value in meganewton_millimeters_per_radian.
        :type meganewton_millimeters_per_radian: float
        :return: A new instance of RotationalStiffness.
        :rtype: RotationalStiffness
        """
        return RotationalStiffness(meganewton_millimeters_per_radian, RotationalStiffnessUnits.MeganewtonMillimeterPerRadian)

    
    @property
    def newton_meters_per_radian(self) -> float:
        """
        
        """
        if self.__newton_meters_per_radian != None:
            return self.__newton_meters_per_radian
        self.__newton_meters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.NewtonMeterPerRadian)
        return self.__newton_meters_per_radian

    
    @property
    def pound_force_feet_per_degrees(self) -> float:
        """
        
        """
        if self.__pound_force_feet_per_degrees != None:
            return self.__pound_force_feet_per_degrees
        self.__pound_force_feet_per_degrees = self.__convert_from_base(RotationalStiffnessUnits.PoundForceFootPerDegrees)
        return self.__pound_force_feet_per_degrees

    
    @property
    def kilopound_force_feet_per_degrees(self) -> float:
        """
        
        """
        if self.__kilopound_force_feet_per_degrees != None:
            return self.__kilopound_force_feet_per_degrees
        self.__kilopound_force_feet_per_degrees = self.__convert_from_base(RotationalStiffnessUnits.KilopoundForceFootPerDegrees)
        return self.__kilopound_force_feet_per_degrees

    
    @property
    def newton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__newton_millimeters_per_degree != None:
            return self.__newton_millimeters_per_degree
        self.__newton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NewtonMillimeterPerDegree)
        return self.__newton_millimeters_per_degree

    
    @property
    def newton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__newton_meters_per_degree != None:
            return self.__newton_meters_per_degree
        self.__newton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NewtonMeterPerDegree)
        return self.__newton_meters_per_degree

    
    @property
    def newton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__newton_millimeters_per_radian != None:
            return self.__newton_millimeters_per_radian
        self.__newton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.NewtonMillimeterPerRadian)
        return self.__newton_millimeters_per_radian

    
    @property
    def pound_force_feet_per_radian(self) -> float:
        """
        
        """
        if self.__pound_force_feet_per_radian != None:
            return self.__pound_force_feet_per_radian
        self.__pound_force_feet_per_radian = self.__convert_from_base(RotationalStiffnessUnits.PoundForceFeetPerRadian)
        return self.__pound_force_feet_per_radian

    
    @property
    def kilonewton_meters_per_radian(self) -> float:
        """
        
        """
        if self.__kilonewton_meters_per_radian != None:
            return self.__kilonewton_meters_per_radian
        self.__kilonewton_meters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.KilonewtonMeterPerRadian)
        return self.__kilonewton_meters_per_radian

    
    @property
    def meganewton_meters_per_radian(self) -> float:
        """
        
        """
        if self.__meganewton_meters_per_radian != None:
            return self.__meganewton_meters_per_radian
        self.__meganewton_meters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MeganewtonMeterPerRadian)
        return self.__meganewton_meters_per_radian

    
    @property
    def nanonewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__nanonewton_millimeters_per_degree != None:
            return self.__nanonewton_millimeters_per_degree
        self.__nanonewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NanonewtonMillimeterPerDegree)
        return self.__nanonewton_millimeters_per_degree

    
    @property
    def micronewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__micronewton_millimeters_per_degree != None:
            return self.__micronewton_millimeters_per_degree
        self.__micronewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MicronewtonMillimeterPerDegree)
        return self.__micronewton_millimeters_per_degree

    
    @property
    def millinewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__millinewton_millimeters_per_degree != None:
            return self.__millinewton_millimeters_per_degree
        self.__millinewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MillinewtonMillimeterPerDegree)
        return self.__millinewton_millimeters_per_degree

    
    @property
    def centinewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__centinewton_millimeters_per_degree != None:
            return self.__centinewton_millimeters_per_degree
        self.__centinewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.CentinewtonMillimeterPerDegree)
        return self.__centinewton_millimeters_per_degree

    
    @property
    def decinewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__decinewton_millimeters_per_degree != None:
            return self.__decinewton_millimeters_per_degree
        self.__decinewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DecinewtonMillimeterPerDegree)
        return self.__decinewton_millimeters_per_degree

    
    @property
    def decanewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__decanewton_millimeters_per_degree != None:
            return self.__decanewton_millimeters_per_degree
        self.__decanewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DecanewtonMillimeterPerDegree)
        return self.__decanewton_millimeters_per_degree

    
    @property
    def kilonewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__kilonewton_millimeters_per_degree != None:
            return self.__kilonewton_millimeters_per_degree
        self.__kilonewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.KilonewtonMillimeterPerDegree)
        return self.__kilonewton_millimeters_per_degree

    
    @property
    def meganewton_millimeters_per_degree(self) -> float:
        """
        
        """
        if self.__meganewton_millimeters_per_degree != None:
            return self.__meganewton_millimeters_per_degree
        self.__meganewton_millimeters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MeganewtonMillimeterPerDegree)
        return self.__meganewton_millimeters_per_degree

    
    @property
    def nanonewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__nanonewton_meters_per_degree != None:
            return self.__nanonewton_meters_per_degree
        self.__nanonewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.NanonewtonMeterPerDegree)
        return self.__nanonewton_meters_per_degree

    
    @property
    def micronewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__micronewton_meters_per_degree != None:
            return self.__micronewton_meters_per_degree
        self.__micronewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MicronewtonMeterPerDegree)
        return self.__micronewton_meters_per_degree

    
    @property
    def millinewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__millinewton_meters_per_degree != None:
            return self.__millinewton_meters_per_degree
        self.__millinewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MillinewtonMeterPerDegree)
        return self.__millinewton_meters_per_degree

    
    @property
    def centinewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__centinewton_meters_per_degree != None:
            return self.__centinewton_meters_per_degree
        self.__centinewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.CentinewtonMeterPerDegree)
        return self.__centinewton_meters_per_degree

    
    @property
    def decinewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__decinewton_meters_per_degree != None:
            return self.__decinewton_meters_per_degree
        self.__decinewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DecinewtonMeterPerDegree)
        return self.__decinewton_meters_per_degree

    
    @property
    def decanewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__decanewton_meters_per_degree != None:
            return self.__decanewton_meters_per_degree
        self.__decanewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.DecanewtonMeterPerDegree)
        return self.__decanewton_meters_per_degree

    
    @property
    def kilonewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__kilonewton_meters_per_degree != None:
            return self.__kilonewton_meters_per_degree
        self.__kilonewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.KilonewtonMeterPerDegree)
        return self.__kilonewton_meters_per_degree

    
    @property
    def meganewton_meters_per_degree(self) -> float:
        """
        
        """
        if self.__meganewton_meters_per_degree != None:
            return self.__meganewton_meters_per_degree
        self.__meganewton_meters_per_degree = self.__convert_from_base(RotationalStiffnessUnits.MeganewtonMeterPerDegree)
        return self.__meganewton_meters_per_degree

    
    @property
    def nanonewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__nanonewton_millimeters_per_radian != None:
            return self.__nanonewton_millimeters_per_radian
        self.__nanonewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.NanonewtonMillimeterPerRadian)
        return self.__nanonewton_millimeters_per_radian

    
    @property
    def micronewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__micronewton_millimeters_per_radian != None:
            return self.__micronewton_millimeters_per_radian
        self.__micronewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MicronewtonMillimeterPerRadian)
        return self.__micronewton_millimeters_per_radian

    
    @property
    def millinewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__millinewton_millimeters_per_radian != None:
            return self.__millinewton_millimeters_per_radian
        self.__millinewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MillinewtonMillimeterPerRadian)
        return self.__millinewton_millimeters_per_radian

    
    @property
    def centinewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__centinewton_millimeters_per_radian != None:
            return self.__centinewton_millimeters_per_radian
        self.__centinewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.CentinewtonMillimeterPerRadian)
        return self.__centinewton_millimeters_per_radian

    
    @property
    def decinewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__decinewton_millimeters_per_radian != None:
            return self.__decinewton_millimeters_per_radian
        self.__decinewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.DecinewtonMillimeterPerRadian)
        return self.__decinewton_millimeters_per_radian

    
    @property
    def decanewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__decanewton_millimeters_per_radian != None:
            return self.__decanewton_millimeters_per_radian
        self.__decanewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.DecanewtonMillimeterPerRadian)
        return self.__decanewton_millimeters_per_radian

    
    @property
    def kilonewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__kilonewton_millimeters_per_radian != None:
            return self.__kilonewton_millimeters_per_radian
        self.__kilonewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.KilonewtonMillimeterPerRadian)
        return self.__kilonewton_millimeters_per_radian

    
    @property
    def meganewton_millimeters_per_radian(self) -> float:
        """
        
        """
        if self.__meganewton_millimeters_per_radian != None:
            return self.__meganewton_millimeters_per_radian
        self.__meganewton_millimeters_per_radian = self.__convert_from_base(RotationalStiffnessUnits.MeganewtonMillimeterPerRadian)
        return self.__meganewton_millimeters_per_radian

    
    def to_string(self, unit: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian, fractional_digits: int = None) -> str:
        """
        Format the RotationalStiffness to a string.
        
        Note: the default format for RotationalStiffness is NewtonMeterPerRadian.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the RotationalStiffness. Default is 'NewtonMeterPerRadian'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.newton_meters_per_radian, fractional_digits)} N·m/rad"""
        
        if unit == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return f"""{super()._truncate_fraction_digits(self.pound_force_feet_per_degrees, fractional_digits)} lbf·ft/deg"""
        
        if unit == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return f"""{super()._truncate_fraction_digits(self.kilopound_force_feet_per_degrees, fractional_digits)} kipf·ft/°"""
        
        if unit == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.newton_millimeters_per_degree, fractional_digits)} N·mm/deg"""
        
        if unit == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.newton_meters_per_degree, fractional_digits)} N·m/deg"""
        
        if unit == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.newton_millimeters_per_radian, fractional_digits)} N·mm/rad"""
        
        if unit == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return f"""{super()._truncate_fraction_digits(self.pound_force_feet_per_radian, fractional_digits)} lbf·ft/rad"""
        
        if unit == RotationalStiffnessUnits.KilonewtonMeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.kilonewton_meters_per_radian, fractional_digits)} kN·m/rad"""
        
        if unit == RotationalStiffnessUnits.MeganewtonMeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.meganewton_meters_per_radian, fractional_digits)} MN·m/rad"""
        
        if unit == RotationalStiffnessUnits.NanonewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.nanonewton_millimeters_per_degree, fractional_digits)} nN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.MicronewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.micronewton_millimeters_per_degree, fractional_digits)} μN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.MillinewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.millinewton_millimeters_per_degree, fractional_digits)} mN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.CentinewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.centinewton_millimeters_per_degree, fractional_digits)} cN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.DecinewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.decinewton_millimeters_per_degree, fractional_digits)} dN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.DecanewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.decanewton_millimeters_per_degree, fractional_digits)} daN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.KilonewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.kilonewton_millimeters_per_degree, fractional_digits)} kN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.MeganewtonMillimeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.meganewton_millimeters_per_degree, fractional_digits)} MN·mm/deg"""
        
        if unit == RotationalStiffnessUnits.NanonewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.nanonewton_meters_per_degree, fractional_digits)} nN·m/deg"""
        
        if unit == RotationalStiffnessUnits.MicronewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.micronewton_meters_per_degree, fractional_digits)} μN·m/deg"""
        
        if unit == RotationalStiffnessUnits.MillinewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.millinewton_meters_per_degree, fractional_digits)} mN·m/deg"""
        
        if unit == RotationalStiffnessUnits.CentinewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.centinewton_meters_per_degree, fractional_digits)} cN·m/deg"""
        
        if unit == RotationalStiffnessUnits.DecinewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.decinewton_meters_per_degree, fractional_digits)} dN·m/deg"""
        
        if unit == RotationalStiffnessUnits.DecanewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.decanewton_meters_per_degree, fractional_digits)} daN·m/deg"""
        
        if unit == RotationalStiffnessUnits.KilonewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.kilonewton_meters_per_degree, fractional_digits)} kN·m/deg"""
        
        if unit == RotationalStiffnessUnits.MeganewtonMeterPerDegree:
            return f"""{super()._truncate_fraction_digits(self.meganewton_meters_per_degree, fractional_digits)} MN·m/deg"""
        
        if unit == RotationalStiffnessUnits.NanonewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.nanonewton_millimeters_per_radian, fractional_digits)} nN·mm/rad"""
        
        if unit == RotationalStiffnessUnits.MicronewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.micronewton_millimeters_per_radian, fractional_digits)} μN·mm/rad"""
        
        if unit == RotationalStiffnessUnits.MillinewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.millinewton_millimeters_per_radian, fractional_digits)} mN·mm/rad"""
        
        if unit == RotationalStiffnessUnits.CentinewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.centinewton_millimeters_per_radian, fractional_digits)} cN·mm/rad"""
        
        if unit == RotationalStiffnessUnits.DecinewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.decinewton_millimeters_per_radian, fractional_digits)} dN·mm/rad"""
        
        if unit == RotationalStiffnessUnits.DecanewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.decanewton_millimeters_per_radian, fractional_digits)} daN·mm/rad"""
        
        if unit == RotationalStiffnessUnits.KilonewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.kilonewton_millimeters_per_radian, fractional_digits)} kN·mm/rad"""
        
        if unit == RotationalStiffnessUnits.MeganewtonMillimeterPerRadian:
            return f"""{super()._truncate_fraction_digits(self.meganewton_millimeters_per_radian, fractional_digits)} MN·mm/rad"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RotationalStiffnessUnits = RotationalStiffnessUnits.NewtonMeterPerRadian) -> str:
        """
        Get RotationalStiffness unit abbreviation.
        Note! the default abbreviation for RotationalStiffness is NewtonMeterPerRadian.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMeterPerRadian:
            return """N·m/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.PoundForceFootPerDegrees:
            return """lbf·ft/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KilopoundForceFootPerDegrees:
            return """kipf·ft/°"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMillimeterPerDegree:
            return """N·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMeterPerDegree:
            return """N·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NewtonMillimeterPerRadian:
            return """N·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.PoundForceFeetPerRadian:
            return """lbf·ft/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KilonewtonMeterPerRadian:
            return """kN·m/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MeganewtonMeterPerRadian:
            return """MN·m/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NanonewtonMillimeterPerDegree:
            return """nN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MicronewtonMillimeterPerDegree:
            return """μN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MillinewtonMillimeterPerDegree:
            return """mN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.CentinewtonMillimeterPerDegree:
            return """cN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecinewtonMillimeterPerDegree:
            return """dN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecanewtonMillimeterPerDegree:
            return """daN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KilonewtonMillimeterPerDegree:
            return """kN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MeganewtonMillimeterPerDegree:
            return """MN·mm/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NanonewtonMeterPerDegree:
            return """nN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MicronewtonMeterPerDegree:
            return """μN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MillinewtonMeterPerDegree:
            return """mN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.CentinewtonMeterPerDegree:
            return """cN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecinewtonMeterPerDegree:
            return """dN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecanewtonMeterPerDegree:
            return """daN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KilonewtonMeterPerDegree:
            return """kN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MeganewtonMeterPerDegree:
            return """MN·m/deg"""
        
        if unit_abbreviation == RotationalStiffnessUnits.NanonewtonMillimeterPerRadian:
            return """nN·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MicronewtonMillimeterPerRadian:
            return """μN·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MillinewtonMillimeterPerRadian:
            return """mN·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.CentinewtonMillimeterPerRadian:
            return """cN·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecinewtonMillimeterPerRadian:
            return """dN·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.DecanewtonMillimeterPerRadian:
            return """daN·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.KilonewtonMillimeterPerRadian:
            return """kN·mm/rad"""
        
        if unit_abbreviation == RotationalStiffnessUnits.MeganewtonMillimeterPerRadian:
            return """MN·mm/rad"""
        