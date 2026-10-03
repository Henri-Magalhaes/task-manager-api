import jwt

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from http import HTTPStatus

from app.core.database import engine
from app.core.security import oauth2_scheme
from app.core.config import settings
from app.repositories.user_repository import UserRepository

def get_session():
    with Session(engine) as db:
        yield db

def get_user(token: str=Depends(oauth2_scheme), session: Session=Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail="token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
            options={
                "require": ["sub", "exp"]
            }
        )

        type_token = payload.get("type")
        user_id = payload.get("sub")

        if type_token != "access":
            raise credentials_exception

        if not user_id:
            raise credentials_exception
         
    except jwt.InvalidTokenError:
        raise credentials_exception

    user = UserRepository(session).buscar_por_id(int(user_id))

    if user is None:
        raise credentials_exception

    return user