from typing import Any, List, Optional
import httpx


class CustomFormModule:
    """Synchronous Custom Form client for AVCI CMS."""

    def __init__(self, client: httpx.Client):
        self._client = client

    # Storefront Methods
    def get_schema(self, form_id: str) -> dict[str, Any]:
        """Fetch form schema for dynamic rendering (GET /v1/customForm/:formId)."""
        response = self._client.get(f"/customForm/{form_id}")
        return response.json().get('data', {})

    def submit(self, form_id: str, answers: dict[str, Any]) -> dict[str, Any]:
        """Submit form responses from Storefront (POST /v1/customForm/submit/:formId)."""
        response = self._client.post(f"/customForm/submit/{form_id}", json=answers)
        return response.json().get('data', {})

    def has_submitted(self, form_id: str) -> bool:
        """Check if user has submitted (GET /v1/customForm/has-submission/:formId)."""
        response = self._client.get(f"/customForm/has-submission/{form_id}")
        return bool(response.json().get('data', {}).get('hasSubmitted', False))

    # Management Methods
    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> dict[str, Any]:
        """List forms with pagination (GET /v1/customForm)."""
        params = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        response = self._client.get("/customForm", params=params)
        return response.json()

    def get(self, form_id: str) -> dict[str, Any]:
        """Get form detail (GET /v1/customForm/:formId)."""
        response = self._client.get(f"/customForm/{form_id}")
        return response.json().get('data', {})

    def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Create new form (POST /v1/customForm)."""
        response = self._client.post("/customForm", json=payload)
        return response.json().get('data', {})

    def update(self, form_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Update form (PUT /v1/customForm/:formId)."""
        response = self._client.put(f"/customForm/{form_id}", json=payload)
        return response.json().get('data', {})

    def delete(self, form_id: str) -> bool:
        """Delete form (DELETE /v1/customForm/:formId)."""
        response = self._client.delete(f"/customForm/{form_id}")
        return response.status_code == 200

    def get_submissions(
        self,
        form_id: str,
        status: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> dict[str, Any]:
        """List form submissions (GET /v1/customForm/:formId/submissions)."""
        params = {}
        if status:
            params['status'] = status
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        response = self._client.get(f"/customForm/{form_id}/submissions", params=params)
        return response.json()

    def get_submission_detail(self, form_id: str, sub_id: str) -> dict[str, Any]:
        """Get submission review detail (GET /v1/customForm/:formId/submissions/:subId)."""
        response = self._client.get(f"/customForm/{form_id}/submissions/{sub_id}")
        return response.json().get('data', {})

    def update_submission_status(self, form_id: str, sub_id: str, status: str, note: Optional[str] = None) -> dict[str, Any]:
        """Update status (PUT /v1/customForm/:formId/submissions/:subId/status)."""
        payload = {"status": status}
        if note:
            payload["note"] = note
        response = self._client.put(f"/customForm/{form_id}/submissions/{sub_id}/status", json=payload)
        return response.json().get('data', {})

    def process_approval(self, submission_id: str, action_payload: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        """Execute approval actions (POST /v1/customForm/submissions/:submissionId/process)."""
        response = self._client.post(f"/customForm/submissions/{submission_id}/process", json=action_payload or {})
        return response.json().get('data', {})

    def get_statistics(self, form_id: str) -> dict[str, Any]:
        """Get form statistics (GET /v1/customForm/:formId/statistics)."""
        response = self._client.get(f"/customForm/{form_id}/statistics")
        return response.json().get('data', {})

    def get_submission_logs(self, submission_id: str) -> List[dict[str, Any]]:
        """Get submission logs (GET /v1/customForm/:submissionId/logs)."""
        response = self._client.get(f"/customForm/{submission_id}/logs")
        return response.json().get('data', [])


class AsyncCustomFormModule:
    """Asynchronous Custom Form client for AVCI CMS."""

    def __init__(self, client: httpx.AsyncClient):
        self._client = client

    async def get_schema(self, form_id: str) -> dict[str, Any]:
        response = await self._client.get(f"/customForm/{form_id}")
        return response.json().get('data', {})

    async def submit(self, form_id: str, answers: dict[str, Any]) -> dict[str, Any]:
        response = await self._client.post(f"/customForm/submit/{form_id}", json=answers)
        return response.json().get('data', {})

    async def has_submitted(self, form_id: str) -> bool:
        response = await self._client.get(f"/customForm/has-submission/{form_id}")
        return bool(response.json().get('data', {}).get('hasSubmitted', False))

    async def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> dict[str, Any]:
        params = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        response = await self._client.get("/customForm", params=params)
        return response.json()

    async def get(self, form_id: str) -> dict[str, Any]:
        response = await self._client.get(f"/customForm/{form_id}")
        return response.json().get('data', {})

    async def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        response = await self._client.post("/customForm", json=payload)
        return response.json().get('data', {})

    async def update(self, form_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        response = await self._client.put(f"/customForm/{form_id}", json=payload)
        return response.json().get('data', {})

    async def delete(self, form_id: str) -> bool:
        response = await self._client.delete(f"/customForm/{form_id}")
        return response.status_code == 200

    async def get_submissions(
        self,
        form_id: str,
        status: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> dict[str, Any]:
        params = {}
        if status:
            params['status'] = status
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        response = await self._client.get(f"/customForm/{form_id}/submissions", params=params)
        return response.json()

    async def get_submission_detail(self, form_id: str, sub_id: str) -> dict[str, Any]:
        response = await self._client.get(f"/customForm/{form_id}/submissions/{sub_id}")
        return response.json().get('data', {})

    async def update_submission_status(self, form_id: str, sub_id: str, status: str, note: Optional[str] = None) -> dict[str, Any]:
        payload = {"status": status}
        if note:
            payload["note"] = note
        response = await self._client.put(f"/customForm/{form_id}/submissions/{sub_id}/status", json=payload)
        return response.json().get('data', {})

    async def process_approval(self, submission_id: str, action_payload: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        response = await self._client.post(f"/customForm/submissions/{submission_id}/process", json=action_payload or {})
        return response.json().get('data', {})

    async def get_statistics(self, form_id: str) -> dict[str, Any]:
        response = await self._client.get(f"/customForm/{form_id}/statistics")
        return response.json().get('data', {})

    async def get_submission_logs(self, submission_id: str) -> List[dict[str, Any]]:
        response = await self._client.get(f"/customForm/{submission_id}/logs")
        return response.json().get('data', [])

