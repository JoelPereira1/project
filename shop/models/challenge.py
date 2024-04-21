# models/product.py
import itertools
from flask import current_app, request, url_for
from sqlalchemy import desc
from sqlalchemy.ext.mutable import MutableDict

from shop.corelib.db import PropsItem, rdb
from shop.database import Column, Model, db
from settings import Config

class ChallangeImage(Model):
  __tablename__ = "challange_image"
  image = Column(db.String(255))
  description = Column(db.Text())
  chat_id = Column(db.Integer())

  def __str__(self):
    return url_for("static", filename=self.image, _external=True)