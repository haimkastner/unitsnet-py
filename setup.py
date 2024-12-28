# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

packages = [
    'unitsnet_py',
    'unitsnet_py.units'
]

package_data = {
    '': ['*']
}

# The UnitNet definition version that the current package is based on to generate units classes
# see 
definition_version = '5.65.0'

setup_kwargs = {
    'name': 'unitsnet-py',
    'version': '0.1.139',
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
    'install_requires': [],
    'classifiers': [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
     ],
    'project_urls': {
        'Source': 'https://github.com/haimkastner/unitsnet-py',
        'Documentation': 'https://github.com/haimkastner/unitsnet-py#readme',
        'Issue Tracker': 'https://github.com/haimkastner/unitsnet-py/issues',
    },
}

setup(**setup_kwargs)
