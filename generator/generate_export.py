from jinja2 import Template, StrictUndefined
from utils import camel_to_snake

# Load jinja template for the python unit class
template_str = ""
with open("generator/export_template.jinja2", "r") as f:
    template_str = f.read()
    
def export_generator(definitions: list):
    template_methods = []

    for definition in definitions:
        singular_name = definition.get("Name")

        template_methods.append(
            {
                "unit": camel_to_snake(singular_name),
                "unit_name": singular_name,
            }
        )

    template_data = {"methods": template_methods}
    
    # Create a Jinja2 template object
    template = Template(template_str, undefined=StrictUndefined)

    # Render the template with the data
    code = template.render(template_data)

    with open(f"unitsnet-py/main.py", "w", encoding="utf-8") as f:
        f.write(code)

    print(f'[generate_unit_class] Generating main.py finished successfully')
