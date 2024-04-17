
from sqlalchemy.orm import relationship
from shop.database import Column, Model, db


class ShoppingCart(Model):
  __tablename__ = "cart"
  id = Column(db.Integer(), primary_key=True)
  user_id = Column(db.Integer(), nullable=False)
  product_id = Column(db.Integer(), nullable=False)
  quantity = Column(db.Integer(), nullable=False)
  # product = relationship('Product', back_populates='shopping_carts')