import pytest
from pybundlr import get_bundlr_node, init


class Test_Get_Bundlr_Node:

    def test_get_bundlr_node_returns_str_on_valid_node(self):
        valid_node = ['https://ubuntu.com/']
        assert isinstance(get_bundlr_node(valid_node), str)

    def test_get_bundlr_node_exits_if_there_are_no_valid_nodes(self):
        invalid_node = ['https://gsdfanExampleofstdoesnotwork.sdsdf/']
        with pytest.raises(SystemExit):
            get_bundlr_node(invalid_node)


class Test_Init:

    def test_init_returns_class_when_valid_paremeters_submitted(self):
        result = init(
            currency_name = pytest.erc20_matic_currency_name,
            private_key = pytest.erc20_matic_private_key,
        )
        assert isinstance(result, object)
        assert result['uploader']['currencyConfig']['wallet'] == pytest.erc20_matic_private_key

    def test_init_returns_exception_if_currency_name_is_not_supported(self):
        with pytest.raises(Exception):
            init(
            currency_name = 'maAAtic',
            private_key = pytest.erc20_matic_private_key)

    def test_init_returns_exception_if_private_key_is_incorrect(self):
        with pytest.raises(Exception):
            init(
            currency_name = pytest.erc20_matic_currency_name,
            private_key='--a4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f')

    def test_init_returns_class_when_valid_paremeters_submitted_and_it_is_a_test_for_ERC20_token(self):
        result = init(
            currency_name = pytest.erc20_chainlink_currency_name,
            private_key = pytest.erc20_chainlink_private_key,
            is_a_test = {
                'testNode': pytest.bundlr_test_node,
                'providerUrl': pytest.erc20_chainlink_provider_url,
                'contractAddress': pytest.erc20_chainlink_contract_address
            })
        assert isinstance(result, object)
        assert result['uploader']['currencyConfig']['name'] == pytest.erc20_chainlink_currency_name
        assert result['uploader']['currencyConfig']['providerUrl'] == pytest.erc20_chainlink_provider_url
        assert result['uploader']['currencyConfig']['contractAddress'] == pytest.erc20_chainlink_contract_address

    def test_init_returns_class_when_valid_paremeters_submitted_and_it_is_a_test_for_Arweave_token(self):
        result = init(
            currency_name = pytest.no_erc20_arweave_currency_name,
            private_key = pytest.no_erc20_arweave_private_key,
            is_a_test = {
                'testNode': pytest.bundlr_test_node,
                # 'providerUrl': pytest.erc20_chainlink_provider_url,
                'contractAddress': pytest.no_erc20_arweave_contract_address
            })
        assert isinstance(result, object)
        assert result['uploader']['currencyConfig']['name'] == pytest.no_erc20_arweave_currency_name
        # assert result['uploader']['currencyConfig']['providerUrl'] == pytest.erc20_chainlink_provider_url
        assert result['uploader']['currencyConfig']['contractAddress'] == pytest.no_erc20_arweave_contract_address
