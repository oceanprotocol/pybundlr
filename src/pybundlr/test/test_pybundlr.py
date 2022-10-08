import os
import pytest

import requests
import web3

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

    
def test_fund_happy():
    eth_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')
    amt_wei = 3
    pybundlr.fund(amt_wei, "ethereum", eth_private_key)


def test_fund_fail_no_eth():
    #randomly create a new account, which therefore has 0 eth
    w3 = web3.Web3()
    acct = w3.eth.account.create()
    eth_private_key = acct.key.hex()

    #watch it fail
    amt_wei = 3
    with pytest.raises(ValueError) as e_info:
        pybundlr.fund(amt_wei, "ethereum", eth_private_key)
        
    assert "Can't fund" in str(e_info)
    assert "balance is 0" in str(e_info)


def test_price(tmp_path):
    num_bytes = 10
    amt_wei = pybundlr.price(num_bytes, "ethereum")
    assert amt_wei > 100000000  # example observed number: 24275774772


def test_upload(tmp_path):
    content_in = "mycontent"
    f = tmp_path / "myfile.txt"
    f.write_text(content_in)
    file_name = str(f)

    num_bytes = os.stat(file_name).st_size

    eth_private_key = os.getenv('REMOTE_TEST_PRIVATE_KEY1')
    p = pybundlr.price(num_bytes, "ethereum")
    
    amt_wei = p * 2 # the 2x is for safety margin, since price fluctuates
    pybundlr.fund(amt_wei, "ethereum", eth_private_key)
    
    url = pybundlr.upload(file_name, "ethereum", eth_private_key)
    assert "https://arweave.net/" in url, url

    result = requests.get(url)
    content_out = result.text

    assert content_in == content_out, content_out

