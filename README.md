# readmdict [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/readmdict.svg)](https://badge.fury.io/py/readmdict)

Read mdx/mdd files (repacking of readmdict from mdict-analysis)

This is a repacking of `readmdict.py` in [https://github.com/csarron/mdict-analysis](https://github.com/csarron/mdict-analysis). All credit goes to the original author(s).

## Installation
```bash
pip install readmdict
# or poetry add readmdict
```

## Usage

### Command line
*   Browse a mdx or mdd file and print its meta information
```bash
readmdict
```
or
```bash
python -m readmdict
```


*   Print meta info of a file `file.mdx`
```bash
readmdict file.mdx
```
or
```bash
python -m readmdict file.mdx
```

*   Print a short summary
```bash
readmdict -h
```
or
```bash
python -m readmdict -h
```

### In Python code
```python
from readmdict import MDX, MDD

filename = "some.mdx"
headwords = [*MDX(filename)]
print(headwods[:10])  # fisrt 10 in bytes format
for hdw in headwods[:10]:
	print(hdw.decode())   # fisrt 10 in string format

items = [*MDX(filename).items()
for key, val in items[:10]:
	print(key.decode(), val.decode())  # first 10 entries

```


## Optional `python-lzo`
If `python-lzo` is not present, you' ll see "LZO compression support is not available" when running `readmdict`. Should this bother you, install `python-lzo`.

```bash
pip install python-lzo
# or poerty add python-lzo
```

When not successful in Windows, head to
[https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-lzo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-lzo). Download and install `python-lzo` whl for your python version.

