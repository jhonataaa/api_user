from pydantic import BaseModel
from pydantic import validator
import re

#TODO criar pasta caso de uso
# #Este arquivo ficam as regras de negócio

class Produtos(BaseModel):
    id: int
    item: str
    peso: float
    numero_caixas: int

    @validator('peso')
    def validate_peso(cls, value):
        if value <= 0:
            raise ValueError('Peso Invalido')
        return value

    @validator('item')
    def validate_item(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Invalid item')
        return value


