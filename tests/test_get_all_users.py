import random

import pytest

from src.base_utils.clients import async_client
from src.base_utils.utils import Response
from config import BASE_URL
from src.schemas.schema import ListUsers, TypicalUser


@pytest.mark.asyncio
async def test_get_all_users(async_client):
    r = await async_client.get(f'{BASE_URL}users')
    response = Response(r)
    response.assert_status_code(200).validate(ListUsers)


@pytest.mark.asyncio
async def test_get_user_by_id(async_client):
    r = await async_client.get(f'{BASE_URL}users/{random.randint(1, 12)}')
    response = Response(r)
    response.assert_status_code(200).validate(TypicalUser)
