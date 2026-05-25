import httpx
from typing import Optional, Any

class AvciCMS:
    def __init__(self, api_key: str, project_id: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.project_id = project_id
        self.base_url = base_url or "https://api.avcicms.com/v1"
        self._client = httpx.Client(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )

    def content(self, model_slug: str):
        # Placeholder for phase 1 automation
        class ContentAPI:
            def find_many(self, limit: int = 10) -> Any:
                print(f"Fetching {model_slug} with limit {limit}")
                return []
        
        return ContentAPI()
