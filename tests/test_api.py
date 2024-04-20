from krakenpull.models import ClosedTransaction, Currency, TickerInfo


def test_kraken_api(get_client, real):
    client = get_client(real)
    time = client._get_server_time_unix()
    assert isinstance(time, int)


def test_kraken_get_account_balance(get_client, real):
    client = get_client(real)
    balances = client.get_account_balance()
    assert balances is not None


def test_kraken_get_order_book(get_client, real):
    client = get_client(real)
    order_book = client.get_order_book((Currency.BTC, Currency.USD))
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
    btc_ticker_info = client.get_ticker_info((Currency.BTC, Currency.USD))

    assert isinstance(btc_ticker_info[0], TickerInfo)
    assert btc_ticker_info[0].currency_pair_id == "XBTZUSD"

    usdt_ticker_info = client.get_ticker_info((Currency.USDT, Currency.USD))

    assert isinstance(usdt_ticker_info[0], TickerInfo)
    assert usdt_ticker_info[0].currency_pair_id == "USDTUSD"
