from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class EnergyDensityUnits(Enum):
        """
            EnergyDensityUnits enumeration
        """
        
        JoulePerCubicMeter = 'joule_per_cubic_meter'
        """
            
        """
        
        WattHourPerCubicMeter = 'watt_hour_per_cubic_meter'
        """
            
        """
        
        KilojoulePerCubicMeter = 'kilojoule_per_cubic_meter'
        """
            
        """
        
        MegajoulePerCubicMeter = 'megajoule_per_cubic_meter'
        """
            
        """
        
        GigajoulePerCubicMeter = 'gigajoule_per_cubic_meter'
        """
            
        """
        
        TerajoulePerCubicMeter = 'terajoule_per_cubic_meter'
        """
            
        """
        
        PetajoulePerCubicMeter = 'petajoule_per_cubic_meter'
        """
            
        """
        
        KilowattHourPerCubicMeter = 'kilowatt_hour_per_cubic_meter'
        """
            
        """
        
        MegawattHourPerCubicMeter = 'megawatt_hour_per_cubic_meter'
        """
            
        """
        
        GigawattHourPerCubicMeter = 'gigawatt_hour_per_cubic_meter'
        """
            
        """
        
        TerawattHourPerCubicMeter = 'terawatt_hour_per_cubic_meter'
        """
            
        """
        
        PetawattHourPerCubicMeter = 'petawatt_hour_per_cubic_meter'
        """
            
        """
        

class EnergyDensity(AbstractMeasure):
    """
    None

    Args:
        value (float): The value.
        from_unit (EnergyDensityUnits): The EnergyDensity unit to create from, The default unit is JoulePerCubicMeter
    """
    def __init__(self, value: float, from_unit: EnergyDensityUnits = EnergyDensityUnits.JoulePerCubicMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__joules_per_cubic_meter = None
        
        self.__watt_hours_per_cubic_meter = None
        
        self.__kilojoules_per_cubic_meter = None
        
        self.__megajoules_per_cubic_meter = None
        
        self.__gigajoules_per_cubic_meter = None
        
        self.__terajoules_per_cubic_meter = None
        
        self.__petajoules_per_cubic_meter = None
        
        self.__kilowatt_hours_per_cubic_meter = None
        
        self.__megawatt_hours_per_cubic_meter = None
        
        self.__gigawatt_hours_per_cubic_meter = None
        
        self.__terawatt_hours_per_cubic_meter = None
        
        self.__petawatt_hours_per_cubic_meter = None
        

    def convert(self, unit: EnergyDensityUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: EnergyDensityUnits) -> float:
        value = self._value
        
        if from_unit == EnergyDensityUnits.JoulePerCubicMeter:
            return (value)
        
        if from_unit == EnergyDensityUnits.WattHourPerCubicMeter:
            return (value / 3.6e+3)
        
        if from_unit == EnergyDensityUnits.KilojoulePerCubicMeter:
            return ((value) / 1000.0)
        
        if from_unit == EnergyDensityUnits.MegajoulePerCubicMeter:
            return ((value) / 1000000.0)
        
        if from_unit == EnergyDensityUnits.GigajoulePerCubicMeter:
            return ((value) / 1000000000.0)
        
        if from_unit == EnergyDensityUnits.TerajoulePerCubicMeter:
            return ((value) / 1000000000000.0)
        
        if from_unit == EnergyDensityUnits.PetajoulePerCubicMeter:
            return ((value) / 1000000000000000.0)
        
        if from_unit == EnergyDensityUnits.KilowattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000.0)
        
        if from_unit == EnergyDensityUnits.MegawattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000.0)
        
        if from_unit == EnergyDensityUnits.GigawattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000000.0)
        
        if from_unit == EnergyDensityUnits.TerawattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000000000.0)
        
        if from_unit == EnergyDensityUnits.PetawattHourPerCubicMeter:
            return ((value / 3.6e+3) / 1000000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: EnergyDensityUnits) -> float:
        
        if to_unit == EnergyDensityUnits.JoulePerCubicMeter:
            return (value)
        
        if to_unit == EnergyDensityUnits.WattHourPerCubicMeter:
            return (value * 3.6e+3)
        
        if to_unit == EnergyDensityUnits.KilojoulePerCubicMeter:
            return ((value) * 1000.0)
        
        if to_unit == EnergyDensityUnits.MegajoulePerCubicMeter:
            return ((value) * 1000000.0)
        
        if to_unit == EnergyDensityUnits.GigajoulePerCubicMeter:
            return ((value) * 1000000000.0)
        
        if to_unit == EnergyDensityUnits.TerajoulePerCubicMeter:
            return ((value) * 1000000000000.0)
        
        if to_unit == EnergyDensityUnits.PetajoulePerCubicMeter:
            return ((value) * 1000000000000000.0)
        
        if to_unit == EnergyDensityUnits.KilowattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000.0)
        
        if to_unit == EnergyDensityUnits.MegawattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000.0)
        
        if to_unit == EnergyDensityUnits.GigawattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000000.0)
        
        if to_unit == EnergyDensityUnits.TerawattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000000000.0)
        
        if to_unit == EnergyDensityUnits.PetawattHourPerCubicMeter:
            return ((value * 3.6e+3) * 1000000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_joules_per_cubic_meter(joules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in joules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in joules_per_cubic_meter.
        :type joules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(joules_per_cubic_meter, EnergyDensityUnits.JoulePerCubicMeter)

    
    @staticmethod
    def from_watt_hours_per_cubic_meter(watt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in watt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in watt_hours_per_cubic_meter.
        :type watt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(watt_hours_per_cubic_meter, EnergyDensityUnits.WattHourPerCubicMeter)

    
    @staticmethod
    def from_kilojoules_per_cubic_meter(kilojoules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in kilojoules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in kilojoules_per_cubic_meter.
        :type kilojoules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(kilojoules_per_cubic_meter, EnergyDensityUnits.KilojoulePerCubicMeter)

    
    @staticmethod
    def from_megajoules_per_cubic_meter(megajoules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in megajoules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in megajoules_per_cubic_meter.
        :type megajoules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(megajoules_per_cubic_meter, EnergyDensityUnits.MegajoulePerCubicMeter)

    
    @staticmethod
    def from_gigajoules_per_cubic_meter(gigajoules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in gigajoules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in gigajoules_per_cubic_meter.
        :type gigajoules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(gigajoules_per_cubic_meter, EnergyDensityUnits.GigajoulePerCubicMeter)

    
    @staticmethod
    def from_terajoules_per_cubic_meter(terajoules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in terajoules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in terajoules_per_cubic_meter.
        :type terajoules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(terajoules_per_cubic_meter, EnergyDensityUnits.TerajoulePerCubicMeter)

    
    @staticmethod
    def from_petajoules_per_cubic_meter(petajoules_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in petajoules_per_cubic_meter.

        

        :param meters: The EnergyDensity value in petajoules_per_cubic_meter.
        :type petajoules_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(petajoules_per_cubic_meter, EnergyDensityUnits.PetajoulePerCubicMeter)

    
    @staticmethod
    def from_kilowatt_hours_per_cubic_meter(kilowatt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in kilowatt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in kilowatt_hours_per_cubic_meter.
        :type kilowatt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(kilowatt_hours_per_cubic_meter, EnergyDensityUnits.KilowattHourPerCubicMeter)

    
    @staticmethod
    def from_megawatt_hours_per_cubic_meter(megawatt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in megawatt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in megawatt_hours_per_cubic_meter.
        :type megawatt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(megawatt_hours_per_cubic_meter, EnergyDensityUnits.MegawattHourPerCubicMeter)

    
    @staticmethod
    def from_gigawatt_hours_per_cubic_meter(gigawatt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in gigawatt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in gigawatt_hours_per_cubic_meter.
        :type gigawatt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(gigawatt_hours_per_cubic_meter, EnergyDensityUnits.GigawattHourPerCubicMeter)

    
    @staticmethod
    def from_terawatt_hours_per_cubic_meter(terawatt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in terawatt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in terawatt_hours_per_cubic_meter.
        :type terawatt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(terawatt_hours_per_cubic_meter, EnergyDensityUnits.TerawattHourPerCubicMeter)

    
    @staticmethod
    def from_petawatt_hours_per_cubic_meter(petawatt_hours_per_cubic_meter: float):
        """
        Create a new instance of EnergyDensity from a value in petawatt_hours_per_cubic_meter.

        

        :param meters: The EnergyDensity value in petawatt_hours_per_cubic_meter.
        :type petawatt_hours_per_cubic_meter: float
        :return: A new instance of EnergyDensity.
        :rtype: EnergyDensity
        """
        return EnergyDensity(petawatt_hours_per_cubic_meter, EnergyDensityUnits.PetawattHourPerCubicMeter)

    
    @property
    def joules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__joules_per_cubic_meter != None:
            return self.__joules_per_cubic_meter
        self.__joules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.JoulePerCubicMeter)
        return self.__joules_per_cubic_meter

    
    @property
    def watt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__watt_hours_per_cubic_meter != None:
            return self.__watt_hours_per_cubic_meter
        self.__watt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.WattHourPerCubicMeter)
        return self.__watt_hours_per_cubic_meter

    
    @property
    def kilojoules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilojoules_per_cubic_meter != None:
            return self.__kilojoules_per_cubic_meter
        self.__kilojoules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.KilojoulePerCubicMeter)
        return self.__kilojoules_per_cubic_meter

    
    @property
    def megajoules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__megajoules_per_cubic_meter != None:
            return self.__megajoules_per_cubic_meter
        self.__megajoules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.MegajoulePerCubicMeter)
        return self.__megajoules_per_cubic_meter

    
    @property
    def gigajoules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__gigajoules_per_cubic_meter != None:
            return self.__gigajoules_per_cubic_meter
        self.__gigajoules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.GigajoulePerCubicMeter)
        return self.__gigajoules_per_cubic_meter

    
    @property
    def terajoules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__terajoules_per_cubic_meter != None:
            return self.__terajoules_per_cubic_meter
        self.__terajoules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.TerajoulePerCubicMeter)
        return self.__terajoules_per_cubic_meter

    
    @property
    def petajoules_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__petajoules_per_cubic_meter != None:
            return self.__petajoules_per_cubic_meter
        self.__petajoules_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.PetajoulePerCubicMeter)
        return self.__petajoules_per_cubic_meter

    
    @property
    def kilowatt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__kilowatt_hours_per_cubic_meter != None:
            return self.__kilowatt_hours_per_cubic_meter
        self.__kilowatt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.KilowattHourPerCubicMeter)
        return self.__kilowatt_hours_per_cubic_meter

    
    @property
    def megawatt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__megawatt_hours_per_cubic_meter != None:
            return self.__megawatt_hours_per_cubic_meter
        self.__megawatt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.MegawattHourPerCubicMeter)
        return self.__megawatt_hours_per_cubic_meter

    
    @property
    def gigawatt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__gigawatt_hours_per_cubic_meter != None:
            return self.__gigawatt_hours_per_cubic_meter
        self.__gigawatt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.GigawattHourPerCubicMeter)
        return self.__gigawatt_hours_per_cubic_meter

    
    @property
    def terawatt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__terawatt_hours_per_cubic_meter != None:
            return self.__terawatt_hours_per_cubic_meter
        self.__terawatt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.TerawattHourPerCubicMeter)
        return self.__terawatt_hours_per_cubic_meter

    
    @property
    def petawatt_hours_per_cubic_meter(self) -> float:
        """
        
        """
        if self.__petawatt_hours_per_cubic_meter != None:
            return self.__petawatt_hours_per_cubic_meter
        self.__petawatt_hours_per_cubic_meter = self.__convert_from_base(EnergyDensityUnits.PetawattHourPerCubicMeter)
        return self.__petawatt_hours_per_cubic_meter

    
    def to_string(self, unit: EnergyDensityUnits = EnergyDensityUnits.JoulePerCubicMeter) -> str:
        """
        Format the EnergyDensity to string.
        Note! the default format for EnergyDensity is JoulePerCubicMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == EnergyDensityUnits.JoulePerCubicMeter:
            return f"""{self.joules_per_cubic_meter} J/m³"""
        
        if unit == EnergyDensityUnits.WattHourPerCubicMeter:
            return f"""{self.watt_hours_per_cubic_meter} Wh/m³"""
        
        if unit == EnergyDensityUnits.KilojoulePerCubicMeter:
            return f"""{self.kilojoules_per_cubic_meter} kJ/m³"""
        
        if unit == EnergyDensityUnits.MegajoulePerCubicMeter:
            return f"""{self.megajoules_per_cubic_meter} MJ/m³"""
        
        if unit == EnergyDensityUnits.GigajoulePerCubicMeter:
            return f"""{self.gigajoules_per_cubic_meter} GJ/m³"""
        
        if unit == EnergyDensityUnits.TerajoulePerCubicMeter:
            return f"""{self.terajoules_per_cubic_meter} TJ/m³"""
        
        if unit == EnergyDensityUnits.PetajoulePerCubicMeter:
            return f"""{self.petajoules_per_cubic_meter} PJ/m³"""
        
        if unit == EnergyDensityUnits.KilowattHourPerCubicMeter:
            return f"""{self.kilowatt_hours_per_cubic_meter} kWh/m³"""
        
        if unit == EnergyDensityUnits.MegawattHourPerCubicMeter:
            return f"""{self.megawatt_hours_per_cubic_meter} MWh/m³"""
        
        if unit == EnergyDensityUnits.GigawattHourPerCubicMeter:
            return f"""{self.gigawatt_hours_per_cubic_meter} GWh/m³"""
        
        if unit == EnergyDensityUnits.TerawattHourPerCubicMeter:
            return f"""{self.terawatt_hours_per_cubic_meter} TWh/m³"""
        
        if unit == EnergyDensityUnits.PetawattHourPerCubicMeter:
            return f"""{self.petawatt_hours_per_cubic_meter} PWh/m³"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: EnergyDensityUnits = EnergyDensityUnits.JoulePerCubicMeter) -> str:
        """
        Get EnergyDensity unit abbreviation.
        Note! the default abbreviation for EnergyDensity is JoulePerCubicMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == EnergyDensityUnits.JoulePerCubicMeter:
            return """J/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.WattHourPerCubicMeter:
            return """Wh/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.KilojoulePerCubicMeter:
            return """kJ/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.MegajoulePerCubicMeter:
            return """MJ/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.GigajoulePerCubicMeter:
            return """GJ/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.TerajoulePerCubicMeter:
            return """TJ/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.PetajoulePerCubicMeter:
            return """PJ/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.KilowattHourPerCubicMeter:
            return """kWh/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.MegawattHourPerCubicMeter:
            return """MWh/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.GigawattHourPerCubicMeter:
            return """GWh/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.TerawattHourPerCubicMeter:
            return """TWh/m³"""
        
        if unit_abbreviation == EnergyDensityUnits.PetawattHourPerCubicMeter:
            return """PWh/m³"""
        