# This module wraps bundlr CLI, which in turn wraps Arweave.
# https://docs.bundlr.network/docs/client/cli

import re
import subprocess

def balance(self, address) -> int:
    """Return balance of address, denominated in winston (arweave base unit)"""
    cmd = f"bundlr balance {address} -h https://node1.bundlr.network -c arweave"
    args = cmd.split()
    completed_process = subprocess.run(args, capture_output=True, check=True)

    #e.g. 'Balance: 50699435393886 winston (50.699435393886 arweave)\n'
    output_s = completed_process.stdout.decode("ascii")

    bal_s = re.search(r'\d+', output_s).group() #grab first number
    bal = int(bal_s)
    return bal
    

@enforce_types
def upload(self, file_name: str, from_wallet: Wallet) -> str:
    """Upload file. Returns url."""
    return "wip"

    # cmd = "bundlr upload image.png -h https://node1.bundlr.network -w wallet.json -c arweave"
    # args = cmd.split()
    # completed_process = subprocess.run(args, capture_output=True, check=True)
