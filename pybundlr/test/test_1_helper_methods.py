import pytest
from pybundlr import getBundlrNode, init


class TestGetBundlrNode:

    def test_getBundlrNode_returns_str_on_valid_node(self):
        valid_node = ['https://ubuntu.com/']
        assert isinstance(getBundlrNode(valid_node), str)

    def test_getBundlrNode_exits_if_there_are_no_valid_nodes(self):
        invalid_node = ['https://gsdfanExampleofstdoesnotwork.sdsdf/']
        with pytest.raises(SystemExit):
            getBundlrNode(invalid_node)


class TestInit:

    def test_init_returns_class_when_valid_paremeters_submitted(self):
        result = init(
            currency_name='matic',
            private_key='8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f')
        assert isinstance(result, object)

    def test_init_returns_class_when_valid_paremeters_submitted_but_node_is_wrong(self):
        invalid_node = ['https://exampleofstdoesnotwork.sdsdf/']
        with pytest.raises(SystemExit):
            init(
            currency_name='matic',
            private_key='8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f',
            node=invalid_node)

    def test_init_returns_exception_if_currency_name_is_not_supported(self):
        with pytest.raises(Exception):
            init(
            currency_name='maAAtic',
            private_key='8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f')

    def test_init_returns_exception_if_private_key_is_incorrect(self):
        with pytest.raises(Exception):
            init(
            currency_name='matic',
            private_key='--a4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f')