# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

packages = \
['unitsnet_py', 'unitsnet_py.units']

package_data = \
{'': ['*']}

# The UnitNet definition version that the current package is based on to generate units classes
# see 
definition_version = '5.54.0'

setup_kwargs = {
    'name': 'unitsnet-py',
    'version': '0.1.117',
    'license': 'MIT',
    'keywords': 'conversion, units-of-measure, units, quantities, unit-converter, converter, unit, measure, measures, measurement, measurements',
    'description': 'A better way to hold unit variables and easily convert to the destination unit',
    'long_description': long_description,
    'long_description_content_type': "text/markdown",
    'author': 'Haim Kastner',
    'author_email': 'hello@haim-kastner.com',
    'maintainer': 'Haim Kastner',
    'maintainer_email': 'hello@haim-kastner.com',
    'url': 'https://github.com/haimkastner/unitsnet-py',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
    'install_requires': []
}


setup(**setup_kwargs)

