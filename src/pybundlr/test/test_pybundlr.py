from src.pybundlr import pybundlr

def test_balance():
    address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
    bal = pybundlr.balance(address)
    assert bal > 0
