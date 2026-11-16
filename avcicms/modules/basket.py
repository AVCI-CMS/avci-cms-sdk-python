from typing import Any, Optional
import httpx


class BasketModule:
    """Synchronous Basket client for AVCI CMS."""

    def __init__(self, client: httpx.Client):
        self._client = client

    def create(self, currency: str = "TRY") -> dict[str, Any]:
        """Create a new shopping basket (POST /v1/basket)."""
        response = self._client.post("/basket", json={"currency": currency})
        return response.json().get('data', {})

    def get(self, basket_id: str) -> dict[str, Any]:
        """Get basket contents by ID (GET /v1/basket/:basketId)."""
        response = self._client.get(f"/basket/{basket_id}")
        return response.json().get('data', {})

    def update(self, basket_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Update basket coupons or addresses (PUT /v1/basket/:basketId)."""
        response = self._client.put(f"/basket/{basket_id}", json=payload)
        return response.json().get('data', {})

    def clear(self, basket_id: str) -> bool:
        """Clear all items from basket (DELETE /v1/basket/:basketId)."""
        response = self._client.delete(f"/basket/{basket_id}")
        return response.status_code == 200

    def add_items(self, basket_id: str, items: list[dict[str, Any]]) -> dict[str, Any]:
        """Add items (products, events, routes) to basket (POST /v1/basket/add/:basketId)."""
        response = self._client.post(f"/basket/add/{basket_id}", json={"items": items})
        return response.json().get('data', {})

    def update_quantity(self, basket_id: str, item_id: str, action: str) -> dict[str, Any]:
        """Update item quantity or remove item (PUT /v1/basket/update/:basketId/:itemId/:action)."""
        response = self._client.put(f"/basket/update/{basket_id}/{item_id}/{action}")
        return response.json().get('data', {})

    def change_currency(self, basket_id: str, currency: str) -> dict[str, Any]:
        """Change basket currency (PUT /v1/basket/currency/:basketId)."""
        response = self._client.put(f"/basket/currency/{basket_id}", json={"currency": currency})
        return response.json().get('data', {})

    def prepare_terms(self, basket_id: str) -> dict[str, Any]:
        """Prepare distance sales agreement & info form (POST /v1/basket/terms/)."""
        response = self._client.post("/basket/terms/", json={"basketId": basket_id})
        return response.json().get('data', {})


class AsyncBasketModule:
    """Asynchronous Basket client for AVCI CMS."""

    def __init__(self, client: httpx.AsyncClient):
        self._client = client

    async def create(self, currency: str = "TRY") -> dict[str, Any]:
        """Create a new shopping basket (POST /v1/basket)."""
        response = await self._client.post("/basket", json={"currency": currency})
        return response.json().get('data', {})

    async def get(self, basket_id: str) -> dict[str, Any]:
        """Get basket contents by ID (GET /v1/basket/:basketId)."""
        response = await self._client.get(f"/basket/{basket_id}")
        return response.json().get('data', {})

    async def update(self, basket_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Update basket coupons or addresses (PUT /v1/basket/:basketId)."""
        response = await self._client.put(f"/basket/{basket_id}", json=payload)
        return response.json().get('data', {})

    async def clear(self, basket_id: str) -> bool:
        """Clear all items from basket (DELETE /v1/basket/:basketId)."""
        response = await self._client.delete(f"/basket/{basket_id}")
        return response.status_code == 200

    async def add_items(self, basket_id: str, items: list[dict[str, Any]]) -> dict[str, Any]:
        """Add items (products, events, routes) to basket (POST /v1/basket/add/:basketId)."""
        response = await self._client.post(f"/basket/add/{basket_id}", json={"items": items})
        return response.json().get('data', {})

    async def update_quantity(self, basket_id: str, item_id: str, action: str) -> dict[str, Any]:
        """Update item quantity or remove item (PUT /v1/basket/update/:basketId/:itemId/:action)."""
        response = await self._client.put(f"/basket/update/{basket_id}/{item_id}/{action}")
        return response.json().get('data', {})

    async def change_currency(self, basket_id: str, currency: str) -> dict[str, Any]:
        """Change basket currency (PUT /v1/basket/currency/:basketId)."""
        response = await self._client.put(f"/basket/currency/{basket_id}", json={"currency": currency})
        return response.json().get('data', {})

    async def prepare_terms(self, basket_id: str) -> dict[str, Any]:
        """Prepare distance sales agreement & info form (POST /v1/basket/terms/)."""
        response = await self._client.post("/basket/terms/", json={"basketId": basket_id})
        return response.json().get('data', {})

