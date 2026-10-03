from sqlalchemy import select

from app.repositories.sql_repository import SqlRepository
from app.models import Task


class TaskRepository(SqlRepository):

    def add_dado(self, id_user: int, titulo: str, descricao: str, status: str, prioridade: str):
        task = Task(
            id_user=id_user,
            titulo=titulo,
            descriçao=descricao,
            status=status,
            prioridade=prioridade
        )

        self._db.add(task)
        return task

    def remover_dado(self, task: Task):
        self._db.delete(task)
        return task

    def atualizar_dado(self, task: Task, dados: dict):
        for chave, valor in dados.items():
            setattr(task, chave, valor)

    def buscar_por_id(self, task_id: int, user_id: int):
        stmt = select(Task).where(
            Task.id == task_id,
            Task.id_user == user_id
        )
        task = self._db.scalar(stmt)

        if not task:
            return None

        return task

    def buscar_por_id_user(self, id_user: int, offset: int, limit: int):
        stmt = (select(Task).where(Task.id_user == id_user).offset(offset).limit(limit))
        tasks = self._db.scalars(stmt).all()

        if not tasks:
            return None

        return tasks
