from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.dependencies import get_session, get_user
from app.services.task_service import TaskService
from app.schemas.task_schemas import TaskUpdate, TaskAddInput, TaskResponse
from app.models.user_model import User

task_router = APIRouter(prefix="/tasks", tags=["Tarefas"])

@task_router.post("/", status_code=201, response_model=TaskResponse)
async def add_task(task: TaskAddInput, user: User=Depends(get_user), session: Session=Depends(get_session)):
    return TaskService(session).adicionar_tarefa(user.id, task.titulo, task.descriçao, task.status, task.prioridade)

@task_router.get("/", response_model=list[TaskResponse])
async def listar_tasks(session: Session=Depends(get_session),
                        user: User=Depends(get_user),
                        offset: int=Query(default=0, ge=0),
                        limit: int=Query(default=10, ge=1, le=100)):

    return TaskService(session).listar_tarefas(user.id, offset, limit)

@task_router.get("/{id_task}", response_model=TaskResponse)
async def buscar_task(id_task: int, user: User=Depends(get_user), session: Session=Depends(get_session)):
    return TaskService(session).buscar_tarefa(id_task, user.id)

@task_router.patch("/{id_task}", response_model=TaskResponse)
async def atualizar_task(id_task: int, dados: TaskUpdate, user: User=Depends(get_user), session: Session=Depends(get_session)):
    return TaskService(session).atualizar_tarefa(id_task, user.id, dados)

@task_router.delete("/{id_task}", status_code=204)
async def deletar_task(id_task: int, user: User=Depends(get_user), session: Session=Depends(get_session)):
    return TaskService(session).remover_tarefa(id_task, user.id)
