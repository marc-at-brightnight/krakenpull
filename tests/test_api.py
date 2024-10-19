from deepdiff import DeepDiff

from krakenpull.models import ClosedTransaction, Currency, TickerInfo
from tests import TEST_DATA_DIR


def test_kraken_api(get_client, real, beta):
    client = get_client(real)
    time = client._get_server_time_unix()
    assert isinstance(time, int)

    pair_map_jsoned = {k: [x.value for x in v] for k, v in client.pair_map.items()}
    results_expected = beta(TEST_DATA_DIR / "expected_pair_map.json", pair_map_jsoned)
    assert not DeepDiff(results_expected, pair_map_jsoned)


def test_kraken_get_account_balance(get_client, real):
    client = get_client(real)
    balances = client.get_account_balance()
    print(balances)
    assert balances is not None


def test_kraken_get_order_book(get_client, real):
    client = get_client(real)
    order_book = client.get_order_book((Currency.XBT, Currency.USD))
    assert order_book is not None
    assert "asks" in order_book.keys()
    assert "bids" in order_book.keys()


def test_kraken_get_closed_orders(get_client, real):
    client = get_client(real)
    closed_orders = client.get_closed_orders(trades=True)
    assert closed_orders is not None
    assert isinstance(closed_orders[0], ClosedTransaction)


def test_kraken_get_ticker_info(get_client, real):
    client = get_client(real)
    btc_ticker_info = client.get_ticker_info((Currency.XBT, Currency.USD))

    assert isinstance(btc_ticker_info[0], TickerInfo)
    assert btc_ticker_info[0].currency_pair_id == "XBTUSD"

    usdt_ticker_info = client.get_ticker_info((Currency.USDT, Currency.USD))

    assert isinstance(usdt_ticker_info[0], TickerInfo)
    assert usdt_ticker_info[0].currency_pair_id == "USDTUSD"

    eth_ticker_info = client.get_ticker_info((Currency.ETH, Currency.USDT))

    assert isinstance(eth_ticker_info[0], TickerInfo)
    assert eth_ticker_info[0].currency_pair_id == "ETHUSDT"

    # reversed, to check if that works as well
    eth_ticker_info2 = client.get_ticker_info((Currency.USDT, Currency.ETH))

    assert isinstance(eth_ticker_info2[0], TickerInfo)
    assert eth_ticker_info2[0].currency_pair_id == "ETHUSDT"
