# models/models.py
from functools import reduce
from operator import or_
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt
from .utils import Permission
from shop.database.engine import session, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

class Order(Base):
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
  product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
  quantity = Column(Integer, nullable=False)
  total_price = Column(Float, nullable=False)
  # product = relationship('Product', back_populates='orders')