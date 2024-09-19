# setup fastapi app
from fastapi import FastAPI, __version__ as fastapi_version
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# from configs import root_path


app = FastAPI(
    title='VIA',
    description='',
    # version=ocr_version.split('+')[0], # remove dirty
    # root_path=root_path,
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

app.mount("/ui", StaticFiles(directory="./static", html=True), name="static")
