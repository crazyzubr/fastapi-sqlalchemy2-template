import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
class TestApiSome:

    URL_PATH = '/api/v1/somes'

    async def test_get_somes_empty(self, async_client: AsyncClient):
        response = await async_client.get(url=self.URL_PATH)
        assert response.status_code == 200
        result = response.json()
        assert result == []

    async def test_get_somes(self, async_client: AsyncClient, some_factory):
        await some_factory()
        response = await async_client.get(url=self.URL_PATH)
        assert response.status_code == 200
        result = response.json()
        assert isinstance(result, list)
        assert len(result) == 1
