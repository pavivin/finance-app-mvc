from datetime import datetime
from fastapi import APIRouter
from models.users import User
from views import Response, ProfileView


router = APIRouter(tags=["auth"], prefix='/auth')


@router.get(
    "/profile",
    response_model=Response[ProfileView],
    summary="Pofile",
    status_code=200,
)
async def get_profile():
    user = await User.get(id=1)
    return Response(payload=ProfileView(**dict(user)))
