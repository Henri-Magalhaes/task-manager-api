from sqlalchemy import select

from app.repositories.sql_repository import SqlRepository
from app.models.user_model import User

class UserRepository(SqlRepository):
    def add_dado(self, nome: str, email: str, senha_criptografada: str):
        user = User(nome=nome, 
                    email=email, 
                    hash_senha=senha_criptografada)

        self._db.add(user)
        return user
    
    def remover_dado(self, user_id: int):
        user = self._db.get(User, user_id)

        if not user:
            return None
            
        self._db.delete(user)
        return user

    def atualizar_dado(self, user: User, dados: dict):
        for keys, values in dados.items():
            setattr(user, keys, values)

    def buscar_por_id(self, user_id: int):
        return self._db.get(User, user_id)
        
    def buscar_por_email(self, email: str):
        stmt = select(User).where(User.email == email)
        user = self._db.scalar(stmt)

        return user
