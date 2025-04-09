from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


# ========== Customer ==========

class CustomerBase(BaseModel):
    name: str
    phone: Optional[str] = None

class CustomerCreate(CustomerBase):
    password: str
    photo: Optional[str] = None

class CustomerOut(CustomerBase):
    id: int
    photo: Optional[str] = None

    class Config:
        orm_mode = True


# ========== Product ==========

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True


# ========== FactorItem ==========

class FactorItemBase(BaseModel):
    product_id: int
    no: int

class FactorItemCreate(FactorItemBase):
    pass

class FactorItemOut(FactorItemBase):
    id: int
    product: ProductOut  # اطلاعات محصول هم بیاد

    class Config:
        orm_mode = True


# ========== Factor ==========

class FactorBase(BaseModel):
    customer_id: int

class FactorCreate(FactorBase):
    items: List[FactorItemCreate]

class FactorOut(FactorBase):
    id: int
    date: datetime
    items: List[FactorItemOut]
    customer: CustomerOut

    class Config:
        orm_mode = True


# ========== Log ==========

class LogBase(BaseModel):
    action: str
    detail: Optional[str] = None
    jalalidate: Optional[str] = None

class LogCreate(LogBase):
    user_id: Optional[int] = None

class LogOut(LogBase):
    id: int
    timestamp: datetime
    user: Optional[CustomerOut]

    class Config:
        orm_mode = True
