"""
Nesse modulo ficarao todas as classes que serao mapeados para tabelas no banco de dados

tb_users -> User

"""

# Importando a classe Base
from database import Base

# Importando as classes do SQLAlchemy que represantam os tipos de dados da tabela
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Table

from sqlalchemy.orm import relationship

"""
O SQLAlchemy irá ...........

CREATE TABLE IF NOT EXISTS tb_users(
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL
)
"""
"bitch"

posts_tags = Table(

)

class User(Base):

    # __tablename__ permite definir o nome da tabela mapeada no banco de dados
    __tablename__ = 'tb_users'

    # s atributos abaixo serão os nomes e os tipos das colunas da tabela tb_users:
    # id será um campo tipo integer, chave primária e auto incremento
    # email e password seão campos do tipo varchar, de tamanho 200 e que não
    # permitem valores nulos
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    profile = relationship("UserProfile", back_populates="user", uselist=False)

    posts = relationship('Post', back_populates='user')

    def __repr__(self):
        return f'<User({self.id}, {self.email})>'

    __str__ = __repr__


class UserProfile(Base):

    __tablename__ = 'tb_users_profiles'

    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)

    user = relationship('User', back_populates="profile", uselist=False)

    def __repr__(self):
        return f"<User Profile({self.id}, {self.first_name}, {self.last_name}>"

    __str__ = __repr__


class Post(Base):

    __tablename__ = 'tb_posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('tb_users.id'), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Post ({self.id}, Title{self.title} {self.content})>'

    user = relationship('User', back_populates='post', uselist=True)

    __str__ = __repr__


class Tag(Base):

    __tablename__ = 'tb_tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_post = Column(Integer, ForeignKey('tb_posts.id'), nullable=False)
    name = Column(String(50), nullable=False)

    posts = relationship('Post', back_populates='tag', secondary=posts_tags)