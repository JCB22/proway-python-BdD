from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Date
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Pessoa(Base):

    __tablename__ = 'tb_pessoas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    senha = Column(String(200), nullable=False)

    profile = relationship("UserProfile", back_populates="user", uselist=False)
    conta = relationship("Conta", back_populates="user")

    def __repr__(self):
        return f'< Usuário: {self.id}. Email: {self.email}.>'

    __str__ = __repr__


class UserProfile(Base):

    __tablename__ = 'tb_profiles'

    id = Column(Integer, ForeignKey("tb_pessoas.id"), autoincrement=True)
    nome = Column(String(200), nullable=False)
    birth_date = Column(Date, nullable=True)

    pessoa = relationship("Pessoa", back_populates="profile", uselist=False)

    def __repr__(self):
        return f'< Perfil: {self.id}. Nome: {self.nome} >'

    __str__ = __repr__


class Conta(Base):

    __tablename__ = 'tb_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer,ForeignKey('tb_users.id'), primary_key=True)
    nome = Column(String(200), nullable=False)
    saldo = Column(Integer, nullable=False)

    def __repr__(self):
        return f'< Conta: {self.id}. Usuário: {self.user_id}. Nome: {self.nome}. Saldo: R${self.saldo}>'

    __str__ = __repr__

    user = relationship('Pessoa', back_populates='accounts', uselist=True)

    debit_transactions = relationship("Transaction", back_populates="debit_account")
    credit_transactions = relationship("Transaction", back_populates="credit_account")


class Transacao(Base):

    __tablename__ = 'tb_transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # Aqui jás a minha versão genuina de como funciona uma transação
    # id_sender = Column(Integer, ForeignKey('tb_accounts.id'), primary_key=True)
    # id_receiver = Column(Integer, ForeignKey('tb_accounts.id'), primary_key=True)

    # sender_account = relationship('Conta', back_populates='transactions', uselist=False)
    # receiver_account = relationship('Conta', back_populates='transactions', uselist=False)

    debit_account_id = Column(Integer, ForeignKey("tb_financial_accounts.id"), nullable=False)
    credit_account_id = Column(Integer, ForeignKey("tb_financial_accounts.id"), nullable=False)
    valor = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    debit_account = relationship(
        "FinancialAccount",
        back_populates="debit_transactions",
        uselist=False,
        foreign_keys=[debit_account_id]

    )
    credit_account = relationship(
        "FinancialAccount",
        back_populates="credit_transactions",
        uselist=False,
        foreign_keys=[credit_account_id]
    )

    def __repr__(self):
        return f'< Transação: {self.id}. Remetente: . Destinatário: . Hora: {self.hora_transacao}. Valor: R${self.valor} >/'

    __str__ = __repr__
