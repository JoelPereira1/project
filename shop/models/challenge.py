# models/product.py
import itertools
from flask import current_app, request, url_for
from sqlalchemy import desc
from sqlalchemy.ext.mutable import MutableDict

from shop.corelib.db import PropsItem, rdb
from shop.database import Column, Model, db
from settings import Config

class Challenge(Model):
  __tablename__ = "challenge"
  chat_id = Column(db.Integer())
  user_id = Column(db.Integer())
  rating = Column(db.DECIMAL(8, 2), default=5.0)

  @property
  def images(self):
    return ChallengeImage.query.filter(ChallengeImage.challenge_id == self.id).all()

  @property
  def first_img(self):
    if self.images:
        return str(self.images[0])
    return ""

@classmethod
def update_images(self, new_images):
    origin_ids = (
      ChallengeImage.query.with_entities(ChallengeImage.id)
      .filter_by(challenge_id=self.id)
      .all()
    )
    origin_ids = set(i for i, in origin_ids)
    new_images = set(int(i) for i in new_images)
    need_del = origin_ids - new_images
    for id in need_del:
      ChallengeImage.get_by_id(id).delete(commit=False)
    db.session.commit()

class ChallengeImage(Model):
  __tablename__ = "challenge_image"
  image = Column(db.String(255))
  description = Column(db.Text())
  challenge_id = Column(db.Integer())

  def __str__(self):
    return url_for("static", filename=self.image, _external=True)

  @classmethod
  def get_challenge_images(challenge_id):
    return ChallengeImage.query.filter_by(challenge_id=challenge_id).all()