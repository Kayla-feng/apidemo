import pytest

from pages.GetToken import GetToken


@pytest.fixture(scope='session')
def token():
    return GetToken.token()
