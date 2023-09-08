from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class AbsorbedDoseOfIonizingRadiationUnits(Enum):
        """
            AbsorbedDoseOfIonizingRadiationUnits enumeration
        """
        
        Gray = 'gray'
        """
            The gray is the unit of ionizing radiation dose in the SI, defined as the absorption of one joule of radiation energy per kilogram of matter.
        """
        
        Rad = 'rad'
        """
            The rad is a unit of absorbed radiation dose, defined as 1 rad = 0.01 Gy = 0.01 J/kg.
        """
        
        Femtogray = 'femtogray'
        """
            
        """
        
        Picogray = 'picogray'
        """
            
        """
        
        Nanogray = 'nanogray'
        """
            
        """
        
        Microgray = 'microgray'
        """
            
        """
        
        Milligray = 'milligray'
        """
            
        """
        
        Centigray = 'centigray'
        """
            
        """
        
        Kilogray = 'kilogray'
        """
            
        """
        
        Megagray = 'megagray'
        """
            
        """
        
        Gigagray = 'gigagray'
        """
            
        """
        
        Teragray = 'teragray'
        """
            
        """
        
        Petagray = 'petagray'
        """
            
        """
        
        Millirad = 'millirad'
        """
            
        """
        
        Kilorad = 'kilorad'
        """
            
        """
        
        Megarad = 'megarad'
        """
            
        """
        

class AbsorbedDoseOfIonizingRadiation(AbstractMeasure):
    """
    Absorbed dose is a dose quantity which is the measure of the energy deposited in matter by ionizing radiation per unit mass.

    Args:
        value (float): The value.
        from_unit (AbsorbedDoseOfIonizingRadiationUnits): The AbsorbedDoseOfIonizingRadiation unit to create from, The default unit is Gray
    """
    def __init__(self, value: float, from_unit: AbsorbedDoseOfIonizingRadiationUnits = AbsorbedDoseOfIonizingRadiationUnits.Gray):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__grays = None
        
        self.__rads = None
        
        self.__femtograys = None
        
        self.__picograys = None
        
        self.__nanograys = None
        
        self.__micrograys = None
        
        self.__milligrays = None
        
        self.__centigrays = None
        
        self.__kilograys = None
        
        self.__megagrays = None
        
        self.__gigagrays = None
        
        self.__teragrays = None
        
        self.__petagrays = None
        
        self.__millirads = None
        
        self.__kilorads = None
        
        self.__megarads = None
        

    def convert(self, unit: AbsorbedDoseOfIonizingRadiationUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: AbsorbedDoseOfIonizingRadiationUnits) -> float:
        value = self._value
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Gray:
            return (value)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Rad:
            return (value * 100)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Femtogray:
            return ((value) / 1e-15)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Picogray:
            return ((value) / 1e-12)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Nanogray:
            return ((value) / 1e-09)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Microgray:
            return ((value) / 1e-06)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Milligray:
            return ((value) / 0.001)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Centigray:
            return ((value) / 0.01)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Kilogray:
            return ((value) / 1000.0)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Megagray:
            return ((value) / 1000000.0)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Gigagray:
            return ((value) / 1000000000.0)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Teragray:
            return ((value) / 1000000000000.0)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Petagray:
            return ((value) / 1000000000000000.0)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Millirad:
            return ((value * 100) / 0.001)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Kilorad:
            return ((value * 100) / 1000.0)
        
        if from_unit == AbsorbedDoseOfIonizingRadiationUnits.Megarad:
            return ((value * 100) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: AbsorbedDoseOfIonizingRadiationUnits) -> float:
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Gray:
            return (value)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Rad:
            return (value / 100)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Femtogray:
            return ((value) * 1e-15)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Picogray:
            return ((value) * 1e-12)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Nanogray:
            return ((value) * 1e-09)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Microgray:
            return ((value) * 1e-06)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Milligray:
            return ((value) * 0.001)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Centigray:
            return ((value) * 0.01)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Kilogray:
            return ((value) * 1000.0)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Megagray:
            return ((value) * 1000000.0)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Gigagray:
            return ((value) * 1000000000.0)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Teragray:
            return ((value) * 1000000000000.0)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Petagray:
            return ((value) * 1000000000000000.0)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Millirad:
            return ((value / 100) * 0.001)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Kilorad:
            return ((value / 100) * 1000.0)
        
        if to_unit == AbsorbedDoseOfIonizingRadiationUnits.Megarad:
            return ((value / 100) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_grays(grays: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in grays.

        The gray is the unit of ionizing radiation dose in the SI, defined as the absorption of one joule of radiation energy per kilogram of matter.

        :param meters: The AbsorbedDoseOfIonizingRadiation value in grays.
        :type grays: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(grays, AbsorbedDoseOfIonizingRadiationUnits.Gray)

    
    @staticmethod
    def from_rads(rads: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in rads.

        The rad is a unit of absorbed radiation dose, defined as 1 rad = 0.01 Gy = 0.01 J/kg.

        :param meters: The AbsorbedDoseOfIonizingRadiation value in rads.
        :type rads: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(rads, AbsorbedDoseOfIonizingRadiationUnits.Rad)

    
    @staticmethod
    def from_femtograys(femtograys: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in femtograys.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in femtograys.
        :type femtograys: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(femtograys, AbsorbedDoseOfIonizingRadiationUnits.Femtogray)

    
    @staticmethod
    def from_picograys(picograys: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in picograys.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in picograys.
        :type picograys: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(picograys, AbsorbedDoseOfIonizingRadiationUnits.Picogray)

    
    @staticmethod
    def from_nanograys(nanograys: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in nanograys.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in nanograys.
        :type nanograys: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(nanograys, AbsorbedDoseOfIonizingRadiationUnits.Nanogray)

    
    @staticmethod
    def from_micrograys(micrograys: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in micrograys.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in micrograys.
        :type micrograys: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(micrograys, AbsorbedDoseOfIonizingRadiationUnits.Microgray)

    
    @staticmethod
    def from_milligrays(milligrays: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in milligrays.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in milligrays.
        :type milligrays: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(milligrays, AbsorbedDoseOfIonizingRadiationUnits.Milligray)

    
    @staticmethod
    def from_centigrays(centigrays: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in centigrays.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in centigrays.
        :type centigrays: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(centigrays, AbsorbedDoseOfIonizingRadiationUnits.Centigray)

    
    @staticmethod
    def from_kilograys(kilograys: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in kilograys.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in kilograys.
        :type kilograys: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(kilograys, AbsorbedDoseOfIonizingRadiationUnits.Kilogray)

    
    @staticmethod
    def from_megagrays(megagrays: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in megagrays.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in megagrays.
        :type megagrays: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(megagrays, AbsorbedDoseOfIonizingRadiationUnits.Megagray)

    
    @staticmethod
    def from_gigagrays(gigagrays: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in gigagrays.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in gigagrays.
        :type gigagrays: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(gigagrays, AbsorbedDoseOfIonizingRadiationUnits.Gigagray)

    
    @staticmethod
    def from_teragrays(teragrays: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in teragrays.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in teragrays.
        :type teragrays: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(teragrays, AbsorbedDoseOfIonizingRadiationUnits.Teragray)

    
    @staticmethod
    def from_petagrays(petagrays: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in petagrays.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in petagrays.
        :type petagrays: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(petagrays, AbsorbedDoseOfIonizingRadiationUnits.Petagray)

    
    @staticmethod
    def from_millirads(millirads: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in millirads.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in millirads.
        :type millirads: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(millirads, AbsorbedDoseOfIonizingRadiationUnits.Millirad)

    
    @staticmethod
    def from_kilorads(kilorads: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in kilorads.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in kilorads.
        :type kilorads: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(kilorads, AbsorbedDoseOfIonizingRadiationUnits.Kilorad)

    
    @staticmethod
    def from_megarads(megarads: float):
        """
        Create a new instance of AbsorbedDoseOfIonizingRadiation from a value in megarads.

        

        :param meters: The AbsorbedDoseOfIonizingRadiation value in megarads.
        :type megarads: float
        :return: A new instance of AbsorbedDoseOfIonizingRadiation.
        :rtype: AbsorbedDoseOfIonizingRadiation
        """
        return AbsorbedDoseOfIonizingRadiation(megarads, AbsorbedDoseOfIonizingRadiationUnits.Megarad)

    
    @property
    def grays(self) -> float:
        """
        The gray is the unit of ionizing radiation dose in the SI, defined as the absorption of one joule of radiation energy per kilogram of matter.
        """
        if self.__grays != None:
            return self.__grays
        self.__grays = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Gray)
        return self.__grays

    
    @property
    def rads(self) -> float:
        """
        The rad is a unit of absorbed radiation dose, defined as 1 rad = 0.01 Gy = 0.01 J/kg.
        """
        if self.__rads != None:
            return self.__rads
        self.__rads = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Rad)
        return self.__rads

    
    @property
    def femtograys(self) -> float:
        """
        
        """
        if self.__femtograys != None:
            return self.__femtograys
        self.__femtograys = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Femtogray)
        return self.__femtograys

    
    @property
    def picograys(self) -> float:
        """
        
        """
        if self.__picograys != None:
            return self.__picograys
        self.__picograys = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Picogray)
        return self.__picograys

    
    @property
    def nanograys(self) -> float:
        """
        
        """
        if self.__nanograys != None:
            return self.__nanograys
        self.__nanograys = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Nanogray)
        return self.__nanograys

    
    @property
    def micrograys(self) -> float:
        """
        
        """
        if self.__micrograys != None:
            return self.__micrograys
        self.__micrograys = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Microgray)
        return self.__micrograys

    
    @property
    def milligrays(self) -> float:
        """
        
        """
        if self.__milligrays != None:
            return self.__milligrays
        self.__milligrays = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Milligray)
        return self.__milligrays

    
    @property
    def centigrays(self) -> float:
        """
        
        """
        if self.__centigrays != None:
            return self.__centigrays
        self.__centigrays = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Centigray)
        return self.__centigrays

    
    @property
    def kilograys(self) -> float:
        """
        
        """
        if self.__kilograys != None:
            return self.__kilograys
        self.__kilograys = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Kilogray)
        return self.__kilograys

    
    @property
    def megagrays(self) -> float:
        """
        
        """
        if self.__megagrays != None:
            return self.__megagrays
        self.__megagrays = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Megagray)
        return self.__megagrays

    
    @property
    def gigagrays(self) -> float:
        """
        
        """
        if self.__gigagrays != None:
            return self.__gigagrays
        self.__gigagrays = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Gigagray)
        return self.__gigagrays

    
    @property
    def teragrays(self) -> float:
        """
        
        """
        if self.__teragrays != None:
            return self.__teragrays
        self.__teragrays = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Teragray)
        return self.__teragrays

    
    @property
    def petagrays(self) -> float:
        """
        
        """
        if self.__petagrays != None:
            return self.__petagrays
        self.__petagrays = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Petagray)
        return self.__petagrays

    
    @property
    def millirads(self) -> float:
        """
        
        """
        if self.__millirads != None:
            return self.__millirads
        self.__millirads = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Millirad)
        return self.__millirads

    
    @property
    def kilorads(self) -> float:
        """
        
        """
        if self.__kilorads != None:
            return self.__kilorads
        self.__kilorads = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Kilorad)
        return self.__kilorads

    
    @property
    def megarads(self) -> float:
        """
        
        """
        if self.__megarads != None:
            return self.__megarads
        self.__megarads = self.__convert_from_base(AbsorbedDoseOfIonizingRadiationUnits.Megarad)
        return self.__megarads

    
    def to_string(self, unit: AbsorbedDoseOfIonizingRadiationUnits = AbsorbedDoseOfIonizingRadiationUnits.Gray) -> str:
        """
        Format the AbsorbedDoseOfIonizingRadiation to string.
        Note! the default format for AbsorbedDoseOfIonizingRadiation is Gray.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Gray:
            return f"""{self.grays} Gy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Rad:
            return f"""{self.rads} rad"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Femtogray:
            return f"""{self.femtograys} fGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Picogray:
            return f"""{self.picograys} pGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Nanogray:
            return f"""{self.nanograys} nGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Microgray:
            return f"""{self.micrograys} μGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Milligray:
            return f"""{self.milligrays} mGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Centigray:
            return f"""{self.centigrays} cGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Kilogray:
            return f"""{self.kilograys} kGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Megagray:
            return f"""{self.megagrays} MGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Gigagray:
            return f"""{self.gigagrays} GGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Teragray:
            return f"""{self.teragrays} TGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Petagray:
            return f"""{self.petagrays} PGy"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Millirad:
            return f"""{self.millirads} mrad"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Kilorad:
            return f"""{self.kilorads} krad"""
        
        if unit == AbsorbedDoseOfIonizingRadiationUnits.Megarad:
            return f"""{self.megarads} Mrad"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: AbsorbedDoseOfIonizingRadiationUnits = AbsorbedDoseOfIonizingRadiationUnits.Gray) -> str:
        """
        Get AbsorbedDoseOfIonizingRadiation unit abbreviation.
        Note! the default abbreviation for AbsorbedDoseOfIonizingRadiation is Gray.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Gray:
            return """Gy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Rad:
            return """rad"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Femtogray:
            return """fGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Picogray:
            return """pGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Nanogray:
            return """nGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Microgray:
            return """μGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Milligray:
            return """mGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Centigray:
            return """cGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Kilogray:
            return """kGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Megagray:
            return """MGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Gigagray:
            return """GGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Teragray:
            return """TGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Petagray:
            return """PGy"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Millirad:
            return """mrad"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Kilorad:
            return """krad"""
        
        if unit_abbreviation == AbsorbedDoseOfIonizingRadiationUnits.Megarad:
            return """Mrad"""
        