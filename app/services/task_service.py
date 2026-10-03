from fastapi import HTTPException
from http import HTTPStatus

from sqlalchemy.orm import Session

from app.repositories.task_repository import TaskRepository
from app.schemas.task_schemas import TaskUpdate

class TaskService:
    def __init__(self, session: Session):
        self._db = session
        self._task_repo = TaskRepository(session)

    def adicionar_tarefa(self, id_user: int, titulo: str, descricao: str, status: str, prioridade: str):
        task = self._task_repo.add_dado(id_user, titulo, descricao, status, prioridade)

        self._db.commit()
        self._db.refresh(task)

        return task

    def listar_tarefas(self, id_user: int, offset: int=0, limit: int=10):
        tasks = self._task_repo.buscar_por_id_user(id_user, offset, limit)

        if tasks is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Tarefas não encontradas!")

        return tasks

    def buscar_tarefa(self, id_tarefa: int, id_user: int):
        task = self._task_repo.buscar_por_id(id_tarefa, id_user)

        if task is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Tarefa não encontrada!")

        return task

    def remover_tarefa(self, id_tarefa: int, id_user: int):
        task = self._task_repo.buscar_por_id(id_tarefa, id_user)

        if not task:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Tarefa não encontrada!")

        self._task_repo.remover_dado(task)
        self._db.commit()

        return None

    def atualizar_tarefa(self, id_tarefa: int, id_user: int, dados: TaskUpdate):
        task = self._task_repo.buscar_por_id(id_tarefa, id_user)

        if not task:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Tarefa não encontrada!")

        dados = dados.model_dump(exclude_unset=True)

        self._task_repo.atualizar_dado(task, dados)

        self._db.commit()
        self._db.refresh(task)

        return task
