import httpx
from typing import Optional

from .exceptions import handle_response_error
from .modules.content import ContentModule, AsyncContentModule
from .modules.workspace import WorkspaceModule, AsyncWorkspaceModule
from .modules.attribute import AttributeModule, AsyncAttributeModule
from .modules.custom_form import CustomFormModule, AsyncCustomFormModule
from .modules.basket import BasketModule, AsyncBasketModule
from .modules.order import OrderModule, AsyncOrderModule
from .modules.user import UserModule, AsyncUserModule
from .modules.merchant import MerchantModule, AsyncMerchantModule
from .modules.brand import BrandModule, AsyncBrandModule
from .modules.organization import OrganizationModule, AsyncOrganizationModule
from .modules.static import StaticModule, AsyncStaticModule
from .modules.team import TeamModule, AsyncTeamModule
from .modules.place import PlaceModule, AsyncPlaceModule

def response_hook(response: httpx.Response):
    handle_response_error(response)

class AvciCMS:
    def __init__(self, api_key: str, project_id: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.project_id = project_id
        self.base_url = base_url or "https://api.avcicms.com/v1"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "x-project-id": self.project_id
        }
        
        self._client = httpx.Client(
            base_url=self.base_url,
            headers=headers,
            event_hooks={'response': [response_hook]}
        )
        self._http = self._client
        
        self.content = ContentModule(self._client)
        self.workspace = WorkspaceModule(self._client)
        self.attribute = AttributeModule(self._client)
        self.custom_form = CustomFormModule(self._client)
        self.basket = BasketModule(self._client)
        self.order = OrderModule(self._client)
        self.user = UserModule(self)
        self.merchant = MerchantModule(self)
        self.brand = BrandModule(self)
        self.organization = OrganizationModule(self)
        self.static = StaticModule(self)
        self.team = TeamModule(self)
        self.place = PlaceModule(self)

class AsyncAvciCMS:
    def __init__(self, api_key: str, project_id: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.project_id = project_id
        self.base_url = base_url or "https://api.avcicms.com/v1"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "x-project-id": self.project_id
        }
        
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=headers,
            event_hooks={'response': [response_hook]}
        )
        self._http = self._client
        
        self.content = AsyncContentModule(self._client)
        self.workspace = AsyncWorkspaceModule(self._client)
        self.attribute = AsyncAttributeModule(self._client)
        self.custom_form = AsyncCustomFormModule(self._client)
        self.basket = AsyncBasketModule(self._client)
        self.order = AsyncOrderModule(self._client)
        self.user = AsyncUserModule(self)
        self.merchant = AsyncMerchantModule(self)
        self.brand = AsyncBrandModule(self)
        self.organization = AsyncOrganizationModule(self)
        self.static = AsyncStaticModule(self)
        self.team = AsyncTeamModule(self)
        self.place = AsyncPlaceModule(self)
