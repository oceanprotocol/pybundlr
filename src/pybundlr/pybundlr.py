import re
import subprocess

from enforce_typing import enforce_types

NODE_URL = "https://node1.bundlr.network"

@enforce_types
def balance(address:str, currency:str) -> int:
    """
    Return balance of address.
    
    Parameters:
      address - balance of address for the given currency at bundlr node
      currency - Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)

    Returns:
      balance - amount held of the target currency, in base unit (winston, wei)
    """
    cmd = f"bundlr balance {address} -c {currency} -h {NODE_URL}"
    print(f"\nCOMMAND: {cmd}")
    args = cmd.split()
    completed_process = subprocess.run(args, capture_output=True, check=True)

    #e.g. 'Balance: 50699435393886 winston (50.699435393886 arweave)\n'
    stdout = completed_process.stdout.decode("ascii")
    stderr = completed_process.stderr.decode("ascii")

    if "error" in stderr.lower() or stdout == "":
        print(stderr)
        raise ValueError(stderr)
    
    print(stdout)
    bal_s = re.search(r'\d+', stdout).group() #grab first number
    bal = int(bal_s)
    return bal


@enforce_types
def fund(amount:int, currency:str, private_key: str) -> str:
    """
    Fund a bundlr node. 

    Parameters:
      amount - how much to fund. In base units (winston, wei, ..)
      currency - Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)
      private_key - private key, or path to json with arweave wallet
    """
    cmd = f"bundlr fund {amount} -c {currency} -h {NODE_URL} -w {private_key}"
    print(f"\nCOMMAND: {cmd}")
    import pdb; pdb.set_trace()
    args = cmd.split()
    completed_process = subprocess.run(args, capture_output=True, check=True)


@enforce_types
def upload(file_name:str, currency:str, private_key:str) -> str:
    """
    Upload file. 

    Parameters:
      file_name -- path to file
      currency -- Eg "arweave" (AR), "ethereum" (ETH), "polygon" (MATIC)
      private_key - private key, or path to json with arweave wallet

    Returns:
      url - location on arweave network where file is now stored
    """
    cmd = f"bundlr upload {filename} -c {currency} -h {NODE_URL} -w {private_key}"
    print(f"\nCOMMAND: {cmd}")
    args = cmd.split()
    completed_process = subprocess.run(args, capture_output=True, check=True)
