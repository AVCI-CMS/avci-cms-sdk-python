import httpx
from typing import Any, List

class WorkspaceModule:
    def __init__(self, client: httpx.Client):
        self._client = client

    def get_settings(self) -> Any:
        # Placeholder for GET /v1/workspace/settings
        return None

    def get_menus(self) -> List[Any]:
        return []

class AsyncWorkspaceModule:
    def __init__(self, client: httpx.AsyncClient):
        self._client = client

    async def get_settings(self) -> Any:
        return None

    async def get_menus(self) -> List[Any]:
        return []
