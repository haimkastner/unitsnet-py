import requests
import json
import re
import os

def ensure_directory_existence(file_path):
    """
    Ensure that the directory containing the given file path exists.
    If the directory does not exist, create it.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_json_file(file_name, data):
    """
    Write JSON data to a file.
    """
    try:
        file_path = os.path.join(os.getcwd(), '.cache', file_name)
        ensure_directory_existence(file_path)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"JSON data has been written to {file_path}")
    except Exception as e:
        print('Error writing JSON file:', e)

def read_json_file(file_name):
    """
    Read JSON data from a file.
    """
    try:
        file_path = os.path.join(os.getcwd(), '.cache', file_name)
        if os.path.exists(file_path):
            print(f"Loading {file_path} cache ...")
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            return None
    except Exception as e:
        print('Error reading JSON file:', e)
        return None
    

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


prefixes_factor_abbreviation = {
    'Exa': 'E',
    'Peta': 'P',
    'Tera': 'T',
    'Giga': 'G',
    'Mega': 'M',
    'Kilo': 'k',
    'Hecto': 'h',
    'Deca': 'da',
    'Deci': 'd',
    'Centi': 'c',
    'Milli': 'm',
    'Micro': 'μ',
    'Nano': 'n',
    'Pico': 'p',
    'Femto': 'f'
}
