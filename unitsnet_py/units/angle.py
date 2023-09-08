from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AngleUnits(Enum):
        """
            AngleUnits enumeration
        """
        
        Radian = 'radian'
        """
            
        """
        
        Degree = 'degree'
        """
            
        """
        
        Arcminute = 'arcminute'
        """
            
        """
        
        Arcsecond = 'arcsecond'
        """
            
        """
        
        Gradian = 'gradian'
        """
            
        """
        
        NatoMil = 'nato_mil'
        """
            
        """
        
        Revolution = 'revolution'
        """
            
        """
        
        Tilt = 'tilt'
        """
            
        """
        
        Nanoradian = 'nanoradian'
        """
            
        """
        
        Microradian = 'microradian'
        """
            
        """
        
        Milliradian = 'milliradian'
        """
            
        """
        
        Centiradian = 'centiradian'
        """
            
        """
        
        Deciradian = 'deciradian'
        """
            
        """
        
        Nanodegree = 'nanodegree'
        """
            
        """
        
        Microdegree = 'microdegree'
        """
            
        """
        
        Millidegree = 'millidegree'
        """
            
        """
        

class Angle(AbstractMeasure):
    """
    In geometry, an angle is the figure formed by two rays, called the sides of the angle, sharing a common endpoint, called the vertex of the angle.

    Args:
        value (float): The value.
        from_unit (AngleUnits): The Angle unit to create from, The default unit is Degree
    """
    def __init__(self, value: float, from_unit: AngleUnits = AngleUnits.Degree):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__radians = None
        
        self.__degrees = None
        
        self.__arcminutes = None
        
        self.__arcseconds = None
        
        self.__gradians = None
        
        self.__nato_mils = None
        
        self.__revolutions = None
        
        self.__tilt = None
        
        self.__nanoradians = None
        
        self.__microradians = None
        
        self.__milliradians = None
        
        self.__centiradians = None
        
        self.__deciradians = None
        
        self.__nanodegrees = None
        
        self.__microdegrees = None
        
        self.__millidegrees = None
        

    def convert(self, unit: AngleUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: AngleUnits) -> float:
        value = self._value
        
        if from_unit == AngleUnits.Radian:
            return (value / 180 * math.pi)
        
        if from_unit == AngleUnits.Degree:
            return (value)
        
        if from_unit == AngleUnits.Arcminute:
            return (value * 60)
        
        if from_unit == AngleUnits.Arcsecond:
            return (value * 3600)
        
        if from_unit == AngleUnits.Gradian:
            return (value / 0.9)
        
        if from_unit == AngleUnits.NatoMil:
            return (value * 160 / 9)
        
        if from_unit == AngleUnits.Revolution:
            return (value / 360)
        
        if from_unit == AngleUnits.Tilt:
            return (math.sin(value / 180 * math.pi))
        
        if from_unit == AngleUnits.Nanoradian:
            return ((value / 180 * math.pi) / 1e-09)
        
        if from_unit == AngleUnits.Microradian:
            return ((value / 180 * math.pi) / 1e-06)
        
        if from_unit == AngleUnits.Milliradian:
            return ((value / 180 * math.pi) / 0.001)
        
        if from_unit == AngleUnits.Centiradian:
            return ((value / 180 * math.pi) / 0.01)
        
        if from_unit == AngleUnits.Deciradian:
            return ((value / 180 * math.pi) / 0.1)
        
        if from_unit == AngleUnits.Nanodegree:
            return ((value) / 1e-09)
        
        if from_unit == AngleUnits.Microdegree:
            return ((value) / 1e-06)
        
        if from_unit == AngleUnits.Millidegree:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AngleUnits) -> float:
        
        if to_unit == AngleUnits.Radian:
            return (value * 180 / math.pi)
        
        if to_unit == AngleUnits.Degree:
            return (value)
        
        if to_unit == AngleUnits.Arcminute:
            return (value / 60)
        
        if to_unit == AngleUnits.Arcsecond:
            return (value / 3600)
        
        if to_unit == AngleUnits.Gradian:
            return (value * 0.9)
        
        if to_unit == AngleUnits.NatoMil:
            return (value * 9 / 160)
        
        if to_unit == AngleUnits.Revolution:
            return (value * 360)
        
        if to_unit == AngleUnits.Tilt:
            return (math.asin(value) * 180 / math.pi)
        
        if to_unit == AngleUnits.Nanoradian:
            return ((value * 180 / math.pi) * 1e-09)
        
        if to_unit == AngleUnits.Microradian:
            return ((value * 180 / math.pi) * 1e-06)
        
        if to_unit == AngleUnits.Milliradian:
            return ((value * 180 / math.pi) * 0.001)
        
        if to_unit == AngleUnits.Centiradian:
            return ((value * 180 / math.pi) * 0.01)
        
        if to_unit == AngleUnits.Deciradian:
            return ((value * 180 / math.pi) * 0.1)
        
        if to_unit == AngleUnits.Nanodegree:
            return ((value) * 1e-09)
        
        if to_unit == AngleUnits.Microdegree:
            return ((value) * 1e-06)
        
        if to_unit == AngleUnits.Millidegree:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_radians(radians: float):
        """
        Create a new instance of Angle from a value in radians.

        

        :param meters: The Angle value in radians.
        :type radians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(radians, AngleUnits.Radian)

    
    @staticmethod
    def from_degrees(degrees: float):
        """
        Create a new instance of Angle from a value in degrees.

        

        :param meters: The Angle value in degrees.
        :type degrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(degrees, AngleUnits.Degree)

    
    @staticmethod
    def from_arcminutes(arcminutes: float):
        """
        Create a new instance of Angle from a value in arcminutes.

        

        :param meters: The Angle value in arcminutes.
        :type arcminutes: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(arcminutes, AngleUnits.Arcminute)

    
    @staticmethod
    def from_arcseconds(arcseconds: float):
        """
        Create a new instance of Angle from a value in arcseconds.

        

        :param meters: The Angle value in arcseconds.
        :type arcseconds: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(arcseconds, AngleUnits.Arcsecond)

    
    @staticmethod
    def from_gradians(gradians: float):
        """
        Create a new instance of Angle from a value in gradians.

        

        :param meters: The Angle value in gradians.
        :type gradians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(gradians, AngleUnits.Gradian)

    
    @staticmethod
    def from_nato_mils(nato_mils: float):
        """
        Create a new instance of Angle from a value in nato_mils.

        

        :param meters: The Angle value in nato_mils.
        :type nato_mils: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(nato_mils, AngleUnits.NatoMil)

    
    @staticmethod
    def from_revolutions(revolutions: float):
        """
        Create a new instance of Angle from a value in revolutions.

        

        :param meters: The Angle value in revolutions.
        :type revolutions: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(revolutions, AngleUnits.Revolution)

    
    @staticmethod
    def from_tilt(tilt: float):
        """
        Create a new instance of Angle from a value in tilt.

        

        :param meters: The Angle value in tilt.
        :type tilt: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(tilt, AngleUnits.Tilt)

    
    @staticmethod
    def from_nanoradians(nanoradians: float):
        """
        Create a new instance of Angle from a value in nanoradians.

        

        :param meters: The Angle value in nanoradians.
        :type nanoradians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(nanoradians, AngleUnits.Nanoradian)

    
    @staticmethod
    def from_microradians(microradians: float):
        """
        Create a new instance of Angle from a value in microradians.

        

        :param meters: The Angle value in microradians.
        :type microradians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(microradians, AngleUnits.Microradian)

    
    @staticmethod
    def from_milliradians(milliradians: float):
        """
        Create a new instance of Angle from a value in milliradians.

        

        :param meters: The Angle value in milliradians.
        :type milliradians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(milliradians, AngleUnits.Milliradian)

    
    @staticmethod
    def from_centiradians(centiradians: float):
        """
        Create a new instance of Angle from a value in centiradians.

        

        :param meters: The Angle value in centiradians.
        :type centiradians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(centiradians, AngleUnits.Centiradian)

    
    @staticmethod
    def from_deciradians(deciradians: float):
        """
        Create a new instance of Angle from a value in deciradians.

        

        :param meters: The Angle value in deciradians.
        :type deciradians: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(deciradians, AngleUnits.Deciradian)

    
    @staticmethod
    def from_nanodegrees(nanodegrees: float):
        """
        Create a new instance of Angle from a value in nanodegrees.

        

        :param meters: The Angle value in nanodegrees.
        :type nanodegrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(nanodegrees, AngleUnits.Nanodegree)

    
    @staticmethod
    def from_microdegrees(microdegrees: float):
        """
        Create a new instance of Angle from a value in microdegrees.

        

        :param meters: The Angle value in microdegrees.
        :type microdegrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(microdegrees, AngleUnits.Microdegree)

    
    @staticmethod
    def from_millidegrees(millidegrees: float):
        """
        Create a new instance of Angle from a value in millidegrees.

        

        :param meters: The Angle value in millidegrees.
        :type millidegrees: float
        :return: A new instance of Angle.
        :rtype: Angle
        """
        return Angle(millidegrees, AngleUnits.Millidegree)

    
    @property
    def radians(self) -> float:
        """
        
        """
        if self.__radians != None:
            return self.__radians
        self.__radians = self.__convert_from_base(AngleUnits.Radian)
        return self.__radians

    
    @property
    def degrees(self) -> float:
        """
        
        """
        if self.__degrees != None:
            return self.__degrees
        self.__degrees = self.__convert_from_base(AngleUnits.Degree)
        return self.__degrees

    
    @property
    def arcminutes(self) -> float:
        """
        
        """
        if self.__arcminutes != None:
            return self.__arcminutes
        self.__arcminutes = self.__convert_from_base(AngleUnits.Arcminute)
        return self.__arcminutes

    
    @property
    def arcseconds(self) -> float:
        """
        
        """
        if self.__arcseconds != None:
            return self.__arcseconds
        self.__arcseconds = self.__convert_from_base(AngleUnits.Arcsecond)
        return self.__arcseconds

    
    @property
    def gradians(self) -> float:
        """
        
        """
        if self.__gradians != None:
            return self.__gradians
        self.__gradians = self.__convert_from_base(AngleUnits.Gradian)
        return self.__gradians

    
    @property
    def nato_mils(self) -> float:
        """
        
        """
        if self.__nato_mils != None:
            return self.__nato_mils
        self.__nato_mils = self.__convert_from_base(AngleUnits.NatoMil)
        return self.__nato_mils

    
    @property
    def revolutions(self) -> float:
        """
        
        """
        if self.__revolutions != None:
            return self.__revolutions
        self.__revolutions = self.__convert_from_base(AngleUnits.Revolution)
        return self.__revolutions

    
    @property
    def tilt(self) -> float:
        """
        
        """
        if self.__tilt != None:
            return self.__tilt
        self.__tilt = self.__convert_from_base(AngleUnits.Tilt)
        return self.__tilt

    
    @property
    def nanoradians(self) -> float:
        """
        
        """
        if self.__nanoradians != None:
            return self.__nanoradians
        self.__nanoradians = self.__convert_from_base(AngleUnits.Nanoradian)
        return self.__nanoradians

    
    @property
    def microradians(self) -> float:
        """
        
        """
        if self.__microradians != None:
            return self.__microradians
        self.__microradians = self.__convert_from_base(AngleUnits.Microradian)
        return self.__microradians

    
    @property
    def milliradians(self) -> float:
        """
        
        """
        if self.__milliradians != None:
            return self.__milliradians
        self.__milliradians = self.__convert_from_base(AngleUnits.Milliradian)
        return self.__milliradians

    
    @property
    def centiradians(self) -> float:
        """
        
        """
        if self.__centiradians != None:
            return self.__centiradians
        self.__centiradians = self.__convert_from_base(AngleUnits.Centiradian)
        return self.__centiradians

    
    @property
    def deciradians(self) -> float:
        """
        
        """
        if self.__deciradians != None:
            return self.__deciradians
        self.__deciradians = self.__convert_from_base(AngleUnits.Deciradian)
        return self.__deciradians

    
    @property
    def nanodegrees(self) -> float:
        """
        
        """
        if self.__nanodegrees != None:
            return self.__nanodegrees
        self.__nanodegrees = self.__convert_from_base(AngleUnits.Nanodegree)
        return self.__nanodegrees

    
    @property
    def microdegrees(self) -> float:
        """
        
        """
        if self.__microdegrees != None:
            return self.__microdegrees
        self.__microdegrees = self.__convert_from_base(AngleUnits.Microdegree)
        return self.__microdegrees

    
    @property
    def millidegrees(self) -> float:
        """
        
        """
        if self.__millidegrees != None:
            return self.__millidegrees
        self.__millidegrees = self.__convert_from_base(AngleUnits.Millidegree)
        return self.__millidegrees

    
    def to_string(self, unit: AngleUnits = AngleUnits.Degree) -> str:
        """
        Format the Angle to string.
        Note! the default format for Angle is Degree.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AngleUnits.Radian:
            return f"""{self.radians} rad"""
        
        if unit == AngleUnits.Degree:
            return f"""{self.degrees} °"""
        
        if unit == AngleUnits.Arcminute:
            return f"""{self.arcminutes} '"""
        
        if unit == AngleUnits.Arcsecond:
            return f"""{self.arcseconds} ″"""
        
        if unit == AngleUnits.Gradian:
            return f"""{self.gradians} g"""
        
        if unit == AngleUnits.NatoMil:
            return f"""{self.nato_mils} mil"""
        
        if unit == AngleUnits.Revolution:
            return f"""{self.revolutions} r"""
        
        if unit == AngleUnits.Tilt:
            return f"""{self.tilt} sin(θ)"""
        
        if unit == AngleUnits.Nanoradian:
            return f"""{self.nanoradians} nrad"""
        
        if unit == AngleUnits.Microradian:
            return f"""{self.microradians} μrad"""
        
        if unit == AngleUnits.Milliradian:
            return f"""{self.milliradians} mrad"""
        
        if unit == AngleUnits.Centiradian:
            return f"""{self.centiradians} crad"""
        
        if unit == AngleUnits.Deciradian:
            return f"""{self.deciradians} drad"""
        
        if unit == AngleUnits.Nanodegree:
            return f"""{self.nanodegrees} n°"""
        
        if unit == AngleUnits.Microdegree:
            return f"""{self.microdegrees} μ°"""
        
        if unit == AngleUnits.Millidegree:
            return f"""{self.millidegrees} m°"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AngleUnits = AngleUnits.Degree) -> str:
        """
        Get Angle unit abbreviation.
        Note! the default abbreviation for Angle is Degree.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AngleUnits.Radian:
            return """rad"""
        
        if unit_abbreviation == AngleUnits.Degree:
            return """°"""
        
        if unit_abbreviation == AngleUnits.Arcminute:
            return """'"""
        
        if unit_abbreviation == AngleUnits.Arcsecond:
            return """″"""
        
        if unit_abbreviation == AngleUnits.Gradian:
            return """g"""
        
        if unit_abbreviation == AngleUnits.NatoMil:
            return """mil"""
        
        if unit_abbreviation == AngleUnits.Revolution:
            return """r"""
        
        if unit_abbreviation == AngleUnits.Tilt:
            return """sin(θ)"""
        
        if unit_abbreviation == AngleUnits.Nanoradian:
            return """nrad"""
        
        if unit_abbreviation == AngleUnits.Microradian:
            return """μrad"""
        
        if unit_abbreviation == AngleUnits.Milliradian:
            return """mrad"""
        
        if unit_abbreviation == AngleUnits.Centiradian:
            return """crad"""
        
        if unit_abbreviation == AngleUnits.Deciradian:
            return """drad"""
        
        if unit_abbreviation == AngleUnits.Nanodegree:
            return """n°"""
        
        if unit_abbreviation == AngleUnits.Microdegree:
            return """μ°"""
        
        if unit_abbreviation == AngleUnits.Millidegree:
            return """m°"""
        