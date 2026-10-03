from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

class SqlRepository(ABC):
    def __init__(self, session: Session):
        self._db = session

        self.db = session

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, valor):
        if not isinstance(valor, Session):
            raise ValueError("Sessão inválida!")

        self._db = valor

    @abstractmethod
    def add_dado(self):
        pass

    @abstractmethod
    def remover_dado(self):
        pass

    @abstractmethod
    def buscar_por_id(self):
        pass

    @abstractmethod
    def atualizar_dado(self):
        pass