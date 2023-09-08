from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class IrradianceUnits(Enum):
        """
            IrradianceUnits enumeration
        """
        
        WattPerSquareMeter = 'watt_per_square_meter'
        """
            
        """
        
        WattPerSquareCentimeter = 'watt_per_square_centimeter'
        """
            
        """
        
        PicowattPerSquareMeter = 'picowatt_per_square_meter'
        """
            
        """
        
        NanowattPerSquareMeter = 'nanowatt_per_square_meter'
        """
            
        """
        
        MicrowattPerSquareMeter = 'microwatt_per_square_meter'
        """
            
        """
        
        MilliwattPerSquareMeter = 'milliwatt_per_square_meter'
        """
            
        """
        
        KilowattPerSquareMeter = 'kilowatt_per_square_meter'
        """
            
        """
        
        MegawattPerSquareMeter = 'megawatt_per_square_meter'
        """
            
        """
        
        PicowattPerSquareCentimeter = 'picowatt_per_square_centimeter'
        """
            
        """
        
        NanowattPerSquareCentimeter = 'nanowatt_per_square_centimeter'
        """
            
        """
        
        MicrowattPerSquareCentimeter = 'microwatt_per_square_centimeter'
        """
            
        """
        
        MilliwattPerSquareCentimeter = 'milliwatt_per_square_centimeter'
        """
            
        """
        
        KilowattPerSquareCentimeter = 'kilowatt_per_square_centimeter'
        """
            
        """
        
        MegawattPerSquareCentimeter = 'megawatt_per_square_centimeter'
        """
            
        """
        

class Irradiance(AbstractMeasure):
    """
    Irradiance is the intensity of ultraviolet (UV) or visible light incident on a surface.

    Args:
        value (float): The value.
        from_unit (IrradianceUnits): The Irradiance unit to create from, The default unit is WattPerSquareMeter
    """
    def __init__(self, value: float, from_unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__watts_per_square_meter = None
        
        self.__watts_per_square_centimeter = None
        
        self.__picowatts_per_square_meter = None
        
        self.__nanowatts_per_square_meter = None
        
        self.__microwatts_per_square_meter = None
        
        self.__milliwatts_per_square_meter = None
        
        self.__kilowatts_per_square_meter = None
        
        self.__megawatts_per_square_meter = None
        
        self.__picowatts_per_square_centimeter = None
        
        self.__nanowatts_per_square_centimeter = None
        
        self.__microwatts_per_square_centimeter = None
        
        self.__milliwatts_per_square_centimeter = None
        
        self.__kilowatts_per_square_centimeter = None
        
        self.__megawatts_per_square_centimeter = None
        

    def convert(self, unit: IrradianceUnits) -> float:
        return self.__convert_from_base(unit)

    def __convert_from_base(self, from_unit: IrradianceUnits) -> float:
        value = self._value
        
        if from_unit == IrradianceUnits.WattPerSquareMeter:
            return (value)
        
        if from_unit == IrradianceUnits.WattPerSquareCentimeter:
            return (value * 0.0001)
        
        if from_unit == IrradianceUnits.PicowattPerSquareMeter:
            return ((value) / 1e-12)
        
        if from_unit == IrradianceUnits.NanowattPerSquareMeter:
            return ((value) / 1e-09)
        
        if from_unit == IrradianceUnits.MicrowattPerSquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == IrradianceUnits.MilliwattPerSquareMeter:
            return ((value) / 0.001)
        
        if from_unit == IrradianceUnits.KilowattPerSquareMeter:
            return ((value) / 1000.0)
        
        if from_unit == IrradianceUnits.MegawattPerSquareMeter:
            return ((value) / 1000000.0)
        
        if from_unit == IrradianceUnits.PicowattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-12)
        
        if from_unit == IrradianceUnits.NanowattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-09)
        
        if from_unit == IrradianceUnits.MicrowattPerSquareCentimeter:
            return ((value * 0.0001) / 1e-06)
        
        if from_unit == IrradianceUnits.MilliwattPerSquareCentimeter:
            return ((value * 0.0001) / 0.001)
        
        if from_unit == IrradianceUnits.KilowattPerSquareCentimeter:
            return ((value * 0.0001) / 1000.0)
        
        if from_unit == IrradianceUnits.MegawattPerSquareCentimeter:
            return ((value * 0.0001) / 1000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: IrradianceUnits) -> float:
        
        if to_unit == IrradianceUnits.WattPerSquareMeter:
            return (value)
        
        if to_unit == IrradianceUnits.WattPerSquareCentimeter:
            return (value * 10000)
        
        if to_unit == IrradianceUnits.PicowattPerSquareMeter:
            return ((value) * 1e-12)
        
        if to_unit == IrradianceUnits.NanowattPerSquareMeter:
            return ((value) * 1e-09)
        
        if to_unit == IrradianceUnits.MicrowattPerSquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == IrradianceUnits.MilliwattPerSquareMeter:
            return ((value) * 0.001)
        
        if to_unit == IrradianceUnits.KilowattPerSquareMeter:
            return ((value) * 1000.0)
        
        if to_unit == IrradianceUnits.MegawattPerSquareMeter:
            return ((value) * 1000000.0)
        
        if to_unit == IrradianceUnits.PicowattPerSquareCentimeter:
            return ((value * 10000) * 1e-12)
        
        if to_unit == IrradianceUnits.NanowattPerSquareCentimeter:
            return ((value * 10000) * 1e-09)
        
        if to_unit == IrradianceUnits.MicrowattPerSquareCentimeter:
            return ((value * 10000) * 1e-06)
        
        if to_unit == IrradianceUnits.MilliwattPerSquareCentimeter:
            return ((value * 10000) * 0.001)
        
        if to_unit == IrradianceUnits.KilowattPerSquareCentimeter:
            return ((value * 10000) * 1000.0)
        
        if to_unit == IrradianceUnits.MegawattPerSquareCentimeter:
            return ((value * 10000) * 1000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_watts_per_square_meter(watts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in watts_per_square_meter.

        

        :param meters: The Irradiance value in watts_per_square_meter.
        :type watts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(watts_per_square_meter, IrradianceUnits.WattPerSquareMeter)

    
    @staticmethod
    def from_watts_per_square_centimeter(watts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in watts_per_square_centimeter.

        

        :param meters: The Irradiance value in watts_per_square_centimeter.
        :type watts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(watts_per_square_centimeter, IrradianceUnits.WattPerSquareCentimeter)

    
    @staticmethod
    def from_picowatts_per_square_meter(picowatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in picowatts_per_square_meter.

        

        :param meters: The Irradiance value in picowatts_per_square_meter.
        :type picowatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(picowatts_per_square_meter, IrradianceUnits.PicowattPerSquareMeter)

    
    @staticmethod
    def from_nanowatts_per_square_meter(nanowatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in nanowatts_per_square_meter.

        

        :param meters: The Irradiance value in nanowatts_per_square_meter.
        :type nanowatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(nanowatts_per_square_meter, IrradianceUnits.NanowattPerSquareMeter)

    
    @staticmethod
    def from_microwatts_per_square_meter(microwatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in microwatts_per_square_meter.

        

        :param meters: The Irradiance value in microwatts_per_square_meter.
        :type microwatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(microwatts_per_square_meter, IrradianceUnits.MicrowattPerSquareMeter)

    
    @staticmethod
    def from_milliwatts_per_square_meter(milliwatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in milliwatts_per_square_meter.

        

        :param meters: The Irradiance value in milliwatts_per_square_meter.
        :type milliwatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(milliwatts_per_square_meter, IrradianceUnits.MilliwattPerSquareMeter)

    
    @staticmethod
    def from_kilowatts_per_square_meter(kilowatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in kilowatts_per_square_meter.

        

        :param meters: The Irradiance value in kilowatts_per_square_meter.
        :type kilowatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(kilowatts_per_square_meter, IrradianceUnits.KilowattPerSquareMeter)

    
    @staticmethod
    def from_megawatts_per_square_meter(megawatts_per_square_meter: float):
        """
        Create a new instance of Irradiance from a value in megawatts_per_square_meter.

        

        :param meters: The Irradiance value in megawatts_per_square_meter.
        :type megawatts_per_square_meter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(megawatts_per_square_meter, IrradianceUnits.MegawattPerSquareMeter)

    
    @staticmethod
    def from_picowatts_per_square_centimeter(picowatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in picowatts_per_square_centimeter.

        

        :param meters: The Irradiance value in picowatts_per_square_centimeter.
        :type picowatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(picowatts_per_square_centimeter, IrradianceUnits.PicowattPerSquareCentimeter)

    
    @staticmethod
    def from_nanowatts_per_square_centimeter(nanowatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in nanowatts_per_square_centimeter.

        

        :param meters: The Irradiance value in nanowatts_per_square_centimeter.
        :type nanowatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(nanowatts_per_square_centimeter, IrradianceUnits.NanowattPerSquareCentimeter)

    
    @staticmethod
    def from_microwatts_per_square_centimeter(microwatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in microwatts_per_square_centimeter.

        

        :param meters: The Irradiance value in microwatts_per_square_centimeter.
        :type microwatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(microwatts_per_square_centimeter, IrradianceUnits.MicrowattPerSquareCentimeter)

    
    @staticmethod
    def from_milliwatts_per_square_centimeter(milliwatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in milliwatts_per_square_centimeter.

        

        :param meters: The Irradiance value in milliwatts_per_square_centimeter.
        :type milliwatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(milliwatts_per_square_centimeter, IrradianceUnits.MilliwattPerSquareCentimeter)

    
    @staticmethod
    def from_kilowatts_per_square_centimeter(kilowatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in kilowatts_per_square_centimeter.

        

        :param meters: The Irradiance value in kilowatts_per_square_centimeter.
        :type kilowatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(kilowatts_per_square_centimeter, IrradianceUnits.KilowattPerSquareCentimeter)

    
    @staticmethod
    def from_megawatts_per_square_centimeter(megawatts_per_square_centimeter: float):
        """
        Create a new instance of Irradiance from a value in megawatts_per_square_centimeter.

        

        :param meters: The Irradiance value in megawatts_per_square_centimeter.
        :type megawatts_per_square_centimeter: float
        :return: A new instance of Irradiance.
        :rtype: Irradiance
        """
        return Irradiance(megawatts_per_square_centimeter, IrradianceUnits.MegawattPerSquareCentimeter)

    
    @property
    def watts_per_square_meter(self) -> float:
        """
        
        """
        if self.__watts_per_square_meter != None:
            return self.__watts_per_square_meter
        self.__watts_per_square_meter = self.__convert_from_base(IrradianceUnits.WattPerSquareMeter)
        return self.__watts_per_square_meter

    
    @property
    def watts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__watts_per_square_centimeter != None:
            return self.__watts_per_square_centimeter
        self.__watts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.WattPerSquareCentimeter)
        return self.__watts_per_square_centimeter

    
    @property
    def picowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__picowatts_per_square_meter != None:
            return self.__picowatts_per_square_meter
        self.__picowatts_per_square_meter = self.__convert_from_base(IrradianceUnits.PicowattPerSquareMeter)
        return self.__picowatts_per_square_meter

    
    @property
    def nanowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__nanowatts_per_square_meter != None:
            return self.__nanowatts_per_square_meter
        self.__nanowatts_per_square_meter = self.__convert_from_base(IrradianceUnits.NanowattPerSquareMeter)
        return self.__nanowatts_per_square_meter

    
    @property
    def microwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__microwatts_per_square_meter != None:
            return self.__microwatts_per_square_meter
        self.__microwatts_per_square_meter = self.__convert_from_base(IrradianceUnits.MicrowattPerSquareMeter)
        return self.__microwatts_per_square_meter

    
    @property
    def milliwatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_square_meter != None:
            return self.__milliwatts_per_square_meter
        self.__milliwatts_per_square_meter = self.__convert_from_base(IrradianceUnits.MilliwattPerSquareMeter)
        return self.__milliwatts_per_square_meter

    
    @property
    def kilowatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_square_meter != None:
            return self.__kilowatts_per_square_meter
        self.__kilowatts_per_square_meter = self.__convert_from_base(IrradianceUnits.KilowattPerSquareMeter)
        return self.__kilowatts_per_square_meter

    
    @property
    def megawatts_per_square_meter(self) -> float:
        """
        
        """
        if self.__megawatts_per_square_meter != None:
            return self.__megawatts_per_square_meter
        self.__megawatts_per_square_meter = self.__convert_from_base(IrradianceUnits.MegawattPerSquareMeter)
        return self.__megawatts_per_square_meter

    
    @property
    def picowatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__picowatts_per_square_centimeter != None:
            return self.__picowatts_per_square_centimeter
        self.__picowatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.PicowattPerSquareCentimeter)
        return self.__picowatts_per_square_centimeter

    
    @property
    def nanowatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__nanowatts_per_square_centimeter != None:
            return self.__nanowatts_per_square_centimeter
        self.__nanowatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.NanowattPerSquareCentimeter)
        return self.__nanowatts_per_square_centimeter

    
    @property
    def microwatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__microwatts_per_square_centimeter != None:
            return self.__microwatts_per_square_centimeter
        self.__microwatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MicrowattPerSquareCentimeter)
        return self.__microwatts_per_square_centimeter

    
    @property
    def milliwatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__milliwatts_per_square_centimeter != None:
            return self.__milliwatts_per_square_centimeter
        self.__milliwatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MilliwattPerSquareCentimeter)
        return self.__milliwatts_per_square_centimeter

    
    @property
    def kilowatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__kilowatts_per_square_centimeter != None:
            return self.__kilowatts_per_square_centimeter
        self.__kilowatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.KilowattPerSquareCentimeter)
        return self.__kilowatts_per_square_centimeter

    
    @property
    def megawatts_per_square_centimeter(self) -> float:
        """
        
        """
        if self.__megawatts_per_square_centimeter != None:
            return self.__megawatts_per_square_centimeter
        self.__megawatts_per_square_centimeter = self.__convert_from_base(IrradianceUnits.MegawattPerSquareCentimeter)
        return self.__megawatts_per_square_centimeter

    
    def to_string(self, unit: IrradianceUnits = IrradianceUnits.WattPerSquareMeter) -> str:
        """
        Format the Irradiance to string.
        Note! the default format for Irradiance is WattPerSquareMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == IrradianceUnits.WattPerSquareMeter:
            return f"""{self.watts_per_square_meter} W/m²"""
        
        if unit == IrradianceUnits.WattPerSquareCentimeter:
            return f"""{self.watts_per_square_centimeter} W/cm²"""
        
        if unit == IrradianceUnits.PicowattPerSquareMeter:
            return f"""{self.picowatts_per_square_meter} pW/m²"""
        
        if unit == IrradianceUnits.NanowattPerSquareMeter:
            return f"""{self.nanowatts_per_square_meter} nW/m²"""
        
        if unit == IrradianceUnits.MicrowattPerSquareMeter:
            return f"""{self.microwatts_per_square_meter} μW/m²"""
        
        if unit == IrradianceUnits.MilliwattPerSquareMeter:
            return f"""{self.milliwatts_per_square_meter} mW/m²"""
        
        if unit == IrradianceUnits.KilowattPerSquareMeter:
            return f"""{self.kilowatts_per_square_meter} kW/m²"""
        
        if unit == IrradianceUnits.MegawattPerSquareMeter:
            return f"""{self.megawatts_per_square_meter} MW/m²"""
        
        if unit == IrradianceUnits.PicowattPerSquareCentimeter:
            return f"""{self.picowatts_per_square_centimeter} pW/cm²"""
        
        if unit == IrradianceUnits.NanowattPerSquareCentimeter:
            return f"""{self.nanowatts_per_square_centimeter} nW/cm²"""
        
        if unit == IrradianceUnits.MicrowattPerSquareCentimeter:
            return f"""{self.microwatts_per_square_centimeter} μW/cm²"""
        
        if unit == IrradianceUnits.MilliwattPerSquareCentimeter:
            return f"""{self.milliwatts_per_square_centimeter} mW/cm²"""
        
        if unit == IrradianceUnits.KilowattPerSquareCentimeter:
            return f"""{self.kilowatts_per_square_centimeter} kW/cm²"""
        
        if unit == IrradianceUnits.MegawattPerSquareCentimeter:
            return f"""{self.megawatts_per_square_centimeter} MW/cm²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: IrradianceUnits = IrradianceUnits.WattPerSquareMeter) -> str:
        """
        Get Irradiance unit abbreviation.
        Note! the default abbreviation for Irradiance is WattPerSquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == IrradianceUnits.WattPerSquareMeter:
            return """W/m²"""
        
        if unit_abbreviation == IrradianceUnits.WattPerSquareCentimeter:
            return """W/cm²"""
        
        if unit_abbreviation == IrradianceUnits.PicowattPerSquareMeter:
            return """pW/m²"""
        
        if unit_abbreviation == IrradianceUnits.NanowattPerSquareMeter:
            return """nW/m²"""
        
        if unit_abbreviation == IrradianceUnits.MicrowattPerSquareMeter:
            return """μW/m²"""
        
        if unit_abbreviation == IrradianceUnits.MilliwattPerSquareMeter:
            return """mW/m²"""
        
        if unit_abbreviation == IrradianceUnits.KilowattPerSquareMeter:
            return """kW/m²"""
        
        if unit_abbreviation == IrradianceUnits.MegawattPerSquareMeter:
            return """MW/m²"""
        
        if unit_abbreviation == IrradianceUnits.PicowattPerSquareCentimeter:
            return """pW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.NanowattPerSquareCentimeter:
            return """nW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.MicrowattPerSquareCentimeter:
            return """μW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.MilliwattPerSquareCentimeter:
            return """mW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.KilowattPerSquareCentimeter:
            return """kW/cm²"""
        
        if unit_abbreviation == IrradianceUnits.MegawattPerSquareCentimeter:
            return """MW/cm²"""
        