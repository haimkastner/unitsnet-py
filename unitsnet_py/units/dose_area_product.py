from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class DoseAreaProductUnits(Enum):
        """
            DoseAreaProductUnits enumeration
        """
        
        GraySquareMeter = 'GraySquareMeter'
        """
            
        """
        
        GraySquareDecimeter = 'GraySquareDecimeter'
        """
            
        """
        
        GraySquareCentimeter = 'GraySquareCentimeter'
        """
            
        """
        
        GraySquareMillimeter = 'GraySquareMillimeter'
        """
            
        """
        
        MicrograySquareMeter = 'MicrograySquareMeter'
        """
            
        """
        
        MilligraySquareMeter = 'MilligraySquareMeter'
        """
            
        """
        
        CentigraySquareMeter = 'CentigraySquareMeter'
        """
            
        """
        
        DecigraySquareMeter = 'DecigraySquareMeter'
        """
            
        """
        
        MicrograySquareDecimeter = 'MicrograySquareDecimeter'
        """
            
        """
        
        MilligraySquareDecimeter = 'MilligraySquareDecimeter'
        """
            
        """
        
        CentigraySquareDecimeter = 'CentigraySquareDecimeter'
        """
            
        """
        
        DecigraySquareDecimeter = 'DecigraySquareDecimeter'
        """
            
        """
        
        MicrograySquareCentimeter = 'MicrograySquareCentimeter'
        """
            
        """
        
        MilligraySquareCentimeter = 'MilligraySquareCentimeter'
        """
            
        """
        
        CentigraySquareCentimeter = 'CentigraySquareCentimeter'
        """
            
        """
        
        DecigraySquareCentimeter = 'DecigraySquareCentimeter'
        """
            
        """
        
        MicrograySquareMillimeter = 'MicrograySquareMillimeter'
        """
            
        """
        
        MilligraySquareMillimeter = 'MilligraySquareMillimeter'
        """
            
        """
        
        CentigraySquareMillimeter = 'CentigraySquareMillimeter'
        """
            
        """
        
        DecigraySquareMillimeter = 'DecigraySquareMillimeter'
        """
            
        """
        

class DoseAreaProductDto:
    """
    A DTO representation of a DoseAreaProduct

    Attributes:
        value (float): The value of the DoseAreaProduct.
        unit (DoseAreaProductUnits): The specific unit that the DoseAreaProduct value is representing.
    """

    def __init__(self, value: float, unit: DoseAreaProductUnits):
        """
        Create a new DTO representation of a DoseAreaProduct

        Parameters:
            value (float): The value of the DoseAreaProduct.
            unit (DoseAreaProductUnits): The specific unit that the DoseAreaProduct value is representing.
        """
        self.value: float = value
        """
        The value of the DoseAreaProduct
        """
        self.unit: DoseAreaProductUnits = unit
        """
        The specific unit that the DoseAreaProduct value is representing
        """

    def to_json(self):
        """
        Get a DoseAreaProduct DTO JSON object representing the current unit.

        :return: JSON object represents DoseAreaProduct DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "GraySquareMeter"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of DoseAreaProduct DTO from a json representation.

        :param data: The DoseAreaProduct DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "GraySquareMeter"}
        :return: A new instance of DoseAreaProductDto.
        :rtype: DoseAreaProductDto
        """
        return DoseAreaProductDto(value=data["value"], unit=DoseAreaProductUnits(data["unit"]))


class DoseAreaProduct(AbstractMeasure):
    """
    It is defined as the absorbed dose multiplied by the area irradiated.

    Args:
        value (float): The value.
        from_unit (DoseAreaProductUnits): The DoseAreaProduct unit to create from, The default unit is GraySquareMeter
    """
    def __init__(self, value: float, from_unit: DoseAreaProductUnits = DoseAreaProductUnits.GraySquareMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__gray_square_meters = None
        
        self.__gray_square_decimeters = None
        
        self.__gray_square_centimeters = None
        
        self.__gray_square_millimeters = None
        
        self.__microgray_square_meters = None
        
        self.__milligray_square_meters = None
        
        self.__centigray_square_meters = None
        
        self.__decigray_square_meters = None
        
        self.__microgray_square_decimeters = None
        
        self.__milligray_square_decimeters = None
        
        self.__centigray_square_decimeters = None
        
        self.__decigray_square_decimeters = None
        
        self.__microgray_square_centimeters = None
        
        self.__milligray_square_centimeters = None
        
        self.__centigray_square_centimeters = None
        
        self.__decigray_square_centimeters = None
        
        self.__microgray_square_millimeters = None
        
        self.__milligray_square_millimeters = None
        
        self.__centigray_square_millimeters = None
        
        self.__decigray_square_millimeters = None
        

    def convert(self, unit: DoseAreaProductUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: DoseAreaProductUnits = DoseAreaProductUnits.GraySquareMeter) -> DoseAreaProductDto:
        """
        Get a new instance of DoseAreaProduct DTO representing the current unit.

        :param hold_in_unit: The specific DoseAreaProduct unit to store the DoseAreaProduct value in the DTO representation.
        :type hold_in_unit: DoseAreaProductUnits
        :return: A new instance of DoseAreaProductDto.
        :rtype: DoseAreaProductDto
        """
        return DoseAreaProductDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: DoseAreaProductUnits = DoseAreaProductUnits.GraySquareMeter):
        """
        Get a DoseAreaProduct DTO JSON object representing the current unit.

        :param hold_in_unit: The specific DoseAreaProduct unit to store the DoseAreaProduct value in the DTO representation.
        :type hold_in_unit: DoseAreaProductUnits
        :return: JSON object represents DoseAreaProduct DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "GraySquareMeter"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(dose_area_product_dto: DoseAreaProductDto):
        """
        Obtain a new instance of DoseAreaProduct from a DTO unit object.

        :param dose_area_product_dto: The DoseAreaProduct DTO representation.
        :type dose_area_product_dto: DoseAreaProductDto
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(dose_area_product_dto.value, dose_area_product_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of DoseAreaProduct from a DTO unit json representation.

        :param data: The DoseAreaProduct DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "GraySquareMeter"}
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct.from_dto(DoseAreaProductDto.from_json(data))

    def __convert_from_base(self, from_unit: DoseAreaProductUnits) -> float:
        value = self._value
        
        if from_unit == DoseAreaProductUnits.GraySquareMeter:
            return (value)
        
        if from_unit == DoseAreaProductUnits.GraySquareDecimeter:
            return (value * 100)
        
        if from_unit == DoseAreaProductUnits.GraySquareCentimeter:
            return (value * 10000)
        
        if from_unit == DoseAreaProductUnits.GraySquareMillimeter:
            return (value * 1000000)
        
        if from_unit == DoseAreaProductUnits.MicrograySquareMeter:
            return ((value) / 1e-06)
        
        if from_unit == DoseAreaProductUnits.MilligraySquareMeter:
            return ((value) / 0.001)
        
        if from_unit == DoseAreaProductUnits.CentigraySquareMeter:
            return ((value) / 0.01)
        
        if from_unit == DoseAreaProductUnits.DecigraySquareMeter:
            return ((value) / 0.1)
        
        if from_unit == DoseAreaProductUnits.MicrograySquareDecimeter:
            return ((value * 100) / 1e-06)
        
        if from_unit == DoseAreaProductUnits.MilligraySquareDecimeter:
            return ((value * 100) / 0.001)
        
        if from_unit == DoseAreaProductUnits.CentigraySquareDecimeter:
            return ((value * 100) / 0.01)
        
        if from_unit == DoseAreaProductUnits.DecigraySquareDecimeter:
            return ((value * 100) / 0.1)
        
        if from_unit == DoseAreaProductUnits.MicrograySquareCentimeter:
            return ((value * 10000) / 1e-06)
        
        if from_unit == DoseAreaProductUnits.MilligraySquareCentimeter:
            return ((value * 10000) / 0.001)
        
        if from_unit == DoseAreaProductUnits.CentigraySquareCentimeter:
            return ((value * 10000) / 0.01)
        
        if from_unit == DoseAreaProductUnits.DecigraySquareCentimeter:
            return ((value * 10000) / 0.1)
        
        if from_unit == DoseAreaProductUnits.MicrograySquareMillimeter:
            return ((value * 1000000) / 1e-06)
        
        if from_unit == DoseAreaProductUnits.MilligraySquareMillimeter:
            return ((value * 1000000) / 0.001)
        
        if from_unit == DoseAreaProductUnits.CentigraySquareMillimeter:
            return ((value * 1000000) / 0.01)
        
        if from_unit == DoseAreaProductUnits.DecigraySquareMillimeter:
            return ((value * 1000000) / 0.1)
        
        return None


    def __convert_to_base(self, value: float, to_unit: DoseAreaProductUnits) -> float:
        
        if to_unit == DoseAreaProductUnits.GraySquareMeter:
            return (value)
        
        if to_unit == DoseAreaProductUnits.GraySquareDecimeter:
            return (value / 100)
        
        if to_unit == DoseAreaProductUnits.GraySquareCentimeter:
            return (value / 10000)
        
        if to_unit == DoseAreaProductUnits.GraySquareMillimeter:
            return (value / 1000000)
        
        if to_unit == DoseAreaProductUnits.MicrograySquareMeter:
            return ((value) * 1e-06)
        
        if to_unit == DoseAreaProductUnits.MilligraySquareMeter:
            return ((value) * 0.001)
        
        if to_unit == DoseAreaProductUnits.CentigraySquareMeter:
            return ((value) * 0.01)
        
        if to_unit == DoseAreaProductUnits.DecigraySquareMeter:
            return ((value) * 0.1)
        
        if to_unit == DoseAreaProductUnits.MicrograySquareDecimeter:
            return ((value / 100) * 1e-06)
        
        if to_unit == DoseAreaProductUnits.MilligraySquareDecimeter:
            return ((value / 100) * 0.001)
        
        if to_unit == DoseAreaProductUnits.CentigraySquareDecimeter:
            return ((value / 100) * 0.01)
        
        if to_unit == DoseAreaProductUnits.DecigraySquareDecimeter:
            return ((value / 100) * 0.1)
        
        if to_unit == DoseAreaProductUnits.MicrograySquareCentimeter:
            return ((value / 10000) * 1e-06)
        
        if to_unit == DoseAreaProductUnits.MilligraySquareCentimeter:
            return ((value / 10000) * 0.001)
        
        if to_unit == DoseAreaProductUnits.CentigraySquareCentimeter:
            return ((value / 10000) * 0.01)
        
        if to_unit == DoseAreaProductUnits.DecigraySquareCentimeter:
            return ((value / 10000) * 0.1)
        
        if to_unit == DoseAreaProductUnits.MicrograySquareMillimeter:
            return ((value / 1000000) * 1e-06)
        
        if to_unit == DoseAreaProductUnits.MilligraySquareMillimeter:
            return ((value / 1000000) * 0.001)
        
        if to_unit == DoseAreaProductUnits.CentigraySquareMillimeter:
            return ((value / 1000000) * 0.01)
        
        if to_unit == DoseAreaProductUnits.DecigraySquareMillimeter:
            return ((value / 1000000) * 0.1)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_gray_square_meters(gray_square_meters: float):
        """
        Create a new instance of DoseAreaProduct from a value in gray_square_meters.

        

        :param meters: The DoseAreaProduct value in gray_square_meters.
        :type gray_square_meters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(gray_square_meters, DoseAreaProductUnits.GraySquareMeter)

    
    @staticmethod
    def from_gray_square_decimeters(gray_square_decimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in gray_square_decimeters.

        

        :param meters: The DoseAreaProduct value in gray_square_decimeters.
        :type gray_square_decimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(gray_square_decimeters, DoseAreaProductUnits.GraySquareDecimeter)

    
    @staticmethod
    def from_gray_square_centimeters(gray_square_centimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in gray_square_centimeters.

        

        :param meters: The DoseAreaProduct value in gray_square_centimeters.
        :type gray_square_centimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(gray_square_centimeters, DoseAreaProductUnits.GraySquareCentimeter)

    
    @staticmethod
    def from_gray_square_millimeters(gray_square_millimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in gray_square_millimeters.

        

        :param meters: The DoseAreaProduct value in gray_square_millimeters.
        :type gray_square_millimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(gray_square_millimeters, DoseAreaProductUnits.GraySquareMillimeter)

    
    @staticmethod
    def from_microgray_square_meters(microgray_square_meters: float):
        """
        Create a new instance of DoseAreaProduct from a value in microgray_square_meters.

        

        :param meters: The DoseAreaProduct value in microgray_square_meters.
        :type microgray_square_meters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(microgray_square_meters, DoseAreaProductUnits.MicrograySquareMeter)

    
    @staticmethod
    def from_milligray_square_meters(milligray_square_meters: float):
        """
        Create a new instance of DoseAreaProduct from a value in milligray_square_meters.

        

        :param meters: The DoseAreaProduct value in milligray_square_meters.
        :type milligray_square_meters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(milligray_square_meters, DoseAreaProductUnits.MilligraySquareMeter)

    
    @staticmethod
    def from_centigray_square_meters(centigray_square_meters: float):
        """
        Create a new instance of DoseAreaProduct from a value in centigray_square_meters.

        

        :param meters: The DoseAreaProduct value in centigray_square_meters.
        :type centigray_square_meters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(centigray_square_meters, DoseAreaProductUnits.CentigraySquareMeter)

    
    @staticmethod
    def from_decigray_square_meters(decigray_square_meters: float):
        """
        Create a new instance of DoseAreaProduct from a value in decigray_square_meters.

        

        :param meters: The DoseAreaProduct value in decigray_square_meters.
        :type decigray_square_meters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(decigray_square_meters, DoseAreaProductUnits.DecigraySquareMeter)

    
    @staticmethod
    def from_microgray_square_decimeters(microgray_square_decimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in microgray_square_decimeters.

        

        :param meters: The DoseAreaProduct value in microgray_square_decimeters.
        :type microgray_square_decimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(microgray_square_decimeters, DoseAreaProductUnits.MicrograySquareDecimeter)

    
    @staticmethod
    def from_milligray_square_decimeters(milligray_square_decimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in milligray_square_decimeters.

        

        :param meters: The DoseAreaProduct value in milligray_square_decimeters.
        :type milligray_square_decimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(milligray_square_decimeters, DoseAreaProductUnits.MilligraySquareDecimeter)

    
    @staticmethod
    def from_centigray_square_decimeters(centigray_square_decimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in centigray_square_decimeters.

        

        :param meters: The DoseAreaProduct value in centigray_square_decimeters.
        :type centigray_square_decimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(centigray_square_decimeters, DoseAreaProductUnits.CentigraySquareDecimeter)

    
    @staticmethod
    def from_decigray_square_decimeters(decigray_square_decimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in decigray_square_decimeters.

        

        :param meters: The DoseAreaProduct value in decigray_square_decimeters.
        :type decigray_square_decimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(decigray_square_decimeters, DoseAreaProductUnits.DecigraySquareDecimeter)

    
    @staticmethod
    def from_microgray_square_centimeters(microgray_square_centimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in microgray_square_centimeters.

        

        :param meters: The DoseAreaProduct value in microgray_square_centimeters.
        :type microgray_square_centimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(microgray_square_centimeters, DoseAreaProductUnits.MicrograySquareCentimeter)

    
    @staticmethod
    def from_milligray_square_centimeters(milligray_square_centimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in milligray_square_centimeters.

        

        :param meters: The DoseAreaProduct value in milligray_square_centimeters.
        :type milligray_square_centimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(milligray_square_centimeters, DoseAreaProductUnits.MilligraySquareCentimeter)

    
    @staticmethod
    def from_centigray_square_centimeters(centigray_square_centimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in centigray_square_centimeters.

        

        :param meters: The DoseAreaProduct value in centigray_square_centimeters.
        :type centigray_square_centimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(centigray_square_centimeters, DoseAreaProductUnits.CentigraySquareCentimeter)

    
    @staticmethod
    def from_decigray_square_centimeters(decigray_square_centimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in decigray_square_centimeters.

        

        :param meters: The DoseAreaProduct value in decigray_square_centimeters.
        :type decigray_square_centimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(decigray_square_centimeters, DoseAreaProductUnits.DecigraySquareCentimeter)

    
    @staticmethod
    def from_microgray_square_millimeters(microgray_square_millimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in microgray_square_millimeters.

        

        :param meters: The DoseAreaProduct value in microgray_square_millimeters.
        :type microgray_square_millimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(microgray_square_millimeters, DoseAreaProductUnits.MicrograySquareMillimeter)

    
    @staticmethod
    def from_milligray_square_millimeters(milligray_square_millimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in milligray_square_millimeters.

        

        :param meters: The DoseAreaProduct value in milligray_square_millimeters.
        :type milligray_square_millimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(milligray_square_millimeters, DoseAreaProductUnits.MilligraySquareMillimeter)

    
    @staticmethod
    def from_centigray_square_millimeters(centigray_square_millimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in centigray_square_millimeters.

        

        :param meters: The DoseAreaProduct value in centigray_square_millimeters.
        :type centigray_square_millimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(centigray_square_millimeters, DoseAreaProductUnits.CentigraySquareMillimeter)

    
    @staticmethod
    def from_decigray_square_millimeters(decigray_square_millimeters: float):
        """
        Create a new instance of DoseAreaProduct from a value in decigray_square_millimeters.

        

        :param meters: The DoseAreaProduct value in decigray_square_millimeters.
        :type decigray_square_millimeters: float
        :return: A new instance of DoseAreaProduct.
        :rtype: DoseAreaProduct
        """
        return DoseAreaProduct(decigray_square_millimeters, DoseAreaProductUnits.DecigraySquareMillimeter)

    
    @property
    def gray_square_meters(self) -> float:
        """
        
        """
        if self.__gray_square_meters != None:
            return self.__gray_square_meters
        self.__gray_square_meters = self.__convert_from_base(DoseAreaProductUnits.GraySquareMeter)
        return self.__gray_square_meters

    
    @property
    def gray_square_decimeters(self) -> float:
        """
        
        """
        if self.__gray_square_decimeters != None:
            return self.__gray_square_decimeters
        self.__gray_square_decimeters = self.__convert_from_base(DoseAreaProductUnits.GraySquareDecimeter)
        return self.__gray_square_decimeters

    
    @property
    def gray_square_centimeters(self) -> float:
        """
        
        """
        if self.__gray_square_centimeters != None:
            return self.__gray_square_centimeters
        self.__gray_square_centimeters = self.__convert_from_base(DoseAreaProductUnits.GraySquareCentimeter)
        return self.__gray_square_centimeters

    
    @property
    def gray_square_millimeters(self) -> float:
        """
        
        """
        if self.__gray_square_millimeters != None:
            return self.__gray_square_millimeters
        self.__gray_square_millimeters = self.__convert_from_base(DoseAreaProductUnits.GraySquareMillimeter)
        return self.__gray_square_millimeters

    
    @property
    def microgray_square_meters(self) -> float:
        """
        
        """
        if self.__microgray_square_meters != None:
            return self.__microgray_square_meters
        self.__microgray_square_meters = self.__convert_from_base(DoseAreaProductUnits.MicrograySquareMeter)
        return self.__microgray_square_meters

    
    @property
    def milligray_square_meters(self) -> float:
        """
        
        """
        if self.__milligray_square_meters != None:
            return self.__milligray_square_meters
        self.__milligray_square_meters = self.__convert_from_base(DoseAreaProductUnits.MilligraySquareMeter)
        return self.__milligray_square_meters

    
    @property
    def centigray_square_meters(self) -> float:
        """
        
        """
        if self.__centigray_square_meters != None:
            return self.__centigray_square_meters
        self.__centigray_square_meters = self.__convert_from_base(DoseAreaProductUnits.CentigraySquareMeter)
        return self.__centigray_square_meters

    
    @property
    def decigray_square_meters(self) -> float:
        """
        
        """
        if self.__decigray_square_meters != None:
            return self.__decigray_square_meters
        self.__decigray_square_meters = self.__convert_from_base(DoseAreaProductUnits.DecigraySquareMeter)
        return self.__decigray_square_meters

    
    @property
    def microgray_square_decimeters(self) -> float:
        """
        
        """
        if self.__microgray_square_decimeters != None:
            return self.__microgray_square_decimeters
        self.__microgray_square_decimeters = self.__convert_from_base(DoseAreaProductUnits.MicrograySquareDecimeter)
        return self.__microgray_square_decimeters

    
    @property
    def milligray_square_decimeters(self) -> float:
        """
        
        """
        if self.__milligray_square_decimeters != None:
            return self.__milligray_square_decimeters
        self.__milligray_square_decimeters = self.__convert_from_base(DoseAreaProductUnits.MilligraySquareDecimeter)
        return self.__milligray_square_decimeters

    
    @property
    def centigray_square_decimeters(self) -> float:
        """
        
        """
        if self.__centigray_square_decimeters != None:
            return self.__centigray_square_decimeters
        self.__centigray_square_decimeters = self.__convert_from_base(DoseAreaProductUnits.CentigraySquareDecimeter)
        return self.__centigray_square_decimeters

    
    @property
    def decigray_square_decimeters(self) -> float:
        """
        
        """
        if self.__decigray_square_decimeters != None:
            return self.__decigray_square_decimeters
        self.__decigray_square_decimeters = self.__convert_from_base(DoseAreaProductUnits.DecigraySquareDecimeter)
        return self.__decigray_square_decimeters

    
    @property
    def microgray_square_centimeters(self) -> float:
        """
        
        """
        if self.__microgray_square_centimeters != None:
            return self.__microgray_square_centimeters
        self.__microgray_square_centimeters = self.__convert_from_base(DoseAreaProductUnits.MicrograySquareCentimeter)
        return self.__microgray_square_centimeters

    
    @property
    def milligray_square_centimeters(self) -> float:
        """
        
        """
        if self.__milligray_square_centimeters != None:
            return self.__milligray_square_centimeters
        self.__milligray_square_centimeters = self.__convert_from_base(DoseAreaProductUnits.MilligraySquareCentimeter)
        return self.__milligray_square_centimeters

    
    @property
    def centigray_square_centimeters(self) -> float:
        """
        
        """
        if self.__centigray_square_centimeters != None:
            return self.__centigray_square_centimeters
        self.__centigray_square_centimeters = self.__convert_from_base(DoseAreaProductUnits.CentigraySquareCentimeter)
        return self.__centigray_square_centimeters

    
    @property
    def decigray_square_centimeters(self) -> float:
        """
        
        """
        if self.__decigray_square_centimeters != None:
            return self.__decigray_square_centimeters
        self.__decigray_square_centimeters = self.__convert_from_base(DoseAreaProductUnits.DecigraySquareCentimeter)
        return self.__decigray_square_centimeters

    
    @property
    def microgray_square_millimeters(self) -> float:
        """
        
        """
        if self.__microgray_square_millimeters != None:
            return self.__microgray_square_millimeters
        self.__microgray_square_millimeters = self.__convert_from_base(DoseAreaProductUnits.MicrograySquareMillimeter)
        return self.__microgray_square_millimeters

    
    @property
    def milligray_square_millimeters(self) -> float:
        """
        
        """
        if self.__milligray_square_millimeters != None:
            return self.__milligray_square_millimeters
        self.__milligray_square_millimeters = self.__convert_from_base(DoseAreaProductUnits.MilligraySquareMillimeter)
        return self.__milligray_square_millimeters

    
    @property
    def centigray_square_millimeters(self) -> float:
        """
        
        """
        if self.__centigray_square_millimeters != None:
            return self.__centigray_square_millimeters
        self.__centigray_square_millimeters = self.__convert_from_base(DoseAreaProductUnits.CentigraySquareMillimeter)
        return self.__centigray_square_millimeters

    
    @property
    def decigray_square_millimeters(self) -> float:
        """
        
        """
        if self.__decigray_square_millimeters != None:
            return self.__decigray_square_millimeters
        self.__decigray_square_millimeters = self.__convert_from_base(DoseAreaProductUnits.DecigraySquareMillimeter)
        return self.__decigray_square_millimeters

    
    def to_string(self, unit: DoseAreaProductUnits = DoseAreaProductUnits.GraySquareMeter, fractional_digits: int = None) -> str:
        """
        Format the DoseAreaProduct to a string.
        
        Note: the default format for DoseAreaProduct is GraySquareMeter.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the DoseAreaProduct. Default is 'GraySquareMeter'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == DoseAreaProductUnits.GraySquareMeter:
            return f"""{super()._truncate_fraction_digits(self.gray_square_meters, fractional_digits)} Gy·m²"""
        
        if unit == DoseAreaProductUnits.GraySquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.gray_square_decimeters, fractional_digits)} Gy·dm²"""
        
        if unit == DoseAreaProductUnits.GraySquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.gray_square_centimeters, fractional_digits)} Gy·cm²"""
        
        if unit == DoseAreaProductUnits.GraySquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.gray_square_millimeters, fractional_digits)} Gy·mm²"""
        
        if unit == DoseAreaProductUnits.MicrograySquareMeter:
            return f"""{super()._truncate_fraction_digits(self.microgray_square_meters, fractional_digits)} μGy·m²"""
        
        if unit == DoseAreaProductUnits.MilligraySquareMeter:
            return f"""{super()._truncate_fraction_digits(self.milligray_square_meters, fractional_digits)} mGy·m²"""
        
        if unit == DoseAreaProductUnits.CentigraySquareMeter:
            return f"""{super()._truncate_fraction_digits(self.centigray_square_meters, fractional_digits)} cGy·m²"""
        
        if unit == DoseAreaProductUnits.DecigraySquareMeter:
            return f"""{super()._truncate_fraction_digits(self.decigray_square_meters, fractional_digits)} dGy·m²"""
        
        if unit == DoseAreaProductUnits.MicrograySquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.microgray_square_decimeters, fractional_digits)} μGy·dm²"""
        
        if unit == DoseAreaProductUnits.MilligraySquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.milligray_square_decimeters, fractional_digits)} mGy·dm²"""
        
        if unit == DoseAreaProductUnits.CentigraySquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.centigray_square_decimeters, fractional_digits)} cGy·dm²"""
        
        if unit == DoseAreaProductUnits.DecigraySquareDecimeter:
            return f"""{super()._truncate_fraction_digits(self.decigray_square_decimeters, fractional_digits)} dGy·dm²"""
        
        if unit == DoseAreaProductUnits.MicrograySquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.microgray_square_centimeters, fractional_digits)} μGy·cm²"""
        
        if unit == DoseAreaProductUnits.MilligraySquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.milligray_square_centimeters, fractional_digits)} mGy·cm²"""
        
        if unit == DoseAreaProductUnits.CentigraySquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.centigray_square_centimeters, fractional_digits)} cGy·cm²"""
        
        if unit == DoseAreaProductUnits.DecigraySquareCentimeter:
            return f"""{super()._truncate_fraction_digits(self.decigray_square_centimeters, fractional_digits)} dGy·cm²"""
        
        if unit == DoseAreaProductUnits.MicrograySquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.microgray_square_millimeters, fractional_digits)} μGy·mm²"""
        
        if unit == DoseAreaProductUnits.MilligraySquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.milligray_square_millimeters, fractional_digits)} mGy·mm²"""
        
        if unit == DoseAreaProductUnits.CentigraySquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.centigray_square_millimeters, fractional_digits)} cGy·mm²"""
        
        if unit == DoseAreaProductUnits.DecigraySquareMillimeter:
            return f"""{super()._truncate_fraction_digits(self.decigray_square_millimeters, fractional_digits)} dGy·mm²"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: DoseAreaProductUnits = DoseAreaProductUnits.GraySquareMeter) -> str:
        """
        Get DoseAreaProduct unit abbreviation.
        Note! the default abbreviation for DoseAreaProduct is GraySquareMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == DoseAreaProductUnits.GraySquareMeter:
            return """Gy·m²"""
        
        if unit_abbreviation == DoseAreaProductUnits.GraySquareDecimeter:
            return """Gy·dm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.GraySquareCentimeter:
            return """Gy·cm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.GraySquareMillimeter:
            return """Gy·mm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MicrograySquareMeter:
            return """μGy·m²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MilligraySquareMeter:
            return """mGy·m²"""
        
        if unit_abbreviation == DoseAreaProductUnits.CentigraySquareMeter:
            return """cGy·m²"""
        
        if unit_abbreviation == DoseAreaProductUnits.DecigraySquareMeter:
            return """dGy·m²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MicrograySquareDecimeter:
            return """μGy·dm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MilligraySquareDecimeter:
            return """mGy·dm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.CentigraySquareDecimeter:
            return """cGy·dm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.DecigraySquareDecimeter:
            return """dGy·dm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MicrograySquareCentimeter:
            return """μGy·cm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MilligraySquareCentimeter:
            return """mGy·cm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.CentigraySquareCentimeter:
            return """cGy·cm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.DecigraySquareCentimeter:
            return """dGy·cm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MicrograySquareMillimeter:
            return """μGy·mm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.MilligraySquareMillimeter:
            return """mGy·mm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.CentigraySquareMillimeter:
            return """cGy·mm²"""
        
        if unit_abbreviation == DoseAreaProductUnits.DecigraySquareMillimeter:
            return """dGy·mm²"""
        