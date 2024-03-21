from random import randint

from httpx import AsyncClient
from asyncio import get_event_loop
import pytest

from src.base_utils.clients import async_client
from src.base_utils.utils import Response, DelResponse, DelayedResponse
from config import BASE_URL
from src.schemas.schema import ListUsers, TypicalUser


@pytest.mark.asyncio
async def test_get_all_users(async_client):
    r = await async_client.get(f'{BASE_URL}users', params={'page': f'{randint(1, 2)}'})
    response = Response(r)
    response.assert_status_code(200).validate(ListUsers)


@pytest.mark.asyncio
async def test_get_user_by_id(async_client):
    r = await async_client.get(f'{BASE_URL}users/{randint(1, 12)}')
    response = Response(r)
    response.assert_status_code(200).validate(TypicalUser)


@pytest.mark.asyncio
async def test_users_delete(async_client):
    r = await async_client.delete(f'{BASE_URL}users/{randint(1, 12)}')
    response = DelResponse(r)
    response.assert_status_code(204)


@pytest.mark.asyncio
async def test_get_delayed_users():
    async with AsyncClient() as client:
        delay_time = randint(1, 4)
        start_time = get_event_loop().time()
        r = await client.get(f'{BASE_URL}users', params=[('page', f'{randint(1, 2)}'), ('delay', f'{delay_time}')])
        end_time = get_event_loop().time()
        elapsed_time = end_time - 100
        response = DelayedResponse(r, received_delay=elapsed_time, expected_delay= delay_time)

        response.assert_status_code(200).assert_compare_delay()

