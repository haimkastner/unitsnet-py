# unitsnet-py

[![Build & Test Status](https://github.com/haimkastner/unitsnet-py/workflows/unitsnet-py/badge.svg?branch=main)](https://github.com/haimkastner/unitsnet-py/actions)

 [![Latest Release](https://img.shields.io/github/v/release/haimkastner/unitsnet-py)](https://github.com/haimkastner/unitsnet-py/releases) 
[![PyPI version](https://img.shields.io/pypi/v/unitsnet-py)](https://pypi.org/project/unitsnet-py/)


[![GitHub stars](https://img.shields.io/github/stars/haimkastner/unitsnet-py.svg?style=social&label=Stars)](https://github.com/haimkastner/unitsnet-py/stargazers) 
[![pypi downloads](https://img.shields.io/pypi/dm/unitsnet-py.svg?style=social)](https://pypi.org/project/unitsnet-py/)
[![License](https://img.shields.io/github/license/haimkastner/unitsnet-py.svg?style=social)](https://github.com/haimkastner/unitsnet-py/blob/master/LICENSE)

The unitsnet-py package provides an efficient way to store unit variables and perform easy conversions to different units when it required. 

It offers support for more than 100 unit types across various unit categories, including pretty-printing, comparison, and arithmetic methods. 

The API is designed to be user-friendly and straightforward to use.

The library is built on top of the [Units.NET](https://github.com/angularsen/UnitsNet) project and leverages their [definitions sources](https://github.com/angularsen/UnitsNet/tree/master/Common/UnitDefinitions) to generate the Python unit classes.

###### The unitsnet-py package does not require any external dependencies or packages to function.


Package is available on PyPI at https://pypi.org/project/unitsnet-py/

[Units.NET on other platforms](#unitsnet-on-other-platforms)

## Install via PyPi

```bash 
pip install unitsnet-py
```

## Example Usage

```python
from unitsnet_py import Angle, AngleUnits, Length, LengthUnits


angle = Angle.from_degrees(180)
# equals to
angle = Angle(180, AngleUnits.Degree)

print(angle.radians)  # 3.141592653589793
print(angle.microradians)  # 3141592.65358979
print(angle.gradians)  # 200
print(angle.microdegrees)  # 180000000


# As an alternative, a convert style method are also available
print(angle.convert(AngleUnits.Radian))  # 3.141592653589793
print(angle.convert(AngleUnits.Microradian))  # 3141592.65358979
print(angle.convert(AngleUnits.Gradian))  # 200
print(angle.convert(AngleUnits.Microdegree))  # 180000000


# Print the default unit to_string (The default for angle is degrees)
print(angle.to_string())  # 180 °

print(angle.to_string(AngleUnits.Degree))  # 180 °
print(angle.to_string(AngleUnits.Radian))  # 3.141592653589793 rad

# Specify fraction digits max length
print(angle.to_string(AngleUnits.Radian, 2))  # 3.14 rad
```

## Additional methods

Check, compare, calculate etc. with unitsnet:

```python
length1 = Length.from_meters(10)
length2 = Length.from_decimeters(100)
length3 = Length.from_meters(3)

# 'equals' method
print(length1 == length2)  # True
print(length1 == length3)  # False

# 'compareTo' method
print(length3 > length1)  # False
print(length3 < length1)  # True
print(length2 >= length1)  # True

# Arithmetics methods
results1 = length1 + length3
results2 = length1 - length3
results3 = length1 * length3
results4 = length1 / length3
results5 = length1 % length3
results6 = length1 ** length3
print(results1.to_string(LengthUnits.Meter))  # 13 m
print(results2.to_string(LengthUnits.Meter))  # 7 m
print(results3.to_string(LengthUnits.Meter))  # 30 m
print(results4.to_string(LengthUnits.Meter))  # 3.3333333333333335 m
print(results5.to_string(LengthUnits.Meter))  # 1 m
print(results6.to_string(LengthUnits.Meter))  # 1000 m

# Complex objects

# Any object supports arithmetic operations can be used as well as unit
# see numpy array example:
import numpy as np

np_array = np.array([[2, 4, 6], [7, 8, 9]])

np_array_length = Length.from_kilometers(np_array)
print(np_array_length.meters) # [[2000. 4000. 6000.][7000. 8000. 9000.]]

np_array_double_length = np_array_length + np_array_length
print(np_array_double_length.kilometers) # [[ 4.  8. 12.][14. 16. 18.]]
print(np_array_double_length.meters) # [[ 4000.  8000. 12000.][14000. 16000. 18000.]]

```
## DTO - Data Transfer Object

As UnitsNet provides a convenient way to work within a running service, there are occasions where the data needs to be exposed outside of the service, typically through an API containing the unit value or consumed from an API.

To support this with a clear API schema and make it easy to convert to and from this schema to the specific format, it's recommended to use DTOs and the UnitsNet flavor converters.

```python
from unitsnet_py import Length, LengthDto, LengthUnits

 # Create a Length unit object
length = Length.from_meters(100.01)
# Obtain the DTO object as json, represented by the default unit - meter
length_dto_json = length.to_dto_json() # {"value":100.01,"unit":"Meter"}
# Obtain the same value but represent DTO in KM 
length_dto_represents_in_km_json = length.to_dto_json(LengthUnits.Kilometer) # {'value': 0.10001, 'unit': 'Kilometer'}
# Load JSON to DTO, and load
length_from_meters_dto = Length.from_dto_json(length_dto_json)
# The exact same value as
length_from_km_dto = Length.from_dto_json(length_dto_represents_in_km_json)

# Additionally, it supports creating and handling as a DTO instance, as well as creating and converting to/from JSON.

# Get a DTO instance from a Length instance
length_dto: LengthDto = length.to_dto()
# Get the json representation of the DTO
length_json = length_dto.to_json() # {"value":100.01,"unit":"Meter"}
# Obtain DTO instance from a json representation
length_dto: LengthDto = LengthDto.from_json(length_json)
# Obtain Length unit from a DTO instance
length = Length.from_dto(length_dto)
```

Check out the OpenAPI [unitsnet-openapi-spec](https://haimkastner.github.io/unitsnet-openapi-spec-example/) example schema.

Also, refer to the detailed discussions on GitHub: [haimkastner/unitsnet-js#31](https://github.com/haimkastner/unitsnet-js/issues/31) & [angularsen/UnitsNet#1378](https://github.com/angularsen/UnitsNet/issues/1378).

## Supported units

[UnitsNet supported Units](https://github.com/haimkastner/unitsnet-py/blob/main/Units.md)

## Units.NET on other platforms

Get the same strongly typed units on other platforms, based on the same [unit definitions](/Common/UnitDefinitions).

| Language                   | Name        | Package                                           					 | Repository                                           | Maintainers  |
|----------------------------|-------------|---------------------------------------------------------------------|------------------------------------------------------|--------------|
| C#                         | UnitsNet    | [nuget](https://www.nuget.org/packages/UnitsNet/) 					 | [github](https://github.com/angularsen/UnitsNet)     | @angularsen  |
| JavaScript /<br>TypeScript | unitsnet-js | [npm](https://www.npmjs.com/package/unitsnet-js)  					 | [github](https://github.com/haimkastner/unitsnet-js) | @haimkastner |
| Python                     | unitsnet-py | [pypi](https://pypi.org/project/unitsnet-py)      					 | [github](https://github.com/haimkastner/unitsnet-py) | @haimkastner |
| Golang                     | unitsnet-go | [pkg.go.dev](https://pkg.go.dev/github.com/haimkastner/unitsnet-go) | [github](https://github.com/haimkastner/unitsnet-go) | @haimkastner |


