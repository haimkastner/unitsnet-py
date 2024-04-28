from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class ElectricConductivityUnits(Enum):
        """
            ElectricConductivityUnits enumeration
        """
        
        SiemensPerMeter = 'SiemensPerMeter'
        """
            
        """
        
        SiemensPerInch = 'SiemensPerInch'
        """
            
        """
        
        SiemensPerFoot = 'SiemensPerFoot'
        """
            
        """
        
        SiemensPerCentimeter = 'SiemensPerCentimeter'
        """
            
        """
        
        MicrosiemensPerCentimeter = 'MicrosiemensPerCentimeter'
        """
            
        """
        
        MillisiemensPerCentimeter = 'MillisiemensPerCentimeter'
        """
            
        """
        

class ElectricConductivityDto:
    """
    A DTO representation of a ElectricConductivity

    Attributes:
        value (float): The value of the ElectricConductivity.
        unit (ElectricConductivityUnits): The specific unit that the ElectricConductivity value is representing.
    """

    def __init__(self, value: float, unit: ElectricConductivityUnits):
        """
        Create a new DTO representation of a ElectricConductivity

        Parameters:
            value (float): The value of the ElectricConductivity.
            unit (ElectricConductivityUnits): The specific unit that the ElectricConductivity value is representing.
        """
        self.value: float = value
        """
        The value of the ElectricConductivity
        """
        self.unit: ElectricConductivityUnits = unit
        """
        The specific unit that the ElectricConductivity value is representing
        """

    def to_json(self):
        """
        Get a ElectricConductivity DTO JSON object representing the current unit.

        :return: JSON object represents ElectricConductivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SiemensPerMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of ElectricConductivity DTO from a json representation.

        :param data: The ElectricConductivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SiemensPerMeter"}
        :return: A new instance of ElectricConductivityDto.
        :rtype: ElectricConductivityDto
        """
        return ElectricConductivityDto(value=data["value"], unit=ElectricConductivityUnits(data["unit"]))


class ElectricConductivity(AbstractMeasure):
    """
    Electrical conductivity or specific conductance is the reciprocal of electrical resistivity, and measures a material's ability to conduct an electric current.

    Args:
        value (float): The value.
        from_unit (ElectricConductivityUnits): The ElectricConductivity unit to create from, The default unit is SiemensPerMeter
    """
    def __init__(self, value: float, from_unit: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__siemens_per_meter = None
        
        self.__siemens_per_inch = None
        
        self.__siemens_per_foot = None
        
        self.__siemens_per_centimeter = None
        
        self.__microsiemens_per_centimeter = None
        
        self.__millisiemens_per_centimeter = None
        

    def convert(self, unit: ElectricConductivityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter) -> ElectricConductivityDto:
        """
        Get a new instance of ElectricConductivity DTO representing the current unit.

        :param hold_in_unit: The specific ElectricConductivity unit to store the ElectricConductivity value in the DTO representation.
        :type hold_in_unit: ElectricConductivityUnits
        :return: A new instance of ElectricConductivityDto.
        :rtype: ElectricConductivityDto
        """
        return ElectricConductivityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter):
        """
        Get a ElectricConductivity DTO JSON object representing the current unit.

        :param hold_in_unit: The specific ElectricConductivity unit to store the ElectricConductivity value in the DTO representation.
        :type hold_in_unit: ElectricConductivityUnits
        :return: JSON object represents ElectricConductivity DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "SiemensPerMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(electric_conductivity_dto: ElectricConductivityDto):
        """
        Obtain a new instance of ElectricConductivity from a DTO unit object.

        :param electric_conductivity_dto: The ElectricConductivity DTO representation.
        :type electric_conductivity_dto: ElectricConductivityDto
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(electric_conductivity_dto.value, electric_conductivity_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of ElectricConductivity from a DTO unit json representation.

        :param data: The ElectricConductivity DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "SiemensPerMeter"}
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity.from_dto(ElectricConductivityDto.from_json(data))

    def __convert_from_base(self, from_unit: ElectricConductivityUnits) -> float:
        value = self._value
        
        if from_unit == ElectricConductivityUnits.SiemensPerMeter:
            return (value)
        
        if from_unit == ElectricConductivityUnits.SiemensPerInch:
            return (value / 3.937007874015748e1)
        
        if from_unit == ElectricConductivityUnits.SiemensPerFoot:
            return (value / 3.2808398950131234)
        
        if from_unit == ElectricConductivityUnits.SiemensPerCentimeter:
            return (value / 1e2)
        
        if from_unit == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return ((value / 1e2) / 1e-06)
        
        if from_unit == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return ((value / 1e2) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: ElectricConductivityUnits) -> float:
        
        if to_unit == ElectricConductivityUnits.SiemensPerMeter:
            return (value)
        
        if to_unit == ElectricConductivityUnits.SiemensPerInch:
            return (value * 3.937007874015748e1)
        
        if to_unit == ElectricConductivityUnits.SiemensPerFoot:
            return (value * 3.2808398950131234)
        
        if to_unit == ElectricConductivityUnits.SiemensPerCentimeter:
            return (value * 1e2)
        
        if to_unit == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return ((value * 1e2) * 1e-06)
        
        if to_unit == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return ((value * 1e2) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_siemens_per_meter(siemens_per_meter: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_meter.

        

        :param meters: The ElectricConductivity value in siemens_per_meter.
        :type siemens_per_meter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_meter, ElectricConductivityUnits.SiemensPerMeter)

    
    @staticmethod
    def from_siemens_per_inch(siemens_per_inch: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_inch.

        

        :param meters: The ElectricConductivity value in siemens_per_inch.
        :type siemens_per_inch: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_inch, ElectricConductivityUnits.SiemensPerInch)

    
    @staticmethod
    def from_siemens_per_foot(siemens_per_foot: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_foot.

        

        :param meters: The ElectricConductivity value in siemens_per_foot.
        :type siemens_per_foot: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_foot, ElectricConductivityUnits.SiemensPerFoot)

    
    @staticmethod
    def from_siemens_per_centimeter(siemens_per_centimeter: float):
        """
        Create a new instance of ElectricConductivity from a value in siemens_per_centimeter.

        

        :param meters: The ElectricConductivity value in siemens_per_centimeter.
        :type siemens_per_centimeter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(siemens_per_centimeter, ElectricConductivityUnits.SiemensPerCentimeter)

    
    @staticmethod
    def from_microsiemens_per_centimeter(microsiemens_per_centimeter: float):
        """
        Create a new instance of ElectricConductivity from a value in microsiemens_per_centimeter.

        

        :param meters: The ElectricConductivity value in microsiemens_per_centimeter.
        :type microsiemens_per_centimeter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(microsiemens_per_centimeter, ElectricConductivityUnits.MicrosiemensPerCentimeter)

    
    @staticmethod
    def from_millisiemens_per_centimeter(millisiemens_per_centimeter: float):
        """
        Create a new instance of ElectricConductivity from a value in millisiemens_per_centimeter.

        

        :param meters: The ElectricConductivity value in millisiemens_per_centimeter.
        :type millisiemens_per_centimeter: float
        :return: A new instance of ElectricConductivity.
        :rtype: ElectricConductivity
        """
        return ElectricConductivity(millisiemens_per_centimeter, ElectricConductivityUnits.MillisiemensPerCentimeter)

    
    @property
    def siemens_per_meter(self) -> float:
        """
        
        """
        if self.__siemens_per_meter != None:
            return self.__siemens_per_meter
        self.__siemens_per_meter = self.__convert_from_base(ElectricConductivityUnits.SiemensPerMeter)
        return self.__siemens_per_meter

    
    @property
    def siemens_per_inch(self) -> float:
        """
        
        """
        if self.__siemens_per_inch != None:
            return self.__siemens_per_inch
        self.__siemens_per_inch = self.__convert_from_base(ElectricConductivityUnits.SiemensPerInch)
        return self.__siemens_per_inch

    
    @property
    def siemens_per_foot(self) -> float:
        """
        
        """
        if self.__siemens_per_foot != None:
            return self.__siemens_per_foot
        self.__siemens_per_foot = self.__convert_from_base(ElectricConductivityUnits.SiemensPerFoot)
        return self.__siemens_per_foot

    
    @property
    def siemens_per_centimeter(self) -> float:
        """
        
        """
        if self.__siemens_per_centimeter != None:
            return self.__siemens_per_centimeter
        self.__siemens_per_centimeter = self.__convert_from_base(ElectricConductivityUnits.SiemensPerCentimeter)
        return self.__siemens_per_centimeter

    
    @property
    def microsiemens_per_centimeter(self) -> float:
        """
        
        """
        if self.__microsiemens_per_centimeter != None:
            return self.__microsiemens_per_centimeter
        self.__microsiemens_per_centimeter = self.__convert_from_base(ElectricConductivityUnits.MicrosiemensPerCentimeter)
        return self.__microsiemens_per_centimeter

    
    @property
    def millisiemens_per_centimeter(self) -> float:
        """
        
        """
        if self.__millisiemens_per_centimeter != None:
            return self.__millisiemens_per_centimeter
        self.__millisiemens_per_centimeter = self.__convert_from_base(ElectricConductivityUnits.MillisiemensPerCentimeter)
        return self.__millisiemens_per_centimeter

    
    def to_string(self, unit: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter, fractional_digits: int = None) -> str:
        """
        Format the ElectricConductivity to a string.
        
        Note: the default format for ElectricConductivity is SiemensPerMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the ElectricConductivity. Default is 'SiemensPerMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == ElectricConductivityUnits.SiemensPerMeter:
            return f"""{super()._truncate_fraction_digits(self.siemens_per_meter, fractional_digits)} S/m"""
        
        if unit == ElectricConductivityUnits.SiemensPerInch:
            return f"""{super()._truncate_fraction_digits(self.siemens_per_inch, fractional_digits)} S/in"""
        
        if unit == ElectricConductivityUnits.SiemensPerFoot:
            return f"""{super()._truncate_fraction_digits(self.siemens_per_foot, fractional_digits)} S/ft"""
        
        if unit == ElectricConductivityUnits.SiemensPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.siemens_per_centimeter, fractional_digits)} S/cm"""
        
        if unit == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.microsiemens_per_centimeter, fractional_digits)} μS/cm"""
        
        if unit == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return f"""{super()._truncate_fraction_digits(self.millisiemens_per_centimeter, fractional_digits)} mS/cm"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: ElectricConductivityUnits = ElectricConductivityUnits.SiemensPerMeter) -> str:
        """
        Get ElectricConductivity unit abbreviation.
        Note! the default abbreviation for ElectricConductivity is SiemensPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerMeter:
            return """S/m"""
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerInch:
            return """S/in"""
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerFoot:
            return """S/ft"""
        
        if unit_abbreviation == ElectricConductivityUnits.SiemensPerCentimeter:
            return """S/cm"""
        
        if unit_abbreviation == ElectricConductivityUnits.MicrosiemensPerCentimeter:
            return """μS/cm"""
        
        if unit_abbreviation == ElectricConductivityUnits.MillisiemensPerCentimeter:
            return """mS/cm"""
        