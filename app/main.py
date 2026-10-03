from fastapi import FastAPI

from app.models import User, Task
from app.routes.auth_route import auth_router
from app.routes.task_route import task_router

app = FastAPI()

@app.get("/home")
async def home():
    return {"menssage": "Api funcionando"}

app.include_router(auth_router)
app.include_router(task_router)