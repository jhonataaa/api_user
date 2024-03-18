from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# O mecanismo acima cria um objeto adaptado para PostgreSQL, bem como um objeto que estabelecerá um Conexão 
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


#3
