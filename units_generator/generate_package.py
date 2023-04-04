from common.fetch_units_definitions import get_definitions
from generators.generate_unit_class import unit_class_generator
from generators.generate_export import export_generator
from generators.generate_readme import readme_generator

print("Starting generating python units...")

# Fetch all units definitions
definitions = get_definitions(repo_owner_and_name="angularsen/UnitsNet")

# Generate python unit class for each unit definition
for definition in definitions:
    unit_class_generator(unit_definition=definition)

# Generate units package export API
export_generator(definitions)

# Generate README doc file
readme_generator(definitions)

print("Generating python units package finished successfully")
