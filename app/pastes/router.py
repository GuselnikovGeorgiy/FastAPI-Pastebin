from fastapi import APIRouter, Depends

from app.pastes.dao import PastesDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/pastes",
    tags=['Pastes'],
)


@router.get("")
async def get_user_pastes(user: Users = Depends(get_current_user)):
    return await PastesDAO.find_all(user_id=user.id)


@router.post("")
async def add_paste(user: Users = Depends(get_current_user),):
    return await PastesDAO.add()


@router.get("/{paste_id}")
def get_paste(paste_id: str):
    pass

