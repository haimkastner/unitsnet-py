from fetch_units_definitions import get_definitions
from class_generator import generate_unit_class
from generate_export import export_generator

print("Starting generating python units...")

# Fetch all units definitions
definitions = get_definitions("angularsen/UnitsNet")

# Generate python unit class for each unit definition
for definition in definitions:
    generate_unit_class(definition)

export_generator(definitions)

print("Generating python units finished successfully")
