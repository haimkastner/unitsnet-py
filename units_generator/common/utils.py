import requests
import json
import re


def get_json_from_cdn(cdn_url):
    try:
        response = requests.get(
            cdn_url, headers={"user-agent": "PostmanRuntime/7.20.1"}
        )
        response.raise_for_status()
        # Skip utf-8 BOM char.
        cleaned_text = response.text.lstrip("\ufeff")
        json_data = json.loads(cleaned_text)
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve JSON from cdn: {e}")


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def upper_to_lower_camelcase(s):
    return s[:1].lower() + s[1:]

# The factor between unit and his prefix.
prefixes_factor = {
    'Exa': 1e18,
    'Peta': 1e15,
    'Tera': 1e12,
    'Giga': 1e9,
    'Mega': 1e6,
    'Kilo': 1e3,
    'Hecto': 1e2,
    'Deca': 1e1,
    'Deci': 1e-1,
    'Centi': 1e-2,
    'Milli': 1e-3,
    'Micro': 1e-6,
    'Nano': 1e-9,
    'Pico': 1e-12,
    'Femto': 1e-15,
}