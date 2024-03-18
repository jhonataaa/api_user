from pydantic import BaseModel
from pydantic import validator
import re
import sqlalchemy


class UserSchema(BaseModel):
    id:int
    username: str
    password: str
    cpf: str
    email: str


    @validator('username')
    def validar_username(cls, username):  
        if len(username) < 4 or len(username) > 20:
            raise ValueError("O username deve ter entre 4 e 15 caracteres.")
        if not re.match("^[a-zA-Z0-9]+$", username):
            raise ValueError("O username deve conter apenas letras e números.")
        return username

    @validator('password')
    def validar_password(cls, password):  
        if len(password) < 8:
            raise ValueError("A password deve ter pelo menos 8 caracteres.")
        if not re.search("[A-Z]", password):
            raise ValueError("A password deve conter pelo menos uma letra maiúscula.")
        if not re.search("[a-z]", password):
            raise ValueError("A password deve conter pelo menos uma letra minúscula.")
        if not re.search("[0-9]", password):
            raise ValueError("A password deve conter pelo menos um número.")
        if not re.search("[!@#$%^&*()-_+=]", password):
            raise ValueError("A password deve conter pelo menos um caractere especial.")
        return password


@validator('cpf')
def validate_cpf(cls, cpf):
        if len(cpf) < 11:
            raise ValueError('cpf invalid')
        return cpf
    
    
