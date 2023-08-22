from typing import List

from jinja2 import Template, StrictUndefined
from common.utils import camel_to_snake
from templates import export_classes_template


def export_generator(definitions: List):
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
    template = Template(export_classes_template, undefined=StrictUndefined)

    # Render the template with the data
    code = template.render(template_data)

    with open("unitsnet_py/__init__.py", "w", encoding="utf-8") as f:
        f.write(code)

    print('[export_generator] Generating "__init__.py" finished successfully')
