from typing import List
from fastapi import APIRouter, Response, Depends, status, Query
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal
from db.models import User as UserModel
from schemas.user import UserSchema as UserOutput
from fastapi import  HTTPException
from sqlalchemy.orm import Session

from db.base import Base


#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/user")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()

#post usando schema
#post usando schema
@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar user')
def add_user(request:UserOutput, db: Session = Depends(get_db)):
        # produto_on_db = ProdutosModel(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
        user_on_db = UserModel(**request.dict())
        db.add(user_on_db)
        db.commit()
        return Response(status_code=status.HTTP_201_CREATED)

@router.get("/{user_name}", description="Listar o user pelo nome")
def get_user(user_name,db: Session = Depends(get_db)):
    user_on_db= db.query(UserModel).filter(UserModel.item == user_name).first()
    return user_on_db


@router.get("/user/listar")
async def get_tarefas(db: Session = Depends(get_db)):
    user= db.query(UserModel).all()
    return user

#validação no código
@router.delete("/{id}", description="Deletar o user pelo id")
def delete_user(id: int, db: Session = Depends(get_db)):


    user_on_db = db.query(UserModel).filter(UserModel.id == id).first()
    if user_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem user com este id')
    db.delete(user_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

#TODO
@router.put('/update/{id}', description='Update product')
def update_user(
    id: int,
    user: UserOutput,
    db: Session = Depends(get_db)
    
    ):
    user_on_db = db.query(UserModel).filter_by(id=id).first()
    if user_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No product was found with the given id')

    user_on_db.id = user.id
    user_on_db.username = user.username 
    user_on_db.password = user.password
    user_on_db.cpf = user.cpf
    user_on_db.email = user.email
    

    db.add(user_on_db)
    db.commit()
    return "ok"

# @router.put("/{id}", )
# async def update_todo(id: int, produtos = Produtos, body: dict) -> dict:
#     produtos_on_db = db.query(Produtos).filter(Produtos.id == id).first()
#     for todo in produtos:
#         if int(todo["id"]) == id:
#             todo["item"] = body["item"]
#             return {
#                 "data": f"Todo with id {id} has been updated."
#             }

#     return {
#         "data": f"Todo with id {id} not found."
#     }

# @app.put("/produto/{id}",response_model=Produtos)
# async def update_produto(request:ProdutosSchema, id: int, db: Session = Depends(get_db)):
#     produto_on_db = db.query(Produtos).filter(Produtos.id == id).first()
#     print(produto_on_db)
#     if produto_on_db is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
#     produto_on_db = Produtos(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
#     db.up
#     db.(produto_on_db)
#     db.commit()
#     db.refresh(produto_on_db)
#     return produto_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


# router = APIRouter()
