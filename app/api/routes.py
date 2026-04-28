from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal
from app.services.route_service import get_route_service, evaluate_transfer_service
router = APIRouter()


class RouteRequest(BaseModel):
    start: str
    end: str
    mode: Literal["fastest", "no_stairs", "wheelchair"] = "fastest"

class TransferCheckRequest(BaseModel):
    start: str
    end: str
    mode: Literal["fastest", "no_stairs", "wheelchair"] = "fastest"
    transfer_time: int
    delay: int
@router.post("/route")
def get_route(request: RouteRequest):
    result = get_route_service(request.start, request.end, request.mode)

    if result["status"] != 200:
        raise HTTPException(status_code=result["status"], detail=result["error"])

    return result["data"]

@router.post("/transfer-check")
def transfer_check(request: TransferCheckRequest):
    result = evaluate_transfer_service(
        request.start,
        request.end,
        request.mode,
        request.transfer_time,
        request.delay
    )

    if result["status"] != 200:
        raise HTTPException(status_code=result["status"], detail=result["error"])

    return result["data"]