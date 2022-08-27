from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Date
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Pessoa(Base):

    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    telefone = Column(String(9), nullable=False)

    def __repr__(self):
        return f'< Usuário: {self.id}. Email: {self.email}. Telefone: {self.telefone}>'

    __str__ = __repr__

    profile = relationship("Profile")


class UserProfile(Base):

    __tablename__ = 'tb_profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'), primary_key=True)
    birth_date = Column(Date, nullable=True)

    def __repr__(self):
        return f'< Perfil: {self.id}. Usuário: {self.user_id}. Email: {self.email}. Telefone: {self.telefone} >'

    __str__ = __repr__

    user = relationship("User", back_populates="user", uselist=False)


class Conta(Base):

    __tablename__ = 'tb_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer,ForeignKey('tb_users.id'), primary_key=True)
    nome = Column(String(200), nullable=False)
    saldo = Column(Integer, nullable=False)

    def __repr__(self):
        return f'< Conta: {self.id}. Usuário: {self.id_user}. Nome: {self.nome}. Saldo: R${self.saldo}>'

    __str__ = __repr__

    user = relationship('Pessoa', back_populates='accounts', uselist=True)


class Transacao(Base):

    __tablename__ = 'tb_transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_sender = Column(Integer, ForeignKey('tb_accounts.id'), primary_key=True)
    id_receiver = Column(Integer, ForeignKey('tb_accounts.id'), primary_key=True)
    valor = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    sender_account = relationship('Conta', back_populates='transactions', uselist=False)
    receiver_account = relationship('Conta', back_populates='transactions', uselist=False)

    def __repr__(self):
        return f'< Transação: {self.id}. Remetente: {self.id_sender}. Destinatário: {self.id_receiver}. Hora: {self.hora_transacao}. Valor: R${self.valor} >/'

    __str__ = __repr__
