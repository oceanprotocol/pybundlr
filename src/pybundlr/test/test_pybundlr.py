import requests

from src.pybundlr import pybundlr

def test_balance_arweave():
    address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
    bal = pybundlr.balance(address, "arweave") #not AR
    assert bal > 0

    
def test_balance_ethereum():
    address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
    bal = pybundlr.balance(address, "ethereum") #not ETH
    assert bal >= 0


def test_upload(tmp_path):
    f = tmp_path / "myfile.txt"
    f.write_text("mycontent")
    url = pybundlr.upload(f.name, private_key)

    result = requests.get(url)
    import pdb; pdb.set_trace()
