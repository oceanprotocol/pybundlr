import pytest
from pybundlr import my_balance

class TestBalance:

    def test_my_balance_for_ethereum(self):
        bal = my_balance(
            currency_name = pytest.erc20_ethereum_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_my_balance_for_matic(self):
        bal = my_balance(
            currency_name = pytest.erc20_matic_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_my_balance_for_bnb(self):
        bal = my_balance(
            currency_name = pytest.erc20_bnb_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_my_balance_for_avalanche(self):
        bal = my_balance(
            currency_name = pytest.erc20_avalanche_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_my_balance_for_arbitrum(self):
        bal = my_balance(
            currency_name = pytest.erc20_arbitrum_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_my_balance_for_chainlink(self):
        bal = my_balance(
            currency_name = pytest.erc20_chainlink_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_my_balance_for_fantom(self):
        bal = my_balance(
            currency_name = pytest.erc20_fantom_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)
