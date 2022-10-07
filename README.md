# pybundlr
Simple py driver for bundlr

Constructed by wrapping [bundlr CLI](https://docs.bundlr.network/docs/client/cli).

Pypi: [Main](https://pypi.org/project/pybundlr/), [test](https://test.pypi.org/project/pybundlr)

## Prerequisites

- Linux/MacOS
- Python 3.8.5+
- Bundlr CLI: `npm install -g @bundlr-network/client`

## Install Pybundlr Library

Open a new terminal and:

```console
#Create & activate venv
python -m venv venv
source venv/bin/activate

#main install
pip install pybundlr
```

## Using Pybundlr Library

From terminal: `python`. Then, in Python console:
```python
from pybundlr import pybundlr
address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
bal = pybundlr.balance(address)
print(f"bal: {bal}")
```

## Development

- [Developers flow](developers.md) - to further develop pybundlr
- [Release process](release-process.md) - to do a new release of pybundlr
