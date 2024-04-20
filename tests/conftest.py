import pytest

from krakenpull.client import get_kraken_client, AbstractKraken
from krakenpull.models import ClosedTransaction
from krakenpull.utils import load_json
from tests import TEST_DATA_DIR


def pytest_addoption(parser):
    parser.addoption("--real", action="store", default=False)


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.real
    if "real" in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("real", [option_value])


@pytest.fixture
def get_client():
    def _get_client(real_client: bool | str = False) -> AbstractKraken:
        real = real_client if isinstance(real_client, bool) else bool(real_client)
        if real:
            from krakenpull.env import KRAKEN_API_KEY, KRAKEN_PRIVATE_KEY

            return get_kraken_client(
                KRAKEN_API_KEY,
                KRAKEN_PRIVATE_KEY,
                emulator=False,
            )

        transactions = load_json(TEST_DATA_DIR / "transactions1.json")
        return get_kraken_client(
            None,
            None,
            emulator=True,
            transactions=[ClosedTransaction.model_validate(t) for t in transactions],
        )

    return _get_client
