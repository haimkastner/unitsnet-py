from enum import Enum
import math
import string


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
        
        FemtoWatt = 'femto_watt'
        """
            
        """
        
        PicoWatt = 'pico_watt'
        """
            
        """
        
        NanoWatt = 'nano_watt'
        """
            
        """
        
        MicroWatt = 'micro_watt'
        """
            
        """
        
        MilliWatt = 'milli_watt'
        """
            
        """
        
        DeciWatt = 'deci_watt'
        """
            
        """
        
        DecaWatt = 'deca_watt'
        """
            
        """
        
        KiloWatt = 'kilo_watt'
        """
            
        """
        
        MegaWatt = 'mega_watt'
        """
            
        """
        
        GigaWatt = 'giga_watt'
        """
            
        """
        
        TeraWatt = 'tera_watt'
        """
            
        """
        
        PetaWatt = 'peta_watt'
        """
            
        """
        
        KiloBritishThermalUnitPerHour = 'kilo_british_thermal_unit_per_hour'
        """
            
        """
        
        MegaBritishThermalUnitPerHour = 'mega_british_thermal_unit_per_hour'
        """
            
        """
        
        MilliJoulePerHour = 'milli_joule_per_hour'
        """
            
        """
        
        KiloJoulePerHour = 'kilo_joule_per_hour'
        """
            
        """
        
        MegaJoulePerHour = 'mega_joule_per_hour'
        """
            
        """
        
        GigaJoulePerHour = 'giga_joule_per_hour'
        """
            
        """
        
    
class Power:
    """
    In physics, power is the rate of doing work. It is equivalent to an amount of energy consumed per unit time.

    Args:
        value (float): The value.
        from_unit (PowerUnits): The Power unit to create from, The default unit is Watt
    """
    def __init__(self, value: float, from_unit: PowerUnits = PowerUnits.Watt):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__watts = None
        
        self.__mechanical_horsepower = None
        
        self.__metric_horsepower = None
        
        self.__electrical_horsepower = None
        
        self.__boiler_horsepower = None
        
        self.__hydraulic_horsepower = None
        
        self.__british_thermal_units_per_hour = None
        
        self.__joules_per_hour = None
        
        self.__femto_watts = None
        
        self.__pico_watts = None
        
        self.__nano_watts = None
        
        self.__micro_watts = None
        
        self.__milli_watts = None
        
        self.__deci_watts = None
        
        self.__deca_watts = None
        
        self.__kilo_watts = None
        
        self.__mega_watts = None
        
        self.__giga_watts = None
        
        self.__tera_watts = None
        
        self.__peta_watts = None
        
        self.__kilo_british_thermal_units_per_hour = None
        
        self.__mega_british_thermal_units_per_hour = None
        
        self.__milli_joules_per_hour = None
        
        self.__kilo_joules_per_hour = None
        
        self.__mega_joules_per_hour = None
        
        self.__giga_joules_per_hour = None
        

    def __convert_from_base(self, from_unit: PowerUnits) -> float:
        value = self.__value
        
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
        
        if from_unit == PowerUnits.FemtoWatt:
            return ((value) / 1e-15)
        
        if from_unit == PowerUnits.PicoWatt:
            return ((value) / 1e-12)
        
        if from_unit == PowerUnits.NanoWatt:
            return ((value) / 1e-09)
        
        if from_unit == PowerUnits.MicroWatt:
            return ((value) / 1e-06)
        
        if from_unit == PowerUnits.MilliWatt:
            return ((value) / 0.001)
        
        if from_unit == PowerUnits.DeciWatt:
            return ((value) / 0.1)
        
        if from_unit == PowerUnits.DecaWatt:
            return ((value) / 10.0)
        
        if from_unit == PowerUnits.KiloWatt:
            return ((value) / 1000.0)
        
        if from_unit == PowerUnits.MegaWatt:
            return ((value) / 1000000.0)
        
        if from_unit == PowerUnits.GigaWatt:
            return ((value) / 1000000000.0)
        
        if from_unit == PowerUnits.TeraWatt:
            return ((value) / 1000000000000.0)
        
        if from_unit == PowerUnits.PetaWatt:
            return ((value) / 1000000000000000.0)
        
        if from_unit == PowerUnits.KiloBritishThermalUnitPerHour:
            return ((value / 0.29307107017) / 1000.0)
        
        if from_unit == PowerUnits.MegaBritishThermalUnitPerHour:
            return ((value / 0.29307107017) / 1000000.0)
        
        if from_unit == PowerUnits.MilliJoulePerHour:
            return ((value * 3600) / 0.001)
        
        if from_unit == PowerUnits.KiloJoulePerHour:
            return ((value * 3600) / 1000.0)
        
        if from_unit == PowerUnits.MegaJoulePerHour:
            return ((value * 3600) / 1000000.0)
        
        if from_unit == PowerUnits.GigaJoulePerHour:
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
        
        if to_unit == PowerUnits.FemtoWatt:
            return ((value) * 1e-15)
        
        if to_unit == PowerUnits.PicoWatt:
            return ((value) * 1e-12)
        
        if to_unit == PowerUnits.NanoWatt:
            return ((value) * 1e-09)
        
        if to_unit == PowerUnits.MicroWatt:
            return ((value) * 1e-06)
        
        if to_unit == PowerUnits.MilliWatt:
            return ((value) * 0.001)
        
        if to_unit == PowerUnits.DeciWatt:
            return ((value) * 0.1)
        
        if to_unit == PowerUnits.DecaWatt:
            return ((value) * 10.0)
        
        if to_unit == PowerUnits.KiloWatt:
            return ((value) * 1000.0)
        
        if to_unit == PowerUnits.MegaWatt:
            return ((value) * 1000000.0)
        
        if to_unit == PowerUnits.GigaWatt:
            return ((value) * 1000000000.0)
        
        if to_unit == PowerUnits.TeraWatt:
            return ((value) * 1000000000000.0)
        
        if to_unit == PowerUnits.PetaWatt:
            return ((value) * 1000000000000000.0)
        
        if to_unit == PowerUnits.KiloBritishThermalUnitPerHour:
            return ((value * 0.29307107017) * 1000.0)
        
        if to_unit == PowerUnits.MegaBritishThermalUnitPerHour:
            return ((value * 0.29307107017) * 1000000.0)
        
        if to_unit == PowerUnits.MilliJoulePerHour:
            return ((value / 3600) * 0.001)
        
        if to_unit == PowerUnits.KiloJoulePerHour:
            return ((value / 3600) * 1000.0)
        
        if to_unit == PowerUnits.MegaJoulePerHour:
            return ((value / 3600) * 1000000.0)
        
        if to_unit == PowerUnits.GigaJoulePerHour:
            return ((value / 3600) * 1000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
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
    def from_femto_watts(femto_watts: float):
        """
        Create a new instance of Power from a value in femto_watts.

        

        :param meters: The Power value in femto_watts.
        :type femto_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(femto_watts, PowerUnits.FemtoWatt)

    
    @staticmethod
    def from_pico_watts(pico_watts: float):
        """
        Create a new instance of Power from a value in pico_watts.

        

        :param meters: The Power value in pico_watts.
        :type pico_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(pico_watts, PowerUnits.PicoWatt)

    
    @staticmethod
    def from_nano_watts(nano_watts: float):
        """
        Create a new instance of Power from a value in nano_watts.

        

        :param meters: The Power value in nano_watts.
        :type nano_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(nano_watts, PowerUnits.NanoWatt)

    
    @staticmethod
    def from_micro_watts(micro_watts: float):
        """
        Create a new instance of Power from a value in micro_watts.

        

        :param meters: The Power value in micro_watts.
        :type micro_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(micro_watts, PowerUnits.MicroWatt)

    
    @staticmethod
    def from_milli_watts(milli_watts: float):
        """
        Create a new instance of Power from a value in milli_watts.

        

        :param meters: The Power value in milli_watts.
        :type milli_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(milli_watts, PowerUnits.MilliWatt)

    
    @staticmethod
    def from_deci_watts(deci_watts: float):
        """
        Create a new instance of Power from a value in deci_watts.

        

        :param meters: The Power value in deci_watts.
        :type deci_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(deci_watts, PowerUnits.DeciWatt)

    
    @staticmethod
    def from_deca_watts(deca_watts: float):
        """
        Create a new instance of Power from a value in deca_watts.

        

        :param meters: The Power value in deca_watts.
        :type deca_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(deca_watts, PowerUnits.DecaWatt)

    
    @staticmethod
    def from_kilo_watts(kilo_watts: float):
        """
        Create a new instance of Power from a value in kilo_watts.

        

        :param meters: The Power value in kilo_watts.
        :type kilo_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(kilo_watts, PowerUnits.KiloWatt)

    
    @staticmethod
    def from_mega_watts(mega_watts: float):
        """
        Create a new instance of Power from a value in mega_watts.

        

        :param meters: The Power value in mega_watts.
        :type mega_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(mega_watts, PowerUnits.MegaWatt)

    
    @staticmethod
    def from_giga_watts(giga_watts: float):
        """
        Create a new instance of Power from a value in giga_watts.

        

        :param meters: The Power value in giga_watts.
        :type giga_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(giga_watts, PowerUnits.GigaWatt)

    
    @staticmethod
    def from_tera_watts(tera_watts: float):
        """
        Create a new instance of Power from a value in tera_watts.

        

        :param meters: The Power value in tera_watts.
        :type tera_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(tera_watts, PowerUnits.TeraWatt)

    
    @staticmethod
    def from_peta_watts(peta_watts: float):
        """
        Create a new instance of Power from a value in peta_watts.

        

        :param meters: The Power value in peta_watts.
        :type peta_watts: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(peta_watts, PowerUnits.PetaWatt)

    
    @staticmethod
    def from_kilo_british_thermal_units_per_hour(kilo_british_thermal_units_per_hour: float):
        """
        Create a new instance of Power from a value in kilo_british_thermal_units_per_hour.

        

        :param meters: The Power value in kilo_british_thermal_units_per_hour.
        :type kilo_british_thermal_units_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(kilo_british_thermal_units_per_hour, PowerUnits.KiloBritishThermalUnitPerHour)

    
    @staticmethod
    def from_mega_british_thermal_units_per_hour(mega_british_thermal_units_per_hour: float):
        """
        Create a new instance of Power from a value in mega_british_thermal_units_per_hour.

        

        :param meters: The Power value in mega_british_thermal_units_per_hour.
        :type mega_british_thermal_units_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(mega_british_thermal_units_per_hour, PowerUnits.MegaBritishThermalUnitPerHour)

    
    @staticmethod
    def from_milli_joules_per_hour(milli_joules_per_hour: float):
        """
        Create a new instance of Power from a value in milli_joules_per_hour.

        

        :param meters: The Power value in milli_joules_per_hour.
        :type milli_joules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(milli_joules_per_hour, PowerUnits.MilliJoulePerHour)

    
    @staticmethod
    def from_kilo_joules_per_hour(kilo_joules_per_hour: float):
        """
        Create a new instance of Power from a value in kilo_joules_per_hour.

        

        :param meters: The Power value in kilo_joules_per_hour.
        :type kilo_joules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(kilo_joules_per_hour, PowerUnits.KiloJoulePerHour)

    
    @staticmethod
    def from_mega_joules_per_hour(mega_joules_per_hour: float):
        """
        Create a new instance of Power from a value in mega_joules_per_hour.

        

        :param meters: The Power value in mega_joules_per_hour.
        :type mega_joules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(mega_joules_per_hour, PowerUnits.MegaJoulePerHour)

    
    @staticmethod
    def from_giga_joules_per_hour(giga_joules_per_hour: float):
        """
        Create a new instance of Power from a value in giga_joules_per_hour.

        

        :param meters: The Power value in giga_joules_per_hour.
        :type giga_joules_per_hour: float
        :return: A new instance of Power.
        :rtype: Power
        """
        return Power(giga_joules_per_hour, PowerUnits.GigaJoulePerHour)

    
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
    def femto_watts(self) -> float:
        """
        
        """
        if self.__femto_watts != None:
            return self.__femto_watts
        self.__femto_watts = self.__convert_from_base(PowerUnits.FemtoWatt)
        return self.__femto_watts

    
    @property
    def pico_watts(self) -> float:
        """
        
        """
        if self.__pico_watts != None:
            return self.__pico_watts
        self.__pico_watts = self.__convert_from_base(PowerUnits.PicoWatt)
        return self.__pico_watts

    
    @property
    def nano_watts(self) -> float:
        """
        
        """
        if self.__nano_watts != None:
            return self.__nano_watts
        self.__nano_watts = self.__convert_from_base(PowerUnits.NanoWatt)
        return self.__nano_watts

    
    @property
    def micro_watts(self) -> float:
        """
        
        """
        if self.__micro_watts != None:
            return self.__micro_watts
        self.__micro_watts = self.__convert_from_base(PowerUnits.MicroWatt)
        return self.__micro_watts

    
    @property
    def milli_watts(self) -> float:
        """
        
        """
        if self.__milli_watts != None:
            return self.__milli_watts
        self.__milli_watts = self.__convert_from_base(PowerUnits.MilliWatt)
        return self.__milli_watts

    
    @property
    def deci_watts(self) -> float:
        """
        
        """
        if self.__deci_watts != None:
            return self.__deci_watts
        self.__deci_watts = self.__convert_from_base(PowerUnits.DeciWatt)
        return self.__deci_watts

    
    @property
    def deca_watts(self) -> float:
        """
        
        """
        if self.__deca_watts != None:
            return self.__deca_watts
        self.__deca_watts = self.__convert_from_base(PowerUnits.DecaWatt)
        return self.__deca_watts

    
    @property
    def kilo_watts(self) -> float:
        """
        
        """
        if self.__kilo_watts != None:
            return self.__kilo_watts
        self.__kilo_watts = self.__convert_from_base(PowerUnits.KiloWatt)
        return self.__kilo_watts

    
    @property
    def mega_watts(self) -> float:
        """
        
        """
        if self.__mega_watts != None:
            return self.__mega_watts
        self.__mega_watts = self.__convert_from_base(PowerUnits.MegaWatt)
        return self.__mega_watts

    
    @property
    def giga_watts(self) -> float:
        """
        
        """
        if self.__giga_watts != None:
            return self.__giga_watts
        self.__giga_watts = self.__convert_from_base(PowerUnits.GigaWatt)
        return self.__giga_watts

    
    @property
    def tera_watts(self) -> float:
        """
        
        """
        if self.__tera_watts != None:
            return self.__tera_watts
        self.__tera_watts = self.__convert_from_base(PowerUnits.TeraWatt)
        return self.__tera_watts

    
    @property
    def peta_watts(self) -> float:
        """
        
        """
        if self.__peta_watts != None:
            return self.__peta_watts
        self.__peta_watts = self.__convert_from_base(PowerUnits.PetaWatt)
        return self.__peta_watts

    
    @property
    def kilo_british_thermal_units_per_hour(self) -> float:
        """
        
        """
        if self.__kilo_british_thermal_units_per_hour != None:
            return self.__kilo_british_thermal_units_per_hour
        self.__kilo_british_thermal_units_per_hour = self.__convert_from_base(PowerUnits.KiloBritishThermalUnitPerHour)
        return self.__kilo_british_thermal_units_per_hour

    
    @property
    def mega_british_thermal_units_per_hour(self) -> float:
        """
        
        """
        if self.__mega_british_thermal_units_per_hour != None:
            return self.__mega_british_thermal_units_per_hour
        self.__mega_british_thermal_units_per_hour = self.__convert_from_base(PowerUnits.MegaBritishThermalUnitPerHour)
        return self.__mega_british_thermal_units_per_hour

    
    @property
    def milli_joules_per_hour(self) -> float:
        """
        
        """
        if self.__milli_joules_per_hour != None:
            return self.__milli_joules_per_hour
        self.__milli_joules_per_hour = self.__convert_from_base(PowerUnits.MilliJoulePerHour)
        return self.__milli_joules_per_hour

    
    @property
    def kilo_joules_per_hour(self) -> float:
        """
        
        """
        if self.__kilo_joules_per_hour != None:
            return self.__kilo_joules_per_hour
        self.__kilo_joules_per_hour = self.__convert_from_base(PowerUnits.KiloJoulePerHour)
        return self.__kilo_joules_per_hour

    
    @property
    def mega_joules_per_hour(self) -> float:
        """
        
        """
        if self.__mega_joules_per_hour != None:
            return self.__mega_joules_per_hour
        self.__mega_joules_per_hour = self.__convert_from_base(PowerUnits.MegaJoulePerHour)
        return self.__mega_joules_per_hour

    
    @property
    def giga_joules_per_hour(self) -> float:
        """
        
        """
        if self.__giga_joules_per_hour != None:
            return self.__giga_joules_per_hour
        self.__giga_joules_per_hour = self.__convert_from_base(PowerUnits.GigaJoulePerHour)
        return self.__giga_joules_per_hour

    
    def to_string(self, unit: PowerUnits = PowerUnits.Watt) -> string:
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
        
        if unit == PowerUnits.FemtoWatt:
            return f"""{self.femto_watts} """
        
        if unit == PowerUnits.PicoWatt:
            return f"""{self.pico_watts} """
        
        if unit == PowerUnits.NanoWatt:
            return f"""{self.nano_watts} """
        
        if unit == PowerUnits.MicroWatt:
            return f"""{self.micro_watts} """
        
        if unit == PowerUnits.MilliWatt:
            return f"""{self.milli_watts} """
        
        if unit == PowerUnits.DeciWatt:
            return f"""{self.deci_watts} """
        
        if unit == PowerUnits.DecaWatt:
            return f"""{self.deca_watts} """
        
        if unit == PowerUnits.KiloWatt:
            return f"""{self.kilo_watts} """
        
        if unit == PowerUnits.MegaWatt:
            return f"""{self.mega_watts} """
        
        if unit == PowerUnits.GigaWatt:
            return f"""{self.giga_watts} """
        
        if unit == PowerUnits.TeraWatt:
            return f"""{self.tera_watts} """
        
        if unit == PowerUnits.PetaWatt:
            return f"""{self.peta_watts} """
        
        if unit == PowerUnits.KiloBritishThermalUnitPerHour:
            return f"""{self.kilo_british_thermal_units_per_hour} """
        
        if unit == PowerUnits.MegaBritishThermalUnitPerHour:
            return f"""{self.mega_british_thermal_units_per_hour} """
        
        if unit == PowerUnits.MilliJoulePerHour:
            return f"""{self.milli_joules_per_hour} """
        
        if unit == PowerUnits.KiloJoulePerHour:
            return f"""{self.kilo_joules_per_hour} """
        
        if unit == PowerUnits.MegaJoulePerHour:
            return f"""{self.mega_joules_per_hour} """
        
        if unit == PowerUnits.GigaJoulePerHour:
            return f"""{self.giga_joules_per_hour} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: PowerUnits = PowerUnits.Watt) -> string:
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
        
        if unit_abbreviation == PowerUnits.FemtoWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.PicoWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.NanoWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.MicroWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.MilliWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.DeciWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.DecaWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.KiloWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.MegaWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.GigaWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.TeraWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.PetaWatt:
            return """"""
        
        if unit_abbreviation == PowerUnits.KiloBritishThermalUnitPerHour:
            return """"""
        
        if unit_abbreviation == PowerUnits.MegaBritishThermalUnitPerHour:
            return """"""
        
        if unit_abbreviation == PowerUnits.MilliJoulePerHour:
            return """"""
        
        if unit_abbreviation == PowerUnits.KiloJoulePerHour:
            return """"""
        
        if unit_abbreviation == PowerUnits.MegaJoulePerHour:
            return """"""
        
        if unit_abbreviation == PowerUnits.GigaJoulePerHour:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for +: 'Power' and '{}'".format(type(other).__name__))
        return Power(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for *: 'Power' and '{}'".format(type(other).__name__))
        return Power(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for -: 'Power' and '{}'".format(type(other).__name__))
        return Power(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for /: 'Power' and '{}'".format(type(other).__name__))
        return Power(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for %: 'Power' and '{}'".format(type(other).__name__))
        return Power(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for **: 'Power' and '{}'".format(type(other).__name__))
        return Power(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for ==: 'Power' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for <: 'Power' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for >: 'Power' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for <=: 'Power' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Power):
            raise TypeError("unsupported operand type(s) for >=: 'Power' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value