# Valores de variáveis de ambiente
import os

# Create engine é uma funcao que cria uma conexão com o banco de dados
from sqlalchemy import create_engine

# Something something classes variadas
from sqlalchemy.ext.declarative import declarative_base

# Session maker cria a sessão de acesso ao banco de dados
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DATABASE_NAME')

connection_string = f'sqlite:///{db_name}'

engine = create_engine(connection_string, echo=True)

# Declarative base retorna a classe base na qual todas as classes do nosso projeto,
# que forem models, irão herdar. PRecisamos isso ara ser possivel mapear as
# classes para as tabelas do banco de dados
Base = declarative_base()

# Criamos a sessão. É por meio desse objeto que o SQLAlchemy executa as instruções SQL
# no banco de dados
Session = sessionmaker(bind=engine)
session = Session()
