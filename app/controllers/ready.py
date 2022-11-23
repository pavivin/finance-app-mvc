from fastapi import APIRouter
from views import Response


router = APIRouter(tags=["ready"], prefix='/healthcheck')


@router.get(
    "/ready",
    response_model=Response,
    summary="Simple health check.",
    status_code=200
)
async def ready_check():
    return Response()
