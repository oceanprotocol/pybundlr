import re
import subprocess

from enforce_typing import enforce_types
import web3

BUNDLR_NODE_URL = "https://node1.bundlr.network"

#picked arbitrarily from https://chainlist.org/chain/1
ETH_NODE_URL = "https://eth-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7"

@enforce_types
def balance(address:str, currency:str) -> int:
    """
    Gets the specified user's balance for the current Bundlr node
    
    Parameters:
      address - balance of address for the given currency at bundlr node
      currency - Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)

    Returns:
      balance - amount held of the target currency, in base unit (winston, wei)
    """
    cmd = f"bundlr balance {address} -c {currency} -h {BUNDLR_NODE_URL}"
    stdout = _run_cmd(cmd)
    bal_s = re.findall("\d+", stdout)[0]
    bal = int(bal_s)
    return bal


@enforce_types
def fund(amount:int, currency:str, private_key: str) -> str:
    """
    Funds your account with the specified amount of atomic units

    Parameters:
      amount - how much to fund. In base units (winston, wei, ..)
      currency - Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)
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
      currency - Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)
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
      currency -- Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)

    Returns:
      amt - price to upload, in base unit (winston, wei)
    """
    cmd = f"bundlr price {num_bytes} -c {currency} -h {BUNDLR_NODE_URL} "
    stdout = _run_cmd(cmd)

    #e.g. stdout = "Price for 10 bytes in ethereum is 24294303017 wei ..."
    amt_s = re.findall("\d+", stdout)[1]
    amt = int(amt_s)
    return amt


@enforce_types
def upload(file_name:str, currency:str, private_key:str) -> str:
    """
    Uploads a specified file

    Parameters:
      file_name -- path to file
      currency -- Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)
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
#helper method

def _run_cmd(cmd:str):
    print(f"\nRUN COMMAND: {cmd}")
    args = cmd.split()
    completed_process = subprocess.run(args, capture_output=True, check=True)

    stdout = completed_process.stdout.decode("ascii")
    stderr = completed_process.stderr.decode("ascii")

    if "error" in stderr.lower() or stdout == "":
        print(stderr)
        raise ValueError(stderr)
    
    print(stdout)
    return stdout


#==========================================================================
#eth convenience functions

def eth_address(eth_private_key:str) -> str:
    account = web3.eth.Account.privateKeyToAccount(eth_private_key)
    #FIXME: 'DeprecationWarning: privateKeyToAccount is deprecated in favor of from_key'
    return account.address


def bal_on_ethereum(eth_address:str) -> int:
    """
    Returns ether balance on Ethereum mainnet
    
    Parameters:
      eth_address - address on eth mainnet

    Returns:
      bal - ether balance, denominated in wei
    """
    bal = w3().eth.get_balance(eth_address)
    return bal

def w3():
    """Return Web3 instance"""
    Web3 = web3.Web3
    return Web3(Web3.HTTPProvider(ETH_NODE_URL))


def usd_to_wei(amt_usd, eth_price_in_usd) -> int:
    """Convert USD to wei"""
    amt_eth = amt_usd / eth_price_in_usd
    amt_wei = pybundlr.w3().toWei(amt_eth, "ether")
    return amt_wei


def wei_to_usd(amt_wei:int, eth_price_in_usd) -> float:
    """Convert wei to usd"""
    amt_eth = pybundlr.w3().fromWei(amt_wei, "ether")
    amt_usd = amt_eth * eth_price_in_usd
    return amt_usd
