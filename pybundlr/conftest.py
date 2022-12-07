import pytest

def pytest_configure():

    pytest.bundlr_test_node = 'https://devnet.bundlr.network'

    # NOT ERC20=============================================================

    pytest.no_erc20_arweave_bundlr_address = '93mQRQG7zpvKQj3sUaDlNu_dOWFmb3-vp2Myu8sw03I'
    pytest.no_erc20_arweave_currency_name = 'arweave'
    pytest.no_erc20_arweave_private_key = '8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f'
    pytest.no_erc20_arweave_provider_url = ''
    pytest.no_erc20_arweave_contract_address = 'OXcT1sVRSA5eGwt2k6Yuz8-3e3g9WJi5uSE99CWqsBs'

    pytest.no_erc20_solana_bundlr_address = '4a7s9iC5NwfUtf8fXpKWxYXcekfqiN6mRqipYXMtcrUS'
    pytest.no_erc20_solana_currency_name = 'solana'
    pytest.no_erc20_solana_private_key = ''
    pytest.no_erc20_solana_provider_url = ''
    pytest.no_erc20_solana_contract_address = 'https://rpc.ankr.com/solana_devnet'

    pytest.no_erc20_algorand_bundlr_address = 'LUWF7XYHEHWVRZTDMEGXV3YJVVD6T3XQPIGQOFMU5QEOO6YM2VBOO6MNB4'
    pytest.no_erc20_algorand_currency_name = 'algorand'
    pytest.no_erc20_algorand_private_key = ''
    pytest.no_erc20_algorand_provider_url = ''
    pytest.no_erc20_algorand_contract_address = ''

    pytest.no_erc20_aptos_bundlr_address = '0xfa3e389d045e057145e29f544f9809c28399f8167e0e45fd157084858dda8a0f'
    pytest.no_erc20_aptos_currency_name = 'aptos'
    pytest.no_erc20_aptos_private_key = ''
    pytest.no_erc20_aptos_provider_url = 'https://rpc.ankr.com/http/aptos_testnet/v1'
    pytest.no_erc20_aptos_contract_address = ''


    # ERC20 =============================================================

    pytest.erc20_bundlr_address = '0x853758425e953739F5438fd6fd0Efe04A477b039'
    pytest.erc20_private_key = '8da4ef21b864d2cc526dbdb2a120bd2874c36c9d0a1fb7f8c63d7f7a8b41de8f'

    pytest.erc20_ethereum_currency_name = 'ethereum'
    pytest.erc20_ethereum_private_key = pytest.erc20_private_key
    pytest.erc20_ethereum_provider_url = 'https://rpc.ankr.com/eth_goerli'
    pytest.erc20_ethereum_contract_address = '0xFfb99f4A02712C909d8F7cC44e67C87Ea1E71E83'

    pytest.erc20_matic_currency_name = 'matic'
    pytest.erc20_matic_private_key = pytest.erc20_private_key
    pytest.erc20_matic_provider_url = 'https://rpc.ankr.com/polygon_mumbai'
    pytest.erc20_matic_contract_address = '0x8A6bE4f8ca7B3B5aA1935b0C5de1801fDe1134d9'

    pytest.erc20_chainlink_currency_name = 'chainlink'
    pytest.erc20_chainlink_private_key = pytest.erc20_private_key
    pytest.erc20_chainlink_provider_url = 'https://rpc.ankr.com/eth_goerli'
    pytest.erc20_chainlink_contract_address = '0x326C977E6efc84E512bB9C30f76E30c160eD06FB'

    pytest.erc20_bnb_currency_name = 'bnb'
    pytest.erc20_bnb_private_key = pytest.erc20_private_key
    pytest.erc20_bnb_provider_url = 'https://rpc.ankr.com/bsc_testnet_chapel'
    pytest.erc20_bnb_contract_address = '0xfb501A48aFFC39aa4b4C83A025D4F0b5C1ca4A6C'

    pytest.erc20_avalanche_currency_name = 'avalanche'
    pytest.erc20_avalanche_private_key = pytest.erc20_private_key
    pytest.erc20_avalanche_provider_url = 'https://rpc.ankr.com/avalanche_fuji'
    pytest.erc20_avalanche_contract_address = '0xFE56426A24424c314273B04E136944492E700f2b'

    pytest.erc20_arbitrum_currency_name = 'arbitrum'
    pytest.erc20_arbitrum_private_key = pytest.erc20_private_key
    pytest.erc20_arbitrum_provider_url = 'https://rpc.ankr.com/arbitrum' # no testnet or mainnet == testnet
    pytest.erc20_arbitrum_contract_address = '0xaDbDafC36B381f820b220255F81319Bc6910749D'

    pytest.erc20_fantom_currency_name = 'fantom'
    pytest.erc20_fantom_private_key = pytest.erc20_private_key
    pytest.erc20_fantom_provider_url = 'https://rpc.ankr.com/fantom_testnet'
    pytest.erc20_fantom_contract_address = '0xB5447C44a3462043Fb908C26eAb9b13464896d1b'
