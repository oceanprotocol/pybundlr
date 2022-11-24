import os
import re
import subprocess

from enforce_typing import enforce_types
import web3
from web3 import Web3

BUNDLR_NODE_URL = "https://node1.bundlr.network"

#picked arbitrarily from https://chainlist.org/chain/1
ETH_NODE_URL = "https://eth-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7"
MATIC_NODE_URL = "https://polygon-rpc.com/"


#==========================================================================
#functions that are 1:1 with bundlr CLI

@enforce_types
def balance(address:str, currency:str) -> int:
    """
    Gets the specified user's balance for the current Bundlr node
    
    Parameters:
      address - balance of address for the given currency at bundlr node
      currency - Eg "arweave" (AR), "ethereum" (ETH), "matic" (MATIC)

    Returns:
      balance - amount held of the target currency, in base unit (winston, wei)
    """
    cmd = f"bundlr balance {address} -c {currency} -h {BUNDLR_NODE_URL}"
    stdout = _run_cmd(cmd)
    bal_s = re.findall(r"\d+", stdout)[0]
    bal = int(bal_s)
    return bal


@enforce_types
def fund(amount:int, currency:str, private_key: str) -> str:
    """
    Funds your account with the specified amount of atomic units

    Parameters:
      amount - how much to fund. In base units (winston, wei, ..)
      currency - Eg "arweave" (AR), "ethereum" (ETH), "matic" (MATIC)
      private_key - private key, or path to json with arweave wallet
    """
    if currency == "ethereum":
        addr = eth_address(private_key)
        b = bal_on_ethereum(addr)
        if b < amount:
            raise ValueError(f"Can't fund {amount} wei: balance is {b}")

    cmd = f"bundlr fund {amount} -c {currency} -h {BUNDLR_NODE_URL} " \
        f"-w {private_key} --no-confirmation"
    stdout = _run_cmd(cmd)


@enforce_types
def withdraw(amount:int, currency:str, private_key: str) -> str:
    """
    Sends a fund withdrawal request

    Parameters:
      amount - how much to withdraw. In base units (winston, wei, ..)
      currency - Eg "arweave" (AR), "ethereum" (ETH), "matic" (MATIC)
      private_key - private key, or path to json with arweave wallet
    """
    cmd = f"bundlr withdraw {amount} -c {currency} -h {BUNDLR_NODE_URL} " \
        f"-w {private_key} --no-confirmation"
    stdout = _run_cmd(cmd)


@enforce_types
def price(num_bytes: int, currency:str) -> int:
    """
    Check how much of a specific currency is required for an upload of num_bytes

    Parameters:
      num_bytes -- how many bytes. E.g. via os.stat(file_name).st_size
      currency -- Eg "arweave" (AR), "ethereum" (ETH), "matic" (MATIC)

    Returns:
      amt - price to upload, in base unit (winston, wei)
    """
    cmd = f"bundlr price {num_bytes} -c {currency} -h {BUNDLR_NODE_URL} "
    stdout = _run_cmd(cmd)

    #e.g. stdout = "Price for 10 bytes in ethereum is 24294303017 wei ..."
    amt_s = re.findall(r"\d+", stdout)[1]
    amt = int(amt_s)
    return amt


@enforce_types
def upload(file_name:str, currency:str, private_key:str) -> str:
    """
    Uploads a specified file

    Parameters:
      file_name -- path to file
      currency -- Eg "arweave" (AR), "ethereum" (ETH), "matic" (MATIC)
      private_key - private key, or path to json with arweave wallet

    Returns:
      url - location on arweave network where file is now stored
    """
    cmd = f"bundlr upload {file_name} -c {currency} -h {BUNDLR_NODE_URL} " \
        f"-w {private_key} --no-confirmation"
    stdout = _run_cmd(cmd)

    #e.g. "Uploaded to https://arweave.net/PJVOHDHjYrTXQJQg9UlgfKxgV2dUspc"
    url = stdout.split()[-1] 
    return url

#==========================================================================
#functions that combine >1 CLI calls

def fund_and_upload(file_name:str, currency:str, private_key:str) -> str:
    """
    Uploads a specified file. Funds first if needed.
    For "ethereum" or "matic" only, for now.

    Parameters:
      file_name -- path to file
      currency -- "ethereum" (ETH), "matic" (MATIC)
      private_key - private key, or path to json with arweave wallet

    Returns:
      url - location on arweave network where file is now stored
    """
    #we don't yet have a convenient conversion from AR private key -> addr
    assert currency in ["ethereum", "matic"], "only currently support evm"
    
    num_bytes = os.stat(file_name).st_size

    p = price(num_bytes, currency)
    
    amt_wei = p * 2 # the 2x is for safety margin, since price fluctuates

    addr = eth_address(private_key)
    bal_wei = balance(addr, currency)
    if bal_wei < amt_wei:
        fund(amt_wei, currency, private_key)

    url = upload(file_name, currency, private_key)

    return url


#==========================================================================
#helper method

def _run_cmd(cmd:str):
    cmd = _remove_0x_in_key(cmd)
    print(f"\nRUN COMMAND: {_safe_print(cmd)}")
    args = cmd.split(" ")

    # only spawn an intermediate shell process if needed (eg in Windows)
    try:
        shell = False
        completed_process = subprocess.run(args, capture_output=True, check=True, shell=shell)
    except (subprocess.CalledProcessError, FileNotFoundError):
        shell = True
        completed_process = subprocess.run(args, capture_output=True, check=True, shell=shell)
    except Exception as e:
        raise Exception(e)    

    stdout = completed_process.stdout.decode("ascii")
    stderr = completed_process.stderr.decode("ascii")

    if "error" in stderr.lower() or stdout == "":
        print(stderr)
        raise ValueError(stderr)
    
    print(stdout)
    return stdout

def _remove_0x_in_key(cmd):
    """For EVM private keys, ensure they don't have '0x' in front"""
    args = cmd.split(" ")
    for i, arg in enumerate(args):
        if arg == "-c" and args[i+1] not in ["matic", "ethereum"]:
            break
        if arg == "-w" and args[i+1][:2] == "0x":
            args[i+1] = args[i+1][2:]
            break
    return " ".join(args)

def _safe_print(cmd: str) -> str:
    """Avoid dangerous logging. E.g. don't show whole private key"""
    args = cmd.split(" ")
    for i, arg in enumerate(args):
        if arg == "-w":
            args[i+1] = args[i+1][:6] + "..." #truncate private key
    return " ".join(args)
    

#==========================================================================
#eth convenience functions

def eth_address(eth_private_key:str) -> str:
    account = web3.eth.Account.from_key(eth_private_key)
    return account.address


def bal_on_ethereum(eth_address:str) -> int:
    """
    Returns ether balance on Ethereum mainnet
    
    Parameters:
      eth_address - address on eth mainnet

    Returns:
      bal - ether balance, denominated in wei
    """
    return _w3_ethereum().eth.get_balance(eth_address)


def bal_on_matic(eth_address:str) -> int:
    """
    Returns ether balance on Matic
    
    Parameters:
      eth_address - address on eth mainnet

    Returns:
      bal - ether balance, denominated in wei
    """
    return _w3_matic().eth.get_balance(eth_address)

def _w3_ethereum():
    """Returns - web3 object pointed to Ethereum mainnet"""
    return Web3(Web3.HTTPProvider(ETH_NODE_URL))

def _w3_matic():
    """Returns - web3 object pointed to Matic (Polygon) mainnet """
    return Web3(Web3.HTTPProvider(MATIC_NODE_URL)) 


