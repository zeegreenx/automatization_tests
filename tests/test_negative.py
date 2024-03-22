import pytest

from src.base_utils.clients import async_client
from src.base_utils.utils import DelResponse, Response
from src.schemas.schema import first_page, empty_page
from config import BASE_URL



@pytest.mark.asyncio
async def test_negative_page_value(async_client):
    r = await async_client.get(f'{BASE_URL}users', params={'page': 200})
    response = Response(r)
    response.assert_status_code(200).validate(empty_page)

@pytest.mark.asyncio
async def test_list_users_with_empty_page_param(async_client):
    r = await async_client.get(f'{BASE_URL}users', params={'page': ''})
    response = Response(r)
    response.assert_status_code(200)

@pytest.mark.asyncio
async def test_non_numeric_page_value(async_client):
    r = await async_client.get(f'{BASE_URL}users', params={'page': 'abc'})
    response = Response(r)
    response.assert_status_code(200).validate(first_page)


@pytest.mark.asyncio
async def test_get_user_with_non_numeric_id(async_client):
    r = await async_client.get(f'{BASE_URL}users/abc')
    response = DelResponse(r)
    response.assert_status_code(404)


@pytest.mark.asyncio
async def test_request_with_excessive_delay(async_client):
    delay_time = 100000
    r = await async_client.get(f'{BASE_URL}users', params={'delay': delay_time})
    response = Response(r)
    response.assert_status_code(200).validate(first_page)

