from fastapi import APIRouter, UploadFile
from src.service.clock.analyser import Analyser

router = APIRouter(prefix='/clock')
analyser = Analyser("resources/clock.pt")


@router.get("/healthcheck", description="API status")
async def check_service():
    return {"status": True}


@router.post("/analyse")
async def analyse(file: UploadFile):
    path = await analyser.recieve_image(file)
    res = await analyser.analyse_image(path)
    return {"result": str(res)}
