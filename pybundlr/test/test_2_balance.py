import pytest
from pybundlr import balance

class TestBalance:

    def test_balance_for_ethereum(self):
        bal = balance(
            address = pytest.erc20_ethereum_contract_address,
            currency_name = pytest.erc20_ethereum_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_balance_for_matic(self):
        bal = balance(
            address= pytest.erc20_matic_contract_address,
            currency_name = pytest.erc20_matic_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_balance_for_bnb(self):
        bal = balance(
            address= pytest.erc20_bnb_contract_address,
            currency_name = pytest.erc20_bnb_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_balance_for_avalanche(self):
        bal = balance(
            address= pytest.erc20_avalanche_contract_address,
            currency_name = pytest.erc20_avalanche_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_balance_for_arbitrum(self):
        bal = balance(
            address= pytest.erc20_arbitrum_contract_address,
            currency_name = pytest.erc20_arbitrum_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_balance_for_chainlink(self):
        bal = balance(
            address= pytest.erc20_chainlink_contract_address,
            currency_name = pytest.erc20_chainlink_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)

    def test_balance_for_fantom(self):
        bal = balance(
            address= pytest.erc20_fantom_contract_address,
            currency_name = pytest.erc20_fantom_currency_name,
            private_key = pytest.erc20_private_key,
            )
        assert isinstance(float(bal), float)
