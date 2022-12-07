from typing import Optional
from enforce_typing import enforce_types
from javascript import require, eval_js
Bundlr = require('@bundlr-network/client', '0.x')
import requests

#==========================================================================
#helper methods

@enforce_types
def get_bundlr_node(bundlers=['https://node1.bundlr.network', 'https://node2.bundlr.network']) -> str:
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
def init(currency_name: str, private_key: str, is_a_test=None) -> Optional[object]:
    r"""
    Instantiates a bundlr object using bundlr's SDK and the javascript module

    Parameters:
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key
      is_a_test - if it is a test contains a dict, default=None

    Returns:
      object - either the bundlr object instantiated or throws an exception
    """
    try:
        if is_a_test:
            test_params = {key: value for (key, value) in is_a_test.items()}
            bundlr = Bundlr.default(test_params['testNode'], currency_name, private_key, test_params)
        else:
            bundlr = Bundlr.default(get_bundlr_node(), currency_name, private_key)
        return bundlr
    except Exception as e:
        if 'Unknown/Unsupported currency' in str(e):
            raise ValueError(f'\n\n\n\n\r\r\r\rPlease make sure that this currency is currently supported.\n\rList of the current supported currencies: https://docs.bundlr.network/docs/currencies\n\n\r\r')
        elif 'Expected private key to be an Uint8Array with length 32' in str(e):
            raise ValueError(f'\n\n\n\n\r\r\r\rPlease make sure that the private key is valid or that it is not an address\n\n\r\r')
        else:
            raise Exception(e)


#==========================================================================
#functions

@enforce_types
def balance(address: str|None, currency_name: str, private_key: str) -> float:
    r"""
    Gets the specified address's balance. It can be any address, not necessarily the user

    Parameters:
      address - address from which balance will be fetched, can be different than private key but must be same chain
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key

    Returns:
      balance - amount held in decimal units. If the does not exist or has no balance in both cases returns 0
    """
    bundlr = init(currency_name, private_key)
    address = bundlr.address if address is None else address
    balance = bundlr.getBalance(address)
    balance = eval_js(''' bundlr.utils.unitConverter(balance).valueOf() ''')
    return balance


@enforce_types
def my_balance(currency_name: str, private_key: str) -> float:
    r"""
    Gets the loaded wallet's balance

    Parameters:
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key

    Returns:
      balance - user's amount held of the target currency in decimal units
    """
    return balance(address=None, currency_name=currency_name, private_key=private_key)


@enforce_types
def fund_bundlr_node(amount: int, currency_name: str, private_key: str):
    r"""
    Adds funds to the bundlr node

    Parameters:
      amount - in atomic units
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key

    Returns:
      balance - user's amount held of the target currency in decimal units
    """
    bundlr = init(currency_name, private_key)
    send_funds = bundlr.fund(amount)
    return send_funds


@enforce_types
def get_price_for_uploading_this_file(file_name: str, currency_name: str, private_key: str) -> float:
    r"""
    Returns the price in decimal units that will cost to upload this file

    Parameters:
      file - a string with the fully qualified filename
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key

    Returns:
      string - amount in atomic units that would cost to upload this number of bytes at this moment
    """
    bundlr = init(currency_name, private_key)
    size = bundlr.createTransaction(file_name).size
    total_cost_atomic = bundlr.getPrice(size)
    total_cost = eval_js(''' bundlr.utils.unitConverter(total_cost_atomic).valueOf() ''')
    return total_cost


@enforce_types
def upload_data(file_name: str, currency_name: str, private_key: str):
    r"""
    Uploads data to Arweave

    Parameters:
      file - a string with the fully qualified filename
      currency_name - name of one of Bundlr's supported currencies
      private_key - user's private key

    Returns:
      string|Exception - a string with the success message or an exception explaining the error
    """
    balance = my_balance(currency_name=currency_name, private_key=private_key)
    price_to_upload = get_price_for_uploading_this_file(file_name=file_name, currency_name=currency_name, private_key=private_key)

    if balance > price_to_upload:
        try:
            bundlr = init(currency_name, private_key)
            tx = bundlr.createTransaction(file_name)
            tx_signed = eval_js(''' tx.sign() ''')
            tx_id = tx_signed['id']
            result = eval_js(''' tx.upload() ''')
            if result:
              return f'\n\rData successfully uploaded!\n\rIt will be instantly accessible at https://arweave.net/${tx_id}\n\r'
        except Exception as e:
            print(str(e))
    else:
      return f'\n\n\n\n\r\r\r\rNot enough funds. Please use the --fund_bundlr_node-- function to fund your node.\n\n\r\rIf you want to know how much it would cost to upload your file use the --get_price_for_uploading_this_file-- function\n\n\r\r'
