# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['readmdict']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['readmdict = readmdict.__main__:main']}

setup_kwargs = {
    'name': 'readmdict',
    'version': '0.1.0',
    'description': 'readmdict (simple repacking of readmdict in mdict-analysis)',
    'long_description': '# readmdict [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/readmdict.svg)](https://badge.fury.io/py/readmdict)\n\nRead mdx/mdd files (repacking of readmdict from mdict-analysis)\n\nThis is a repacking of `readmdict.py` in [https://github.com/csarron/mdict-analysis](https://github.com/csarron/mdict-analysis). All credit goes to the original author(s).\n\n## Installation\n```bash\npip install readmdict\n# or poetry add readmdict\n```\n\n## Usage\n\n### Command line\n*   Browse a mdx or mdd file and print its meta information\n```bash\nreadmdict\n```\nor\n```bash\npython -m readmdict\n```\n\n\n*   Print meta info of a file `file.mdx`\n```bash\nreadmdict file.mdx\n```\nor\n```bash\npython -m readmdict file.mdx\n```\n\n*   Print a short summary\n```bash\nreadmdict -h\n```\nor\n```bash\npython -m readmdict -h\n```\n\n### In Python code\n```python\nfrom readmdict import MDX, MDD\n\nfilename = "some.mdx"\nheadwords = [*MDX(filename)]\nprint(headwods[:10])  # fisrt 10 in bytes format\nfor hdw in headwods[:10]:\n\tprint(hdw.decode())   # fisrt 10 in string format\n\nitems = [*MDX(filename).items()\nfor key, val in items[:10]:\n\tprint(key.decode(), val.decode())  # first 10 entries\n\n```\n\n## Optional `python-lzo`\nIf `python-lzo` is not present, you\' ll see "LZO compression support is not available" when running `readmdict`. Should this bother you, install `python-lzo`.\n\n```bash\npip install python-lzo\n# or poerty add python-lzo\n```\n\nIn Windows without a functioning C++ environment, you won\'t be able to install `python-lzo` via `pip`. Head to\n[https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-lzo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-lzo). Download and install `python-lzo` whl for your python version.\n',
    'author': 'freemt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ffreemt/readmdict',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
