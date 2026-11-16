from typing import Any, Optional
import httpx


class OrderModule:
    """Synchronous Order client for AVCI CMS (Storefront & Vendor operations)."""

    def __init__(self, client: httpx.Client):
        self._client = client

    # Storefront / Customer Operations
    def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Finalize checkout and create order from basket (POST /v1/order)."""
        response = self._client.post("/order", json=payload)
        return response.json().get('data', {})

    def list_customer_orders(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict[str, Any]:
        """List orders for authenticated customer (GET /v1/order)."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if status is not None:
            params['status'] = status
        response = self._client.get("/order", params=params)
        return response.json()

    def get_customer_order(self, order_id: str) -> dict[str, Any]:
        """Get single order details for customer (GET /v1/order/:orderId)."""
        response = self._client.get(f"/order/{order_id}")
        return response.json().get('data', {})

    def get_installments(self, bin_number: str, price: float) -> list[dict[str, Any]]:
        """Query installment options by credit card BIN (POST /v1/order/installment)."""
        response = self._client.post("/order/installment", json={"binNumber": bin_number, "price": price})
        return response.json().get('data', [])

    def get_saved_cards(self) -> list[dict[str, Any]]:
        """List stored payment cards (GET /v1/order/saved-cards)."""
        response = self._client.get("/order/saved-cards")
        return response.json().get('data', [])

    def save_card(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Store payment card for one-click checkout (POST /v1/order/saved-cards)."""
        response = self._client.post("/order/saved-cards", json=payload)
        return response.json().get('data', {})

    def delete_saved_card(self, card_id: str) -> bool:
        """Delete stored payment card (DELETE /v1/order/saved-cards/:id)."""
        response = self._client.delete(f"/order/saved-cards/{card_id}")
        return response.status_code == 200

    # Vendor / Merchant Operations (Isolated)
    def list_vendor_orders(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict[str, Any]:
        """List assigned sub-orders for authenticated merchant (GET /v1/order/vendor)."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if status is not None:
            params['status'] = status
        response = self._client.get("/order/vendor", params=params)
        return response.json()

    def get_vendor_order(self, order_id: str) -> dict[str, Any]:
        """Get assigned sub-order details for authenticated merchant (GET /v1/order/vendor/:orderId)."""
        response = self._client.get(f"/order/vendor/{order_id}")
        return response.json().get('data', {})


class AsyncOrderModule:
    """Asynchronous Order client for AVCI CMS (Storefront & Vendor operations)."""

    def __init__(self, client: httpx.AsyncClient):
        self._client = client

    # Storefront / Customer Operations
    async def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Finalize checkout and create order from basket (POST /v1/order)."""
        response = await self._client.post("/order", json=payload)
        return response.json().get('data', {})

    async def list_customer_orders(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict[str, Any]:
        """List orders for authenticated customer (GET /v1/order)."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if status is not None:
            params['status'] = status
        response = await self._client.get("/order", params=params)
        return response.json()

    async def get_customer_order(self, order_id: str) -> dict[str, Any]:
        """Get single order details for customer (GET /v1/order/:orderId)."""
        response = await self._client.get(f"/order/{order_id}")
        return response.json().get('data', {})

    async def get_installments(self, bin_number: str, price: float) -> list[dict[str, Any]]:
        """Query installment options by credit card BIN (POST /v1/order/installment)."""
        response = await self._client.post("/order/installment", json={"binNumber": bin_number, "price": price})
        return response.json().get('data', [])

    async def get_saved_cards(self) -> list[dict[str, Any]]:
        """List stored payment cards (GET /v1/order/saved-cards)."""
        response = await self._client.get("/order/saved-cards")
        return response.json().get('data', [])

    async def save_card(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Store payment card for one-click checkout (POST /v1/order/saved-cards)."""
        response = await self._client.post("/order/saved-cards", json=payload)
        return response.json().get('data', {})

    async def delete_saved_card(self, card_id: str) -> bool:
        """Delete stored payment card (DELETE /v1/order/saved-cards/:id)."""
        response = await self._client.delete(f"/order/saved-cards/{card_id}")
        return response.status_code == 200

    # Vendor / Merchant Operations (Isolated)
    async def list_vendor_orders(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict[str, Any]:
        """List assigned sub-orders for authenticated merchant (GET /v1/order/vendor)."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if status is not None:
            params['status'] = status
        response = await self._client.get("/order/vendor", params=params)
        return response.json()

    async def get_vendor_order(self, order_id: str) -> dict[str, Any]:
        """Get assigned sub-order details for authenticated merchant (GET /v1/order/vendor/:orderId)."""
        response = await self._client.get(f"/order/vendor/{order_id}")
        return response.json().get('data', {})

