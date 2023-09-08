from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class PowerUnits(Enum):
        """
            PowerUnits enumeration
        """
        
        Watt = 'watt'
        """
            
        """
        
        MechanicalHorsepower = 'mechanical_horsepower'
        """
            
        """
        
        MetricHorsepower = 'metric_horsepower'
        """
            
        """
        
        ElectricalHorsepower = 'electrical_horsepower'
        """
            
        """
        
        BoilerHorsepower = 'boiler_horsepower'
        """
            
        """
        
        HydraulicHorsepower = 'hydraulic_horsepower'
        """
            
        """
        
        BritishThermalUnitPerHour = 'british_thermal_unit_per_hour'
        """
            
        """
        
        JoulePerHour = 'joule_per_hour'
        """
            
        """
        
        Femtowatt = 'femtowatt'
        """
            
        """
        
        Picowatt = 'picowatt'
        """
            
        """
        
        Nanowatt = 'nanowatt'
        """
            
        """
        
        Microwatt = 'microwatt'
        """
            
        """
        
        Milliwatt = 'milliwatt'
        """
            
        """
        
        Deciwatt = 'deciwatt'
        """
            
        """
        
        Decawatt = 'decawatt'
        """
            
        """
        
        Kilowatt = 'kilowatt'
        """
            
        """
        
        Megawatt = 'megawatt'
        """
            
        """
        
        Gigawatt = 'gigawatt'
        """
            
        """
        
        Terawatt = 'terawatt'
        """
            
        """
        
        Petawatt = 'petawatt'
        """
            
        """
        
        KilobritishThermalUnitPerHour = 'kilobritish_thermal_unit_per_hour'
        """
            
        """
        
        MegabritishThermalUnitPerHour = 'megabritish_thermal_unit_per_hour'
        """
            
        """
        
        MillijoulePerHour = 'millijoule_per_hour'
        """
            
        """
        
        KilojoulePerHour = 'kilojoule_per_hour'
        """
            
        """
        
        MegajoulePerHour = 'megajoule_per_hour'
        """
            
        """
        
        GigajoulePerHour = 'gigajoule_per_hour'
        """
            
        """
        

class Power(AbstractMeasure):
    """
    In physics, power is the rate of doing work. It is equivalent to an amount of energy consumed per unit time.

    Args:
        value (float): The value.
        from_unit (PowerUnits): The Power unit to create from, The default unit is Watt
    """
    def __init__(self, value: float, from_unit: PowerUnits = PowerUnits.Watt):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts = None
        
        self.__mechanical_horsepower = None
        
        self.__metric_horsepower = None
        
        self.__electrical_horsepower = None
        
        self.__boiler_horsepower = None
        
        self.__hydraulic_horsepower = None
        
        self.__british_thermal_units_per_hour = None
        
        self.__joules_per_hour = None
        
        self.__femtowatts = None
        
        self.__picowatts = None
        
        self.__nanowatts = None
        
        self.__microwatts = None
        
        self.__milliwatts = None
        
        self.__deciwatts = None
        
        self.__decawatts = None
        
        self.__kilowatts = None
        
        self.__megawatts = None
        
        self.__gigawatts = None
        
        self.__terawatts = None
        
        self.__petawatts = None
        
        self.__kilobritish_thermal_units_per_hour = None
        
        self.__megabritish_thermal_units_per_hour = None
        
        self.__millijoules_per_hour = None
        
        self.__kilojoules_per_hour = None
        
        self.__megajoules_per_hour = None
        
        self.__gigajoules_per_hour = None
        

    def convert(self, unit: PowerUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: PowerUnits) -> float:
        value = self._value
        
        if from_unit == PowerUnits.Watt:
            return (value)
        
        if from_unit == PowerUnits.MechanicalHorsepower:
            return (value / 745.69)
        
        if from_unit == PowerUnits.MetricHorsepower:
            return (value / 735.49875)
        
        if from_unit == PowerUnits.ElectricalHorsepower:
            return (value / 746)
        
        if from_unit == PowerUnits.BoilerHorsepower:
            return (value / 9812.5)
        
        if from_unit == PowerUnits.HydraulicHorsepower:
            return (value / 745.69988145)
        
        if from_unit == PowerUnits.BritishThermalUnitPerHour:
            return (value / 0.29307107017)
        
        if from_unit == PowerUnits.JoulePerHour:
            return (value * 3600)
        
        if from_unit == PowerUnits.Femtowatt:
            return ((value) / 1e-15)
        
        if from_unit == PowerUnits.Picowatt:
            return ((value) / 1e-12)
        
        if from_unit == PowerUnits.Nanowatt:
            return ((value) / 1e-09)
        
        if from_unit == PowerUnits.Microwatt:
            return ((value) / 1e-06)
        
        if from_unit == PowerUnits.Milliwatt:
            return ((value) / 0.001)
        
        if from_unit == PowerUnits.Deciwatt:
            return ((value) / 0.1)
        
        if from_unit == PowerUnits.Decawatt:
            return ((value) / 10.0)
        
        if from_unit == PowerUnits.Kilowatt:
            return ((value) / 1000.0)
        
        if from_unit == PowerUnits.Megawatt:
            return ((value) / 1000000.0)
        
        if from_unit == PowerUnits.Gigawatt:
            return ((value) / 1000000000.0)
        
        if from_unit == PowerUnits.Terawatt:
            return ((value) / 1000000000000.0)
        
        if from_unit == PowerUnits.Petawatt:
            return ((value) / 1000000000000000.0)
        
        if from_unit == PowerUnits.KilobritishThermalUnitPerHour:
            return ((value / 0.29307107017) / 1000.0)
        
        if from_unit == PowerUnits.MegabritishThermalUnitPerHour:
            return ((value / 0.29307107017) / 1000000.0)
        
        if from_unit == PowerUnits.MillijoulePerHour:
            return ((value * 3600) / 0.001)
        
        if from_unit == PowerUnits.KilojoulePerHour:
            return ((value * 3600) / 1000.0)
        
        if from_unit == PowerUnits.MegajoulePerHour:
            return ((value * 3600) / 1000000.0)
        
        if from_unit == PowerUnits.GigajoulePerHour:
            return ((value * 3600) / 1000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PowerUnits) -> float:
        
        if to_unit == PowerUnits.Watt:
            return (value)
        
        if to_unit == PowerUnits.MechanicalHorsepower:
            return (value * 745.69)
        
        if to_unit == PowerUnits.MetricHorsepower:
            return (value * 735.49875)
        
        if to_unit == PowerUnits.ElectricalHorsepower:
            return (value * 746)
        
        if to_unit == PowerUnits.BoilerHorsepower:
            return (value * 9812.5)
        
        if to_unit == PowerUnits.HydraulicHorsepower:
            return (value * 745.69988145)
        
        if to_unit == PowerUnits.BritishThermalUnitPerHour:
            return (value * 0.29307107017)
        
        if to_unit == PowerUnits.JoulePerHour:
            return (value / 3600)
        
        if to_unit == PowerUnits.Femtowatt:
            return ((value) * 1e-15)
        
        if to_unit == PowerUnits.Picowatt:
            return ((value) * 1e-12)
        
        if to_unit == PowerUnits.Nanowatt:
            return ((value) * 1e-09)
        
        if to_unit == PowerUnits.Microwatt:
            return ((value) * 1e-06)
        
        if to_unit == PowerUnits.Milliwatt:
            return ((value) * 0.001)
        
        if to_unit == PowerUnits.Deciwatt:
            return ((value) * 0.1)
        
        if to_unit == PowerUnits.Decawatt:
            return ((value) * 10.0)
        
        if to_unit == PowerUnits.Kilowatt:
            return ((value) * 1000.0)
        
        if to_unit == PowerUnits.Megawatt:
            return ((value) * 1000000.0)
        
        if to_unit == PowerUnits.Gigawatt:
            return ((value) * 1000000000.0)
        
        if to_unit == PowerUnits.Terawatt:
            return ((value) * 1000000000000.0)
        
        if to_unit == PowerUnits.Petawatt:
            return ((value) * 1000000000000000.0)
        
        if to_unit == PowerUnits.KilobritishThermalUnitPerHour:
            return ((value * 0.29307107017) * 1000.0)
        
        if to_unit == PowerUnits.MegabritishThermalUnitPerHour:
            return ((value * 0.29307107017) * 1000000.0)
        
        if to_unit == PowerUnits.MillijoulePerHour:
            return ((value / 3600) * 0.001)
        
        if to_unit == PowerUnits.KilojoulePerHour:
            return ((value / 3600) * 1000.0)
        
        if to_unit == PowerUnits.MegajoulePerHour:
            return ((value / 3600) * 1000000.0)
        
        if to_unit == PowerUnits.GigajoulePerHour:
            return ((value / 3600) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts(watts: float):
        """
        Create a new instance of Power from a value in watts.

        

        :param meters: The Power value in watts.
        :type watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(watts, PowerUnits.Watt)

    
    @staticmethod
    def from_mechanical_horsepower(mechanical_horsepower: float):
        """
        Create a new instance of Power from a value in mechanical_horsepower.

        

        :param meters: The Power value in mechanical_horsepower.
        :type mechanical_horsepower: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(mechanical_horsepower, PowerUnits.MechanicalHorsepower)

    
    @staticmethod
    def from_metric_horsepower(metric_horsepower: float):
        """
        Create a new instance of Power from a value in metric_horsepower.

        

        :param meters: The Power value in metric_horsepower.
        :type metric_horsepower: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(metric_horsepower, PowerUnits.MetricHorsepower)

    
    @staticmethod
    def from_electrical_horsepower(electrical_horsepower: float):
        """
        Create a new instance of Power from a value in electrical_horsepower.

        

        :param meters: The Power value in electrical_horsepower.
        :type electrical_horsepower: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(electrical_horsepower, PowerUnits.ElectricalHorsepower)

    
    @staticmethod
    def from_boiler_horsepower(boiler_horsepower: float):
        """
        Create a new instance of Power from a value in boiler_horsepower.

        

        :param meters: The Power value in boiler_horsepower.
        :type boiler_horsepower: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(boiler_horsepower, PowerUnits.BoilerHorsepower)

    
    @staticmethod
    def from_hydraulic_horsepower(hydraulic_horsepower: float):
        """
        Create a new instance of Power from a value in hydraulic_horsepower.

        

        :param meters: The Power value in hydraulic_horsepower.
        :type hydraulic_horsepower: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(hydraulic_horsepower, PowerUnits.HydraulicHorsepower)

    
    @staticmethod
    def from_british_thermal_units_per_hour(british_thermal_units_per_hour: float):
        """
        Create a new instance of Power from a value in british_thermal_units_per_hour.

        

        :param meters: The Power value in british_thermal_units_per_hour.
        :type british_thermal_units_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(british_thermal_units_per_hour, PowerUnits.BritishThermalUnitPerHour)

    
    @staticmethod
    def from_joules_per_hour(joules_per_hour: float):
        """
        Create a new instance of Power from a value in joules_per_hour.

        

        :param meters: The Power value in joules_per_hour.
        :type joules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(joules_per_hour, PowerUnits.JoulePerHour)

    
    @staticmethod
    def from_femtowatts(femtowatts: float):
        """
        Create a new instance of Power from a value in femtowatts.

        

        :param meters: The Power value in femtowatts.
        :type femtowatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(femtowatts, PowerUnits.Femtowatt)

    
    @staticmethod
    def from_picowatts(picowatts: float):
        """
        Create a new instance of Power from a value in picowatts.

        

        :param meters: The Power value in picowatts.
        :type picowatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(picowatts, PowerUnits.Picowatt)

    
    @staticmethod
    def from_nanowatts(nanowatts: float):
        """
        Create a new instance of Power from a value in nanowatts.

        

        :param meters: The Power value in nanowatts.
        :type nanowatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(nanowatts, PowerUnits.Nanowatt)

    
    @staticmethod
    def from_microwatts(microwatts: float):
        """
        Create a new instance of Power from a value in microwatts.

        

        :param meters: The Power value in microwatts.
        :type microwatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(microwatts, PowerUnits.Microwatt)

    
    @staticmethod
    def from_milliwatts(milliwatts: float):
        """
        Create a new instance of Power from a value in milliwatts.

        

        :param meters: The Power value in milliwatts.
        :type milliwatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(milliwatts, PowerUnits.Milliwatt)

    
    @staticmethod
    def from_deciwatts(deciwatts: float):
        """
        Create a new instance of Power from a value in deciwatts.

        

        :param meters: The Power value in deciwatts.
        :type deciwatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(deciwatts, PowerUnits.Deciwatt)

    
    @staticmethod
    def from_decawatts(decawatts: float):
        """
        Create a new instance of Power from a value in decawatts.

        

        :param meters: The Power value in decawatts.
        :type decawatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(decawatts, PowerUnits.Decawatt)

    
    @staticmethod
    def from_kilowatts(kilowatts: float):
        """
        Create a new instance of Power from a value in kilowatts.

        

        :param meters: The Power value in kilowatts.
        :type kilowatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(kilowatts, PowerUnits.Kilowatt)

    
    @staticmethod
    def from_megawatts(megawatts: float):
        """
        Create a new instance of Power from a value in megawatts.

        

        :param meters: The Power value in megawatts.
        :type megawatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(megawatts, PowerUnits.Megawatt)

    
    @staticmethod
    def from_gigawatts(gigawatts: float):
        """
        Create a new instance of Power from a value in gigawatts.

        

        :param meters: The Power value in gigawatts.
        :type gigawatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(gigawatts, PowerUnits.Gigawatt)

    
    @staticmethod
    def from_terawatts(terawatts: float):
        """
        Create a new instance of Power from a value in terawatts.

        

        :param meters: The Power value in terawatts.
        :type terawatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(terawatts, PowerUnits.Terawatt)

    
    @staticmethod
    def from_petawatts(petawatts: float):
        """
        Create a new instance of Power from a value in petawatts.

        

        :param meters: The Power value in petawatts.
        :type petawatts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(petawatts, PowerUnits.Petawatt)

    
    @staticmethod
    def from_kilobritish_thermal_units_per_hour(kilobritish_thermal_units_per_hour: float):
        """
        Create a new instance of Power from a value in kilobritish_thermal_units_per_hour.

        

        :param meters: The Power value in kilobritish_thermal_units_per_hour.
        :type kilobritish_thermal_units_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(kilobritish_thermal_units_per_hour, PowerUnits.KilobritishThermalUnitPerHour)

    
    @staticmethod
    def from_megabritish_thermal_units_per_hour(megabritish_thermal_units_per_hour: float):
        """
        Create a new instance of Power from a value in megabritish_thermal_units_per_hour.

        

        :param meters: The Power value in megabritish_thermal_units_per_hour.
        :type megabritish_thermal_units_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(megabritish_thermal_units_per_hour, PowerUnits.MegabritishThermalUnitPerHour)

    
    @staticmethod
    def from_millijoules_per_hour(millijoules_per_hour: float):
        """
        Create a new instance of Power from a value in millijoules_per_hour.

        

        :param meters: The Power value in millijoules_per_hour.
        :type millijoules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(millijoules_per_hour, PowerUnits.MillijoulePerHour)

    
    @staticmethod
    def from_kilojoules_per_hour(kilojoules_per_hour: float):
        """
        Create a new instance of Power from a value in kilojoules_per_hour.

        

        :param meters: The Power value in kilojoules_per_hour.
        :type kilojoules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(kilojoules_per_hour, PowerUnits.KilojoulePerHour)

    
    @staticmethod
    def from_megajoules_per_hour(megajoules_per_hour: float):
        """
        Create a new instance of Power from a value in megajoules_per_hour.

        

        :param meters: The Power value in megajoules_per_hour.
        :type megajoules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(megajoules_per_hour, PowerUnits.MegajoulePerHour)

    
    @staticmethod
    def from_gigajoules_per_hour(gigajoules_per_hour: float):
        """
        Create a new instance of Power from a value in gigajoules_per_hour.

        

        :param meters: The Power value in gigajoules_per_hour.
        :type gigajoules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(gigajoules_per_hour, PowerUnits.GigajoulePerHour)

    
    @property
    def watts(self) -> float:
        """
        
        """
        if self.__watts != None:
            return self.__watts
        self.__watts = self.__convert_from_base(PowerUnits.Watt)
        return self.__watts

    
    @property
    def mechanical_horsepower(self) -> float:
        """
        
        """
        if self.__mechanical_horsepower != None:
            return self.__mechanical_horsepower
        self.__mechanical_horsepower = self.__convert_from_base(PowerUnits.MechanicalHorsepower)
        return self.__mechanical_horsepower

    
    @property
    def metric_horsepower(self) -> float:
        """
        
        """
        if self.__metric_horsepower != None:
            return self.__metric_horsepower
        self.__metric_horsepower = self.__convert_from_base(PowerUnits.MetricHorsepower)
        return self.__metric_horsepower

    
    @property
    def electrical_horsepower(self) -> float:
        """
        
        """
        if self.__electrical_horsepower != None:
            return self.__electrical_horsepower
        self.__electrical_horsepower = self.__convert_from_base(PowerUnits.ElectricalHorsepower)
        return self.__electrical_horsepower

    
    @property
    def boiler_horsepower(self) -> float:
        """
        
        """
        if self.__boiler_horsepower != None:
            return self.__boiler_horsepower
        self.__boiler_horsepower = self.__convert_from_base(PowerUnits.BoilerHorsepower)
        return self.__boiler_horsepower

    
    @property
    def hydraulic_horsepower(self) -> float:
        """
        
        """
        if self.__hydraulic_horsepower != None:
            return self.__hydraulic_horsepower
        self.__hydraulic_horsepower = self.__convert_from_base(PowerUnits.HydraulicHorsepower)
        return self.__hydraulic_horsepower

    
    @property
    def british_thermal_units_per_hour(self) -> float:
        """
        
        """
        if self.__british_thermal_units_per_hour != None:
            return self.__british_thermal_units_per_hour
        self.__british_thermal_units_per_hour = self.__convert_from_base(PowerUnits.BritishThermalUnitPerHour)
        return self.__british_thermal_units_per_hour

    
    @property
    def joules_per_hour(self) -> float:
        """
        
        """
        if self.__joules_per_hour != None:
            return self.__joules_per_hour
        self.__joules_per_hour = self.__convert_from_base(PowerUnits.JoulePerHour)
        return self.__joules_per_hour

    
    @property
    def femtowatts(self) -> float:
        """
        
        """
        if self.__femtowatts != None:
            return self.__femtowatts
        self.__femtowatts = self.__convert_from_base(PowerUnits.Femtowatt)
        return self.__femtowatts

    
    @property
    def picowatts(self) -> float:
        """
        
        """
        if self.__picowatts != None:
            return self.__picowatts
        self.__picowatts = self.__convert_from_base(PowerUnits.Picowatt)
        return self.__picowatts

    
    @property
    def nanowatts(self) -> float:
        """
        
        """
        if self.__nanowatts != None:
            return self.__nanowatts
        self.__nanowatts = self.__convert_from_base(PowerUnits.Nanowatt)
        return self.__nanowatts

    
    @property
    def microwatts(self) -> float:
        """
        
        """
        if self.__microwatts != None:
            return self.__microwatts
        self.__microwatts = self.__convert_from_base(PowerUnits.Microwatt)
        return self.__microwatts

    
    @property
    def milliwatts(self) -> float:
        """
        
        """
        if self.__milliwatts != None:
            return self.__milliwatts
        self.__milliwatts = self.__convert_from_base(PowerUnits.Milliwatt)
        return self.__milliwatts

    
    @property
    def deciwatts(self) -> float:
        """
        
        """
        if self.__deciwatts != None:
            return self.__deciwatts
        self.__deciwatts = self.__convert_from_base(PowerUnits.Deciwatt)
        return self.__deciwatts

    
    @property
    def decawatts(self) -> float:
        """
        
        """
        if self.__decawatts != None:
            return self.__decawatts
        self.__decawatts = self.__convert_from_base(PowerUnits.Decawatt)
        return self.__decawatts

    
    @property
    def kilowatts(self) -> float:
        """
        
        """
        if self.__kilowatts != None:
            return self.__kilowatts
        self.__kilowatts = self.__convert_from_base(PowerUnits.Kilowatt)
        return self.__kilowatts

    
    @property
    def megawatts(self) -> float:
        """
        
        """
        if self.__megawatts != None:
            return self.__megawatts
        self.__megawatts = self.__convert_from_base(PowerUnits.Megawatt)
        return self.__megawatts

    
    @property
    def gigawatts(self) -> float:
        """
        
        """
        if self.__gigawatts != None:
            return self.__gigawatts
        self.__gigawatts = self.__convert_from_base(PowerUnits.Gigawatt)
        return self.__gigawatts

    
    @property
    def terawatts(self) -> float:
        """
        
        """
        if self.__terawatts != None:
            return self.__terawatts
        self.__terawatts = self.__convert_from_base(PowerUnits.Terawatt)
        return self.__terawatts

    
    @property
    def petawatts(self) -> float:
        """
        
        """
        if self.__petawatts != None:
            return self.__petawatts
        self.__petawatts = self.__convert_from_base(PowerUnits.Petawatt)
        return self.__petawatts

    
    @property
    def kilobritish_thermal_units_per_hour(self) -> float:
        """
        
        """
        if self.__kilobritish_thermal_units_per_hour != None:
            return self.__kilobritish_thermal_units_per_hour
        self.__kilobritish_thermal_units_per_hour = self.__convert_from_base(PowerUnits.KilobritishThermalUnitPerHour)
        return self.__kilobritish_thermal_units_per_hour

    
    @property
    def megabritish_thermal_units_per_hour(self) -> float:
        """
        
        """
        if self.__megabritish_thermal_units_per_hour != None:
            return self.__megabritish_thermal_units_per_hour
        self.__megabritish_thermal_units_per_hour = self.__convert_from_base(PowerUnits.MegabritishThermalUnitPerHour)
        return self.__megabritish_thermal_units_per_hour

    
    @property
    def millijoules_per_hour(self) -> float:
        """
        
        """
        if self.__millijoules_per_hour != None:
            return self.__millijoules_per_hour
        self.__millijoules_per_hour = self.__convert_from_base(PowerUnits.MillijoulePerHour)
        return self.__millijoules_per_hour

    
    @property
    def kilojoules_per_hour(self) -> float:
        """
        
        """
        if self.__kilojoules_per_hour != None:
            return self.__kilojoules_per_hour
        self.__kilojoules_per_hour = self.__convert_from_base(PowerUnits.KilojoulePerHour)
        return self.__kilojoules_per_hour

    
    @property
    def megajoules_per_hour(self) -> float:
        """
        
        """
        if self.__megajoules_per_hour != None:
            return self.__megajoules_per_hour
        self.__megajoules_per_hour = self.__convert_from_base(PowerUnits.MegajoulePerHour)
        return self.__megajoules_per_hour

    
    @property
    def gigajoules_per_hour(self) -> float:
        """
        
        """
        if self.__gigajoules_per_hour != None:
            return self.__gigajoules_per_hour
        self.__gigajoules_per_hour = self.__convert_from_base(PowerUnits.GigajoulePerHour)
        return self.__gigajoules_per_hour

    
    def to_string(self, unit: PowerUnits = PowerUnits.Watt) -> str:
        """
        Format the Power to string.
        Note! the default format for Power is Watt.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PowerUnits.Watt:
            return f"""{self.watts} W"""
        
        if unit == PowerUnits.MechanicalHorsepower:
            return f"""{self.mechanical_horsepower} hp(I)"""
        
        if unit == PowerUnits.MetricHorsepower:
            return f"""{self.metric_horsepower} hp(M)"""
        
        if unit == PowerUnits.ElectricalHorsepower:
            return f"""{self.electrical_horsepower} hp(E)"""
        
        if unit == PowerUnits.BoilerHorsepower:
            return f"""{self.boiler_horsepower} hp(S)"""
        
        if unit == PowerUnits.HydraulicHorsepower:
            return f"""{self.hydraulic_horsepower} hp(H)"""
        
        if unit == PowerUnits.BritishThermalUnitPerHour:
            return f"""{self.british_thermal_units_per_hour} Btu/h"""
        
        if unit == PowerUnits.JoulePerHour:
            return f"""{self.joules_per_hour} J/h"""
        
        if unit == PowerUnits.Femtowatt:
            return f"""{self.femtowatts} fW"""
        
        if unit == PowerUnits.Picowatt:
            return f"""{self.picowatts} pW"""
        
        if unit == PowerUnits.Nanowatt:
            return f"""{self.nanowatts} nW"""
        
        if unit == PowerUnits.Microwatt:
            return f"""{self.microwatts} μW"""
        
        if unit == PowerUnits.Milliwatt:
            return f"""{self.milliwatts} mW"""
        
        if unit == PowerUnits.Deciwatt:
            return f"""{self.deciwatts} dW"""
        
        if unit == PowerUnits.Decawatt:
            return f"""{self.decawatts} daW"""
        
        if unit == PowerUnits.Kilowatt:
            return f"""{self.kilowatts} kW"""
        
        if unit == PowerUnits.Megawatt:
            return f"""{self.megawatts} MW"""
        
        if unit == PowerUnits.Gigawatt:
            return f"""{self.gigawatts} GW"""
        
        if unit == PowerUnits.Terawatt:
            return f"""{self.terawatts} TW"""
        
        if unit == PowerUnits.Petawatt:
            return f"""{self.petawatts} PW"""
        
        if unit == PowerUnits.KilobritishThermalUnitPerHour:
            return f"""{self.kilobritish_thermal_units_per_hour} kBtu/h"""
        
        if unit == PowerUnits.MegabritishThermalUnitPerHour:
            return f"""{self.megabritish_thermal_units_per_hour} MBtu/h"""
        
        if unit == PowerUnits.MillijoulePerHour:
            return f"""{self.millijoules_per_hour} mJ/h"""
        
        if unit == PowerUnits.KilojoulePerHour:
            return f"""{self.kilojoules_per_hour} kJ/h"""
        
        if unit == PowerUnits.MegajoulePerHour:
            return f"""{self.megajoules_per_hour} MJ/h"""
        
        if unit == PowerUnits.GigajoulePerHour:
            return f"""{self.gigajoules_per_hour} GJ/h"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PowerUnits = PowerUnits.Watt) -> str:
        """
        Get Power unit abbreviation.
        Note! the default abbreviation for Power is Watt.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PowerUnits.Watt:
            return """W"""
        
        if unit_abbreviation == PowerUnits.MechanicalHorsepower:
            return """hp(I)"""
        
        if unit_abbreviation == PowerUnits.MetricHorsepower:
            return """hp(M)"""
        
        if unit_abbreviation == PowerUnits.ElectricalHorsepower:
            return """hp(E)"""
        
        if unit_abbreviation == PowerUnits.BoilerHorsepower:
            return """hp(S)"""
        
        if unit_abbreviation == PowerUnits.HydraulicHorsepower:
            return """hp(H)"""
        
        if unit_abbreviation == PowerUnits.BritishThermalUnitPerHour:
            return """Btu/h"""
        
        if unit_abbreviation == PowerUnits.JoulePerHour:
            return """J/h"""
        
        if unit_abbreviation == PowerUnits.Femtowatt:
            return """fW"""
        
        if unit_abbreviation == PowerUnits.Picowatt:
            return """pW"""
        
        if unit_abbreviation == PowerUnits.Nanowatt:
            return """nW"""
        
        if unit_abbreviation == PowerUnits.Microwatt:
            return """μW"""
        
        if unit_abbreviation == PowerUnits.Milliwatt:
            return """mW"""
        
        if unit_abbreviation == PowerUnits.Deciwatt:
            return """dW"""
        
        if unit_abbreviation == PowerUnits.Decawatt:
            return """daW"""
        
        if unit_abbreviation == PowerUnits.Kilowatt:
            return """kW"""
        
        if unit_abbreviation == PowerUnits.Megawatt:
            return """MW"""
        
        if unit_abbreviation == PowerUnits.Gigawatt:
            return """GW"""
        
        if unit_abbreviation == PowerUnits.Terawatt:
            return """TW"""
        
        if unit_abbreviation == PowerUnits.Petawatt:
            return """PW"""
        
        if unit_abbreviation == PowerUnits.KilobritishThermalUnitPerHour:
            return """kBtu/h"""
        
        if unit_abbreviation == PowerUnits.MegabritishThermalUnitPerHour:
            return """MBtu/h"""
        
        if unit_abbreviation == PowerUnits.MillijoulePerHour:
            return """mJ/h"""
        
        if unit_abbreviation == PowerUnits.KilojoulePerHour:
            return """kJ/h"""
        
        if unit_abbreviation == PowerUnits.MegajoulePerHour:
            return """MJ/h"""
        
        if unit_abbreviation == PowerUnits.GigajoulePerHour:
            return """GJ/h"""
        