from typing import Optional
from enforce_typing import enforce_types
from javascript import require, eval_js
Bundlr = require('@bundlr-network/client', '0.x')
import requests

#==========================================================================
#helper methods

@enforce_types
def getBundlrNode(bundlers=['https://node1.bundlr.network', 'https://node2.bundlr.network']) -> str:
  r"""Looks for an available public bundlr, if no url is valid stops execution otherwise returns a valid url"""
  bundlr_node = None
  for url in bundlers:
      try:
          if requests.get(url).status_code == 200:
              bundlr_node = url
              break
      except:
          pass
  if bundlr_node is None:
    raise SystemExit(f'\n\n\r\rBundlr service is down.\n\rAt the moment there are no Bundlr nodes available.\n\rPlease try again later\n\n\r\r')
  else:
    return bundlr_node

@enforce_types
def init(currency_name: str, private_key: str, node=None) -> Optional[object]:
    r"""
    Instantiates a bundlr object using bundlr's SDK and the javascript module

    Parameters:
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key
      node - one of bundlr's bundlers https://docs.bundlr.network/docs/bundlers

    Returns:
      object - either the bundlr object instantiated or throws an exception
    """
    try:
        node = getBundlrNode() if node is None else getBundlrNode(bundlers=[node])
        bundlr = Bundlr.default(node, currency_name, private_key)
        return bundlr
    except Exception as e:
        if 'Unknown/Unsupported currency' in str(e):
            raise ValueError(f'\n\n\n\n\r\r\r\rPlease make sure that this currency is currently supported.\n\rList of the current supported currencies: https://docs.bundlr.network/docs/currencies\n\n\r\r')
        elif 'Expected private key to be an Uint8Array with length 32' in str(e):
            raise ValueError(f'\n\n\n\n\r\r\r\rPlease make sure that the private key is valid or that it is not an address\n\n\r\r')
        else:
            raise Exception(e)

#==========================================================================
#functions that are 1:1 with bundlr SDK

@enforce_types
def balance(address: str|None, currency_name: str, private_key: str, node=None) -> int:
    r"""
    Gets the specified address's balance. It can be any address, not necessarily the user

    Parameters:
      address - balance of the address submitted in the bundlr node
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key

    Returns:
      balance - amount held in decimal units. If the does not exist or has no balance in both cases returns 0
    """
    bundlr = init(currency_name, private_key, node)
    address = bundlr.address if address is None else address
    balance = bundlr.getBalance(address)
    balance = eval_js(''' bundlr.utils.unitConverter(balance).valueOf() ''')
    return balance


@enforce_types
def myBalance(currency_name: str, private_key: str, node=None) -> int:
    r"""
    Gets the loaded wallet's balance

    Parameters:
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key

    Returns:
      balance - user's amount held of the target currency in decimal units
    """
    return balance(address=None, currency_name=currency_name, private_key=private_key, node=node)





bal= balance(
    address='0x853758425e953739F5438fd6fd0Efe04A477b039',
    currency_name='chainlink',
    private_key='8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f',
    node='https://devnet.bundlr.network/')
print(bal)
