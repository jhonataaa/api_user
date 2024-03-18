from typing import List
from fastapi import APIRouter, Response, Depends, status, Query
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal
from db.models import Produtos as ProdutosModel
from schemas.produto import Produtos as ProdutosOutput
from sqlalchemy.orm import Session
from fastapi import HTTPException

from db.base import Base


#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/produtos")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()

#post usando schema
#post usando schema
@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar produto')
def add_produto(request:ProdutosOutput, db: Session = Depends(get_db)):
        # produto_on_db = ProdutosModel(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
        produto_on_db = ProdutosModel(**request.dict())
        db.add(produto_on_db)
        db.commit()
        return Response(status_code=status.HTTP_201_CREATED)

@router.get("/{produto_name}", description="Listar o produto pelo nome")
def get_produtos(produto_name,db: Session = Depends(get_db)):
    produto_on_db= db.query(ProdutosModel).filter(ProdutosModel.item == produto_name).first()
    return produto_on_db


@router.get("/produtos/listar")
async def get_tarefas(db: Session = Depends(get_db)):
    produtos= db.query(ProdutosModel).all()
    return produtos

#validação no código
@router.delete("/{id}", description="Deletar o produto pelo id")
def delete_produto(id: int, db: Session = Depends(get_db)):


    produto_on_db = db.query(ProdutosModel).filter(ProdutosModel.id == id).first()
    if produto_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
    db.delete(produto_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

#TODO
@router.put('/update/{id}', description='Update product')
def update_produto(
    id: int,
    produto: ProdutosOutput,
    db: Session = Depends(get_db)
    
    ):
    product_on_db = db.query(ProdutosModel).filter_by(id=id).first()
    if product_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No product was found with the given id')
        
    product_on_db.item = produto.item
    product_on_db.peso = produto.peso
    product_on_db.numero_caixas = produto.numero_caixas
    

    db.add(product_on_db)
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
