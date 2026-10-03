from fastapi import HTTPException
from http import HTTPStatus

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self, session: Session):
        self._db = session
        self._user_repo = UserRepository(session)

    def cadastrar_user(self, nome: str, email: str, senha: str):
        if self._user_repo.buscar_por_email(email):
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Usuario já cadastrado!")
        
        senha_criptografada = hash_password(senha)

        try:
            user = self._user_repo.add_dado(nome, email, senha_criptografada)

            self._db.commit()
            self._db.refresh(user)

            return {"menssage": "Usuário cadastrado",
                    "email": user.email}
        
        except IntegrityError:
            self._db.rollback()
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=f"Usuario já cadastrado!")

    def login_user(self, email: str, senha: str):
        user = self._user_repo.buscar_por_email(email)

        if not user:
            raise HTTPException(status_code=401, detail="Email ou senha inválidos!")

        if not verify_password(senha, user.hash_senha):
            raise HTTPException(status_code=401, detail="Email ou senha inválidos!")

        access_token = create_access_token(user.id)

        return {"access_token": access_token,
                "token_type": "bearer"}