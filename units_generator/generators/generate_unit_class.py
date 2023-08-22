from typing import Dict, List

from jinja2 import Template, StrictUndefined
from common.utils import camel_to_snake, prefixes_factor, upper_to_lower_camelcase
from templates import unit_class_template


def __format_formula(original_formula: str):
    # Remove C# number types
    python_formula = original_formula.replace("d", "").replace("m", "")
    # Convert to python code
    python_formula = python_formula.replace("{x}", "value").lower()
    return f"({python_formula})"


def __generate_prefixes(unit, prefixes) -> List[Dict]:
    prefixes_units = []
    for prefix in prefixes:
        prefix_factor = prefixes_factor.get(prefix)
        if not prefix_factor:
            continue
        # Build the prefix formula based on the original unit formula.
        from_unit_prefix_to_base_formula = (
            f'({unit.get("FromUnitToBaseFunc")}) * {prefix_factor}'
        )
        from_base_to_unit_prefix_formula = (
            f'({unit.get("FromBaseToUnitFunc")}) / {prefix_factor}'
        )

        deprecated = unit.get("Deprecated")
        singular_name = unit.get("SingularName")
        plural_nName = unit.get("PluralName")

        prefixes_units.append(
            {
                "Deprecated": deprecated,
                "FromUnitToBaseFunc": from_unit_prefix_to_base_formula,
                "FromBaseToUnitFunc": from_base_to_unit_prefix_formula,
                "SingularName": f"{prefix}{upper_to_lower_camelcase(singular_name)}",
                "PluralName": f"{prefix}{upper_to_lower_camelcase(plural_nName)}",
                "Localization": [
                    {
                        "Culture": "en-US",
                        "Abbreviations": [""],
                    }
                ],
            }
        )

    return prefixes_units


def __extant_unit_prefixes(units: List) -> List:
    prefixes_units = []

    for unit in units:
        prefixes = unit.get("Prefixes")
        if not prefixes:
            continue

        prefixes_units += __generate_prefixes(unit, prefixes)

    return prefixes_units


def __get_unit_abbreviation(abbreviation: List) -> str:
    us_abbreviation = next(
        filter(lambda x: x.get("Culture") == "en-US", abbreviation), None
    )

    if not us_abbreviation:
        return ""

    abbreviations = us_abbreviation.get("Abbreviations")
    return "" if not len(abbreviations) else abbreviations[0]


def unit_class_generator(unit_definition):
    # Filter out all deprecated units
    units = list(filter(lambda x: not x.get("Deprecated"), unit_definition["Units"]))

    unit_name = unit_definition.get("Name")

    print(f"[unit_class_generator] Generating units for {unit_name}...")

    # Add the units prefixes (like MiliXXX or KiloXXX) as unit in the unit units collection.
    all_units = units + __extant_unit_prefixes(units)

    template_methods = []

    for unit in all_units:
        singular_name = unit.get("SingularName")
        singular_name_camel_case = camel_to_snake(singular_name)
        plural_name = camel_to_snake(unit.get("PluralName"))
        description = unit.get("XmlDocSummary") or ""

        template_methods.append(
            {
                "unit_value": singular_name_camel_case,
                "name": plural_name,
                "unit": singular_name,
                "description": description,
                "formula_from_base": __format_formula(unit.get("FromBaseToUnitFunc")),
                "formula_to_base": __format_formula(unit.get("FromUnitToBaseFunc")),
                "abbreviation": __get_unit_abbreviation(unit.get("Localization")),
            }
        )

    template_data = {
        "unit": unit_name,
        "base_unit": unit_definition.get("BaseUnit"),
        "description": unit_definition.get("XmlDocSummary"),
        "methods": template_methods,
    }

    # Create a Jinja2 template object
    template = Template(unit_class_template, undefined=StrictUndefined)

    # Render the template with the data
    code = template.render(template_data)

    with open(
        f"unitsnet_py/units/{camel_to_snake(unit_name)}.py", "w", encoding="utf-8"
    ) as f:
        f.write(code)

    print(
        f"[unit_class_generator] Generating units for {unit_name} finished successfully"
    )
