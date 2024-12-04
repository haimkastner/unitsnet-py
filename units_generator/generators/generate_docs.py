from typing import List

from jinja2 import Template, StrictUndefined
from templates import docs_template


def units_docs_generator(definitions: List):
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
    template = Template(docs_template, undefined=StrictUndefined)

    # Render the template with the data
    code = template.render(template_data)

    with open(f"Units.md", "w", encoding="utf-8") as f:
        f.write(code)

    print(f'[units_docs_generator] Generating "Units.md" finished successfully')
