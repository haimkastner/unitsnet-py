from enum import Enum
import math
import string


class ForceUnits(Enum):
        """
            ForceUnits enumeration
        """
        
        Dyn = 'dyn'
        """
            
        """
        
        KilogramForce = 'kilogram_force'
        """
            
        """
        
        TonneForce = 'tonne_force'
        """
            
        """
        
        Newton = 'newton'
        """
            
        """
        
        KiloPond = 'kilo_pond'
        """
            
        """
        
        Poundal = 'poundal'
        """
            
        """
        
        PoundForce = 'pound_force'
        """
            
        """
        
        OunceForce = 'ounce_force'
        """
            
        """
        
        ShortTonForce = 'short_ton_force'
        """
            The short ton-force is a unit of force equal to 2,000 pounds-force (907.18474 kgf), that is most commonly used in the United States – known there simply as the ton or US ton.
        """
        
        MicroNewton = 'micro_newton'
        """
            
        """
        
        MilliNewton = 'milli_newton'
        """
            
        """
        
        DecaNewton = 'deca_newton'
        """
            
        """
        
        KiloNewton = 'kilo_newton'
        """
            
        """
        
        MegaNewton = 'mega_newton'
        """
            
        """
        
        KiloPoundForce = 'kilo_pound_force'
        """
            
        """
        
    
class Force:
    """
    In physics, a force is any influence that causes an object to undergo a certain change, either concerning its movement, direction, or geometrical construction. In other words, a force can cause an object with mass to change its velocity (which includes to begin moving from a state of rest), i.e., to accelerate, or a flexible object to deform, or both. Force can also be described by intuitive concepts such as a push or a pull. A force has both magnitude and direction, making it a vector quantity. It is measured in the SI unit of newtons and represented by the symbol F.

    Args:
        value (float): The value.
        from_unit (ForceUnits): The Force unit to create from, The default unit is Newton
    """
    def __init__(self, value: float, from_unit: ForceUnits = ForceUnits.Newton):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__dyne = None
        
        self.__kilograms_force = None
        
        self.__tonnes_force = None
        
        self.__newtons = None
        
        self.__kilo_ponds = None
        
        self.__poundals = None
        
        self.__pounds_force = None
        
        self.__ounce_force = None
        
        self.__short_tons_force = None
        
        self.__micro_newtons = None
        
        self.__milli_newtons = None
        
        self.__deca_newtons = None
        
        self.__kilo_newtons = None
        
        self.__mega_newtons = None
        
        self.__kilo_pounds_force = None
        

    def __convert_from_base(self, from_unit: ForceUnits) -> float:
        value = self.__value
        
        if from_unit == ForceUnits.Dyn:
            return (value * 1e5)
        
        if from_unit == ForceUnits.KilogramForce:
            return (value / 9.80665002864)
        
        if from_unit == ForceUnits.TonneForce:
            return (value / 9.80665002864e3)
        
        if from_unit == ForceUnits.Newton:
            return (value)
        
        if from_unit == ForceUnits.KiloPond:
            return (value / 9.80665002864)
        
        if from_unit == ForceUnits.Poundal:
            return (value / 0.13825502798973041652092282466083)
        
        if from_unit == ForceUnits.PoundForce:
            return (value / 4.4482216152605095551842641431421)
        
        if from_unit == ForceUnits.OunceForce:
            return (value / 2.780138509537812e-1)
        
        if from_unit == ForceUnits.ShortTonForce:
            return (value / 8.896443230521e3)
        
        if from_unit == ForceUnits.MicroNewton:
            return ((value) / 1e-06)
        
        if from_unit == ForceUnits.MilliNewton:
            return ((value) / 0.001)
        
        if from_unit == ForceUnits.DecaNewton:
            return ((value) / 10.0)
        
        if from_unit == ForceUnits.KiloNewton:
            return ((value) / 1000.0)
        
        if from_unit == ForceUnits.MegaNewton:
            return ((value) / 1000000.0)
        
        if from_unit == ForceUnits.KiloPoundForce:
            return ((value / 4.4482216152605095551842641431421) / 1000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ForceUnits) -> float:
        
        if to_unit == ForceUnits.Dyn:
            return (value / 1e5)
        
        if to_unit == ForceUnits.KilogramForce:
            return (value * 9.80665002864)
        
        if to_unit == ForceUnits.TonneForce:
            return (value * 9.80665002864e3)
        
        if to_unit == ForceUnits.Newton:
            return (value)
        
        if to_unit == ForceUnits.KiloPond:
            return (value * 9.80665002864)
        
        if to_unit == ForceUnits.Poundal:
            return (value * 0.13825502798973041652092282466083)
        
        if to_unit == ForceUnits.PoundForce:
            return (value * 4.4482216152605095551842641431421)
        
        if to_unit == ForceUnits.OunceForce:
            return (value * 2.780138509537812e-1)
        
        if to_unit == ForceUnits.ShortTonForce:
            return (value * 8.896443230521e3)
        
        if to_unit == ForceUnits.MicroNewton:
            return ((value) * 1e-06)
        
        if to_unit == ForceUnits.MilliNewton:
            return ((value) * 0.001)
        
        if to_unit == ForceUnits.DecaNewton:
            return ((value) * 10.0)
        
        if to_unit == ForceUnits.KiloNewton:
            return ((value) * 1000.0)
        
        if to_unit == ForceUnits.MegaNewton:
            return ((value) * 1000000.0)
        
        if to_unit == ForceUnits.KiloPoundForce:
            return ((value * 4.4482216152605095551842641431421) * 1000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_dyne(dyne: float):
        """
        Create a new instance of Force from a value in dyne.

        

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
    def from_micro_newtons(micro_newtons: float):
        """
        Create a new instance of Force from a value in micro_newtons.

        

        :param meters: The Force value in micro_newtons.
        :type micro_newtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(micro_newtons, ForceUnits.MicroNewton)

    
    @staticmethod
    def from_milli_newtons(milli_newtons: float):
        """
        Create a new instance of Force from a value in milli_newtons.

        

        :param meters: The Force value in milli_newtons.
        :type milli_newtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(milli_newtons, ForceUnits.MilliNewton)

    
    @staticmethod
    def from_deca_newtons(deca_newtons: float):
        """
        Create a new instance of Force from a value in deca_newtons.

        

        :param meters: The Force value in deca_newtons.
        :type deca_newtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(deca_newtons, ForceUnits.DecaNewton)

    
    @staticmethod
    def from_kilo_newtons(kilo_newtons: float):
        """
        Create a new instance of Force from a value in kilo_newtons.

        

        :param meters: The Force value in kilo_newtons.
        :type kilo_newtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(kilo_newtons, ForceUnits.KiloNewton)

    
    @staticmethod
    def from_mega_newtons(mega_newtons: float):
        """
        Create a new instance of Force from a value in mega_newtons.

        

        :param meters: The Force value in mega_newtons.
        :type mega_newtons: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(mega_newtons, ForceUnits.MegaNewton)

    
    @staticmethod
    def from_kilo_pounds_force(kilo_pounds_force: float):
        """
        Create a new instance of Force from a value in kilo_pounds_force.

        

        :param meters: The Force value in kilo_pounds_force.
        :type kilo_pounds_force: float
        :return: A new instance of Force.
        :rtype: Force
        """
        return Force(kilo_pounds_force, ForceUnits.KiloPoundForce)

    
    @property
    def dyne(self) -> float:
        """
        
        """
        if self.__dyne != None:
            return self.__dyne
        self.__dyne = self.__convert_from_base(ForceUnits.Dyn)
        return self.__dyne

    
    @property
    def kilograms_force(self) -> float:
        """
        
        """
        if self.__kilograms_force != None:
            return self.__kilograms_force
        self.__kilograms_force = self.__convert_from_base(ForceUnits.KilogramForce)
        return self.__kilograms_force

    
    @property
    def tonnes_force(self) -> float:
        """
        
        """
        if self.__tonnes_force != None:
            return self.__tonnes_force
        self.__tonnes_force = self.__convert_from_base(ForceUnits.TonneForce)
        return self.__tonnes_force

    
    @property
    def newtons(self) -> float:
        """
        
        """
        if self.__newtons != None:
            return self.__newtons
        self.__newtons = self.__convert_from_base(ForceUnits.Newton)
        return self.__newtons

    
    @property
    def kilo_ponds(self) -> float:
        """
        
        """
        if self.__kilo_ponds != None:
            return self.__kilo_ponds
        self.__kilo_ponds = self.__convert_from_base(ForceUnits.KiloPond)
        return self.__kilo_ponds

    
    @property
    def poundals(self) -> float:
        """
        
        """
        if self.__poundals != None:
            return self.__poundals
        self.__poundals = self.__convert_from_base(ForceUnits.Poundal)
        return self.__poundals

    
    @property
    def pounds_force(self) -> float:
        """
        
        """
        if self.__pounds_force != None:
            return self.__pounds_force
        self.__pounds_force = self.__convert_from_base(ForceUnits.PoundForce)
        return self.__pounds_force

    
    @property
    def ounce_force(self) -> float:
        """
        
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
    def micro_newtons(self) -> float:
        """
        
        """
        if self.__micro_newtons != None:
            return self.__micro_newtons
        self.__micro_newtons = self.__convert_from_base(ForceUnits.MicroNewton)
        return self.__micro_newtons

    
    @property
    def milli_newtons(self) -> float:
        """
        
        """
        if self.__milli_newtons != None:
            return self.__milli_newtons
        self.__milli_newtons = self.__convert_from_base(ForceUnits.MilliNewton)
        return self.__milli_newtons

    
    @property
    def deca_newtons(self) -> float:
        """
        
        """
        if self.__deca_newtons != None:
            return self.__deca_newtons
        self.__deca_newtons = self.__convert_from_base(ForceUnits.DecaNewton)
        return self.__deca_newtons

    
    @property
    def kilo_newtons(self) -> float:
        """
        
        """
        if self.__kilo_newtons != None:
            return self.__kilo_newtons
        self.__kilo_newtons = self.__convert_from_base(ForceUnits.KiloNewton)
        return self.__kilo_newtons

    
    @property
    def mega_newtons(self) -> float:
        """
        
        """
        if self.__mega_newtons != None:
            return self.__mega_newtons
        self.__mega_newtons = self.__convert_from_base(ForceUnits.MegaNewton)
        return self.__mega_newtons

    
    @property
    def kilo_pounds_force(self) -> float:
        """
        
        """
        if self.__kilo_pounds_force != None:
            return self.__kilo_pounds_force
        self.__kilo_pounds_force = self.__convert_from_base(ForceUnits.KiloPoundForce)
        return self.__kilo_pounds_force

    
    def to_string(self, unit: ForceUnits = ForceUnits.Newton) -> string:
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
        
        if unit == ForceUnits.MicroNewton:
            return f"""{self.micro_newtons} """
        
        if unit == ForceUnits.MilliNewton:
            return f"""{self.milli_newtons} """
        
        if unit == ForceUnits.DecaNewton:
            return f"""{self.deca_newtons} """
        
        if unit == ForceUnits.KiloNewton:
            return f"""{self.kilo_newtons} """
        
        if unit == ForceUnits.MegaNewton:
            return f"""{self.mega_newtons} """
        
        if unit == ForceUnits.KiloPoundForce:
            return f"""{self.kilo_pounds_force} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: ForceUnits = ForceUnits.Newton) -> string:
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
        
        if unit_abbreviation == ForceUnits.MicroNewton:
            return """"""
        
        if unit_abbreviation == ForceUnits.MilliNewton:
            return """"""
        
        if unit_abbreviation == ForceUnits.DecaNewton:
            return """"""
        
        if unit_abbreviation == ForceUnits.KiloNewton:
            return """"""
        
        if unit_abbreviation == ForceUnits.MegaNewton:
            return """"""
        
        if unit_abbreviation == ForceUnits.KiloPoundForce:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for +: 'Force' and '{}'".format(type(other).__name__))
        return Force(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for *: 'Force' and '{}'".format(type(other).__name__))
        return Force(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for -: 'Force' and '{}'".format(type(other).__name__))
        return Force(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for /: 'Force' and '{}'".format(type(other).__name__))
        return Force(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for %: 'Force' and '{}'".format(type(other).__name__))
        return Force(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for **: 'Force' and '{}'".format(type(other).__name__))
        return Force(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for ==: 'Force' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for <: 'Force' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for >: 'Force' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for <=: 'Force' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Force):
            raise TypeError("unsupported operand type(s) for >=: 'Force' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value