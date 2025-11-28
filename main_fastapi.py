from fastapi import FastAPI
from sailocus.apis.base import api_router

class Config():
    
    def __init__(self):
        self.PROJ_TITLE = "Sailocus"
        self.PROJ_VERSION = "0.0.1"

settings = Config()

def start_app() -> FastAPI:
    app = FastAPI(title=settings.PROJ_TITLE, version=settings.PROJ_VERSION)
    include_routers(app)
    return app

def include_routers(app):
    app.include_router(api_router)

app = start_app()

@app.get("/")
def index():
    return {"msg":"Hello.  This is Paul and at least the server is working"}