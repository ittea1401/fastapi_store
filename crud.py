from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ========== Customer ==========

def create_customer(db: Session, customer: schemas.CustomerCreate):
    hashed_password = pwd_context.hash(customer.password)
    db_customer = models.Customer(
        name=customer.name,
        phone=customer.phone,
        photo=customer.photo,
        password_hash=hashed_password
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


# ========== Product ==========

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ========== Factor ==========

def create_factor(db: Session, factor_data: schemas.FactorCreate):
    # اول فاکتور رو بساز
    db_factor = models.Factor(
        customer_id=factor_data.customer_id,
        date=datetime.utcnow()
    )
    db.add(db_factor)
    db.commit()
    db.refresh(db_factor)

    # حالا آیتم‌ها رو اضافه کن
    for item in factor_data.items:
        db_item = models.FactorItem(
            factor_id=db_factor.id,
            product_id=item.product_id,
            no=item.no
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_factor)
    return db_factor


def get_factor_by_id(db: Session, factor_id: int):
    return db.query(models.Factor).filter(models.Factor.id == factor_id).first()


# ========== FactorItem ==========

def get_items_by_factor_id(db: Session, factor_id: int):
    return db.query(models.FactorItem).filter(models.FactorItem.factor_id == factor_id).all()


# ========== Log ==========

def create_log(db: Session, log_data: schemas.LogCreate):
    db_log = models.Log(
        user_id=log_data.user_id,
        action=log_data.action,
        detail=log_data.detail,
        jalalidate=log_data.jalalidate,
        timestamp=datetime.utcnow()
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_logs_by_user(db: Session, user_id: int):
    return db.query(models.Log).filter(models.Log.user_id == user_id).order_by(models.Log.timestamp.desc()).all()
