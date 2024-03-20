from random import randint

import pytest

from config import BASE_URL
from src.base_utils.utils import Response
from src.data_set.user_test_data import upd_user, upd_field
from src.schemas.schema import CreateUser, UpdateUser, UpdField

from src.base_utils.clients import async_client, base_client


def test_create_user(base_client):
    r = base_client.post(f'{BASE_URL}users')
    response = Response(r)
    response.assert_status_code(201).validate(CreateUser)


@pytest.mark.asyncio
async def test_update_user(async_client):
    r = await async_client.put(f'{BASE_URL}users/{randint(1, 12)}', data=upd_user)
    response = Response(r)
    response.assert_status_code(200).validate(UpdateUser)


@pytest.mark.asyncio
async def test_update_users_with_patch(async_client):
    r = await async_client.patch(f'{BASE_URL}users/{randint(1, 12)}', data=upd_field)
    response = Response(r)
    response.assert_status_code(200).validate(UpdField)
