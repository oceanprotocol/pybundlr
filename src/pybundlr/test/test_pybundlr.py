import pytest

import requests

from src.pybundlr import pybundlr

def test_balance_arweave():
    address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
    bal = pybundlr.balance(address, "arweave") #not AR
    assert bal > 0

    
def test_balance_ethereum():
    address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
    bal = pybundlr.balance(address, "ethereum") #not ETH
    assert bal == 0

    
def test_balance_foo():
    address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
    with pytest.raises(ValueError) as e_info:
        pybundlr.balance(address, "foo")
    assert "Unknown/Unsupported currency foo" in str(e_info)


def test_upload(tmp_path):

    private_key = "/home/trentmc/Desktop/wallet.json" #HACK

    
    f = tmp_path / "myfile.txt"
    f.write_text("mycontent")
    url = pybundlr.upload(f.name, private_key)

    result = requests.get(url)
    import pdb; pdb.set_trace()
