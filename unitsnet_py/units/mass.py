from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class MassUnits(Enum):
        """
            MassUnits enumeration
        """
        
        Gram = 'Gram'
        """
            
        """
        
        Tonne = 'Tonne'
        """
            
        """
        
        ShortTon = 'ShortTon'
        """
            The short ton is a unit of mass equal to 2,000 pounds (907.18474 kg), that is most commonly used in the United States – known there simply as the ton.
        """
        
        LongTon = 'LongTon'
        """
            Long ton (weight ton or Imperial ton) is a unit of mass equal to 2,240 pounds (1,016 kg) and is the name for the unit called the "ton" in the avoirdupois or Imperial system of measurements that was used in the United Kingdom and several other Commonwealth countries before metrication.
        """
        
        Pound = 'Pound'
        """
            The pound or pound-mass (abbreviations: lb, lbm) is a unit of mass used in the imperial, United States customary and other systems of measurement. A number of different definitions have been used, the most common today being the international avoirdupois pound which is legally defined as exactly 0.45359237 kilograms, and which is divided into 16 avoirdupois ounces.
        """
        
        Ounce = 'Ounce'
        """
            The international avoirdupois ounce (abbreviated oz) is defined as exactly 28.349523125 g under the international yard and pound agreement of 1959, signed by the United States and countries of the Commonwealth of Nations. 16 oz make up an avoirdupois pound.
        """
        
        Slug = 'Slug'
        """
            The slug (abbreviation slug) is a unit of mass that is accelerated by 1 ft/s² when a force of one pound (lbf) is exerted on it.
        """
        
        Stone = 'Stone'
        """
            The stone (abbreviation st) is a unit of mass equal to 14 pounds avoirdupois (about 6.35 kilograms) used in Great Britain and Ireland for measuring human body weight.
        """
        
        ShortHundredweight = 'ShortHundredweight'
        """
            The short hundredweight (abbreviation cwt) is a unit of mass equal to 100 pounds in US and Canada. In British English, the short hundredweight is referred to as the "cental".
        """
        
        LongHundredweight = 'LongHundredweight'
        """
            The long or imperial hundredweight (abbreviation cwt) is a unit of mass equal to 112 pounds in US and Canada.
        """
        
        Grain = 'Grain'
        """
            A grain is a unit of measurement of mass, and in the troy weight, avoirdupois, and Apothecaries' system, equal to exactly 64.79891 milligrams.
        """
        
        SolarMass = 'SolarMass'
        """
            Solar mass is a ratio unit to the mass of the solar system star, the sun.
        """
        
        EarthMass = 'EarthMass'
        """
            Earth mass is a ratio unit to the mass of planet Earth.
        """
        
        Femtogram = 'Femtogram'
        """
            
        """
        
        Picogram = 'Picogram'
        """
            
        """
        
        Nanogram = 'Nanogram'
        """
            
        """
        
        Microgram = 'Microgram'
        """
            
        """
        
        Milligram = 'Milligram'
        """
            
        """
        
        Centigram = 'Centigram'
        """
            
        """
        
        Decigram = 'Decigram'
        """
            
        """
        
        Decagram = 'Decagram'
        """
            
        """
        
        Hectogram = 'Hectogram'
        """
            
        """
        
        Kilogram = 'Kilogram'
        """
            
        """
        
        Kilotonne = 'Kilotonne'
        """
            
        """
        
        Megatonne = 'Megatonne'
        """
            
        """
        
        Kilopound = 'Kilopound'
        """
            
        """
        
        Megapound = 'Megapound'
        """
            
        """
        

class MassDto:
    """
    A DTO representation of a Mass

    Attributes:
        value (float): The value of the Mass.
        unit (MassUnits): The specific unit that the Mass value is representing.
    """

    def __init__(self, value: float, unit: MassUnits):
        """
        Create a new DTO representation of a Mass

        Parameters:
            value (float): The value of the Mass.
            unit (MassUnits): The specific unit that the Mass value is representing.
        """
        self.value: float = value
        """
        The value of the Mass
        """
        self.unit: MassUnits = unit
        """
        The specific unit that the Mass value is representing
        """

    def to_json(self):
        """
        Get a Mass DTO JSON object representing the current unit.

        :return: JSON object represents Mass DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Kilogram"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Mass DTO from a json representation.

        :param data: The Mass DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Kilogram"}
        :return: A new instance of MassDto.
        :rtype: MassDto
        """
        return MassDto(value=data["value"], unit=MassUnits(data["unit"]))


class Mass(AbstractMeasure):
    """
    In physics, mass (from Greek μᾶζα "barley cake, lump [of dough]") is a property of a physical system or body, giving rise to the phenomena of the body's resistance to being accelerated by a force and the strength of its mutual gravitational attraction with other bodies. Instruments such as mass balances or scales use those phenomena to measure mass. The SI unit of mass is the kilogram (kg).

    Args:
        value (float): The value.
        from_unit (MassUnits): The Mass unit to create from, The default unit is Kilogram
    """
    def __init__(self, value: float, from_unit: MassUnits = MassUnits.Kilogram):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
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
        
        self.__femtograms = None
        
        self.__picograms = None
        
        self.__nanograms = None
        
        self.__micrograms = None
        
        self.__milligrams = None
        
        self.__centigrams = None
        
        self.__decigrams = None
        
        self.__decagrams = None
        
        self.__hectograms = None
        
        self.__kilograms = None
        
        self.__kilotonnes = None
        
        self.__megatonnes = None
        
        self.__kilopounds = None
        
        self.__megapounds = None
        

    def convert(self, unit: MassUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: MassUnits = MassUnits.Kilogram) -> MassDto:
        """
        Get a new instance of Mass DTO representing the current unit.

        :param hold_in_unit: The specific Mass unit to store the Mass value in the DTO representation.
        :type hold_in_unit: MassUnits
        :return: A new instance of MassDto.
        :rtype: MassDto
        """
        return MassDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: MassUnits = MassUnits.Kilogram):
        """
        Get a Mass DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Mass unit to store the Mass value in the DTO representation.
        :type hold_in_unit: MassUnits
        :return: JSON object represents Mass DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Kilogram"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(mass_dto: MassDto):
        """
        Obtain a new instance of Mass from a DTO unit object.

        :param mass_dto: The Mass DTO representation.
        :type mass_dto: MassDto
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(mass_dto.value, mass_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Mass from a DTO unit json representation.

        :param data: The Mass DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Kilogram"}
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass.from_dto(MassDto.from_json(data))

    def __convert_from_base(self, from_unit: MassUnits) -> float:
        value = self._value
        
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
        
        if from_unit == MassUnits.Femtogram:
            return ((value * 1e3) / 1e-15)
        
        if from_unit == MassUnits.Picogram:
            return ((value * 1e3) / 1e-12)
        
        if from_unit == MassUnits.Nanogram:
            return ((value * 1e3) / 1e-09)
        
        if from_unit == MassUnits.Microgram:
            return ((value * 1e3) / 1e-06)
        
        if from_unit == MassUnits.Milligram:
            return ((value * 1e3) / 0.001)
        
        if from_unit == MassUnits.Centigram:
            return ((value * 1e3) / 0.01)
        
        if from_unit == MassUnits.Decigram:
            return ((value * 1e3) / 0.1)
        
        if from_unit == MassUnits.Decagram:
            return ((value * 1e3) / 10.0)
        
        if from_unit == MassUnits.Hectogram:
            return ((value * 1e3) / 100.0)
        
        if from_unit == MassUnits.Kilogram:
            return ((value * 1e3) / 1000.0)
        
        if from_unit == MassUnits.Kilotonne:
            return ((value / 1e3) / 1000.0)
        
        if from_unit == MassUnits.Megatonne:
            return ((value / 1e3) / 1000000.0)
        
        if from_unit == MassUnits.Kilopound:
            return ((value / 0.45359237) / 1000.0)
        
        if from_unit == MassUnits.Megapound:
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
        
        if to_unit == MassUnits.Femtogram:
            return ((value / 1e3) * 1e-15)
        
        if to_unit == MassUnits.Picogram:
            return ((value / 1e3) * 1e-12)
        
        if to_unit == MassUnits.Nanogram:
            return ((value / 1e3) * 1e-09)
        
        if to_unit == MassUnits.Microgram:
            return ((value / 1e3) * 1e-06)
        
        if to_unit == MassUnits.Milligram:
            return ((value / 1e3) * 0.001)
        
        if to_unit == MassUnits.Centigram:
            return ((value / 1e3) * 0.01)
        
        if to_unit == MassUnits.Decigram:
            return ((value / 1e3) * 0.1)
        
        if to_unit == MassUnits.Decagram:
            return ((value / 1e3) * 10.0)
        
        if to_unit == MassUnits.Hectogram:
            return ((value / 1e3) * 100.0)
        
        if to_unit == MassUnits.Kilogram:
            return ((value / 1e3) * 1000.0)
        
        if to_unit == MassUnits.Kilotonne:
            return ((value * 1e3) * 1000.0)
        
        if to_unit == MassUnits.Megatonne:
            return ((value * 1e3) * 1000000.0)
        
        if to_unit == MassUnits.Kilopound:
            return ((value * 0.45359237) * 1000.0)
        
        if to_unit == MassUnits.Megapound:
            return ((value * 0.45359237) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
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
    def from_femtograms(femtograms: float):
        """
        Create a new instance of Mass from a value in femtograms.

        

        :param meters: The Mass value in femtograms.
        :type femtograms: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(femtograms, MassUnits.Femtogram)

    
    @staticmethod
    def from_picograms(picograms: float):
        """
        Create a new instance of Mass from a value in picograms.

        

        :param meters: The Mass value in picograms.
        :type picograms: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(picograms, MassUnits.Picogram)

    
    @staticmethod
    def from_nanograms(nanograms: float):
        """
        Create a new instance of Mass from a value in nanograms.

        

        :param meters: The Mass value in nanograms.
        :type nanograms: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(nanograms, MassUnits.Nanogram)

    
    @staticmethod
    def from_micrograms(micrograms: float):
        """
        Create a new instance of Mass from a value in micrograms.

        

        :param meters: The Mass value in micrograms.
        :type micrograms: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(micrograms, MassUnits.Microgram)

    
    @staticmethod
    def from_milligrams(milligrams: float):
        """
        Create a new instance of Mass from a value in milligrams.

        

        :param meters: The Mass value in milligrams.
        :type milligrams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(milligrams, MassUnits.Milligram)

    
    @staticmethod
    def from_centigrams(centigrams: float):
        """
        Create a new instance of Mass from a value in centigrams.

        

        :param meters: The Mass value in centigrams.
        :type centigrams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(centigrams, MassUnits.Centigram)

    
    @staticmethod
    def from_decigrams(decigrams: float):
        """
        Create a new instance of Mass from a value in decigrams.

        

        :param meters: The Mass value in decigrams.
        :type decigrams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(decigrams, MassUnits.Decigram)

    
    @staticmethod
    def from_decagrams(decagrams: float):
        """
        Create a new instance of Mass from a value in decagrams.

        

        :param meters: The Mass value in decagrams.
        :type decagrams: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(decagrams, MassUnits.Decagram)

    
    @staticmethod
    def from_hectograms(hectograms: float):
        """
        Create a new instance of Mass from a value in hectograms.

        

        :param meters: The Mass value in hectograms.
        :type hectograms: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(hectograms, MassUnits.Hectogram)

    
    @staticmethod
    def from_kilograms(kilograms: float):
        """
        Create a new instance of Mass from a value in kilograms.

        

        :param meters: The Mass value in kilograms.
        :type kilograms: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(kilograms, MassUnits.Kilogram)

    
    @staticmethod
    def from_kilotonnes(kilotonnes: float):
        """
        Create a new instance of Mass from a value in kilotonnes.

        

        :param meters: The Mass value in kilotonnes.
        :type kilotonnes: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(kilotonnes, MassUnits.Kilotonne)

    
    @staticmethod
    def from_megatonnes(megatonnes: float):
        """
        Create a new instance of Mass from a value in megatonnes.

        

        :param meters: The Mass value in megatonnes.
        :type megatonnes: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(megatonnes, MassUnits.Megatonne)

    
    @staticmethod
    def from_kilopounds(kilopounds: float):
        """
        Create a new instance of Mass from a value in kilopounds.

        

        :param meters: The Mass value in kilopounds.
        :type kilopounds: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(kilopounds, MassUnits.Kilopound)

    
    @staticmethod
    def from_megapounds(megapounds: float):
        """
        Create a new instance of Mass from a value in megapounds.

        

        :param meters: The Mass value in megapounds.
        :type megapounds: float
        :return: A new instance of Mass.
        :rtype: Mass
        """
        return Mass(megapounds, MassUnits.Megapound)

    
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
    def femtograms(self) -> float:
        """
        
        """
        if self.__femtograms != None:
            return self.__femtograms
        self.__femtograms = self.__convert_from_base(MassUnits.Femtogram)
        return self.__femtograms

    
    @property
    def picograms(self) -> float:
        """
        
        """
        if self.__picograms != None:
            return self.__picograms
        self.__picograms = self.__convert_from_base(MassUnits.Picogram)
        return self.__picograms

    
    @property
    def nanograms(self) -> float:
        """
        
        """
        if self.__nanograms != None:
            return self.__nanograms
        self.__nanograms = self.__convert_from_base(MassUnits.Nanogram)
        return self.__nanograms

    
    @property
    def micrograms(self) -> float:
        """
        
        """
        if self.__micrograms != None:
            return self.__micrograms
        self.__micrograms = self.__convert_from_base(MassUnits.Microgram)
        return self.__micrograms

    
    @property
    def milligrams(self) -> float:
        """
        
        """
        if self.__milligrams != None:
            return self.__milligrams
        self.__milligrams = self.__convert_from_base(MassUnits.Milligram)
        return self.__milligrams

    
    @property
    def centigrams(self) -> float:
        """
        
        """
        if self.__centigrams != None:
            return self.__centigrams
        self.__centigrams = self.__convert_from_base(MassUnits.Centigram)
        return self.__centigrams

    
    @property
    def decigrams(self) -> float:
        """
        
        """
        if self.__decigrams != None:
            return self.__decigrams
        self.__decigrams = self.__convert_from_base(MassUnits.Decigram)
        return self.__decigrams

    
    @property
    def decagrams(self) -> float:
        """
        
        """
        if self.__decagrams != None:
            return self.__decagrams
        self.__decagrams = self.__convert_from_base(MassUnits.Decagram)
        return self.__decagrams

    
    @property
    def hectograms(self) -> float:
        """
        
        """
        if self.__hectograms != None:
            return self.__hectograms
        self.__hectograms = self.__convert_from_base(MassUnits.Hectogram)
        return self.__hectograms

    
    @property
    def kilograms(self) -> float:
        """
        
        """
        if self.__kilograms != None:
            return self.__kilograms
        self.__kilograms = self.__convert_from_base(MassUnits.Kilogram)
        return self.__kilograms

    
    @property
    def kilotonnes(self) -> float:
        """
        
        """
        if self.__kilotonnes != None:
            return self.__kilotonnes
        self.__kilotonnes = self.__convert_from_base(MassUnits.Kilotonne)
        return self.__kilotonnes

    
    @property
    def megatonnes(self) -> float:
        """
        
        """
        if self.__megatonnes != None:
            return self.__megatonnes
        self.__megatonnes = self.__convert_from_base(MassUnits.Megatonne)
        return self.__megatonnes

    
    @property
    def kilopounds(self) -> float:
        """
        
        """
        if self.__kilopounds != None:
            return self.__kilopounds
        self.__kilopounds = self.__convert_from_base(MassUnits.Kilopound)
        return self.__kilopounds

    
    @property
    def megapounds(self) -> float:
        """
        
        """
        if self.__megapounds != None:
            return self.__megapounds
        self.__megapounds = self.__convert_from_base(MassUnits.Megapound)
        return self.__megapounds

    
    def to_string(self, unit: MassUnits = MassUnits.Kilogram, fractional_digits: int = None) -> str:
        """
        Format the Mass to a string.
        
        Note: the default format for Mass is Kilogram.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Mass. Default is 'Kilogram'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == MassUnits.Gram:
            return f"""{super()._truncate_fraction_digits(self.grams, fractional_digits)} g"""
        
        if unit == MassUnits.Tonne:
            return f"""{super()._truncate_fraction_digits(self.tonnes, fractional_digits)} t"""
        
        if unit == MassUnits.ShortTon:
            return f"""{super()._truncate_fraction_digits(self.short_tons, fractional_digits)} t (short)"""
        
        if unit == MassUnits.LongTon:
            return f"""{super()._truncate_fraction_digits(self.long_tons, fractional_digits)} long tn"""
        
        if unit == MassUnits.Pound:
            return f"""{super()._truncate_fraction_digits(self.pounds, fractional_digits)} lb"""
        
        if unit == MassUnits.Ounce:
            return f"""{super()._truncate_fraction_digits(self.ounces, fractional_digits)} oz"""
        
        if unit == MassUnits.Slug:
            return f"""{super()._truncate_fraction_digits(self.slugs, fractional_digits)} slug"""
        
        if unit == MassUnits.Stone:
            return f"""{super()._truncate_fraction_digits(self.stone, fractional_digits)} st"""
        
        if unit == MassUnits.ShortHundredweight:
            return f"""{super()._truncate_fraction_digits(self.short_hundredweight, fractional_digits)} cwt"""
        
        if unit == MassUnits.LongHundredweight:
            return f"""{super()._truncate_fraction_digits(self.long_hundredweight, fractional_digits)} cwt"""
        
        if unit == MassUnits.Grain:
            return f"""{super()._truncate_fraction_digits(self.grains, fractional_digits)} gr"""
        
        if unit == MassUnits.SolarMass:
            return f"""{super()._truncate_fraction_digits(self.solar_masses, fractional_digits)} M☉"""
        
        if unit == MassUnits.EarthMass:
            return f"""{super()._truncate_fraction_digits(self.earth_masses, fractional_digits)} em"""
        
        if unit == MassUnits.Femtogram:
            return f"""{super()._truncate_fraction_digits(self.femtograms, fractional_digits)} fg"""
        
        if unit == MassUnits.Picogram:
            return f"""{super()._truncate_fraction_digits(self.picograms, fractional_digits)} pg"""
        
        if unit == MassUnits.Nanogram:
            return f"""{super()._truncate_fraction_digits(self.nanograms, fractional_digits)} ng"""
        
        if unit == MassUnits.Microgram:
            return f"""{super()._truncate_fraction_digits(self.micrograms, fractional_digits)} μg"""
        
        if unit == MassUnits.Milligram:
            return f"""{super()._truncate_fraction_digits(self.milligrams, fractional_digits)} mg"""
        
        if unit == MassUnits.Centigram:
            return f"""{super()._truncate_fraction_digits(self.centigrams, fractional_digits)} cg"""
        
        if unit == MassUnits.Decigram:
            return f"""{super()._truncate_fraction_digits(self.decigrams, fractional_digits)} dg"""
        
        if unit == MassUnits.Decagram:
            return f"""{super()._truncate_fraction_digits(self.decagrams, fractional_digits)} dag"""
        
        if unit == MassUnits.Hectogram:
            return f"""{super()._truncate_fraction_digits(self.hectograms, fractional_digits)} hg"""
        
        if unit == MassUnits.Kilogram:
            return f"""{super()._truncate_fraction_digits(self.kilograms, fractional_digits)} kg"""
        
        if unit == MassUnits.Kilotonne:
            return f"""{super()._truncate_fraction_digits(self.kilotonnes, fractional_digits)} kt"""
        
        if unit == MassUnits.Megatonne:
            return f"""{super()._truncate_fraction_digits(self.megatonnes, fractional_digits)} Mt"""
        
        if unit == MassUnits.Kilopound:
            return f"""{super()._truncate_fraction_digits(self.kilopounds, fractional_digits)} klb"""
        
        if unit == MassUnits.Megapound:
            return f"""{super()._truncate_fraction_digits(self.megapounds, fractional_digits)} Mlb"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: MassUnits = MassUnits.Kilogram) -> str:
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
        
        if unit_abbreviation == MassUnits.Femtogram:
            return """fg"""
        
        if unit_abbreviation == MassUnits.Picogram:
            return """pg"""
        
        if unit_abbreviation == MassUnits.Nanogram:
            return """ng"""
        
        if unit_abbreviation == MassUnits.Microgram:
            return """μg"""
        
        if unit_abbreviation == MassUnits.Milligram:
            return """mg"""
        
        if unit_abbreviation == MassUnits.Centigram:
            return """cg"""
        
        if unit_abbreviation == MassUnits.Decigram:
            return """dg"""
        
        if unit_abbreviation == MassUnits.Decagram:
            return """dag"""
        
        if unit_abbreviation == MassUnits.Hectogram:
            return """hg"""
        
        if unit_abbreviation == MassUnits.Kilogram:
            return """kg"""
        
        if unit_abbreviation == MassUnits.Kilotonne:
            return """kt"""
        
        if unit_abbreviation == MassUnits.Megatonne:
            return """Mt"""
        
        if unit_abbreviation == MassUnits.Kilopound:
            return """klb"""
        
        if unit_abbreviation == MassUnits.Megapound:
            return """Mlb"""
        