from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.app_routes import app_routes

def create_app() -> FastAPI:
    app = FastAPI(
        title="ADHD",
        description="ADHD API",
        version="0.0.1",
    )
    app.include_router(app_routes)
    return app


app = create_app()
