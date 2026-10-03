from pydantic import BaseModel, Field, ConfigDict

from app.models.task_model import StatusTask, PrioridadeTask

class TaskUpdate(BaseModel):
    titulo: str | None = None
    descriçao: str | None = None
    status: StatusTask | None = None
    prioridade: PrioridadeTask | None = None


class TaskAddInput(BaseModel):
    titulo: str = Field(min_length=6, max_length=100)
    descriçao: str | None = Field(max_length=1200, default=None)
    status: StatusTask = StatusTask.ATIVO
    prioridade: PrioridadeTask = PrioridadeTask.MEDIA


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    id_user: int
    titulo: str
    descriçao: str
    status: StatusTask
    prioridade: PrioridadeTask