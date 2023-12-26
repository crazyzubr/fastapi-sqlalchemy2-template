from logging import getLogger

from fastapi import FastAPI
from starlette.responses import PlainTextResponse

from core.api.routes.api_v1 import api_v1_router


__all__ = ('app', )

logger = getLogger('app')
app = FastAPI()
app.include_router(api_v1_router)


@app.get('/', response_class=PlainTextResponse)
def main_view():
    """Stub view for main route."""
    return 'Empty page'
