from fastapi import APIRouter, Depends

from app.exceptions import NotFoundException
from app.pastes.dao import PastesDAO
from app.pastes.schemas import SNewPaste
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/pastes",
    tags=["Pastes"],
)


@router.get("")
async def get_user_pastes(user: Users = Depends(get_current_user)):
    return await PastesDAO.find_all(user_id=user.id)


@router.post("/new")
async def add_paste(
    paste: SNewPaste,
    user: Users = Depends(get_current_user),
):
    paste = await PastesDAO.add(title=paste.title, body=paste.body, user_id=user.id)
    return paste


@router.get("/{paste_id}")
async def get_paste(paste_id: str):
    paste = await PastesDAO.find_one_or_none(id=paste_id)
    if not paste:
        raise NotFoundException
    return paste
