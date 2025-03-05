# setup fastapi app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(
        title='VIA',
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

    app.mount('/ui', StaticFiles(directory="./static", html=True), name="static")
    return app
