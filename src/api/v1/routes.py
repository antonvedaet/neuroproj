from fastapi import APIRouter

from src.api.v1.handlers import meta, clock

app_routes_v1 = APIRouter(prefix='/v1')

app_routes_v1.include_router(clock.router)
app_routes_v1.include_router(meta.router)
