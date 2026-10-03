import jwt

from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta, timezone
from argon2 import PasswordHasher

from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login_forms")

ph = PasswordHasher()

def hash_password(senha: str):
    return ph.hash(senha)

def verify_password(senha: str, hash_senha: str):
    try:
        return ph.verify(hash_senha, senha)
    except Exception:
        return False

def create_token(id_user: int, type: str, tempo: timedelta):
    payload = {
        "sub": str(id_user),
        "type": type,
        "exp": datetime.now(timezone.utc) + tempo
    }

    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

def create_access_token(id_user: int):
    return create_token(id_user, "access", timedelta(minutes=settings.access_token_time))