from __future__ import annotations

from typing import TYPE_CHECKING, Any

from avcicms.models import PlaceModel, PlaceShortModel

if TYPE_CHECKING:
    from avcicms.client import AsyncAvciCMS, AvciCMS


class PlaceModule:
    """Place (Venue & Physical Location) operations (synchronous)."""

    def __init__(self, client: AvciCMS) -> None:
        self._client = client

    def list(
        self,
        page: int | None = None,
        limit: int | None = None,
        area: str | None = None,
        search: str | None = None,
        status: str | None = None,
    ) -> list[PlaceModel]:
        """List active public places/venues."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if area:
            params['area'] = area
        if search:
            params['search'] = search
        if status:
            params['status'] = status
        res = self._client._http.get('/v1/place', params=params)
        data = res.get('data') or []
        return [PlaceModel.model_validate(item) for item in data]

    def get_by_slug(self, slug: str) -> PlaceModel:
        """Get place details by slug."""
        res = self._client._http.get(f'/v1/place/{slug}')
        return PlaceModel.model_validate(res.get('data') or res)

    def get_by_id(self, id: str) -> PlaceModel:
        """Get place details by ID."""
        res = self._client._http.get(f'/v1/place/id/{id}')
        return PlaceModel.model_validate(res.get('data') or res)

    def get_short_by_slug(self, slug: str) -> PlaceShortModel:
        """Get lightweight place summary card by slug."""
        res = self._client._http.get(f'/v1/place/short/{slug}')
        return PlaceShortModel.model_validate(res.get('data') or res)


class AsyncPlaceModule:
    """Place (Venue & Physical Location) operations (asynchronous)."""

    def __init__(self, client: AsyncAvciCMS) -> None:
        self._client = client

    async def list(
        self,
        page: int | None = None,
        limit: int | None = None,
        area: str | None = None,
        search: str | None = None,
        status: str | None = None,
    ) -> list[PlaceModel]:
        """List active public places/venues."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if area:
            params['area'] = area
        if search:
            params['search'] = search
        if status:
            params['status'] = status
        res = await self._client._http.get('/v1/place', params=params)
        data = res.get('data') or []
        return [PlaceModel.model_validate(item) for item in data]

    async def get_by_slug(self, slug: str) -> PlaceModel:
        """Get place details by slug."""
        res = await self._client._http.get(f'/v1/place/{slug}')
        return PlaceModel.model_validate(res.get('data') or res)

    async def get_by_id(self, id: str) -> PlaceModel:
        """Get place details by ID."""
        res = await self._client._http.get(f'/v1/place/id/{id}')
        return PlaceModel.model_validate(res.get('data') or res)

    async def get_short_by_slug(self, slug: str) -> PlaceShortModel:
        """Get lightweight place summary card by slug."""
        res = await self._client._http.get(f'/v1/place/short/{slug}')
        return PlaceShortModel.model_validate(res.get('data') or res)
