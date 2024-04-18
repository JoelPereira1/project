
# from flask_login import LoginManager, UserMixin

from datetime import datetime, timezone

import arrow
from flask import abort, request, session
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model, DefaultMeta, _QueryProperty
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import Column, DateTime, Integer, event
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base
from .corelib.db import PropsMixin, PropsItem

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
migrate = Migrate(compare_type=True)
bootstrap = Bootstrap()

class BaseModel(PropsMixin, Model):
  __table_args__ = {"extend_existing": True}
  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime, default=datetime.now(timezone.utc))
  updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

  def __repr__(self):
    return f"<{self.__class__.__name__} id:{self.id}>"

  def get_uuid(self):
    return f"/bran/{self.__class__.__name__}/{self.id}"

  @classmethod
  def get(cls, id):
    return cls.query.get(id)

  @classmethod
  def get_or_404(cls, id):
    rv = cls.get(id)
    if rv is None:
      abort(404)
    return rv

  @classmethod
  def get_multi(cls, ids):
    return [cls.get(id) for id in ids]

  def url(self):
    return f"/{self.__class__.__name__.lower()}/{self.id}"

  def to_dict(self):
    columns = self.__table__.columns.keys() + ["kind"]
    return {key: getattr(self, key, None) for key in columns}

  @property
  def created_at_human(self):
    return arrow.get(self.created_at).humanize()

class BindDBPropertyMixin:
  def __init__(cls, name, bases, d):
    super().__init__(name, bases, d)
    db_columns = []
    for k, v in d.items():
      if isinstance(v, PropsItem):
        db_columns.append((k, v.default))
    setattr(cls, "_db_columns", db_columns)

class CombinedMeta(BindDBPropertyMixin, DefaultMeta):
  pass

class UnLockedAlchemy(SQLAlchemy):
  def _make_declarative_base(self, model_class, disable_autonaming: bool = False, ):
    metadata = self._make_metadata(None)
    if not isinstance(model_class, DeclarativeMeta):
      model = declarative_base(
        cls=model_class, name="Model", metadata=metadata, metaclass=CombinedMeta
      )
    else:
      model = model_class

    if None not in self.metadatas:
      # Use the model's metadata as the default metadata.
      model.metadata.info["bind_key"] = None
      self.metadatas[None] = model.metadata
    else:
      # Use the passed in default metadata as the model's metadata.
      model.metadata = self.metadatas[None]

    model.query_class = self.Query
    model.query = _QueryProperty()
    model.__fsa__ = self
    return model

db = UnLockedAlchemy(model_class=BaseModel)
