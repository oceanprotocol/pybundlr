# pybundlr
Simple py driver for bundlr

Constructed by wrapping [bundlr CLI](https://docs.bundlr.network/docs/client/cli).

# Installation

### Prerequisites

Ensure prerequisites:
- Linux/MacOS
- Python 3.8.5+
- Bundlr CLI: `npm install -g @bundlr-network/client`

### Install pybundlr

Open a new terminal and:

```console
#create a virtual environment
python -m venv venv

#activate env
source venv/bin/activate

#avoid issues
pip install wheel

#main install
pip install pybundlr
```

## Example Usage

From terminal, start a Python console:
```console
python
```

In Python console:
```python
import pybundlr
address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
bal = pybundlr.balance(address)
print(f"bal: {bal}")
```


## Release Process

Find the current version number at [pypi](https://pypi.org/project/pybundlr/).

Open `pyproject.toml` in an editor, and update the value in `"version" = x.y.z`.



In terminal:

```console
#go to root of directory
cd ~/code/pybundlr

#ensure repo is up-to-date
git commit -am "Release x.y.z"
git push

#turn off virtual env't
deactivate

#ensure `dist/` folder is empty
rm -rf dist

#generate distribution archives: create `dist` folder with two files 
python -m build

#run twine to upload `dist` files
python3 -m twine upload dist/*
```

Done! The updated package will be [at pypi](https://pypi.org/project/pybundlr/).

Notes: this section is based on [packaging.python.org tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).