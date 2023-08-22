from typing import List

from jinja2 import Template, StrictUndefined
from templates import readme_template


def readme_generator(definitions: List):
    template_methods = []

    for definition in definitions:
        singular_name = definition.get("Name")
        description = definition.get("XmlDocSummary") or ""
        template_methods.append(
            {
                "description": description,
                "unit_name": singular_name,
            }
        )

    template_data = {"methods": template_methods}

    # Create a Jinja2 template object
    template = Template(readme_template, undefined=StrictUndefined)

    # Render the template with the data
    code = template.render(template_data)

    with open(f"README.md", "w", encoding="utf-8") as f:
        f.write(code)

    print(f'[readme_generator] Generating "README.md" finished successfully')
