from fastapi import APIRouter

router = APIRouter(prefix='/clock', tags=["Healthcheck"])


@router.get("/healthcheck", description="API status")
async def check_service():
    return {"status": True}