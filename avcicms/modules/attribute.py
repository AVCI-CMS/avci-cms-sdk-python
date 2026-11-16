from typing import Any, List, Optional, Union
import httpx

from ..models import (
    AttributeDto,
    AttributeEntityType,
    AttributeModel,
    AttributeShortModel,
    CreateAttributePayload,
    SourceOptionDto,
)


class AttributeModule:
    """Synchronous Attribute client for AVCI CMS."""

    def __init__(self, client: httpx.Client):
        self._client = client

    def get_public_list(self, entity_type: Union[AttributeEntityType, str]) -> List[dict[str, Any]]:
        """Get public attributes for storefront filtering (GET /v1/attribute/:type)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.get(f"/attribute/{val}")
        return response.json().get('data', [])

    def get_source_options(self, entity_type: Union[AttributeEntityType, str]) -> List[dict[str, Any]]:
        """Get dynamic options for SOURCE type attributes (GET /v1/attribute/:type/source-options)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.get(f"/attribute/{val}/source-options")
        return response.json().get('data', [])

    def list(
        self,
        entity_type: Union[AttributeEntityType, str],
        page: Optional[int] = None,
        limit: Optional[int] = None,
        search: Optional[str] = None,
    ) -> dict[str, Any]:
        """List paginated attributes for management console (GET /v1/attribute/:type)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        params = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if search:
            params['search'] = search
        response = self._client.get(f"/attribute/{val}", params=params)
        return response.json()

    def list_for_form(self, entity_type: Union[AttributeEntityType, str]) -> List[dict[str, Any]]:
        """Get simplified attribute list for form selects (GET /v1/attribute/:type/list)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.get(f"/attribute/{val}/list")
        return response.json().get('data', [])

    def get_by_id(self, entity_type: Union[AttributeEntityType, str], id: str) -> dict[str, Any]:
        """Get attribute details by ID (GET /v1/attribute/:type/:id)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.get(f"/attribute/{val}/{id}")
        return response.json().get('data', {})

    def check_key(self, entity_type: Union[AttributeEntityType, str], key: str) -> bool:
        """Check if attribute key is available (GET /v1/attribute/:type/check?key=...)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.get(f"/attribute/{val}/check", params={'key': key})
        return bool(response.json().get('data', {}).get('available', False))

    def create(self, entity_type: Union[AttributeEntityType, str], payload: dict[str, Any]) -> dict[str, Any]:
        """Create a new attribute (POST /v1/attribute/:type)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.post(f"/attribute/{val}", json=payload)
        return response.json().get('data', {})

    def update(self, entity_type: Union[AttributeEntityType, str], id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Update an existing attribute (PUT /v1/attribute/:type/:id)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.put(f"/attribute/{val}/{id}", json=payload)
        return response.json().get('data', {})

    def delete(self, entity_type: Union[AttributeEntityType, str], id: str) -> bool:
        """Delete an attribute (DELETE /v1/attribute/:type/:id)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.delete(f"/attribute/{val}/{id}")
        return response.status_code == 200

    def bulk_delete(self, entity_type: Union[AttributeEntityType, str], ids: List[str]) -> int:
        """Bulk delete multiple attributes (DELETE /v1/attribute/:type/bulk)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.request("DELETE", f"/attribute/{val}/bulk", json={"ids": ids})
        return int(response.json().get('data', {}).get('deletedCount', len(ids)))

    def bulk_update_status(self, entity_type: Union[AttributeEntityType, str], ids: List[str], status: str) -> int:
        """Bulk update status for attributes (PUT /v1/attribute/:type/bulk/status)."""
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = self._client.put(f"/attribute/{val}/bulk/status", json={"ids": ids, "status": status})
        return int(response.json().get('data', {}).get('updatedCount', len(ids)))


class AsyncAttributeModule:
    """Asynchronous Attribute client for AVCI CMS."""

    def __init__(self, client: httpx.AsyncClient):
        self._client = client

    async def get_public_list(self, entity_type: Union[AttributeEntityType, str]) -> List[dict[str, Any]]:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.get(f"/attribute/{val}")
        return response.json().get('data', [])

    async def get_source_options(self, entity_type: Union[AttributeEntityType, str]) -> List[dict[str, Any]]:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.get(f"/attribute/{val}/source-options")
        return response.json().get('data', [])

    async def list(
        self,
        entity_type: Union[AttributeEntityType, str],
        page: Optional[int] = None,
        limit: Optional[int] = None,
        search: Optional[str] = None,
    ) -> dict[str, Any]:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        params = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if search:
            params['search'] = search
        response = await self._client.get(f"/attribute/{val}", params=params)
        return response.json()

    async def list_for_form(self, entity_type: Union[AttributeEntityType, str]) -> List[dict[str, Any]]:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.get(f"/attribute/{val}/list")
        return response.json().get('data', [])

    async def get_by_id(self, entity_type: Union[AttributeEntityType, str], id: str) -> dict[str, Any]:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.get(f"/attribute/{val}/{id}")
        return response.json().get('data', {})

    async def check_key(self, entity_type: Union[AttributeEntityType, str], key: str) -> bool:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.get(f"/attribute/{val}/check", params={'key': key})
        return bool(response.json().get('data', {}).get('available', False))

    async def create(self, entity_type: Union[AttributeEntityType, str], payload: dict[str, Any]) -> dict[str, Any]:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.post(f"/attribute/{val}", json=payload)
        return response.json().get('data', {})

    async def update(self, entity_type: Union[AttributeEntityType, str], id: str, payload: dict[str, Any]) -> dict[str, Any]:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.put(f"/attribute/{val}/{id}", json=payload)
        return response.json().get('data', {})

    async def delete(self, entity_type: Union[AttributeEntityType, str], id: str) -> bool:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.delete(f"/attribute/{val}/{id}")
        return response.status_code == 200

    async def bulk_delete(self, entity_type: Union[AttributeEntityType, str], ids: List[str]) -> int:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.request("DELETE", f"/attribute/{val}/bulk", json={"ids": ids})
        return int(response.json().get('data', {}).get('deletedCount', len(ids)))

    async def bulk_update_status(self, entity_type: Union[AttributeEntityType, str], ids: List[str], status: str) -> int:
        val = entity_type.value if hasattr(entity_type, 'value') else entity_type
        response = await self._client.put(f"/attribute/{val}/bulk/status", json={"ids": ids, "status": status})
        return int(response.json().get('data', {}).get('updatedCount', len(ids)))

