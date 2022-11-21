import pytest
from pybundlr import balance, myBalance


@pytest.fixture
def get_test_node():
    return 'https://devnet.bundlr.network'

@pytest.fixture
def ERC20_wallet():
    return '0x853758425e953739F5438fd6fd0Efe04A477b039'

@pytest.fixture
def ERC20_private_key():
    return '8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f'

class TestBalance:

    #.------------------arveaveTODO: # "arweave":"93mQRQG7zpvKQj3sUaDlNu_dOWFmb3-vp2Myu8sw03I",

    def test_balance_for_ethereum(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'ethereum',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_matic(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'matic',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_bnb(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'bnb',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_avalanche(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'avalanche',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    #TODO: solana    "solana":"4a7s9iC5NwfUtf8fXpKWxYXcekfqiN6mRqipYXMtcrUS",

    def test_balance_for_arbitrum(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'arbitrum',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_boba_eth(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'boba-eth',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_boba(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'boba',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_chainlink(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'chainlink',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_kyve(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'kyve',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    def test_balance_for_fantom(self, ERC20_wallet, ERC20_private_key, get_test_node):
        bal = balance(
            address= ERC20_wallet,
            currency_name = 'fantom',
            private_key = ERC20_private_key,
            node = get_test_node,
            )
        assert isinstance(int(bal), int)

    #TODO: "algorand":"LUWF7XYHEHWVRZTDMEGXV3YJVVD6T3XQPIGQOFMU5QEOO6YM2VBOO6MNB4","aptos":"0xfa3e389d045e057145e29f544f9809c28399f8167e0e45fd157084858dda8a0f"

