from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from app.core.database import Base

class User(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hash_senha: Mapped[str] = mapped_column(nullable=False)
    dt_criacao: Mapped[datetime] = mapped_column(server_default=func.now())

    tarefas: Mapped[list["Task"]] = relationship(
        back_populates="user"
    )
