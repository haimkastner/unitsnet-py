from jinja2 import Template, StrictUndefined

from fetch_units_definitions import get_definitions
from class_generator import generate_unit_class


definitions = get_definitions('angularsen/UnitsNet')

for definition in definitions:
    generate_unit_class(definition)

# template_str = ""

# with open("unit_template.jinja2", "r") as f:
#     template_str = f.read()


# # Define the data to be used with the template
# data = {
#     "unit": "Length",
#     "units": [
#         {"unit_name": "meter", "description": "Bla bla meter"},
#         {"unit_name": "kilometer", "description": "Bla bla kilometer"},
#     ],
#     "base_unit": 'meter',
#     "methods": [
#         {
#             "name": "meters",
#             "unit": "meter",
#             "description": "Bla bla meter",
#             "formula_from_base": 'value',
#             "formula_to_base": 'value',
#             "abbreviation": "m",
#         },
#         {
#             "name": "kilometers",
#             "unit": "kilometer",
#             "description": "Bla bla kilometer",
#             "formula_from_base": 'value / 1000',
#             "formula_to_base": 'value * 1000',
#             "abbreviation": "km",
#         },
#     ],
# }

# # Create a Jinja2 template object
# template = Template(template_str, undefined=StrictUndefined)

# # Render the template with the data
# code = template.render(data)

# # Output the generated code
# print(code)

# with open("unitlength.py", "w") as f:
#     f.write(code)


# print("f")
