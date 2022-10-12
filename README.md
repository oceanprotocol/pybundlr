# pybundlr
Simple py driver for bundlr.

- Constructed by wrapping [bundlr CLI](https://docs.bundlr.network/docs/client/cli).
- [Full API in pybundlr.py](https://github.com/oceanprotocol/pybundlr/blob/main/src/pybundlr/pybundlr.py)
- [Pypi main](https://pypi.org/project/pybundlr/), [test](https://test.pypi.org/project/pybundlr)
- [GitHub repo](https://github.com/oceanprotocol/pybundlr)

## Installation

Ensure prerequisites:
- Linux/MacOS
- Python 3.8.5+
- Bundlr CLI: `npm install -g @bundlr-network/client`

Open a new terminal and:

```console
#Create & activate venv
python -m venv venv
source venv/bin/activate

#main install
pip3 install pybundlr
```

## Using Pybundlr Library

First, a quick example that reads information from a bundlr node. In this case, a balance.

In terminal, go into Python console: `python`

In Python console:
```python
from pybundlr import pybundlr
eth_address = "0x7BA3d8551A6f2C70a5d47bb448BcF7EF69661822"
bal = pybundlr.balance(eth_address, "matic")
print(f"{eth_address[:4]}'s MATIC balance in bundlr node: {bal} wei")
```

Exit the Python console for the next step.

Now, for more thorough example. We'll create a file, publish it online, then read it back.

The bundlr node will need funds to pay for storage. So, please ensure that you have a Polygon account that holds some MATIC. Just a few cents' worth should be enough.

In terminal, export the private key of your Polygon account:
```console
export TEST_PRIVATE_KEY1=<your private key>
```

In terminal, go into Python console: `python`

In Python console:
```python
import os
import requests
from pybundlr import pybundlr

eth_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')

#create test file
file_name = "/tmp/testfile.txt"
content_in = "test content" + "\n"
with open(file_name, 'a') as f:
    f.write(content_in)

#fund the node, and upload the file
url = pybundlr.fund_and_upload(file_name, "matic", eth_private_key)
print(f"Uploaded file. It's online at: {url}")

#retrieve the result
result = requests.get(url)
content_out = result.text
assert content_out == content_in
```

This example was on Polygon mainnet, with `currency = "matic"`. Pybundlr also works on Ethereum mainnet (`"ethereum"`), Arweave (`"arweave"`), and more.

## Development

- [Developers flow](developers.md) - to further develop pybundlr
- [Release process](release-process.md) - to do a new release of pybundlr
