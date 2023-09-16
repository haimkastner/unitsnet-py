from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ForceUnits(Enum):
        """
            ForceUnits enumeration
        """
        
        Dyn = 'dyn'
        """
            One dyne is equal to 10 micronewtons, 10e−5 N or to 10 nsn (nanosthenes) in the old metre–tonne–second system of units.
        """
        
        KilogramForce = 'kilogram_force'
        """
            The kilogram-force, or kilopond, is equal to the magnitude of the force exerted on one kilogram of mass in a 9.80665 m/s2 gravitational field (standard gravity). Therefore, one kilogram-force is by definition equal to 9.80665 N.
        """
        
        TonneForce = 'tonne_force'
        """
            The tonne-force, metric ton-force, megagram-force, and megapond (Mp) are each 1000 kilograms-force.
        """
        
        Newton = 'newton'
        """
            The newton (symbol: N) is the unit of force in the International System of Units (SI). It is defined as 1 kg⋅m/s2, the force which gives a mass of 1 kilogram an acceleration of 1 metre per second per second.
        """
        
        KiloPond = 'kilo_pond'
        """
            The kilogram-force, or kilopond, is equal to the magnitude of the force exerted on one kilogram of mass in a 9.80665 m/s2 gravitational field (standard gravity). Therefore, one kilogram-force is by definition equal to 9.80665 N.
        """
        
        Poundal = 'poundal'
        """
            The poundal is defined as the force necessary to accelerate 1 pound-mass at 1 foot per second per second. 1 pdl = 0.138254954376 N exactly.
        """
        
        PoundForce = 'pound_force'
        """
            The standard values of acceleration of the standard gravitational field (gn) and the international avoirdupois pound (lb) result in a pound-force equal to 4.4482216152605 N.
        """
        
        OunceForce = 'ounce_force'
        """
            An ounce-force is 1⁄16 of a pound-force, or about 0.2780139 newtons.
        """
        
        ShortTonForce = 'short_ton_force'
        """
            The short ton-force is a unit of force equal to 2,000 pounds-force (907.18474 kgf), that is most commonly used in the United States – known there simply as the ton or US ton.
        """
        
        Micronewton = 'micronewton'
        """
            
        """
        
        Millinewton = 'millinewton'
        """
            
        """
        
        Decanewton = 'decanewton'
        """
            
        """
        
        Kilonewton = 'kilonewton'
        """
            
        """
        
        Meganewton = 'meganewton'
        """
            
        """
        
        KilopoundForce = 'kilopound_force'
        """
            
        """
        

class Force(AbstractMeasure):
    """
    In physics, a force is any influence that causes an object to undergo a certain change, either concerning its movement, direction, or geometrical construction. In other words, a force can cause an object with mass to change its velocity (which includes to begin moving from a state of rest), i.e., to accelerate, or a flexible object to deform, or both. Force can also be described by intuitive concepts such as a push or a pull. A force has both magnitude and direction, making it a vector quantity. It is measured in the SI unit of newtons and represented by the symbol F.

    Args:
        value (float): The value.
        from_unit (ForceUnits): The Force unit to create from, The default unit is Newton
    """
    def __init__(self, value: float, from_unit: ForceUnits = ForceUnits.Newton):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__dyne = None
        
        self.__kilograms_force = None
        
        self.__tonnes_force = None
        
        self.__newtons = None
        
        self.__kilo_ponds = None
        
        self.__poundals = None
        
        self.__pounds_force = None
        
        self.__ounce_force = None
        
        self.__short_tons_force = None
        
        self.__micronewtons = None
        
        self.__millinewtons = None
        
        self.__decanewtons = None
        
        self.__kilonewtons = None
        
        self.__meganewtons = None
        
        self.__kilopounds_force = None
        

    def convert(self, unit: ForceUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: ForceUnits) -> float:
        value = self._value
        
        if from_unit == ForceUnits.Dyn:
            return (value * 1e5)
        
        if from_unit == ForceUnits.KilogramForce:
            return (value / 9.80665)
        
        if from_unit == ForceUnits.TonneForce:
            return (value / (9.80665 * 1000))
        
        if from_unit == ForceUnits.Newton:
            return (value)
        
        if from_unit == ForceUnits.KiloPond:
            return (value / 9.80665)
        
        if from_unit == ForceUnits.Poundal:
            return (value / 0.138254954376)
        
        if from_unit == ForceUnits.PoundForce:
            return (value / 4.4482216152605)
        
        if from_unit == ForceUnits.OunceForce:
            return (value / (4.4482216152605 / 16))
        
        if from_unit == ForceUnits.ShortTonForce:
            return (value / (4.4482216152605 * 2000))
        
        if from_unit == ForceUnits.Micronewton:
            return ((value) / 1e-06)
        
        if from_unit == ForceUnits.Millinewton:
            return ((value) / 0.001)
        
        if from_unit == ForceUnits.Decanewton:
            return ((value) / 10.0)
        
        if from_unit == ForceUnits.Kilonewton:
            return ((value) / 1000.0)
        
        if from_unit == ForceUnits.Meganewton:
            return ((value) / 1000000.0)
        
        if from_unit == ForceUnits.KilopoundForce:
            return ((value / 4.4482216152605) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ForceUnits) -> float:
        
        if to_unit == ForceUnits.Dyn:
            return (value / 1e5)
        
        if to_unit == ForceUnits.KilogramForce:
            return (value * 9.80665)
        
        if to_unit == ForceUnits.TonneForce:
            return (value * (9.80665 * 1000))
        
        if to_unit == ForceUnits.Newton:
            return (value)
        
        if to_unit == ForceUnits.KiloPond:
            return (value * 9.80665)
        
        if to_unit == ForceUnits.Poundal:
            return (value * 0.138254954376)
        
        if to_unit == ForceUnits.PoundForce:
            return (value * 4.4482216152605)
        
        if to_unit == ForceUnits.OunceForce:
            return (value * (4.4482216152605 / 16))
        
        if to_unit == ForceUnits.ShortTonForce:
            return (value * (4.4482216152605 * 2000))
        
        if to_unit == ForceUnits.Micronewton:
            return ((value) * 1e-06)
        
        if to_unit == ForceUnits.Millinewton:
            return ((value) * 0.001)
        
        if to_unit == ForceUnits.Decanewton:
            return ((value) * 10.0)
        
        if to_unit == ForceUnits.Kilonewton:
            return ((value) * 1000.0)
        
        if to_unit == ForceUnits.Meganewton:
            return ((value) * 1000000.0)
        
        if to_unit == ForceUnits.KilopoundForce:
            return ((value * 4.4482216152605) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_dyne(dyne: float):
        """
        Create a new instance of Force from a value in dyne.

        One dyne is equal to 10 micronewtons, 10e−5 N or to 10 nsn (nanosthenes) in the old metre–tonne–second system of units.

        :param meters: The Force value in dyne.
        :type dyne: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(dyne, ForceUnits.Dyn)

    
    @staticmethod
    def from_kilograms_force(kilograms_force: float):
        """
        Create a new instance of Force from a value in kilograms_force.

        The kilogram-force, or kilopond, is equal to the magnitude of the force exerted on one kilogram of mass in a 9.80665 m/s2 gravitational field (standard gravity). Therefore, one kilogram-force is by definition equal to 9.80665 N.

        :param meters: The Force value in kilograms_force.
        :type kilograms_force: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(kilograms_force, ForceUnits.KilogramForce)

    
    @staticmethod
    def from_tonnes_force(tonnes_force: float):
        """
        Create a new instance of Force from a value in tonnes_force.

        The tonne-force, metric ton-force, megagram-force, and megapond (Mp) are each 1000 kilograms-force.

        :param meters: The Force value in tonnes_force.
        :type tonnes_force: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(tonnes_force, ForceUnits.TonneForce)

    
    @staticmethod
    def from_newtons(newtons: float):
        """
        Create a new instance of Force from a value in newtons.

        The newton (symbol: N) is the unit of force in the International System of Units (SI). It is defined as 1 kg⋅m/s2, the force which gives a mass of 1 kilogram an acceleration of 1 metre per second per second.

        :param meters: The Force value in newtons.
        :type newtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(newtons, ForceUnits.Newton)

    
    @staticmethod
    def from_kilo_ponds(kilo_ponds: float):
        """
        Create a new instance of Force from a value in kilo_ponds.

        The kilogram-force, or kilopond, is equal to the magnitude of the force exerted on one kilogram of mass in a 9.80665 m/s2 gravitational field (standard gravity). Therefore, one kilogram-force is by definition equal to 9.80665 N.

        :param meters: The Force value in kilo_ponds.
        :type kilo_ponds: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(kilo_ponds, ForceUnits.KiloPond)

    
    @staticmethod
    def from_poundals(poundals: float):
        """
        Create a new instance of Force from a value in poundals.

        The poundal is defined as the force necessary to accelerate 1 pound-mass at 1 foot per second per second. 1 pdl = 0.138254954376 N exactly.

        :param meters: The Force value in poundals.
        :type poundals: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(poundals, ForceUnits.Poundal)

    
    @staticmethod
    def from_pounds_force(pounds_force: float):
        """
        Create a new instance of Force from a value in pounds_force.

        The standard values of acceleration of the standard gravitational field (gn) and the international avoirdupois pound (lb) result in a pound-force equal to 4.4482216152605 N.

        :param meters: The Force value in pounds_force.
        :type pounds_force: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(pounds_force, ForceUnits.PoundForce)

    
    @staticmethod
    def from_ounce_force(ounce_force: float):
        """
        Create a new instance of Force from a value in ounce_force.

        An ounce-force is 1⁄16 of a pound-force, or about 0.2780139 newtons.

        :param meters: The Force value in ounce_force.
        :type ounce_force: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(ounce_force, ForceUnits.OunceForce)

    
    @staticmethod
    def from_short_tons_force(short_tons_force: float):
        """
        Create a new instance of Force from a value in short_tons_force.

        The short ton-force is a unit of force equal to 2,000 pounds-force (907.18474 kgf), that is most commonly used in the United States – known there simply as the ton or US ton.

        :param meters: The Force value in short_tons_force.
        :type short_tons_force: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(short_tons_force, ForceUnits.ShortTonForce)

    
    @staticmethod
    def from_micronewtons(micronewtons: float):
        """
        Create a new instance of Force from a value in micronewtons.

        

        :param meters: The Force value in micronewtons.
        :type micronewtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(micronewtons, ForceUnits.Micronewton)

    
    @staticmethod
    def from_millinewtons(millinewtons: float):
        """
        Create a new instance of Force from a value in millinewtons.

        

        :param meters: The Force value in millinewtons.
        :type millinewtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(millinewtons, ForceUnits.Millinewton)

    
    @staticmethod
    def from_decanewtons(decanewtons: float):
        """
        Create a new instance of Force from a value in decanewtons.

        

        :param meters: The Force value in decanewtons.
        :type decanewtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(decanewtons, ForceUnits.Decanewton)

    
    @staticmethod
    def from_kilonewtons(kilonewtons: float):
        """
        Create a new instance of Force from a value in kilonewtons.

        

        :param meters: The Force value in kilonewtons.
        :type kilonewtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(kilonewtons, ForceUnits.Kilonewton)

    
    @staticmethod
    def from_meganewtons(meganewtons: float):
        """
        Create a new instance of Force from a value in meganewtons.

        

        :param meters: The Force value in meganewtons.
        :type meganewtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(meganewtons, ForceUnits.Meganewton)

    
    @staticmethod
    def from_kilopounds_force(kilopounds_force: float):
        """
        Create a new instance of Force from a value in kilopounds_force.

        

        :param meters: The Force value in kilopounds_force.
        :type kilopounds_force: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(kilopounds_force, ForceUnits.KilopoundForce)

    
    @property
    def dyne(self) -> float:
        """
        One dyne is equal to 10 micronewtons, 10e−5 N or to 10 nsn (nanosthenes) in the old metre–tonne–second system of units.
        """
        if self.__dyne != None:
            return self.__dyne
        self.__dyne = self.__convert_from_base(ForceUnits.Dyn)
        return self.__dyne

    
    @property
    def kilograms_force(self) -> float:
        """
        The kilogram-force, or kilopond, is equal to the magnitude of the force exerted on one kilogram of mass in a 9.80665 m/s2 gravitational field (standard gravity). Therefore, one kilogram-force is by definition equal to 9.80665 N.
        """
        if self.__kilograms_force != None:
            return self.__kilograms_force
        self.__kilograms_force = self.__convert_from_base(ForceUnits.KilogramForce)
        return self.__kilograms_force

    
    @property
    def tonnes_force(self) -> float:
        """
        The tonne-force, metric ton-force, megagram-force, and megapond (Mp) are each 1000 kilograms-force.
        """
        if self.__tonnes_force != None:
            return self.__tonnes_force
        self.__tonnes_force = self.__convert_from_base(ForceUnits.TonneForce)
        return self.__tonnes_force

    
    @property
    def newtons(self) -> float:
        """
        The newton (symbol: N) is the unit of force in the International System of Units (SI). It is defined as 1 kg⋅m/s2, the force which gives a mass of 1 kilogram an acceleration of 1 metre per second per second.
        """
        if self.__newtons != None:
            return self.__newtons
        self.__newtons = self.__convert_from_base(ForceUnits.Newton)
        return self.__newtons

    
    @property
    def kilo_ponds(self) -> float:
        """
        The kilogram-force, or kilopond, is equal to the magnitude of the force exerted on one kilogram of mass in a 9.80665 m/s2 gravitational field (standard gravity). Therefore, one kilogram-force is by definition equal to 9.80665 N.
        """
        if self.__kilo_ponds != None:
            return self.__kilo_ponds
        self.__kilo_ponds = self.__convert_from_base(ForceUnits.KiloPond)
        return self.__kilo_ponds

    
    @property
    def poundals(self) -> float:
        """
        The poundal is defined as the force necessary to accelerate 1 pound-mass at 1 foot per second per second. 1 pdl = 0.138254954376 N exactly.
        """
        if self.__poundals != None:
            return self.__poundals
        self.__poundals = self.__convert_from_base(ForceUnits.Poundal)
        return self.__poundals

    
    @property
    def pounds_force(self) -> float:
        """
        The standard values of acceleration of the standard gravitational field (gn) and the international avoirdupois pound (lb) result in a pound-force equal to 4.4482216152605 N.
        """
        if self.__pounds_force != None:
            return self.__pounds_force
        self.__pounds_force = self.__convert_from_base(ForceUnits.PoundForce)
        return self.__pounds_force

    
    @property
    def ounce_force(self) -> float:
        """
        An ounce-force is 1⁄16 of a pound-force, or about 0.2780139 newtons.
        """
        if self.__ounce_force != None:
            return self.__ounce_force
        self.__ounce_force = self.__convert_from_base(ForceUnits.OunceForce)
        return self.__ounce_force

    
    @property
    def short_tons_force(self) -> float:
        """
        The short ton-force is a unit of force equal to 2,000 pounds-force (907.18474 kgf), that is most commonly used in the United States – known there simply as the ton or US ton.
        """
        if self.__short_tons_force != None:
            return self.__short_tons_force
        self.__short_tons_force = self.__convert_from_base(ForceUnits.ShortTonForce)
        return self.__short_tons_force

    
    @property
    def micronewtons(self) -> float:
        """
        
        """
        if self.__micronewtons != None:
            return self.__micronewtons
        self.__micronewtons = self.__convert_from_base(ForceUnits.Micronewton)
        return self.__micronewtons

    
    @property
    def millinewtons(self) -> float:
        """
        
        """
        if self.__millinewtons != None:
            return self.__millinewtons
        self.__millinewtons = self.__convert_from_base(ForceUnits.Millinewton)
        return self.__millinewtons

    
    @property
    def decanewtons(self) -> float:
        """
        
        """
        if self.__decanewtons != None:
            return self.__decanewtons
        self.__decanewtons = self.__convert_from_base(ForceUnits.Decanewton)
        return self.__decanewtons

    
    @property
    def kilonewtons(self) -> float:
        """
        
        """
        if self.__kilonewtons != None:
            return self.__kilonewtons
        self.__kilonewtons = self.__convert_from_base(ForceUnits.Kilonewton)
        return self.__kilonewtons

    
    @property
    def meganewtons(self) -> float:
        """
        
        """
        if self.__meganewtons != None:
            return self.__meganewtons
        self.__meganewtons = self.__convert_from_base(ForceUnits.Meganewton)
        return self.__meganewtons

    
    @property
    def kilopounds_force(self) -> float:
        """
        
        """
        if self.__kilopounds_force != None:
            return self.__kilopounds_force
        self.__kilopounds_force = self.__convert_from_base(ForceUnits.KilopoundForce)
        return self.__kilopounds_force

    
    def to_string(self, unit: ForceUnits = ForceUnits.Newton) -> str:
        """
        Format the Force to string.
        Note! the default format for Force is Newton.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == ForceUnits.Dyn:
            return f"""{self.dyne} dyn"""
        
        if unit == ForceUnits.KilogramForce:
            return f"""{self.kilograms_force} kgf"""
        
        if unit == ForceUnits.TonneForce:
            return f"""{self.tonnes_force} tf"""
        
        if unit == ForceUnits.Newton:
            return f"""{self.newtons} N"""
        
        if unit == ForceUnits.KiloPond:
            return f"""{self.kilo_ponds} kp"""
        
        if unit == ForceUnits.Poundal:
            return f"""{self.poundals} pdl"""
        
        if unit == ForceUnits.PoundForce:
            return f"""{self.pounds_force} lbf"""
        
        if unit == ForceUnits.OunceForce:
            return f"""{self.ounce_force} ozf"""
        
        if unit == ForceUnits.ShortTonForce:
            return f"""{self.short_tons_force} tf (short)"""
        
        if unit == ForceUnits.Micronewton:
            return f"""{self.micronewtons} μN"""
        
        if unit == ForceUnits.Millinewton:
            return f"""{self.millinewtons} mN"""
        
        if unit == ForceUnits.Decanewton:
            return f"""{self.decanewtons} daN"""
        
        if unit == ForceUnits.Kilonewton:
            return f"""{self.kilonewtons} kN"""
        
        if unit == ForceUnits.Meganewton:
            return f"""{self.meganewtons} MN"""
        
        if unit == ForceUnits.KilopoundForce:
            return f"""{self.kilopounds_force} klbf"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ForceUnits = ForceUnits.Newton) -> str:
        """
        Get Force unit abbreviation.
        Note! the default abbreviation for Force is Newton.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ForceUnits.Dyn:
            return """dyn"""
        
        if unit_abbreviation == ForceUnits.KilogramForce:
            return """kgf"""
        
        if unit_abbreviation == ForceUnits.TonneForce:
            return """tf"""
        
        if unit_abbreviation == ForceUnits.Newton:
            return """N"""
        
        if unit_abbreviation == ForceUnits.KiloPond:
            return """kp"""
        
        if unit_abbreviation == ForceUnits.Poundal:
            return """pdl"""
        
        if unit_abbreviation == ForceUnits.PoundForce:
            return """lbf"""
        
        if unit_abbreviation == ForceUnits.OunceForce:
            return """ozf"""
        
        if unit_abbreviation == ForceUnits.ShortTonForce:
            return """tf (short)"""
        
        if unit_abbreviation == ForceUnits.Micronewton:
            return """μN"""
        
        if unit_abbreviation == ForceUnits.Millinewton:
            return """mN"""
        
        if unit_abbreviation == ForceUnits.Decanewton:
            return """daN"""
        
        if unit_abbreviation == ForceUnits.Kilonewton:
            return """kN"""
        
        if unit_abbreviation == ForceUnits.Meganewton:
            return """MN"""
        
        if unit_abbreviation == ForceUnits.KilopoundForce:
            return """klbf"""
        