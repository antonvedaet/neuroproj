from fastapi import APIRouter

from src.api.v1.routes import app_routes_v1

app_routes = APIRouter(prefix='/api')

app_routes.include_router(app_routes_v1)