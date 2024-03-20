import httpx
import pytest


@pytest.fixture
async def async_client():
    async with httpx.AsyncClient() as client:
        yield client


@pytest.fixture
def base_client():
    with httpx.Client() as client:
        yield client
