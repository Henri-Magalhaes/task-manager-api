from sqlalchemy import String, ForeignKey, func, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from enum import Enum

from app.core.database import Base


class StatusTask(str, Enum):
    ATIVO = "ATIVO"
    CONCLUIDO = "CONCLUIDO"

class PrioridadeTask(str, Enum):
    BAIXA = "BAIXA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"

class Task(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descriçao: Mapped[str] = mapped_column(String(1200), default="Sem-Descricao")
    status: Mapped[StatusTask] = mapped_column(SQLEnum(StatusTask), nullable=False, default=StatusTask.ATIVO)
    prioridade: Mapped[PrioridadeTask] = mapped_column(SQLEnum(PrioridadeTask), nullable=False)
    dt_criacao: Mapped[datetime] = mapped_column(server_default=func.now())
    dt_atualizacao: Mapped[datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now())

    user: Mapped["User"] = relationship(
        back_populates="tarefas"
    )