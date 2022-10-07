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
