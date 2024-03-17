from fastapi import APIRouter, Depends, Response

from app.exceptions import UserAlreadyExistsException
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserRegister, SUserLogin

router = APIRouter(prefix="/auth", tags=["Auth and Users"])


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password,
    )


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("pastebin_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("pastebin_access_cookie")


@router.get("/me")
async def get_me(current_user: Users = Depends(get_current_user)):
    return current_user
