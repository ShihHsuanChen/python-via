# setup fastapi app
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from . import __version__


def create_app():
    app = FastAPI(
        title='VIA',
        version=__version__,
        docs_url=None,
        redoc_url=None,
        description='Local VGG Annotator with Uvicorn server',
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost",
            "http://localhost:8080",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get('/')
    def root():
        return RedirectResponse('/ui/index.html')

    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    app.mount('/ui', StaticFiles(directory=static_dir), name="static")
    return app
