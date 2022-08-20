import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DATABASE_USER')
db_pass = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')
db_port = os.getenv('DATABASE_PORT')
db_name = os.getenv('DATABASE_NAME')

connection_string = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

engine = create_engine(connection_string, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
