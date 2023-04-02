from enum import Enum
import math
import string


class MassUnits(Enum):
        """
            MassUnits enumeration
        """
        
        Gram = 'gram'
        """
            
        """
        
        Tonne = 'tonne'
        """
            
        """
        
        ShortTon = 'short_ton'
        """
            The short ton is a unit of mass equal to 2,000 pounds (907.18474 kg), that is most commonly used in the United States – known there simply as the ton.
        """
        
        LongTon = 'long_ton'
        """
            Long ton (weight ton or Imperial ton) is a unit of mass equal to 2,240 pounds (1,016 kg) and is the name for the unit called the "ton" in the avoirdupois or Imperial system of measurements that was used in the United Kingdom and several other Commonwealth countries before metrication.
        """
        
        Pound = 'pound'
        """
            The pound or pound-mass (abbreviations: lb, lbm) is a unit of mass used in the imperial, United States customary and other systems of measurement. A number of different definitions have been used, the most common today being the international avoirdupois pound which is legally defined as exactly 0.45359237 kilograms, and which is divided into 16 avoirdupois ounces.
        """
        
        Ounce = 'ounce'
        """
            The international avoirdupois ounce (abbreviated oz) is defined as exactly 28.349523125 g under the international yard and pound agreement of 1959, signed by the United States and countries of the Commonwealth of Nations. 16 oz make up an avoirdupois pound.
        """
        
        Slug = 'slug'
        """
            The slug (abbreviation slug) is a unit of mass that is accelerated by 1 ft/s² when a force of one pound (lbf) is exerted on it.
        """
        
        Stone = 'stone'
        """
            The stone (abbreviation st) is a unit of mass equal to 14 pounds avoirdupois (about 6.35 kilograms) used in Great Britain and Ireland for measuring human body weight.
        """
        
        ShortHundredweight = 'short_hundredweight'
        """
            The short hundredweight (abbreviation cwt) is a unit of mass equal to 100 pounds in US and Canada. In British English, the short hundredweight is referred to as the "cental".
        """
        
        LongHundredweight = 'long_hundredweight'
        """
            The long or imperial hundredweight (abbreviation cwt) is a unit of mass equal to 112 pounds in US and Canada.
        """
        
        Grain = 'grain'
        """
            A grain is a unit of measurement of mass, and in the troy weight, avoirdupois, and Apothecaries' system, equal to exactly 64.79891 milligrams.
        """
        
        SolarMass = 'solar_mass'
        """
            Solar mass is a ratio unit to the mass of the solar system star, the sun.
        """
        
        EarthMass = 'earth_mass'
        """
            Earth mass is a ratio unit to the mass of planet Earth.
        """
        
        NanoGram = 'nano_gram'
        """
            
        """
        
        MicroGram = 'micro_gram'
        """
            
        """
        
        MilliGram = 'milli_gram'
        """
            
        """
        
        CentiGram = 'centi_gram'
        """
            
        """
        
        DeciGram = 'deci_gram'
        """
            
        """
        
        DecaGram = 'deca_gram'
        """
            
        """
        
        HectoGram = 'hecto_gram'
        """
            
        """
        
        KiloGram = 'kilo_gram'
        """
            
        """
        
        KiloTonne = 'kilo_tonne'
        """
            
        """
        
        MegaTonne = 'mega_tonne'
        """
            
        """
        
        KiloPound = 'kilo_pound'
        """
            
        """
        
        MegaPound = 'mega_pound'
        """
            
        """
        

class Mass:
    """
    In physics, mass (from Greek μᾶζα "barley cake, lump [of dough]") is a property of a physical system or body, giving rise to the phenomena of the body's resistance to being accelerated by a force and the strength of its mutual gravitational attraction with other bodies. Instruments such as mass balances or scales use those phenomena to measure mass. The SI unit of mass is the kilogram (kg).

    Args:
        value (float): The value.
        from_unit (MassUnits): The Mass unit to create from, The default unit is Kilogram
    """
    def __init__(self, value: float, from_unit: MassUnits = MassUnits.Kilogram):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__grams = None
        
        self.__tonnes = None
        
        self.__short_tons = None
        
        self.__long_tons = None
        
        self.__pounds = None
        
        self.__ounces = None
        
        self.__slugs = None
        
        self.__stone = None
        
        self.__short_hundredweight = None
        
        self.__long_hundredweight = None
        
        self.__grains = None
        
        self.__solar_masses = None
        
        self.__earth_masses = None
        
        self.__nano_grams = None
        
        self.__micro_grams = None
        
        self.__milli_grams = None
        
        self.__centi_grams = None
        
        self.__deci_grams = None
        
        self.__deca_grams = None
        
        self.__hecto_grams = None
        
        self.__kilo_grams = None
        
        self.__kilo_tonnes = None
        
        self.__mega_tonnes = None
        
        self.__kilo_pounds = None
        
        self.__mega_pounds = None
        

    def __convert_from_base(self, from_unit: MassUnits) -> float:
        value = self.__value
        
        if from_unit == MassUnits.Gram:
            return (value * 1e3)
        
        if from_unit == MassUnits.Tonne:
            return (value / 1e3)
        
        if from_unit == MassUnits.ShortTon:
            return (value / 9.0718474e2)
        
        if from_unit == MassUnits.LongTon:
            return (value / 1.0160469088e3)
        
        if from_unit == MassUnits.Pound:
            return (value / 0.45359237)
        
        if from_unit == MassUnits.Ounce:
            return (value / 0.028349523125)
        
        if from_unit == MassUnits.Slug:
            return (value * 6.852176556196105e-2)
        
        if from_unit == MassUnits.Stone:
            return (value * 0.1574731728702698)
        
        if from_unit == MassUnits.ShortHundredweight:
            return (value * 0.022046226218487758)
        
        if from_unit == MassUnits.LongHundredweight:
            return (value * 0.01968413055222121)
        
        if from_unit == MassUnits.Grain:
            return (value * 15432.358352941431)
        
        if from_unit == MassUnits.SolarMass:
            return (value / 1.98947e30)
        
        if from_unit == MassUnits.EarthMass:
            return (value / 5.9722e+24)
        
        if from_unit == MassUnits.NanoGram:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == MassUnits.MicroGram:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MassUnits.MilliGram:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassUnits.CentiGram:
            return ((value * 1e3) / 0.01)
        
        if from_unit == MassUnits.DeciGram:
            return ((value * 1e3) / 0.1)
        
        if from_unit == MassUnits.DecaGram:
            return ((value * 1e3) / 10.0)
        
        if from_unit == MassUnits.HectoGram:
            return ((value * 1e3) / 100.0)
        
        if from_unit == MassUnits.KiloGram:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassUnits.KiloTonne:
            return ((value / 1e3) / 1000.0)
        
        if from_unit == MassUnits.MegaTonne:
            return ((value / 1e3) / 1000000.0)
        
        if from_unit == MassUnits.KiloPound:
            return ((value / 0.45359237) / 1000.0)
        
        if from_unit == MassUnits.MegaPound:
            return ((value / 0.45359237) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: MassUnits) -> float:
        
        if to_unit == MassUnits.Gram:
            return (value / 1e3)
        
        if to_unit == MassUnits.Tonne:
            return (value * 1e3)
        
        if to_unit == MassUnits.ShortTon:
            return (value * 9.0718474e2)
        
        if to_unit == MassUnits.LongTon:
            return (value * 1.0160469088e3)
        
        if to_unit == MassUnits.Pound:
            return (value * 0.45359237)
        
        if to_unit == MassUnits.Ounce:
            return (value * 0.028349523125)
        
        if to_unit == MassUnits.Slug:
            return (value / 6.852176556196105e-2)
        
        if to_unit == MassUnits.Stone:
            return (value / 0.1574731728702698)
        
        if to_unit == MassUnits.ShortHundredweight:
            return (value / 0.022046226218487758)
        
        if to_unit == MassUnits.LongHundredweight:
            return (value / 0.01968413055222121)
        
        if to_unit == MassUnits.Grain:
            return (value / 15432.358352941431)
        
        if to_unit == MassUnits.SolarMass:
            return (value * 1.98947e30)
        
        if to_unit == MassUnits.EarthMass:
            return (value * 5.9722e+24)
        
        if to_unit == MassUnits.NanoGram:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == MassUnits.MicroGram:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MassUnits.MilliGram:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassUnits.CentiGram:
            return ((value / 1e3) * 0.01)
        
        if to_unit == MassUnits.DeciGram:
            return ((value / 1e3) * 0.1)
        
        if to_unit == MassUnits.DecaGram:
            return ((value / 1e3) * 10.0)
        
        if to_unit == MassUnits.HectoGram:
            return ((value / 1e3) * 100.0)
        
        if to_unit == MassUnits.KiloGram:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassUnits.KiloTonne:
            return ((value * 1e3) * 1000.0)
        
        if to_unit == MassUnits.MegaTonne:
            return ((value * 1e3) * 1000000.0)
        
        if to_unit == MassUnits.KiloPound:
            return ((value * 0.45359237) * 1000.0)
        
        if to_unit == MassUnits.MegaPound:
            return ((value * 0.45359237) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_grams(grams: float):
        """
        Create a new instance of Mass from a value in grams.

        

        :param meters: The Mass value in grams.
        :type grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(grams, MassUnits.Gram)

    
    @staticmethod
    def from_tonnes(tonnes: float):
        """
        Create a new instance of Mass from a value in tonnes.

        

        :param meters: The Mass value in tonnes.
        :type tonnes: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(tonnes, MassUnits.Tonne)

    
    @staticmethod
    def from_short_tons(short_tons: float):
        """
        Create a new instance of Mass from a value in short_tons.

        The short ton is a unit of mass equal to 2,000 pounds (907.18474 kg), that is most commonly used in the United States – known there simply as the ton.

        :param meters: The Mass value in short_tons.
        :type short_tons: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(short_tons, MassUnits.ShortTon)

    
    @staticmethod
    def from_long_tons(long_tons: float):
        """
        Create a new instance of Mass from a value in long_tons.

        Long ton (weight ton or Imperial ton) is a unit of mass equal to 2,240 pounds (1,016 kg) and is the name for the unit called the "ton" in the avoirdupois or Imperial system of measurements that was used in the United Kingdom and several other Commonwealth countries before metrication.

        :param meters: The Mass value in long_tons.
        :type long_tons: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(long_tons, MassUnits.LongTon)

    
    @staticmethod
    def from_pounds(pounds: float):
        """
        Create a new instance of Mass from a value in pounds.

        The pound or pound-mass (abbreviations: lb, lbm) is a unit of mass used in the imperial, United States customary and other systems of measurement. A number of different definitions have been used, the most common today being the international avoirdupois pound which is legally defined as exactly 0.45359237 kilograms, and which is divided into 16 avoirdupois ounces.

        :param meters: The Mass value in pounds.
        :type pounds: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(pounds, MassUnits.Pound)

    
    @staticmethod
    def from_ounces(ounces: float):
        """
        Create a new instance of Mass from a value in ounces.

        The international avoirdupois ounce (abbreviated oz) is defined as exactly 28.349523125 g under the international yard and pound agreement of 1959, signed by the United States and countries of the Commonwealth of Nations. 16 oz make up an avoirdupois pound.

        :param meters: The Mass value in ounces.
        :type ounces: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(ounces, MassUnits.Ounce)

    
    @staticmethod
    def from_slugs(slugs: float):
        """
        Create a new instance of Mass from a value in slugs.

        The slug (abbreviation slug) is a unit of mass that is accelerated by 1 ft/s² when a force of one pound (lbf) is exerted on it.

        :param meters: The Mass value in slugs.
        :type slugs: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(slugs, MassUnits.Slug)

    
    @staticmethod
    def from_stone(stone: float):
        """
        Create a new instance of Mass from a value in stone.

        The stone (abbreviation st) is a unit of mass equal to 14 pounds avoirdupois (about 6.35 kilograms) used in Great Britain and Ireland for measuring human body weight.

        :param meters: The Mass value in stone.
        :type stone: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(stone, MassUnits.Stone)

    
    @staticmethod
    def from_short_hundredweight(short_hundredweight: float):
        """
        Create a new instance of Mass from a value in short_hundredweight.

        The short hundredweight (abbreviation cwt) is a unit of mass equal to 100 pounds in US and Canada. In British English, the short hundredweight is referred to as the "cental".

        :param meters: The Mass value in short_hundredweight.
        :type short_hundredweight: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(short_hundredweight, MassUnits.ShortHundredweight)

    
    @staticmethod
    def from_long_hundredweight(long_hundredweight: float):
        """
        Create a new instance of Mass from a value in long_hundredweight.

        The long or imperial hundredweight (abbreviation cwt) is a unit of mass equal to 112 pounds in US and Canada.

        :param meters: The Mass value in long_hundredweight.
        :type long_hundredweight: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(long_hundredweight, MassUnits.LongHundredweight)

    
    @staticmethod
    def from_grains(grains: float):
        """
        Create a new instance of Mass from a value in grains.

        A grain is a unit of measurement of mass, and in the troy weight, avoirdupois, and Apothecaries' system, equal to exactly 64.79891 milligrams.

        :param meters: The Mass value in grains.
        :type grains: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(grains, MassUnits.Grain)

    
    @staticmethod
    def from_solar_masses(solar_masses: float):
        """
        Create a new instance of Mass from a value in solar_masses.

        Solar mass is a ratio unit to the mass of the solar system star, the sun.

        :param meters: The Mass value in solar_masses.
        :type solar_masses: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(solar_masses, MassUnits.SolarMass)

    
    @staticmethod
    def from_earth_masses(earth_masses: float):
        """
        Create a new instance of Mass from a value in earth_masses.

        Earth mass is a ratio unit to the mass of planet Earth.

        :param meters: The Mass value in earth_masses.
        :type earth_masses: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(earth_masses, MassUnits.EarthMass)

    
    @staticmethod
    def from_nano_grams(nano_grams: float):
        """
        Create a new instance of Mass from a value in nano_grams.

        

        :param meters: The Mass value in nano_grams.
        :type nano_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(nano_grams, MassUnits.NanoGram)

    
    @staticmethod
    def from_micro_grams(micro_grams: float):
        """
        Create a new instance of Mass from a value in micro_grams.

        

        :param meters: The Mass value in micro_grams.
        :type micro_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(micro_grams, MassUnits.MicroGram)

    
    @staticmethod
    def from_milli_grams(milli_grams: float):
        """
        Create a new instance of Mass from a value in milli_grams.

        

        :param meters: The Mass value in milli_grams.
        :type milli_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(milli_grams, MassUnits.MilliGram)

    
    @staticmethod
    def from_centi_grams(centi_grams: float):
        """
        Create a new instance of Mass from a value in centi_grams.

        

        :param meters: The Mass value in centi_grams.
        :type centi_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(centi_grams, MassUnits.CentiGram)

    
    @staticmethod
    def from_deci_grams(deci_grams: float):
        """
        Create a new instance of Mass from a value in deci_grams.

        

        :param meters: The Mass value in deci_grams.
        :type deci_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(deci_grams, MassUnits.DeciGram)

    
    @staticmethod
    def from_deca_grams(deca_grams: float):
        """
        Create a new instance of Mass from a value in deca_grams.

        

        :param meters: The Mass value in deca_grams.
        :type deca_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(deca_grams, MassUnits.DecaGram)

    
    @staticmethod
    def from_hecto_grams(hecto_grams: float):
        """
        Create a new instance of Mass from a value in hecto_grams.

        

        :param meters: The Mass value in hecto_grams.
        :type hecto_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(hecto_grams, MassUnits.HectoGram)

    
    @staticmethod
    def from_kilo_grams(kilo_grams: float):
        """
        Create a new instance of Mass from a value in kilo_grams.

        

        :param meters: The Mass value in kilo_grams.
        :type kilo_grams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(kilo_grams, MassUnits.KiloGram)

    
    @staticmethod
    def from_kilo_tonnes(kilo_tonnes: float):
        """
        Create a new instance of Mass from a value in kilo_tonnes.

        

        :param meters: The Mass value in kilo_tonnes.
        :type kilo_tonnes: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(kilo_tonnes, MassUnits.KiloTonne)

    
    @staticmethod
    def from_mega_tonnes(mega_tonnes: float):
        """
        Create a new instance of Mass from a value in mega_tonnes.

        

        :param meters: The Mass value in mega_tonnes.
        :type mega_tonnes: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(mega_tonnes, MassUnits.MegaTonne)

    
    @staticmethod
    def from_kilo_pounds(kilo_pounds: float):
        """
        Create a new instance of Mass from a value in kilo_pounds.

        

        :param meters: The Mass value in kilo_pounds.
        :type kilo_pounds: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(kilo_pounds, MassUnits.KiloPound)

    
    @staticmethod
    def from_mega_pounds(mega_pounds: float):
        """
        Create a new instance of Mass from a value in mega_pounds.

        

        :param meters: The Mass value in mega_pounds.
        :type mega_pounds: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(mega_pounds, MassUnits.MegaPound)

    
    @property
    def grams(self) -> float:
        """
        
        """
        if self.__grams != None:
            return self.__grams
        self.__grams = self.__convert_from_base(MassUnits.Gram)
        return self.__grams

    
    @property
    def tonnes(self) -> float:
        """
        
        """
        if self.__tonnes != None:
            return self.__tonnes
        self.__tonnes = self.__convert_from_base(MassUnits.Tonne)
        return self.__tonnes

    
    @property
    def short_tons(self) -> float:
        """
        The short ton is a unit of mass equal to 2,000 pounds (907.18474 kg), that is most commonly used in the United States – known there simply as the ton.
        """
        if self.__short_tons != None:
            return self.__short_tons
        self.__short_tons = self.__convert_from_base(MassUnits.ShortTon)
        return self.__short_tons

    
    @property
    def long_tons(self) -> float:
        """
        Long ton (weight ton or Imperial ton) is a unit of mass equal to 2,240 pounds (1,016 kg) and is the name for the unit called the "ton" in the avoirdupois or Imperial system of measurements that was used in the United Kingdom and several other Commonwealth countries before metrication.
        """
        if self.__long_tons != None:
            return self.__long_tons
        self.__long_tons = self.__convert_from_base(MassUnits.LongTon)
        return self.__long_tons

    
    @property
    def pounds(self) -> float:
        """
        The pound or pound-mass (abbreviations: lb, lbm) is a unit of mass used in the imperial, United States customary and other systems of measurement. A number of different definitions have been used, the most common today being the international avoirdupois pound which is legally defined as exactly 0.45359237 kilograms, and which is divided into 16 avoirdupois ounces.
        """
        if self.__pounds != None:
            return self.__pounds
        self.__pounds = self.__convert_from_base(MassUnits.Pound)
        return self.__pounds

    
    @property
    def ounces(self) -> float:
        """
        The international avoirdupois ounce (abbreviated oz) is defined as exactly 28.349523125 g under the international yard and pound agreement of 1959, signed by the United States and countries of the Commonwealth of Nations. 16 oz make up an avoirdupois pound.
        """
        if self.__ounces != None:
            return self.__ounces
        self.__ounces = self.__convert_from_base(MassUnits.Ounce)
        return self.__ounces

    
    @property
    def slugs(self) -> float:
        """
        The slug (abbreviation slug) is a unit of mass that is accelerated by 1 ft/s² when a force of one pound (lbf) is exerted on it.
        """
        if self.__slugs != None:
            return self.__slugs
        self.__slugs = self.__convert_from_base(MassUnits.Slug)
        return self.__slugs

    
    @property
    def stone(self) -> float:
        """
        The stone (abbreviation st) is a unit of mass equal to 14 pounds avoirdupois (about 6.35 kilograms) used in Great Britain and Ireland for measuring human body weight.
        """
        if self.__stone != None:
            return self.__stone
        self.__stone = self.__convert_from_base(MassUnits.Stone)
        return self.__stone

    
    @property
    def short_hundredweight(self) -> float:
        """
        The short hundredweight (abbreviation cwt) is a unit of mass equal to 100 pounds in US and Canada. In British English, the short hundredweight is referred to as the "cental".
        """
        if self.__short_hundredweight != None:
            return self.__short_hundredweight
        self.__short_hundredweight = self.__convert_from_base(MassUnits.ShortHundredweight)
        return self.__short_hundredweight

    
    @property
    def long_hundredweight(self) -> float:
        """
        The long or imperial hundredweight (abbreviation cwt) is a unit of mass equal to 112 pounds in US and Canada.
        """
        if self.__long_hundredweight != None:
            return self.__long_hundredweight
        self.__long_hundredweight = self.__convert_from_base(MassUnits.LongHundredweight)
        return self.__long_hundredweight

    
    @property
    def grains(self) -> float:
        """
        A grain is a unit of measurement of mass, and in the troy weight, avoirdupois, and Apothecaries' system, equal to exactly 64.79891 milligrams.
        """
        if self.__grains != None:
            return self.__grains
        self.__grains = self.__convert_from_base(MassUnits.Grain)
        return self.__grains

    
    @property
    def solar_masses(self) -> float:
        """
        Solar mass is a ratio unit to the mass of the solar system star, the sun.
        """
        if self.__solar_masses != None:
            return self.__solar_masses
        self.__solar_masses = self.__convert_from_base(MassUnits.SolarMass)
        return self.__solar_masses

    
    @property
    def earth_masses(self) -> float:
        """
        Earth mass is a ratio unit to the mass of planet Earth.
        """
        if self.__earth_masses != None:
            return self.__earth_masses
        self.__earth_masses = self.__convert_from_base(MassUnits.EarthMass)
        return self.__earth_masses

    
    @property
    def nano_grams(self) -> float:
        """
        
        """
        if self.__nano_grams != None:
            return self.__nano_grams
        self.__nano_grams = self.__convert_from_base(MassUnits.NanoGram)
        return self.__nano_grams

    
    @property
    def micro_grams(self) -> float:
        """
        
        """
        if self.__micro_grams != None:
            return self.__micro_grams
        self.__micro_grams = self.__convert_from_base(MassUnits.MicroGram)
        return self.__micro_grams

    
    @property
    def milli_grams(self) -> float:
        """
        
        """
        if self.__milli_grams != None:
            return self.__milli_grams
        self.__milli_grams = self.__convert_from_base(MassUnits.MilliGram)
        return self.__milli_grams

    
    @property
    def centi_grams(self) -> float:
        """
        
        """
        if self.__centi_grams != None:
            return self.__centi_grams
        self.__centi_grams = self.__convert_from_base(MassUnits.CentiGram)
        return self.__centi_grams

    
    @property
    def deci_grams(self) -> float:
        """
        
        """
        if self.__deci_grams != None:
            return self.__deci_grams
        self.__deci_grams = self.__convert_from_base(MassUnits.DeciGram)
        return self.__deci_grams

    
    @property
    def deca_grams(self) -> float:
        """
        
        """
        if self.__deca_grams != None:
            return self.__deca_grams
        self.__deca_grams = self.__convert_from_base(MassUnits.DecaGram)
        return self.__deca_grams

    
    @property
    def hecto_grams(self) -> float:
        """
        
        """
        if self.__hecto_grams != None:
            return self.__hecto_grams
        self.__hecto_grams = self.__convert_from_base(MassUnits.HectoGram)
        return self.__hecto_grams

    
    @property
    def kilo_grams(self) -> float:
        """
        
        """
        if self.__kilo_grams != None:
            return self.__kilo_grams
        self.__kilo_grams = self.__convert_from_base(MassUnits.KiloGram)
        return self.__kilo_grams

    
    @property
    def kilo_tonnes(self) -> float:
        """
        
        """
        if self.__kilo_tonnes != None:
            return self.__kilo_tonnes
        self.__kilo_tonnes = self.__convert_from_base(MassUnits.KiloTonne)
        return self.__kilo_tonnes

    
    @property
    def mega_tonnes(self) -> float:
        """
        
        """
        if self.__mega_tonnes != None:
            return self.__mega_tonnes
        self.__mega_tonnes = self.__convert_from_base(MassUnits.MegaTonne)
        return self.__mega_tonnes

    
    @property
    def kilo_pounds(self) -> float:
        """
        
        """
        if self.__kilo_pounds != None:
            return self.__kilo_pounds
        self.__kilo_pounds = self.__convert_from_base(MassUnits.KiloPound)
        return self.__kilo_pounds

    
    @property
    def mega_pounds(self) -> float:
        """
        
        """
        if self.__mega_pounds != None:
            return self.__mega_pounds
        self.__mega_pounds = self.__convert_from_base(MassUnits.MegaPound)
        return self.__mega_pounds

    
    def to_string(self, unit: MassUnits = MassUnits.Kilogram) -> string:
        """
        Format the Mass to string.
        Note! the default format for Mass is Kilogram.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == MassUnits.Gram:
            return f"""{self.grams} g"""
        
        if unit == MassUnits.Tonne:
            return f"""{self.tonnes} t"""
        
        if unit == MassUnits.ShortTon:
            return f"""{self.short_tons} t (short)"""
        
        if unit == MassUnits.LongTon:
            return f"""{self.long_tons} long tn"""
        
        if unit == MassUnits.Pound:
            return f"""{self.pounds} lb"""
        
        if unit == MassUnits.Ounce:
            return f"""{self.ounces} oz"""
        
        if unit == MassUnits.Slug:
            return f"""{self.slugs} slug"""
        
        if unit == MassUnits.Stone:
            return f"""{self.stone} st"""
        
        if unit == MassUnits.ShortHundredweight:
            return f"""{self.short_hundredweight} cwt"""
        
        if unit == MassUnits.LongHundredweight:
            return f"""{self.long_hundredweight} cwt"""
        
        if unit == MassUnits.Grain:
            return f"""{self.grains} gr"""
        
        if unit == MassUnits.SolarMass:
            return f"""{self.solar_masses} M☉"""
        
        if unit == MassUnits.EarthMass:
            return f"""{self.earth_masses} em"""
        
        if unit == MassUnits.NanoGram:
            return f"""{self.nano_grams} """
        
        if unit == MassUnits.MicroGram:
            return f"""{self.micro_grams} """
        
        if unit == MassUnits.MilliGram:
            return f"""{self.milli_grams} """
        
        if unit == MassUnits.CentiGram:
            return f"""{self.centi_grams} """
        
        if unit == MassUnits.DeciGram:
            return f"""{self.deci_grams} """
        
        if unit == MassUnits.DecaGram:
            return f"""{self.deca_grams} """
        
        if unit == MassUnits.HectoGram:
            return f"""{self.hecto_grams} """
        
        if unit == MassUnits.KiloGram:
            return f"""{self.kilo_grams} """
        
        if unit == MassUnits.KiloTonne:
            return f"""{self.kilo_tonnes} """
        
        if unit == MassUnits.MegaTonne:
            return f"""{self.mega_tonnes} """
        
        if unit == MassUnits.KiloPound:
            return f"""{self.kilo_pounds} """
        
        if unit == MassUnits.MegaPound:
            return f"""{self.mega_pounds} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassUnits = MassUnits.Kilogram) -> string:
        """
        Get Mass unit abbreviation.
        Note! the default abbreviation for Mass is Kilogram.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == MassUnits.Gram:
            return """g"""
        
        if unit_abbreviation == MassUnits.Tonne:
            return """t"""
        
        if unit_abbreviation == MassUnits.ShortTon:
            return """t (short)"""
        
        if unit_abbreviation == MassUnits.LongTon:
            return """long tn"""
        
        if unit_abbreviation == MassUnits.Pound:
            return """lb"""
        
        if unit_abbreviation == MassUnits.Ounce:
            return """oz"""
        
        if unit_abbreviation == MassUnits.Slug:
            return """slug"""
        
        if unit_abbreviation == MassUnits.Stone:
            return """st"""
        
        if unit_abbreviation == MassUnits.ShortHundredweight:
            return """cwt"""
        
        if unit_abbreviation == MassUnits.LongHundredweight:
            return """cwt"""
        
        if unit_abbreviation == MassUnits.Grain:
            return """gr"""
        
        if unit_abbreviation == MassUnits.SolarMass:
            return """M☉"""
        
        if unit_abbreviation == MassUnits.EarthMass:
            return """em"""
        
        if unit_abbreviation == MassUnits.NanoGram:
            return """"""
        
        if unit_abbreviation == MassUnits.MicroGram:
            return """"""
        
        if unit_abbreviation == MassUnits.MilliGram:
            return """"""
        
        if unit_abbreviation == MassUnits.CentiGram:
            return """"""
        
        if unit_abbreviation == MassUnits.DeciGram:
            return """"""
        
        if unit_abbreviation == MassUnits.DecaGram:
            return """"""
        
        if unit_abbreviation == MassUnits.HectoGram:
            return """"""
        
        if unit_abbreviation == MassUnits.KiloGram:
            return """"""
        
        if unit_abbreviation == MassUnits.KiloTonne:
            return """"""
        
        if unit_abbreviation == MassUnits.MegaTonne:
            return """"""
        
        if unit_abbreviation == MassUnits.KiloPound:
            return """"""
        
        if unit_abbreviation == MassUnits.MegaPound:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for +: 'Mass' and '{}'".format(type(other).__name__))
        return Mass(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for *: 'Mass' and '{}'".format(type(other).__name__))
        return Mass(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for -: 'Mass' and '{}'".format(type(other).__name__))
        return Mass(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for /: 'Mass' and '{}'".format(type(other).__name__))
        return Mass(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for %: 'Mass' and '{}'".format(type(other).__name__))
        return Mass(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for **: 'Mass' and '{}'".format(type(other).__name__))
        return Mass(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for ==: 'Mass' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for <: 'Mass' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for >: 'Mass' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for <=: 'Mass' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Mass):
            raise TypeError("unsupported operand type(s) for >=: 'Mass' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value