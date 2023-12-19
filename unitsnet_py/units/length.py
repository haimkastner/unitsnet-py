from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class LengthUnits(Enum):
        """
            LengthUnits enumeration
        """
        
        Meter = 'meter'
        """
            
        """
        
        Mile = 'mile'
        """
            The statute mile was standardised between the British Commonwealth and the United States by an international agreement in 1959, when it was formally redefined with respect to SI units as exactly 1,609.344 metres.
        """
        
        Yard = 'yard'
        """
            The yard (symbol: yd) is an English unit of length in both the British imperial and US customary systems of measurement equalling 3 feet (or 36 inches). Since 1959 the yard has been by international agreement standardized as exactly 0.9144 meter. A distance of 1,760 yards is equal to 1 mile.
        """
        
        Foot = 'foot'
        """
            
        """
        
        UsSurveyFoot = 'us_survey_foot'
        """
            In the United States, the foot was defined as 12 inches, with the inch being defined by the Mendenhall Order of 1893 as 39.37 inches = 1 m. This makes a U.S. survey foot exactly 1200/3937 meters.
        """
        
        Inch = 'inch'
        """
            
        """
        
        Mil = 'mil'
        """
            
        """
        
        NauticalMile = 'nautical_mile'
        """
            
        """
        
        Fathom = 'fathom'
        """
            
        """
        
        Shackle = 'shackle'
        """
            
        """
        
        Microinch = 'microinch'
        """
            
        """
        
        PrinterPoint = 'printer_point'
        """
            
        """
        
        DtpPoint = 'dtp_point'
        """
            
        """
        
        PrinterPica = 'printer_pica'
        """
            
        """
        
        DtpPica = 'dtp_pica'
        """
            
        """
        
        Twip = 'twip'
        """
            
        """
        
        Hand = 'hand'
        """
            
        """
        
        AstronomicalUnit = 'astronomical_unit'
        """
            One Astronomical Unit is the distance from the solar system Star, the sun, to planet Earth.
        """
        
        Parsec = 'parsec'
        """
            A parsec is defined as the distance at which one astronomical unit (AU) subtends an angle of one arcsecond.
        """
        
        LightYear = 'light_year'
        """
            A Light Year (ly) is the distance that light travel during an Earth year, ie 365 days.
        """
        
        SolarRadius = 'solar_radius'
        """
            Solar radius is a ratio unit to the radius of the solar system star, the sun.
        """
        
        Chain = 'chain'
        """
            
        """
        
        Angstrom = 'angstrom'
        """
            Angstrom is a metric unit of length equal to 1e-10 meter
        """
        
        DataMile = 'data_mile'
        """
            In radar-related subjects and in JTIDS, a data mile is a unit of distance equal to 6000 feet (1.8288 kilometres or 0.987 nautical miles).
        """
        
        Femtometer = 'femtometer'
        """
            
        """
        
        Picometer = 'picometer'
        """
            
        """
        
        Nanometer = 'nanometer'
        """
            
        """
        
        Micrometer = 'micrometer'
        """
            
        """
        
        Millimeter = 'millimeter'
        """
            
        """
        
        Centimeter = 'centimeter'
        """
            
        """
        
        Decimeter = 'decimeter'
        """
            
        """
        
        Decameter = 'decameter'
        """
            
        """
        
        Hectometer = 'hectometer'
        """
            
        """
        
        Kilometer = 'kilometer'
        """
            
        """
        
        Megameter = 'megameter'
        """
            
        """
        
        Gigameter = 'gigameter'
        """
            
        """
        
        Kiloyard = 'kiloyard'
        """
            
        """
        
        Kilofoot = 'kilofoot'
        """
            
        """
        
        Kiloparsec = 'kiloparsec'
        """
            
        """
        
        Megaparsec = 'megaparsec'
        """
            
        """
        
        KilolightYear = 'kilolight_year'
        """
            
        """
        
        MegalightYear = 'megalight_year'
        """
            
        """
        

class Length(AbstractMeasure):
    """
    Many different units of length have been used around the world. The main units in modern use are U.S. customary units in the United States and the Metric system elsewhere. British Imperial units are still used for some purposes in the United Kingdom and some other countries. The metric system is sub-divided into SI and non-SI units.

    Args:
        value (float): The value.
        from_unit (LengthUnits): The Length unit to create from, The default unit is Meter
    """
    def __init__(self, value: float, from_unit: LengthUnits = LengthUnits.Meter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__meters = None
        
        self.__miles = None
        
        self.__yards = None
        
        self.__feet = None
        
        self.__us_survey_feet = None
        
        self.__inches = None
        
        self.__mils = None
        
        self.__nautical_miles = None
        
        self.__fathoms = None
        
        self.__shackles = None
        
        self.__microinches = None
        
        self.__printer_points = None
        
        self.__dtp_points = None
        
        self.__printer_picas = None
        
        self.__dtp_picas = None
        
        self.__twips = None
        
        self.__hands = None
        
        self.__astronomical_units = None
        
        self.__parsecs = None
        
        self.__light_years = None
        
        self.__solar_radiuses = None
        
        self.__chains = None
        
        self.__angstroms = None
        
        self.__data_miles = None
        
        self.__femtometers = None
        
        self.__picometers = None
        
        self.__nanometers = None
        
        self.__micrometers = None
        
        self.__millimeters = None
        
        self.__centimeters = None
        
        self.__decimeters = None
        
        self.__decameters = None
        
        self.__hectometers = None
        
        self.__kilometers = None
        
        self.__megameters = None
        
        self.__gigameters = None
        
        self.__kiloyards = None
        
        self.__kilofeet = None
        
        self.__kiloparsecs = None
        
        self.__megaparsecs = None
        
        self.__kilolight_years = None
        
        self.__megalight_years = None
        

    def convert(self, unit: LengthUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: LengthUnits) -> float:
        value = self._value
        
        if from_unit == LengthUnits.Meter:
            return (value)
        
        if from_unit == LengthUnits.Mile:
            return (value / 1609.344)
        
        if from_unit == LengthUnits.Yard:
            return (value / 0.9144)
        
        if from_unit == LengthUnits.Foot:
            return (value / 0.3048)
        
        if from_unit == LengthUnits.UsSurveyFoot:
            return (value * 3937 / 1200)
        
        if from_unit == LengthUnits.Inch:
            return (value / 2.54e-2)
        
        if from_unit == LengthUnits.Mil:
            return (value / 2.54e-5)
        
        if from_unit == LengthUnits.NauticalMile:
            return (value / 1852)
        
        if from_unit == LengthUnits.Fathom:
            return (value / 1.8288)
        
        if from_unit == LengthUnits.Shackle:
            return (value / 27.432)
        
        if from_unit == LengthUnits.Microinch:
            return (value / 2.54e-8)
        
        if from_unit == LengthUnits.PrinterPoint:
            return ((value / 2.54e-2) * 72.27)
        
        if from_unit == LengthUnits.DtpPoint:
            return ((value / 2.54e-2) * 72)
        
        if from_unit == LengthUnits.PrinterPica:
            return (value * 237.106301584)
        
        if from_unit == LengthUnits.DtpPica:
            return (value * 236.220472441)
        
        if from_unit == LengthUnits.Twip:
            return (value * 56692.913385826)
        
        if from_unit == LengthUnits.Hand:
            return (value / 1.016e-1)
        
        if from_unit == LengthUnits.AstronomicalUnit:
            return (value / 1.4959787070e11)
        
        if from_unit == LengthUnits.Parsec:
            return (value / 3.08567758128e16)
        
        if from_unit == LengthUnits.LightYear:
            return (value / 9.46073047258e15)
        
        if from_unit == LengthUnits.SolarRadius:
            return (value / 6.95510000e+08)
        
        if from_unit == LengthUnits.Chain:
            return (value / 20.1168)
        
        if from_unit == LengthUnits.Angstrom:
            return (value / 1e-10)
        
        if from_unit == LengthUnits.DataMile:
            return (value / 1828.8)
        
        if from_unit == LengthUnits.Femtometer:
            return ((value) / 1e-15)
        
        if from_unit == LengthUnits.Picometer:
            return ((value) / 1e-12)
        
        if from_unit == LengthUnits.Nanometer:
            return ((value) / 1e-09)
        
        if from_unit == LengthUnits.Micrometer:
            return ((value) / 1e-06)
        
        if from_unit == LengthUnits.Millimeter:
            return ((value) / 0.001)
        
        if from_unit == LengthUnits.Centimeter:
            return ((value) / 0.01)
        
        if from_unit == LengthUnits.Decimeter:
            return ((value) / 0.1)
        
        if from_unit == LengthUnits.Decameter:
            return ((value) / 10.0)
        
        if from_unit == LengthUnits.Hectometer:
            return ((value) / 100.0)
        
        if from_unit == LengthUnits.Kilometer:
            return ((value) / 1000.0)
        
        if from_unit == LengthUnits.Megameter:
            return ((value) / 1000000.0)
        
        if from_unit == LengthUnits.Gigameter:
            return ((value) / 1000000000.0)
        
        if from_unit == LengthUnits.Kiloyard:
            return ((value / 0.9144) / 1000.0)
        
        if from_unit == LengthUnits.Kilofoot:
            return ((value / 0.3048) / 1000.0)
        
        if from_unit == LengthUnits.Kiloparsec:
            return ((value / 3.08567758128e16) / 1000.0)
        
        if from_unit == LengthUnits.Megaparsec:
            return ((value / 3.08567758128e16) / 1000000.0)
        
        if from_unit == LengthUnits.KilolightYear:
            return ((value / 9.46073047258e15) / 1000.0)
        
        if from_unit == LengthUnits.MegalightYear:
            return ((value / 9.46073047258e15) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: LengthUnits) -> float:
        
        if to_unit == LengthUnits.Meter:
            return (value)
        
        if to_unit == LengthUnits.Mile:
            return (value * 1609.344)
        
        if to_unit == LengthUnits.Yard:
            return (value * 0.9144)
        
        if to_unit == LengthUnits.Foot:
            return (value * 0.3048)
        
        if to_unit == LengthUnits.UsSurveyFoot:
            return (value * 1200 / 3937)
        
        if to_unit == LengthUnits.Inch:
            return (value * 2.54e-2)
        
        if to_unit == LengthUnits.Mil:
            return (value * 2.54e-5)
        
        if to_unit == LengthUnits.NauticalMile:
            return (value * 1852)
        
        if to_unit == LengthUnits.Fathom:
            return (value * 1.8288)
        
        if to_unit == LengthUnits.Shackle:
            return (value * 27.432)
        
        if to_unit == LengthUnits.Microinch:
            return (value * 2.54e-8)
        
        if to_unit == LengthUnits.PrinterPoint:
            return ((value / 72.27) * 2.54e-2)
        
        if to_unit == LengthUnits.DtpPoint:
            return ((value / 72) * 2.54e-2)
        
        if to_unit == LengthUnits.PrinterPica:
            return (value / 237.106301584)
        
        if to_unit == LengthUnits.DtpPica:
            return (value / 236.220472441)
        
        if to_unit == LengthUnits.Twip:
            return (value / 56692.913385826)
        
        if to_unit == LengthUnits.Hand:
            return (value * 1.016e-1)
        
        if to_unit == LengthUnits.AstronomicalUnit:
            return (value * 1.4959787070e11)
        
        if to_unit == LengthUnits.Parsec:
            return (value * 3.08567758128e16)
        
        if to_unit == LengthUnits.LightYear:
            return (value * 9.46073047258e15)
        
        if to_unit == LengthUnits.SolarRadius:
            return (value * 6.95510000e+08)
        
        if to_unit == LengthUnits.Chain:
            return (value * 20.1168)
        
        if to_unit == LengthUnits.Angstrom:
            return (value * 1e-10)
        
        if to_unit == LengthUnits.DataMile:
            return (value * 1828.8)
        
        if to_unit == LengthUnits.Femtometer:
            return ((value) * 1e-15)
        
        if to_unit == LengthUnits.Picometer:
            return ((value) * 1e-12)
        
        if to_unit == LengthUnits.Nanometer:
            return ((value) * 1e-09)
        
        if to_unit == LengthUnits.Micrometer:
            return ((value) * 1e-06)
        
        if to_unit == LengthUnits.Millimeter:
            return ((value) * 0.001)
        
        if to_unit == LengthUnits.Centimeter:
            return ((value) * 0.01)
        
        if to_unit == LengthUnits.Decimeter:
            return ((value) * 0.1)
        
        if to_unit == LengthUnits.Decameter:
            return ((value) * 10.0)
        
        if to_unit == LengthUnits.Hectometer:
            return ((value) * 100.0)
        
        if to_unit == LengthUnits.Kilometer:
            return ((value) * 1000.0)
        
        if to_unit == LengthUnits.Megameter:
            return ((value) * 1000000.0)
        
        if to_unit == LengthUnits.Gigameter:
            return ((value) * 1000000000.0)
        
        if to_unit == LengthUnits.Kiloyard:
            return ((value * 0.9144) * 1000.0)
        
        if to_unit == LengthUnits.Kilofoot:
            return ((value * 0.3048) * 1000.0)
        
        if to_unit == LengthUnits.Kiloparsec:
            return ((value * 3.08567758128e16) * 1000.0)
        
        if to_unit == LengthUnits.Megaparsec:
            return ((value * 3.08567758128e16) * 1000000.0)
        
        if to_unit == LengthUnits.KilolightYear:
            return ((value * 9.46073047258e15) * 1000.0)
        
        if to_unit == LengthUnits.MegalightYear:
            return ((value * 9.46073047258e15) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_meters(meters: float):
        """
        Create a new instance of Length from a value in meters.

        

        :param meters: The Length value in meters.
        :type meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(meters, LengthUnits.Meter)

    
    @staticmethod
    def from_miles(miles: float):
        """
        Create a new instance of Length from a value in miles.

        The statute mile was standardised between the British Commonwealth and the United States by an international agreement in 1959, when it was formally redefined with respect to SI units as exactly 1,609.344 metres.

        :param meters: The Length value in miles.
        :type miles: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(miles, LengthUnits.Mile)

    
    @staticmethod
    def from_yards(yards: float):
        """
        Create a new instance of Length from a value in yards.

        The yard (symbol: yd) is an English unit of length in both the British imperial and US customary systems of measurement equalling 3 feet (or 36 inches). Since 1959 the yard has been by international agreement standardized as exactly 0.9144 meter. A distance of 1,760 yards is equal to 1 mile.

        :param meters: The Length value in yards.
        :type yards: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(yards, LengthUnits.Yard)

    
    @staticmethod
    def from_feet(feet: float):
        """
        Create a new instance of Length from a value in feet.

        

        :param meters: The Length value in feet.
        :type feet: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(feet, LengthUnits.Foot)

    
    @staticmethod
    def from_us_survey_feet(us_survey_feet: float):
        """
        Create a new instance of Length from a value in us_survey_feet.

        In the United States, the foot was defined as 12 inches, with the inch being defined by the Mendenhall Order of 1893 as 39.37 inches = 1 m. This makes a U.S. survey foot exactly 1200/3937 meters.

        :param meters: The Length value in us_survey_feet.
        :type us_survey_feet: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(us_survey_feet, LengthUnits.UsSurveyFoot)

    
    @staticmethod
    def from_inches(inches: float):
        """
        Create a new instance of Length from a value in inches.

        

        :param meters: The Length value in inches.
        :type inches: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(inches, LengthUnits.Inch)

    
    @staticmethod
    def from_mils(mils: float):
        """
        Create a new instance of Length from a value in mils.

        

        :param meters: The Length value in mils.
        :type mils: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(mils, LengthUnits.Mil)

    
    @staticmethod
    def from_nautical_miles(nautical_miles: float):
        """
        Create a new instance of Length from a value in nautical_miles.

        

        :param meters: The Length value in nautical_miles.
        :type nautical_miles: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(nautical_miles, LengthUnits.NauticalMile)

    
    @staticmethod
    def from_fathoms(fathoms: float):
        """
        Create a new instance of Length from a value in fathoms.

        

        :param meters: The Length value in fathoms.
        :type fathoms: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(fathoms, LengthUnits.Fathom)

    
    @staticmethod
    def from_shackles(shackles: float):
        """
        Create a new instance of Length from a value in shackles.

        

        :param meters: The Length value in shackles.
        :type shackles: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(shackles, LengthUnits.Shackle)

    
    @staticmethod
    def from_microinches(microinches: float):
        """
        Create a new instance of Length from a value in microinches.

        

        :param meters: The Length value in microinches.
        :type microinches: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(microinches, LengthUnits.Microinch)

    
    @staticmethod
    def from_printer_points(printer_points: float):
        """
        Create a new instance of Length from a value in printer_points.

        

        :param meters: The Length value in printer_points.
        :type printer_points: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(printer_points, LengthUnits.PrinterPoint)

    
    @staticmethod
    def from_dtp_points(dtp_points: float):
        """
        Create a new instance of Length from a value in dtp_points.

        

        :param meters: The Length value in dtp_points.
        :type dtp_points: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(dtp_points, LengthUnits.DtpPoint)

    
    @staticmethod
    def from_printer_picas(printer_picas: float):
        """
        Create a new instance of Length from a value in printer_picas.

        

        :param meters: The Length value in printer_picas.
        :type printer_picas: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(printer_picas, LengthUnits.PrinterPica)

    
    @staticmethod
    def from_dtp_picas(dtp_picas: float):
        """
        Create a new instance of Length from a value in dtp_picas.

        

        :param meters: The Length value in dtp_picas.
        :type dtp_picas: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(dtp_picas, LengthUnits.DtpPica)

    
    @staticmethod
    def from_twips(twips: float):
        """
        Create a new instance of Length from a value in twips.

        

        :param meters: The Length value in twips.
        :type twips: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(twips, LengthUnits.Twip)

    
    @staticmethod
    def from_hands(hands: float):
        """
        Create a new instance of Length from a value in hands.

        

        :param meters: The Length value in hands.
        :type hands: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(hands, LengthUnits.Hand)

    
    @staticmethod
    def from_astronomical_units(astronomical_units: float):
        """
        Create a new instance of Length from a value in astronomical_units.

        One Astronomical Unit is the distance from the solar system Star, the sun, to planet Earth.

        :param meters: The Length value in astronomical_units.
        :type astronomical_units: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(astronomical_units, LengthUnits.AstronomicalUnit)

    
    @staticmethod
    def from_parsecs(parsecs: float):
        """
        Create a new instance of Length from a value in parsecs.

        A parsec is defined as the distance at which one astronomical unit (AU) subtends an angle of one arcsecond.

        :param meters: The Length value in parsecs.
        :type parsecs: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(parsecs, LengthUnits.Parsec)

    
    @staticmethod
    def from_light_years(light_years: float):
        """
        Create a new instance of Length from a value in light_years.

        A Light Year (ly) is the distance that light travel during an Earth year, ie 365 days.

        :param meters: The Length value in light_years.
        :type light_years: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(light_years, LengthUnits.LightYear)

    
    @staticmethod
    def from_solar_radiuses(solar_radiuses: float):
        """
        Create a new instance of Length from a value in solar_radiuses.

        Solar radius is a ratio unit to the radius of the solar system star, the sun.

        :param meters: The Length value in solar_radiuses.
        :type solar_radiuses: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(solar_radiuses, LengthUnits.SolarRadius)

    
    @staticmethod
    def from_chains(chains: float):
        """
        Create a new instance of Length from a value in chains.

        

        :param meters: The Length value in chains.
        :type chains: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(chains, LengthUnits.Chain)

    
    @staticmethod
    def from_angstroms(angstroms: float):
        """
        Create a new instance of Length from a value in angstroms.

        Angstrom is a metric unit of length equal to 1e-10 meter

        :param meters: The Length value in angstroms.
        :type angstroms: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(angstroms, LengthUnits.Angstrom)

    
    @staticmethod
    def from_data_miles(data_miles: float):
        """
        Create a new instance of Length from a value in data_miles.

        In radar-related subjects and in JTIDS, a data mile is a unit of distance equal to 6000 feet (1.8288 kilometres or 0.987 nautical miles).

        :param meters: The Length value in data_miles.
        :type data_miles: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(data_miles, LengthUnits.DataMile)

    
    @staticmethod
    def from_femtometers(femtometers: float):
        """
        Create a new instance of Length from a value in femtometers.

        

        :param meters: The Length value in femtometers.
        :type femtometers: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(femtometers, LengthUnits.Femtometer)

    
    @staticmethod
    def from_picometers(picometers: float):
        """
        Create a new instance of Length from a value in picometers.

        

        :param meters: The Length value in picometers.
        :type picometers: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(picometers, LengthUnits.Picometer)

    
    @staticmethod
    def from_nanometers(nanometers: float):
        """
        Create a new instance of Length from a value in nanometers.

        

        :param meters: The Length value in nanometers.
        :type nanometers: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(nanometers, LengthUnits.Nanometer)

    
    @staticmethod
    def from_micrometers(micrometers: float):
        """
        Create a new instance of Length from a value in micrometers.

        

        :param meters: The Length value in micrometers.
        :type micrometers: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(micrometers, LengthUnits.Micrometer)

    
    @staticmethod
    def from_millimeters(millimeters: float):
        """
        Create a new instance of Length from a value in millimeters.

        

        :param meters: The Length value in millimeters.
        :type millimeters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(millimeters, LengthUnits.Millimeter)

    
    @staticmethod
    def from_centimeters(centimeters: float):
        """
        Create a new instance of Length from a value in centimeters.

        

        :param meters: The Length value in centimeters.
        :type centimeters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(centimeters, LengthUnits.Centimeter)

    
    @staticmethod
    def from_decimeters(decimeters: float):
        """
        Create a new instance of Length from a value in decimeters.

        

        :param meters: The Length value in decimeters.
        :type decimeters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(decimeters, LengthUnits.Decimeter)

    
    @staticmethod
    def from_decameters(decameters: float):
        """
        Create a new instance of Length from a value in decameters.

        

        :param meters: The Length value in decameters.
        :type decameters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(decameters, LengthUnits.Decameter)

    
    @staticmethod
    def from_hectometers(hectometers: float):
        """
        Create a new instance of Length from a value in hectometers.

        

        :param meters: The Length value in hectometers.
        :type hectometers: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(hectometers, LengthUnits.Hectometer)

    
    @staticmethod
    def from_kilometers(kilometers: float):
        """
        Create a new instance of Length from a value in kilometers.

        

        :param meters: The Length value in kilometers.
        :type kilometers: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kilometers, LengthUnits.Kilometer)

    
    @staticmethod
    def from_megameters(megameters: float):
        """
        Create a new instance of Length from a value in megameters.

        

        :param meters: The Length value in megameters.
        :type megameters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(megameters, LengthUnits.Megameter)

    
    @staticmethod
    def from_gigameters(gigameters: float):
        """
        Create a new instance of Length from a value in gigameters.

        

        :param meters: The Length value in gigameters.
        :type gigameters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(gigameters, LengthUnits.Gigameter)

    
    @staticmethod
    def from_kiloyards(kiloyards: float):
        """
        Create a new instance of Length from a value in kiloyards.

        

        :param meters: The Length value in kiloyards.
        :type kiloyards: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kiloyards, LengthUnits.Kiloyard)

    
    @staticmethod
    def from_kilofeet(kilofeet: float):
        """
        Create a new instance of Length from a value in kilofeet.

        

        :param meters: The Length value in kilofeet.
        :type kilofeet: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kilofeet, LengthUnits.Kilofoot)

    
    @staticmethod
    def from_kiloparsecs(kiloparsecs: float):
        """
        Create a new instance of Length from a value in kiloparsecs.

        

        :param meters: The Length value in kiloparsecs.
        :type kiloparsecs: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kiloparsecs, LengthUnits.Kiloparsec)

    
    @staticmethod
    def from_megaparsecs(megaparsecs: float):
        """
        Create a new instance of Length from a value in megaparsecs.

        

        :param meters: The Length value in megaparsecs.
        :type megaparsecs: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(megaparsecs, LengthUnits.Megaparsec)

    
    @staticmethod
    def from_kilolight_years(kilolight_years: float):
        """
        Create a new instance of Length from a value in kilolight_years.

        

        :param meters: The Length value in kilolight_years.
        :type kilolight_years: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kilolight_years, LengthUnits.KilolightYear)

    
    @staticmethod
    def from_megalight_years(megalight_years: float):
        """
        Create a new instance of Length from a value in megalight_years.

        

        :param meters: The Length value in megalight_years.
        :type megalight_years: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(megalight_years, LengthUnits.MegalightYear)

    
    @property
    def meters(self) -> float:
        """
        
        """
        if self.__meters != None:
            return self.__meters
        self.__meters = self.__convert_from_base(LengthUnits.Meter)
        return self.__meters

    
    @property
    def miles(self) -> float:
        """
        The statute mile was standardised between the British Commonwealth and the United States by an international agreement in 1959, when it was formally redefined with respect to SI units as exactly 1,609.344 metres.
        """
        if self.__miles != None:
            return self.__miles
        self.__miles = self.__convert_from_base(LengthUnits.Mile)
        return self.__miles

    
    @property
    def yards(self) -> float:
        """
        The yard (symbol: yd) is an English unit of length in both the British imperial and US customary systems of measurement equalling 3 feet (or 36 inches). Since 1959 the yard has been by international agreement standardized as exactly 0.9144 meter. A distance of 1,760 yards is equal to 1 mile.
        """
        if self.__yards != None:
            return self.__yards
        self.__yards = self.__convert_from_base(LengthUnits.Yard)
        return self.__yards

    
    @property
    def feet(self) -> float:
        """
        
        """
        if self.__feet != None:
            return self.__feet
        self.__feet = self.__convert_from_base(LengthUnits.Foot)
        return self.__feet

    
    @property
    def us_survey_feet(self) -> float:
        """
        In the United States, the foot was defined as 12 inches, with the inch being defined by the Mendenhall Order of 1893 as 39.37 inches = 1 m. This makes a U.S. survey foot exactly 1200/3937 meters.
        """
        if self.__us_survey_feet != None:
            return self.__us_survey_feet
        self.__us_survey_feet = self.__convert_from_base(LengthUnits.UsSurveyFoot)
        return self.__us_survey_feet

    
    @property
    def inches(self) -> float:
        """
        
        """
        if self.__inches != None:
            return self.__inches
        self.__inches = self.__convert_from_base(LengthUnits.Inch)
        return self.__inches

    
    @property
    def mils(self) -> float:
        """
        
        """
        if self.__mils != None:
            return self.__mils
        self.__mils = self.__convert_from_base(LengthUnits.Mil)
        return self.__mils

    
    @property
    def nautical_miles(self) -> float:
        """
        
        """
        if self.__nautical_miles != None:
            return self.__nautical_miles
        self.__nautical_miles = self.__convert_from_base(LengthUnits.NauticalMile)
        return self.__nautical_miles

    
    @property
    def fathoms(self) -> float:
        """
        
        """
        if self.__fathoms != None:
            return self.__fathoms
        self.__fathoms = self.__convert_from_base(LengthUnits.Fathom)
        return self.__fathoms

    
    @property
    def shackles(self) -> float:
        """
        
        """
        if self.__shackles != None:
            return self.__shackles
        self.__shackles = self.__convert_from_base(LengthUnits.Shackle)
        return self.__shackles

    
    @property
    def microinches(self) -> float:
        """
        
        """
        if self.__microinches != None:
            return self.__microinches
        self.__microinches = self.__convert_from_base(LengthUnits.Microinch)
        return self.__microinches

    
    @property
    def printer_points(self) -> float:
        """
        
        """
        if self.__printer_points != None:
            return self.__printer_points
        self.__printer_points = self.__convert_from_base(LengthUnits.PrinterPoint)
        return self.__printer_points

    
    @property
    def dtp_points(self) -> float:
        """
        
        """
        if self.__dtp_points != None:
            return self.__dtp_points
        self.__dtp_points = self.__convert_from_base(LengthUnits.DtpPoint)
        return self.__dtp_points

    
    @property
    def printer_picas(self) -> float:
        """
        
        """
        if self.__printer_picas != None:
            return self.__printer_picas
        self.__printer_picas = self.__convert_from_base(LengthUnits.PrinterPica)
        return self.__printer_picas

    
    @property
    def dtp_picas(self) -> float:
        """
        
        """
        if self.__dtp_picas != None:
            return self.__dtp_picas
        self.__dtp_picas = self.__convert_from_base(LengthUnits.DtpPica)
        return self.__dtp_picas

    
    @property
    def twips(self) -> float:
        """
        
        """
        if self.__twips != None:
            return self.__twips
        self.__twips = self.__convert_from_base(LengthUnits.Twip)
        return self.__twips

    
    @property
    def hands(self) -> float:
        """
        
        """
        if self.__hands != None:
            return self.__hands
        self.__hands = self.__convert_from_base(LengthUnits.Hand)
        return self.__hands

    
    @property
    def astronomical_units(self) -> float:
        """
        One Astronomical Unit is the distance from the solar system Star, the sun, to planet Earth.
        """
        if self.__astronomical_units != None:
            return self.__astronomical_units
        self.__astronomical_units = self.__convert_from_base(LengthUnits.AstronomicalUnit)
        return self.__astronomical_units

    
    @property
    def parsecs(self) -> float:
        """
        A parsec is defined as the distance at which one astronomical unit (AU) subtends an angle of one arcsecond.
        """
        if self.__parsecs != None:
            return self.__parsecs
        self.__parsecs = self.__convert_from_base(LengthUnits.Parsec)
        return self.__parsecs

    
    @property
    def light_years(self) -> float:
        """
        A Light Year (ly) is the distance that light travel during an Earth year, ie 365 days.
        """
        if self.__light_years != None:
            return self.__light_years
        self.__light_years = self.__convert_from_base(LengthUnits.LightYear)
        return self.__light_years

    
    @property
    def solar_radiuses(self) -> float:
        """
        Solar radius is a ratio unit to the radius of the solar system star, the sun.
        """
        if self.__solar_radiuses != None:
            return self.__solar_radiuses
        self.__solar_radiuses = self.__convert_from_base(LengthUnits.SolarRadius)
        return self.__solar_radiuses

    
    @property
    def chains(self) -> float:
        """
        
        """
        if self.__chains != None:
            return self.__chains
        self.__chains = self.__convert_from_base(LengthUnits.Chain)
        return self.__chains

    
    @property
    def angstroms(self) -> float:
        """
        Angstrom is a metric unit of length equal to 1e-10 meter
        """
        if self.__angstroms != None:
            return self.__angstroms
        self.__angstroms = self.__convert_from_base(LengthUnits.Angstrom)
        return self.__angstroms

    
    @property
    def data_miles(self) -> float:
        """
        In radar-related subjects and in JTIDS, a data mile is a unit of distance equal to 6000 feet (1.8288 kilometres or 0.987 nautical miles).
        """
        if self.__data_miles != None:
            return self.__data_miles
        self.__data_miles = self.__convert_from_base(LengthUnits.DataMile)
        return self.__data_miles

    
    @property
    def femtometers(self) -> float:
        """
        
        """
        if self.__femtometers != None:
            return self.__femtometers
        self.__femtometers = self.__convert_from_base(LengthUnits.Femtometer)
        return self.__femtometers

    
    @property
    def picometers(self) -> float:
        """
        
        """
        if self.__picometers != None:
            return self.__picometers
        self.__picometers = self.__convert_from_base(LengthUnits.Picometer)
        return self.__picometers

    
    @property
    def nanometers(self) -> float:
        """
        
        """
        if self.__nanometers != None:
            return self.__nanometers
        self.__nanometers = self.__convert_from_base(LengthUnits.Nanometer)
        return self.__nanometers

    
    @property
    def micrometers(self) -> float:
        """
        
        """
        if self.__micrometers != None:
            return self.__micrometers
        self.__micrometers = self.__convert_from_base(LengthUnits.Micrometer)
        return self.__micrometers

    
    @property
    def millimeters(self) -> float:
        """
        
        """
        if self.__millimeters != None:
            return self.__millimeters
        self.__millimeters = self.__convert_from_base(LengthUnits.Millimeter)
        return self.__millimeters

    
    @property
    def centimeters(self) -> float:
        """
        
        """
        if self.__centimeters != None:
            return self.__centimeters
        self.__centimeters = self.__convert_from_base(LengthUnits.Centimeter)
        return self.__centimeters

    
    @property
    def decimeters(self) -> float:
        """
        
        """
        if self.__decimeters != None:
            return self.__decimeters
        self.__decimeters = self.__convert_from_base(LengthUnits.Decimeter)
        return self.__decimeters

    
    @property
    def decameters(self) -> float:
        """
        
        """
        if self.__decameters != None:
            return self.__decameters
        self.__decameters = self.__convert_from_base(LengthUnits.Decameter)
        return self.__decameters

    
    @property
    def hectometers(self) -> float:
        """
        
        """
        if self.__hectometers != None:
            return self.__hectometers
        self.__hectometers = self.__convert_from_base(LengthUnits.Hectometer)
        return self.__hectometers

    
    @property
    def kilometers(self) -> float:
        """
        
        """
        if self.__kilometers != None:
            return self.__kilometers
        self.__kilometers = self.__convert_from_base(LengthUnits.Kilometer)
        return self.__kilometers

    
    @property
    def megameters(self) -> float:
        """
        
        """
        if self.__megameters != None:
            return self.__megameters
        self.__megameters = self.__convert_from_base(LengthUnits.Megameter)
        return self.__megameters

    
    @property
    def gigameters(self) -> float:
        """
        
        """
        if self.__gigameters != None:
            return self.__gigameters
        self.__gigameters = self.__convert_from_base(LengthUnits.Gigameter)
        return self.__gigameters

    
    @property
    def kiloyards(self) -> float:
        """
        
        """
        if self.__kiloyards != None:
            return self.__kiloyards
        self.__kiloyards = self.__convert_from_base(LengthUnits.Kiloyard)
        return self.__kiloyards

    
    @property
    def kilofeet(self) -> float:
        """
        
        """
        if self.__kilofeet != None:
            return self.__kilofeet
        self.__kilofeet = self.__convert_from_base(LengthUnits.Kilofoot)
        return self.__kilofeet

    
    @property
    def kiloparsecs(self) -> float:
        """
        
        """
        if self.__kiloparsecs != None:
            return self.__kiloparsecs
        self.__kiloparsecs = self.__convert_from_base(LengthUnits.Kiloparsec)
        return self.__kiloparsecs

    
    @property
    def megaparsecs(self) -> float:
        """
        
        """
        if self.__megaparsecs != None:
            return self.__megaparsecs
        self.__megaparsecs = self.__convert_from_base(LengthUnits.Megaparsec)
        return self.__megaparsecs

    
    @property
    def kilolight_years(self) -> float:
        """
        
        """
        if self.__kilolight_years != None:
            return self.__kilolight_years
        self.__kilolight_years = self.__convert_from_base(LengthUnits.KilolightYear)
        return self.__kilolight_years

    
    @property
    def megalight_years(self) -> float:
        """
        
        """
        if self.__megalight_years != None:
            return self.__megalight_years
        self.__megalight_years = self.__convert_from_base(LengthUnits.MegalightYear)
        return self.__megalight_years

    
    def to_string(self, unit: LengthUnits = LengthUnits.Meter) -> str:
        """
        Format the Length to string.
        Note! the default format for Length is Meter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == LengthUnits.Meter:
            return f"""{self.meters} m"""
        
        if unit == LengthUnits.Mile:
            return f"""{self.miles} mi"""
        
        if unit == LengthUnits.Yard:
            return f"""{self.yards} yd"""
        
        if unit == LengthUnits.Foot:
            return f"""{self.feet} ft"""
        
        if unit == LengthUnits.UsSurveyFoot:
            return f"""{self.us_survey_feet} ftUS"""
        
        if unit == LengthUnits.Inch:
            return f"""{self.inches} in"""
        
        if unit == LengthUnits.Mil:
            return f"""{self.mils} mil"""
        
        if unit == LengthUnits.NauticalMile:
            return f"""{self.nautical_miles} NM"""
        
        if unit == LengthUnits.Fathom:
            return f"""{self.fathoms} fathom"""
        
        if unit == LengthUnits.Shackle:
            return f"""{self.shackles} shackle"""
        
        if unit == LengthUnits.Microinch:
            return f"""{self.microinches} µin"""
        
        if unit == LengthUnits.PrinterPoint:
            return f"""{self.printer_points} pt"""
        
        if unit == LengthUnits.DtpPoint:
            return f"""{self.dtp_points} pt"""
        
        if unit == LengthUnits.PrinterPica:
            return f"""{self.printer_picas} pica"""
        
        if unit == LengthUnits.DtpPica:
            return f"""{self.dtp_picas} pica"""
        
        if unit == LengthUnits.Twip:
            return f"""{self.twips} twip"""
        
        if unit == LengthUnits.Hand:
            return f"""{self.hands} h"""
        
        if unit == LengthUnits.AstronomicalUnit:
            return f"""{self.astronomical_units} au"""
        
        if unit == LengthUnits.Parsec:
            return f"""{self.parsecs} pc"""
        
        if unit == LengthUnits.LightYear:
            return f"""{self.light_years} ly"""
        
        if unit == LengthUnits.SolarRadius:
            return f"""{self.solar_radiuses} R⊙"""
        
        if unit == LengthUnits.Chain:
            return f"""{self.chains} ch"""
        
        if unit == LengthUnits.Angstrom:
            return f"""{self.angstroms} Å"""
        
        if unit == LengthUnits.DataMile:
            return f"""{self.data_miles} DM"""
        
        if unit == LengthUnits.Femtometer:
            return f"""{self.femtometers} fm"""
        
        if unit == LengthUnits.Picometer:
            return f"""{self.picometers} pm"""
        
        if unit == LengthUnits.Nanometer:
            return f"""{self.nanometers} nm"""
        
        if unit == LengthUnits.Micrometer:
            return f"""{self.micrometers} μm"""
        
        if unit == LengthUnits.Millimeter:
            return f"""{self.millimeters} mm"""
        
        if unit == LengthUnits.Centimeter:
            return f"""{self.centimeters} cm"""
        
        if unit == LengthUnits.Decimeter:
            return f"""{self.decimeters} dm"""
        
        if unit == LengthUnits.Decameter:
            return f"""{self.decameters} dam"""
        
        if unit == LengthUnits.Hectometer:
            return f"""{self.hectometers} hm"""
        
        if unit == LengthUnits.Kilometer:
            return f"""{self.kilometers} km"""
        
        if unit == LengthUnits.Megameter:
            return f"""{self.megameters} Mm"""
        
        if unit == LengthUnits.Gigameter:
            return f"""{self.gigameters} Gm"""
        
        if unit == LengthUnits.Kiloyard:
            return f"""{self.kiloyards} kyd"""
        
        if unit == LengthUnits.Kilofoot:
            return f"""{self.kilofeet} kft"""
        
        if unit == LengthUnits.Kiloparsec:
            return f"""{self.kiloparsecs} kpc"""
        
        if unit == LengthUnits.Megaparsec:
            return f"""{self.megaparsecs} Mpc"""
        
        if unit == LengthUnits.KilolightYear:
            return f"""{self.kilolight_years} kly"""
        
        if unit == LengthUnits.MegalightYear:
            return f"""{self.megalight_years} Mly"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: LengthUnits = LengthUnits.Meter) -> str:
        """
        Get Length unit abbreviation.
        Note! the default abbreviation for Length is Meter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == LengthUnits.Meter:
            return """m"""
        
        if unit_abbreviation == LengthUnits.Mile:
            return """mi"""
        
        if unit_abbreviation == LengthUnits.Yard:
            return """yd"""
        
        if unit_abbreviation == LengthUnits.Foot:
            return """ft"""
        
        if unit_abbreviation == LengthUnits.UsSurveyFoot:
            return """ftUS"""
        
        if unit_abbreviation == LengthUnits.Inch:
            return """in"""
        
        if unit_abbreviation == LengthUnits.Mil:
            return """mil"""
        
        if unit_abbreviation == LengthUnits.NauticalMile:
            return """NM"""
        
        if unit_abbreviation == LengthUnits.Fathom:
            return """fathom"""
        
        if unit_abbreviation == LengthUnits.Shackle:
            return """shackle"""
        
        if unit_abbreviation == LengthUnits.Microinch:
            return """µin"""
        
        if unit_abbreviation == LengthUnits.PrinterPoint:
            return """pt"""
        
        if unit_abbreviation == LengthUnits.DtpPoint:
            return """pt"""
        
        if unit_abbreviation == LengthUnits.PrinterPica:
            return """pica"""
        
        if unit_abbreviation == LengthUnits.DtpPica:
            return """pica"""
        
        if unit_abbreviation == LengthUnits.Twip:
            return """twip"""
        
        if unit_abbreviation == LengthUnits.Hand:
            return """h"""
        
        if unit_abbreviation == LengthUnits.AstronomicalUnit:
            return """au"""
        
        if unit_abbreviation == LengthUnits.Parsec:
            return """pc"""
        
        if unit_abbreviation == LengthUnits.LightYear:
            return """ly"""
        
        if unit_abbreviation == LengthUnits.SolarRadius:
            return """R⊙"""
        
        if unit_abbreviation == LengthUnits.Chain:
            return """ch"""
        
        if unit_abbreviation == LengthUnits.Angstrom:
            return """Å"""
        
        if unit_abbreviation == LengthUnits.DataMile:
            return """DM"""
        
        if unit_abbreviation == LengthUnits.Femtometer:
            return """fm"""
        
        if unit_abbreviation == LengthUnits.Picometer:
            return """pm"""
        
        if unit_abbreviation == LengthUnits.Nanometer:
            return """nm"""
        
        if unit_abbreviation == LengthUnits.Micrometer:
            return """μm"""
        
        if unit_abbreviation == LengthUnits.Millimeter:
            return """mm"""
        
        if unit_abbreviation == LengthUnits.Centimeter:
            return """cm"""
        
        if unit_abbreviation == LengthUnits.Decimeter:
            return """dm"""
        
        if unit_abbreviation == LengthUnits.Decameter:
            return """dam"""
        
        if unit_abbreviation == LengthUnits.Hectometer:
            return """hm"""
        
        if unit_abbreviation == LengthUnits.Kilometer:
            return """km"""
        
        if unit_abbreviation == LengthUnits.Megameter:
            return """Mm"""
        
        if unit_abbreviation == LengthUnits.Gigameter:
            return """Gm"""
        
        if unit_abbreviation == LengthUnits.Kiloyard:
            return """kyd"""
        
        if unit_abbreviation == LengthUnits.Kilofoot:
            return """kft"""
        
        if unit_abbreviation == LengthUnits.Kiloparsec:
            return """kpc"""
        
        if unit_abbreviation == LengthUnits.Megaparsec:
            return """Mpc"""
        
        if unit_abbreviation == LengthUnits.KilolightYear:
            return """kly"""
        
        if unit_abbreviation == LengthUnits.MegalightYear:
            return """Mly"""
        