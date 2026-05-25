# AVCI CMS Python SDK

The official Python SDK for AVCI CMS. Built with `httpx` and `Pydantic` to provide both synchronous and asynchronous support for modern Python applications (like FastAPI and Django).

## 🚀 Getting Started

**Important:** Before using the SDK, you must create an account and a project on the [AVCI CMS App](https://app.avcicms.com). Once your project is created, you will be able to generate your `API Key` and `Client ID`.

### Installation

```bash
pip install avcicms
# or with poetry
poetry add avcicms
```

### Usage

#### Asynchronous Usage (FastAPI, Starlette)
```python
from avcicms import AsyncAvciCMS

async def fetch_posts():
    cms = AsyncAvciCMS(api_key="YOUR_API_KEY", project_id="YOUR_PROJECT_ID")
    posts = await cms.content.find_many("posts")
    print(posts)
```

#### Synchronous Usage (Django, Scripts)
```python
from avcicms import AvciCMS

def fetch_posts():
    cms = AvciCMS(api_key="YOUR_API_KEY", project_id="YOUR_PROJECT_ID")
    posts = cms.content.find_many("posts")
    print(posts)
```

## Features
- Sync and Async clients (`httpx` based)
- Pydantic models for type safety
- Built-in Error Handling (`AvciAPIError`, `UnauthorizedError`, etc.)

## Resources
- **Documentation & Guides:** https://doc.avcicms.com
- **Official Website:** https://avcicms.com
- **Help Center:** https://avcicms.com/resources/help-center
