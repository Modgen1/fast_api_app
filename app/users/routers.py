from fastapi import APIRouter
import jwt

from app.users.dao import UsersDAO
from app.users.schemas import SUser
from app.config import settings

reg_router = APIRouter(prefix='/api', tags=['Registration and login handling'])


@reg_router.post('/register')
async def register_user(user: SUser) -> dict:
    check = await UsersDAO.find_by_username(user.username)
    if not check:
        await UsersDAO.register(**user.model_dump())
        return {"message": "User successfully registered"}
    else:
        return {"message": "Registration error"}


@reg_router.post('/login')
async def login_user(user: SUser) -> dict:
    check = await UsersDAO.find_by_username(user.username)
    if check and check.pass_hash == user.pass_hash:
        token = jwt.encode({'username': user.username}, settings.SECRET)
        return {"message": "Logged in successfully", 'token': token}
    else:
        return {"message": "Username or password is incorrect"}
