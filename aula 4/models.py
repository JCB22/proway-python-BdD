from database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    profile = relationship("UserProfile", back_populates="user", uselist=False)

    def __repr__(self):
        return f'<User({self.id}, {self.email})>'

    __str__ = __repr__


class UserProfile(Base):

    __tablename__ = 'tb_users_profiles'

    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    birth_date = Column(DateTime, nullable=True)

    user = relationship('User', back_populates="profile", uselist=False)

    def __repr__(self):
        return f"<User Profile({self.id}, {self.first_name}, {self.last_name}>"

    __str__ = __repr__


class Product(Base):

    __tablename__ = 'tb_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Order({self.id}, {self.name}, {self.price}>"

    __str__ = __repr__


class Order(Base):

    __tablename__ = 'tb_orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('tb_users.id'), primary_key=True)
    order_date = Column(DateTime, nullable=False)
    desc = Column(String(200), nullable=True)

    def __repr__(self):
        return f"<Order({self.id}, User: {self.id_user}, {self.order_date}>"

    __str__ = __repr__


class OrderDetail(Base):

    __tablename__ = 'tb_order_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_product = Column(Integer, ForeignKey('tb_products.id'), primary_key=True)
    id_order = Column(Integer, ForeignKey('tb_orders.id'), nullable=False)
    quant = Column(Float, nullable=False)
    desc = Column(String(200), nullable=True)

    def __repr__(self):
        return f"<Order({self.id}, User: {self.id_user}, Preço: {self.price}>"

    __str__ = __repr__
