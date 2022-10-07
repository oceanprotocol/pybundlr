from ocean_lib import bundlr

def test_balance():
    address = "Ry2bDGfBIvYtvDPYnf0eg_ijH4A1EDKaaEEecyjbUQ4"
    bal = bundlr.balance(address)
    assert address > 0
