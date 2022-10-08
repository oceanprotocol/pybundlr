import re
import subprocess

from enforce_typing import enforce_types

@enforce_types
def balance(address:str, currency:str = "arweave") -> int:
    """Return balance of address, denominated in base unit (winston, wei, ..)"""
    url = "https://node1.bundlr.network"
    cmd = f"bundlr balance {address} -h {url} -c {currency}"
    print(f"\nCOMMAND: {cmd}")
    args = cmd.split()
    completed_process = subprocess.run(args, capture_output=True, check=True)

    #e.g. 'Balance: 50699435393886 winston (50.699435393886 arweave)\n'
    output_s = completed_process.stdout.decode("ascii")

    bal_s = re.search(r'\d+', output_s).group() #grab first number
    bal = int(bal_s)
    return bal

@enforce_types
def upload(file_name: str, private_key: str) -> str:
    """Upload file. Returns url."""
    private_key = "/home/trentmc/Desktop/wallet.json" #HACK
    cmd = f"bundlr upload {filename} -h https://node1.bundlr.network -w {private_key} -c arweave"
    print(f"\nCOMMAND: {cmd}")
    args = cmd.split()
    completed_process = subprocess.run(args, capture_output=True, check=True)
