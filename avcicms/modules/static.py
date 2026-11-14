from __future__ import annotations

from typing import TYPE_CHECKING, Any

from avcicms.models import CityModel, DistrictModel, NeighborhoodModel, TaxOfficeModel

if TYPE_CHECKING:
    from avcicms.client import AsyncAvciCMS, AvciCMS


class StaticModule:
    """Static Geographic and Tax Administration operations (synchronous)."""

    def __init__(self, client: AvciCMS) -> None:
        self._client = client

    def get_cities(self) -> list[CityModel]:
        """List 81 provinces in Turkey."""
        res = self._client._http.get('/v1/static/cities')
        data = res.get('data') or []
        return [CityModel.model_validate(item) for item in data]

    def get_districts(self, city_id: str) -> list[DistrictModel]:
        """List districts belonging to the specified province."""
        res = self._client._http.get(f'/v1/static/districts/{city_id}')
        data = res.get('data') or []
        return [DistrictModel.model_validate(item) for item in data]

    def get_neighborhoods(self, district_id: str) -> list[NeighborhoodModel]:
        """List neighborhoods belonging to the specified district."""
        res = self._client._http.get(f'/v1/static/neighborhoods/{district_id}')
        data = res.get('data') or []
        return [NeighborhoodModel.model_validate(item) for item in data]

    def get_tax_offices(self, city_id: str, district: str | None = None) -> list[TaxOfficeModel]:
        """List tax offices for the given province/plate code with optional district filter."""
        params: dict[str, Any] = {}
        if district:
            params['district'] = district
        res = self._client._http.get(f'/v1/static/tax-administration/{city_id}', params=params)
        data = res.get('data') or []
        return [TaxOfficeModel.model_validate(item) for item in data]


class AsyncStaticModule:
    """Static Geographic and Tax Administration operations (asynchronous)."""

    def __init__(self, client: AsyncAvciCMS) -> None:
        self._client = client

    async def get_cities(self) -> list[CityModel]:
        """List 81 provinces in Turkey."""
        res = await self._client._http.get('/v1/static/cities')
        data = res.get('data') or []
        return [CityModel.model_validate(item) for item in data]

    async def get_districts(self, city_id: str) -> list[DistrictModel]:
        """List districts belonging to the specified province."""
        res = await self._client._http.get(f'/v1/static/districts/{city_id}')
        data = res.get('data') or []
        return [DistrictModel.model_validate(item) for item in data]

    async def get_neighborhoods(self, district_id: str) -> list[NeighborhoodModel]:
        """List neighborhoods belonging to the specified district."""
        res = await self._client._http.get(f'/v1/static/neighborhoods/{district_id}')
        data = res.get('data') or []
        return [NeighborhoodModel.model_validate(item) for item in data]

    async def get_tax_offices(self, city_id: str, district: str | None = None) -> list[TaxOfficeModel]:
        """List tax offices for the given province/plate code with optional district filter."""
        params: dict[str, Any] = {}
        if district:
            params['district'] = district
        res = await self._client._http.get(f'/v1/static/tax-administration/{city_id}', params=params)
        data = res.get('data') or []
        return [TaxOfficeModel.model_validate(item) for item in data]

