from __future__ import annotations

from typing import TYPE_CHECKING, Any

from avcicms.models import TeamMemberModel

if TYPE_CHECKING:
    from avcicms.client import AsyncAvciCMS, AvciCMS


class TeamModule:
    """Corporate Team operations (synchronous)."""

    def __init__(self, client: AvciCMS) -> None:
        self._client = client

    def list(self, page: int | None = None, limit: int | None = None, lg: str | None = None) -> list[TeamMemberModel]:
        """List published corporate team members."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if lg:
            params['lg'] = lg
        res = self._client._http.get('/v1/team', params=params)
        data = res.get('data') or []
        return [TeamMemberModel.model_validate(item) for item in data]

    def get_by_slug(self, slug: str, lg: str | None = None) -> TeamMemberModel:
        """Get team member details by slug."""
        params: dict[str, Any] = {}
        if lg:
            params['lg'] = lg
        res = self._client._http.get(f'/v1/team/{slug}', params=params)
        return TeamMemberModel.model_validate(res.get('data') or res)

    def get_by_id(self, member_id: str) -> TeamMemberModel:
        """Get team member details by ID."""
        res = self._client._http.get(f'/v1/team/id/{member_id}')
        return TeamMemberModel.model_validate(res.get('data') or res)


class AsyncTeamModule:
    """Corporate Team operations (asynchronous)."""

    def __init__(self, client: AsyncAvciCMS) -> None:
        self._client = client

    async def list(self, page: int | None = None, limit: int | None = None, lg: str | None = None) -> list[TeamMemberModel]:
        """List published corporate team members."""
        params: dict[str, Any] = {}
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit
        if lg:
            params['lg'] = lg
        res = await self._client._http.get('/v1/team', params=params)
        data = res.get('data') or []
        return [TeamMemberModel.model_validate(item) for item in data]

    async def get_by_slug(self, slug: str, lg: str | None = None) -> TeamMemberModel:
        """Get team member details by slug."""
        params: dict[str, Any] = {}
        if lg:
            params['lg'] = lg
        res = await self._client._http.get(f'/v1/team/{slug}', params=params)
        return TeamMemberModel.model_validate(res.get('data') or res)

    async def get_by_id(self, member_id: str) -> TeamMemberModel:
        """Get team member details by ID."""
        res = await self._client._http.get(f'/v1/team/id/{member_id}')
        return TeamMemberModel.model_validate(res.get('data') or res)

