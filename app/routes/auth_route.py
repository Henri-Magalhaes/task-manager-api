from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_session, get_user
from app.schemas.user_schemas import UserRegisterInput, UserLoginInput, UserResponse
from app.services.auth_service import AuthService
from app.models import User

auth_router = APIRouter(prefix="/auth", tags=["autenticação"])

@auth_router.post("/register", status_code=201)
async def registrar_usuario(user: UserRegisterInput, session: Session=Depends(get_session)):
    return AuthService(session).cadastrar_user(user.nome, user.email, user.senha)

@auth_router.post("/login")
async def login_usuario(user: UserLoginInput, session: Session=Depends(get_session)):
    return AuthService(session).login_user(user.email, user.senha)

@auth_router.post("/login_forms")
async def login_forms(dados: OAuth2PasswordRequestForm=Depends(), session: Session=Depends(get_session)):
    return AuthService(session).login_user(dados.username, dados.password)

@auth_router.get("/me", response_model=UserResponse)
async def me(user: User=Depends(get_user)):
    return user