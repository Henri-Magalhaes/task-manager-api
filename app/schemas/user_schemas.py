from pydantic import BaseModel, EmailStr, Field

class UserRegisterInput(BaseModel):
    nome: str = Field(min_length=6, max_length=100)
    email: EmailStr = Field(max_length=100)
    senha: str = Field(min_length=6, max_length=100)

class UserLoginInput(BaseModel):
    email: EmailStr = Field(max_length=100)
    senha: str = Field(min_length=6)

class UserUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    senha: str | None = None

class UserResponse(BaseModel):
    id: int
    nome: str
    email: str