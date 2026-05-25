import pytest
from avcicms import AvciCMS, AsyncAvciCMS

def test_sync_client_initialization():
    cms = AvciCMS(api_key="test-key", project_id="test-project")
    assert cms.api_key == "test-key"
    assert cms.project_id == "test-project"
    assert hasattr(cms, "content")
    assert hasattr(cms, "workspace")

@pytest.mark.asyncio
async def test_async_client_initialization():
    cms = AsyncAvciCMS(api_key="test-key", project_id="test-project")
    assert cms.api_key == "test-key"
    assert cms.project_id == "test-project"
    assert hasattr(cms, "content")
    assert hasattr(cms, "workspace")
