from __future__ import annotations

from typing import TYPE_CHECKING, Any

from avcicms.models import EntityProfileModel, UpdateEntityMeRequest

if TYPE_CHECKING:
    from avcicms.client import AsyncAvciCMS, AvciCMS


class BrandModule:
    """Brand operations (synchronous)."""

    def __init__(self, client: AvciCMS) -> None:
        self._client = client

    def get_me(self) -> EntityProfileModel:
        """Fetch the authenticated brand's own showcase profile (/profil/sayfam)."""
        res = self._client._http.get('/v1/brand/me')
        return EntityProfileModel.model_validate(res.get('data') or res)

    def update_me(self, payload: UpdateEntityMeRequest | dict[str, Any]) -> EntityProfileModel:
        """Update the authenticated brand's showcase profile."""
        body = payload.model_dump(exclude_none=True) if isinstance(payload, UpdateEntityMeRequest) else payload
        res = self._client._http.put('/v1/brand/me', json=body)
        return EntityProfileModel.model_validate(res.get('data') or res)

    def list(self, page: int | None = None, limit: int | None = None, search: str | None = None) -> list[EntityProfileModel]:
        """List active public brands."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if search:
            params['search'] = search
        res = self._client._http.get('/v1/brand', params=params)
        data = res.get('data') or []
        return [EntityProfileModel.model_validate(item) for item in data]

    def get_by_slug(self, slug: str) -> EntityProfileModel:
        """Get brand details by slug."""
        res = self._client._http.get(f'/v1/brand/{slug}')
        return EntityProfileModel.model_validate(res.get('data') or res)


class AsyncBrandModule:
    """Brand operations (asynchronous)."""

    def __init__(self, client: AsyncAvciCMS) -> None:
        self._client = client

    async def get_me(self) -> EntityProfileModel:
        """Fetch the authenticated brand's own showcase profile (/profil/sayfam)."""
        res = await self._client._http.get('/v1/brand/me')
        return EntityProfileModel.model_validate(res.get('data') or res)

    async def update_me(self, payload: UpdateEntityMeRequest | dict[str, Any]) -> EntityProfileModel:
        """Update the authenticated brand's showcase profile."""
        body = payload.model_dump(exclude_none=True) if isinstance(payload, UpdateEntityMeRequest) else payload
        res = await self._client._http.put('/v1/brand/me', json=body)
        return EntityProfileModel.model_validate(res.get('data') or res)

    async def list(self, page: int | None = None, limit: int | None = None, search: str | None = None) -> list[EntityProfileModel]:
        """List active public brands."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if search:
            params['search'] = search
        res = await self._client._http.get('/v1/brand', params=params)
        data = res.get('data') or []
        return [EntityProfileModel.model_validate(item) for item in data]

    async def get_by_slug(self, slug: str) -> EntityProfileModel:
        """Get brand details by slug."""
        res = await self._client._http.get(f'/v1/brand/{slug}')
        return EntityProfileModel.model_validate(res.get('data') or res)

