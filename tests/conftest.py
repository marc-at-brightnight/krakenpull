import json
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from pydantic import TypeAdapter

from krakenpull import Currency, ClosedTransaction
from krakenpull.client import Kraken
from krakenpull.models import JSON
from krakenpull.utils import load_json
from tests import TEST_DATA_DIR


def pytest_addoption(parser):
    parser.addoption("--real", action="store", default=False)
    parser.addoption(
        "--beta",
        action="store_true",
        default=False,
        help="Update expected values",
    )


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.real
    if "real" in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("real", [option_value])


@pytest.fixture
def get_client():
    def _get_client(real_client: bool | str = False) -> Kraken:
        real = real_client if isinstance(real_client, bool) else bool(real_client)
        if real:
            from krakenpull.env import KRAKEN_API_KEY, KRAKEN_PRIVATE_KEY

            return Kraken(KRAKEN_API_KEY, KRAKEN_PRIVATE_KEY)

        transactions = load_json(TEST_DATA_DIR / "transactions1.json")
        client = Kraken("key", "private_key")
        client.get_closed_orders = MagicMock(return_value=TypeAdapter(list[ClosedTransaction]).validate_python(transactions))  # type: ignore
        client.get_account_balance = MagicMock(  # type: ignore
            return_value={
                Currency.FLR: 1062.2314,
                Currency.SGB: 1062.2666259600,
                Currency.USDT: 10474.11937100,
                Currency.XBT: 4.2375553847,
                Currency.XMR: 1.600,
            }
        )
        client.get_order_book = MagicMock(  # type: ignore
            return_value={
                "asks": [
                    ["69854.10000", "17.384", 1711832989],
                    ["69854.20000", "0.189", 1711832983],
                    ["69863.60000", "0.118", 1711832989],
                    ["69863.70000", "0.042", 1711832983],
                    ["69866.90000", "17.247", 1711832988],
                ],
                "bids": [
                    ["69854.00000", "0.015", 1711832988],
                    ["69850.00000", "0.005", 1711832881],
                    ["69844.60000", "0.001", 1711832857],
                    ["69838.00000", "0.010", 1711832884],
                    ["69836.50000", "0.003", 1711832881],
                ],
            }
        )

        return client

    return _get_client


class Beta:
    def __init__(self, update: bool):
        self._update = update

    def __call__(self, path: Path, actual: JSON) -> JSON:
        with open(path) as f:
            expected = json.load(f)
        if self._update:
            with open(path, "w") as f:
                json.dump(actual, f, indent=2, sort_keys=True)
        return expected


@pytest.fixture()
def beta(request):
    update = request.config.getoption("--beta")
    yield Beta(update)
