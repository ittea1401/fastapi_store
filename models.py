from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    photo = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)

    factors = relationship("Factor", back_populates="customer")
    logs = relationship("Log", back_populates="user")


class Factor(Base):
    __tablename__ = 'factors'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    date = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="factors")
    items = relationship("FactorItem", back_populates="factor")


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    items = relationship("FactorItem", back_populates="product")


class FactorItem(Base):
    __tablename__ = 'factor_items'

    id = Column(Integer, primary_key=True, index=True)
    factor_id = Column(Integer, ForeignKey('factors.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    no = Column(Integer, default=1)

    factor = relationship("Factor", back_populates="items")
    product = relationship("Product", back_populates="items")


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    jalalidate = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    action = Column(String, nullable=False)
    detail = Column(String, nullable=True)

    user = relationship("Customer", back_populates="logs")
