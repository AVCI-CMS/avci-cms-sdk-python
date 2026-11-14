from __future__ import annotations

from typing import TYPE_CHECKING, Any

from avcicms.models import CreateAddressRequest, UpdateAddressRequest, UserAddressModel

if TYPE_CHECKING:
    from avcicms.client import AsyncAvciCMS, AvciCMS


class UserModule:
    """User and Address operations (synchronous)."""

    def __init__(self, client: AvciCMS) -> None:
        self._client = client

    def get_addresses(self) -> list[UserAddressModel]:
        """List user's registered delivery and billing addresses."""
        res = self._client._http.get('/v1/user/address/')
        data = res.get('data') or []
        return [UserAddressModel.model_validate(item) for item in data]

    def add_address(self, payload: CreateAddressRequest | dict[str, Any]) -> Any:
        """Create a new address for the authenticated user."""
        body = payload.model_dump(exclude_none=True) if isinstance(payload, CreateAddressRequest) else payload
        return self._client._http.post('/v1/user/address/', json=body)

    def update_address(self, address_id: str, payload: UpdateAddressRequest | dict[str, Any]) -> Any:
        """Update an existing address (setting isPrimary=True marks it as default)."""
        body = payload.model_dump(exclude_none=True) if isinstance(payload, UpdateAddressRequest) else payload
        return self._client._http.put(f'/v1/user/address/{address_id}', json=body)

    def set_primary_address(self, address_id: str) -> list[UserAddressModel]:
        """Mark the specified address as the primary default address."""
        res = self._client._http.put(f'/v1/user/address/{address_id}/primary', json={})
        data = res.get('data') or []
        return [UserAddressModel.model_validate(item) for item in data]

    def delete_address(self, address_id: str) -> Any:
        """Delete an address."""
        return self._client._http.delete(f'/v1/user/address/{address_id}')


class AsyncUserModule:
    """User and Address operations (asynchronous)."""

    def __init__(self, client: AsyncAvciCMS) -> None:
        self._client = client

    async def get_addresses(self) -> list[UserAddressModel]:
        """List user's registered delivery and billing addresses."""
        res = await self._client._http.get('/v1/user/address/')
        data = res.get('data') or []
        return [UserAddressModel.model_validate(item) for item in data]

    async def add_address(self, payload: CreateAddressRequest | dict[str, Any]) -> Any:
        """Create a new address for the authenticated user."""
        body = payload.model_dump(exclude_none=True) if isinstance(payload, CreateAddressRequest) else payload
        return await self._client._http.post('/v1/user/address/', json=body)

    async def update_address(self, address_id: str, payload: UpdateAddressRequest | dict[str, Any]) -> Any:
        """Update an existing address (setting isPrimary=True marks it as default)."""
        body = payload.model_dump(exclude_none=True) if isinstance(payload, UpdateAddressRequest) else payload
        return await self._client._http.put(f'/v1/user/address/{address_id}', json=body)

    async def set_primary_address(self, address_id: str) -> list[UserAddressModel]:
        """Mark the specified address as the primary default address."""
        res = await self._client._http.put(f'/v1/user/address/{address_id}/primary', json={})
        data = res.get('data') or []
        return [UserAddressModel.model_validate(item) for item in data]

    async def delete_address(self, address_id: str) -> Any:
        """Delete an address."""
        return await self._client._http.delete(f'/v1/user/address/{address_id}')

