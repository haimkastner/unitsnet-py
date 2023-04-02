from enum import Enum
import math
import string


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
        
        NanoMeter = 'nano_meter'
        """
            
        """
        
        MicroMeter = 'micro_meter'
        """
            
        """
        
        MilliMeter = 'milli_meter'
        """
            
        """
        
        CentiMeter = 'centi_meter'
        """
            
        """
        
        DeciMeter = 'deci_meter'
        """
            
        """
        
        DecaMeter = 'deca_meter'
        """
            
        """
        
        HectoMeter = 'hecto_meter'
        """
            
        """
        
        KiloMeter = 'kilo_meter'
        """
            
        """
        
        MegaMeter = 'mega_meter'
        """
            
        """
        
        KiloParsec = 'kilo_parsec'
        """
            
        """
        
        MegaParsec = 'mega_parsec'
        """
            
        """
        
        KiloLightYear = 'kilo_light_year'
        """
            
        """
        
        MegaLightYear = 'mega_light_year'
        """
            
        """
        

class Length:
    """
    Many different units of length have been used around the world. The main units in modern use are U.S. customary units in the United States and the Metric system elsewhere. British Imperial units are still used for some purposes in the United Kingdom and some other countries. The metric system is sub-divided into SI and non-SI units.

    Args:
        value (float): The value.
        from_unit (LengthUnits): The Length unit to create from, The default unit is Meter
    """
    def __init__(self, value: float, from_unit: LengthUnits = LengthUnits.Meter):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__nano_meters = None
        
        self.__micro_meters = None
        
        self.__milli_meters = None
        
        self.__centi_meters = None
        
        self.__deci_meters = None
        
        self.__deca_meters = None
        
        self.__hecto_meters = None
        
        self.__kilo_meters = None
        
        self.__mega_meters = None
        
        self.__kilo_parsecs = None
        
        self.__mega_parsecs = None
        
        self.__kilo_light_years = None
        
        self.__mega_light_years = None
        

    def __convert_from_base(self, from_unit: LengthUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == LengthUnits.NanoMeter:
            return ((value) / 1e-09)
        
        if from_unit == LengthUnits.MicroMeter:
            return ((value) / 1e-06)
        
        if from_unit == LengthUnits.MilliMeter:
            return ((value) / 0.001)
        
        if from_unit == LengthUnits.CentiMeter:
            return ((value) / 0.01)
        
        if from_unit == LengthUnits.DeciMeter:
            return ((value) / 0.1)
        
        if from_unit == LengthUnits.DecaMeter:
            return ((value) / 10.0)
        
        if from_unit == LengthUnits.HectoMeter:
            return ((value) / 100.0)
        
        if from_unit == LengthUnits.KiloMeter:
            return ((value) / 1000.0)
        
        if from_unit == LengthUnits.MegaMeter:
            return ((value) / 1000000.0)
        
        if from_unit == LengthUnits.KiloParsec:
            return ((value / 3.08567758128e16) / 1000.0)
        
        if from_unit == LengthUnits.MegaParsec:
            return ((value / 3.08567758128e16) / 1000000.0)
        
        if from_unit == LengthUnits.KiloLightYear:
            return ((value / 9.46073047258e15) / 1000.0)
        
        if from_unit == LengthUnits.MegaLightYear:
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
        
        if to_unit == LengthUnits.NanoMeter:
            return ((value) * 1e-09)
        
        if to_unit == LengthUnits.MicroMeter:
            return ((value) * 1e-06)
        
        if to_unit == LengthUnits.MilliMeter:
            return ((value) * 0.001)
        
        if to_unit == LengthUnits.CentiMeter:
            return ((value) * 0.01)
        
        if to_unit == LengthUnits.DeciMeter:
            return ((value) * 0.1)
        
        if to_unit == LengthUnits.DecaMeter:
            return ((value) * 10.0)
        
        if to_unit == LengthUnits.HectoMeter:
            return ((value) * 100.0)
        
        if to_unit == LengthUnits.KiloMeter:
            return ((value) * 1000.0)
        
        if to_unit == LengthUnits.MegaMeter:
            return ((value) * 1000000.0)
        
        if to_unit == LengthUnits.KiloParsec:
            return ((value * 3.08567758128e16) * 1000.0)
        
        if to_unit == LengthUnits.MegaParsec:
            return ((value * 3.08567758128e16) * 1000000.0)
        
        if to_unit == LengthUnits.KiloLightYear:
            return ((value * 9.46073047258e15) * 1000.0)
        
        if to_unit == LengthUnits.MegaLightYear:
            return ((value * 9.46073047258e15) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_nano_meters(nano_meters: float):
        """
        Create a new instance of Length from a value in nano_meters.

        

        :param meters: The Length value in nano_meters.
        :type nano_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(nano_meters, LengthUnits.NanoMeter)

    
    @staticmethod
    def from_micro_meters(micro_meters: float):
        """
        Create a new instance of Length from a value in micro_meters.

        

        :param meters: The Length value in micro_meters.
        :type micro_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(micro_meters, LengthUnits.MicroMeter)

    
    @staticmethod
    def from_milli_meters(milli_meters: float):
        """
        Create a new instance of Length from a value in milli_meters.

        

        :param meters: The Length value in milli_meters.
        :type milli_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(milli_meters, LengthUnits.MilliMeter)

    
    @staticmethod
    def from_centi_meters(centi_meters: float):
        """
        Create a new instance of Length from a value in centi_meters.

        

        :param meters: The Length value in centi_meters.
        :type centi_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(centi_meters, LengthUnits.CentiMeter)

    
    @staticmethod
    def from_deci_meters(deci_meters: float):
        """
        Create a new instance of Length from a value in deci_meters.

        

        :param meters: The Length value in deci_meters.
        :type deci_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(deci_meters, LengthUnits.DeciMeter)

    
    @staticmethod
    def from_deca_meters(deca_meters: float):
        """
        Create a new instance of Length from a value in deca_meters.

        

        :param meters: The Length value in deca_meters.
        :type deca_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(deca_meters, LengthUnits.DecaMeter)

    
    @staticmethod
    def from_hecto_meters(hecto_meters: float):
        """
        Create a new instance of Length from a value in hecto_meters.

        

        :param meters: The Length value in hecto_meters.
        :type hecto_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(hecto_meters, LengthUnits.HectoMeter)

    
    @staticmethod
    def from_kilo_meters(kilo_meters: float):
        """
        Create a new instance of Length from a value in kilo_meters.

        

        :param meters: The Length value in kilo_meters.
        :type kilo_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kilo_meters, LengthUnits.KiloMeter)

    
    @staticmethod
    def from_mega_meters(mega_meters: float):
        """
        Create a new instance of Length from a value in mega_meters.

        

        :param meters: The Length value in mega_meters.
        :type mega_meters: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(mega_meters, LengthUnits.MegaMeter)

    
    @staticmethod
    def from_kilo_parsecs(kilo_parsecs: float):
        """
        Create a new instance of Length from a value in kilo_parsecs.

        

        :param meters: The Length value in kilo_parsecs.
        :type kilo_parsecs: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kilo_parsecs, LengthUnits.KiloParsec)

    
    @staticmethod
    def from_mega_parsecs(mega_parsecs: float):
        """
        Create a new instance of Length from a value in mega_parsecs.

        

        :param meters: The Length value in mega_parsecs.
        :type mega_parsecs: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(mega_parsecs, LengthUnits.MegaParsec)

    
    @staticmethod
    def from_kilo_light_years(kilo_light_years: float):
        """
        Create a new instance of Length from a value in kilo_light_years.

        

        :param meters: The Length value in kilo_light_years.
        :type kilo_light_years: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(kilo_light_years, LengthUnits.KiloLightYear)

    
    @staticmethod
    def from_mega_light_years(mega_light_years: float):
        """
        Create a new instance of Length from a value in mega_light_years.

        

        :param meters: The Length value in mega_light_years.
        :type mega_light_years: float
        :return: A new instance of Length.
        :rtype: Length
        """
        return Length(mega_light_years, LengthUnits.MegaLightYear)

    
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
    def nano_meters(self) -> float:
        """
        
        """
        if self.__nano_meters != None:
            return self.__nano_meters
        self.__nano_meters = self.__convert_from_base(LengthUnits.NanoMeter)
        return self.__nano_meters

    
    @property
    def micro_meters(self) -> float:
        """
        
        """
        if self.__micro_meters != None:
            return self.__micro_meters
        self.__micro_meters = self.__convert_from_base(LengthUnits.MicroMeter)
        return self.__micro_meters

    
    @property
    def milli_meters(self) -> float:
        """
        
        """
        if self.__milli_meters != None:
            return self.__milli_meters
        self.__milli_meters = self.__convert_from_base(LengthUnits.MilliMeter)
        return self.__milli_meters

    
    @property
    def centi_meters(self) -> float:
        """
        
        """
        if self.__centi_meters != None:
            return self.__centi_meters
        self.__centi_meters = self.__convert_from_base(LengthUnits.CentiMeter)
        return self.__centi_meters

    
    @property
    def deci_meters(self) -> float:
        """
        
        """
        if self.__deci_meters != None:
            return self.__deci_meters
        self.__deci_meters = self.__convert_from_base(LengthUnits.DeciMeter)
        return self.__deci_meters

    
    @property
    def deca_meters(self) -> float:
        """
        
        """
        if self.__deca_meters != None:
            return self.__deca_meters
        self.__deca_meters = self.__convert_from_base(LengthUnits.DecaMeter)
        return self.__deca_meters

    
    @property
    def hecto_meters(self) -> float:
        """
        
        """
        if self.__hecto_meters != None:
            return self.__hecto_meters
        self.__hecto_meters = self.__convert_from_base(LengthUnits.HectoMeter)
        return self.__hecto_meters

    
    @property
    def kilo_meters(self) -> float:
        """
        
        """
        if self.__kilo_meters != None:
            return self.__kilo_meters
        self.__kilo_meters = self.__convert_from_base(LengthUnits.KiloMeter)
        return self.__kilo_meters

    
    @property
    def mega_meters(self) -> float:
        """
        
        """
        if self.__mega_meters != None:
            return self.__mega_meters
        self.__mega_meters = self.__convert_from_base(LengthUnits.MegaMeter)
        return self.__mega_meters

    
    @property
    def kilo_parsecs(self) -> float:
        """
        
        """
        if self.__kilo_parsecs != None:
            return self.__kilo_parsecs
        self.__kilo_parsecs = self.__convert_from_base(LengthUnits.KiloParsec)
        return self.__kilo_parsecs

    
    @property
    def mega_parsecs(self) -> float:
        """
        
        """
        if self.__mega_parsecs != None:
            return self.__mega_parsecs
        self.__mega_parsecs = self.__convert_from_base(LengthUnits.MegaParsec)
        return self.__mega_parsecs

    
    @property
    def kilo_light_years(self) -> float:
        """
        
        """
        if self.__kilo_light_years != None:
            return self.__kilo_light_years
        self.__kilo_light_years = self.__convert_from_base(LengthUnits.KiloLightYear)
        return self.__kilo_light_years

    
    @property
    def mega_light_years(self) -> float:
        """
        
        """
        if self.__mega_light_years != None:
            return self.__mega_light_years
        self.__mega_light_years = self.__convert_from_base(LengthUnits.MegaLightYear)
        return self.__mega_light_years

    
    def to_string(self, unit: LengthUnits = LengthUnits.Meter) -> string:
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
        
        if unit == LengthUnits.NanoMeter:
            return f"""{self.nano_meters} """
        
        if unit == LengthUnits.MicroMeter:
            return f"""{self.micro_meters} """
        
        if unit == LengthUnits.MilliMeter:
            return f"""{self.milli_meters} """
        
        if unit == LengthUnits.CentiMeter:
            return f"""{self.centi_meters} """
        
        if unit == LengthUnits.DeciMeter:
            return f"""{self.deci_meters} """
        
        if unit == LengthUnits.DecaMeter:
            return f"""{self.deca_meters} """
        
        if unit == LengthUnits.HectoMeter:
            return f"""{self.hecto_meters} """
        
        if unit == LengthUnits.KiloMeter:
            return f"""{self.kilo_meters} """
        
        if unit == LengthUnits.MegaMeter:
            return f"""{self.mega_meters} """
        
        if unit == LengthUnits.KiloParsec:
            return f"""{self.kilo_parsecs} """
        
        if unit == LengthUnits.MegaParsec:
            return f"""{self.mega_parsecs} """
        
        if unit == LengthUnits.KiloLightYear:
            return f"""{self.kilo_light_years} """
        
        if unit == LengthUnits.MegaLightYear:
            return f"""{self.mega_light_years} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: LengthUnits = LengthUnits.Meter) -> string:
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
        
        if unit_abbreviation == LengthUnits.NanoMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.MicroMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.MilliMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.CentiMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.DeciMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.DecaMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.HectoMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.KiloMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.MegaMeter:
            return """"""
        
        if unit_abbreviation == LengthUnits.KiloParsec:
            return """"""
        
        if unit_abbreviation == LengthUnits.MegaParsec:
            return """"""
        
        if unit_abbreviation == LengthUnits.KiloLightYear:
            return """"""
        
        if unit_abbreviation == LengthUnits.MegaLightYear:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for +: 'Length' and '{}'".format(type(other).__name__))
        return Length(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for *: 'Length' and '{}'".format(type(other).__name__))
        return Length(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for -: 'Length' and '{}'".format(type(other).__name__))
        return Length(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for /: 'Length' and '{}'".format(type(other).__name__))
        return Length(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for %: 'Length' and '{}'".format(type(other).__name__))
        return Length(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for **: 'Length' and '{}'".format(type(other).__name__))
        return Length(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for ==: 'Length' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for <: 'Length' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for >: 'Length' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for <=: 'Length' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Length):
            raise TypeError("unsupported operand type(s) for >=: 'Length' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value