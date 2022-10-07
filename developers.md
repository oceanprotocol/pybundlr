
## Developing pybundlr

This README is for those further improving the pybundlr library.

### Installation from source

In a new terminal:

```console
#clone the repo and enter into it
git clone https://github.com/oceanprotocol/pybundlr
cd pybundlr

#Create & activate venv
python -m venv venv
source venv/bin/activate

#Install modules in the environment
pip install -r requirements.txt
```


### Testing

From the terminal:
```console
pytest
```

### Usage

From the same terminal: `python`. Then, in Python console:
```python
from src.pybundlr import pybundlr
address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
bal = pybundlr.balance(address)
print(f"bal: {bal}")
```
