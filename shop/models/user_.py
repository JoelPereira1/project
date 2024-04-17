# models/user.py
from functools import reduce
from operator import or_
from sqlalchemy.ext.hybrid import hybrid_property
from shop.extensions import bcrypt
# # from flask_login import UserMixin
from shop.database.engine import Base, engine, session


from functools import reduce
from operator import or_

from flask_login import UserMixin
from libgravatar import Gravatar
from sqlalchemy.ext.hybrid import hybrid_property

from .utils import Permission
from database.props import Column, Model, db
from shop.extensions import bcrypt


class User(Model, UserMixin):
    __tablename__ = "account_user"
    username = Column(db.String(80), unique=True, nullable=False, comment="user`s name")
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    _password = db.Column(db.String(255), nullable=False)
    nick_name = Column(db.String(255))
    is_active = Column(db.Boolean(), default=False)
    open_id = Column(db.String(80), index=True)
    session_key = Column(db.String(80), index=True)

    def __init__(self, username, email, password, **kwargs):
      super().__init__(username=username, email=email, password=password, **kwargs)

    def __str__(self):
      return self.username

    @hybrid_property
    def password(self):
      return self._password

    @password.setter
    def password(self, value):
      self._password = bcrypt.generate_password_hash(value).decode("UTF-8")

    def check_password(self, value):
      """Check password."""
      return bcrypt.check_password_hash(self.password.encode("utf-8"), value)

    @property
    def addresses(self):
      return UserAddress.query.filter_by(user_id=self.id).all()

    @property
    def is_active_human(self):
      return "Y" if self.is_active else "N"

    @property
    def roles(self):
      at_ids = (
        UserRole.query.with_entities(UserRole.role_id)
        .filter_by(user_id=self.id)
        .all()
      )
      return Role.query.filter(Role.id.in_(id for id, in at_ids)).all()

    def delete(self):
      for addr in self.addresses:
        addr.delete()
      return super().delete()

    def can(self, permissions):
      if not self.roles:
        return False
      all_perms = reduce(or_, map(lambda x: x.permissions, self.roles))
      return all_perms >= permissions

    def can_admin(self):
      return self.can(Permission.ADMINISTER)

    def can_edit(self):
      return self.can(Permission.EDITOR)

    def can_op(self):
      return self.can(Permission.OPERATOR)

class UserAddress(Base):
    __tablename__ = "account_address"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer())
    province = Column(String(255))
    city = Column(String(255))
    district = Column(String(255))
    address = Column(String(255))
    contact_name = Column(String(255))
    contact_phone = Column(String(80))

    @property
    def full_address(self):
        return (
            f"{self.province}<br>{self.city}<br>{self.district}<br>"
            f"{self.address}<br>{self.contact_name}<br>{self.contact_phone}"
        )

    @hybrid_property
    def user(self):
        return User.get_by_id(self.user_id)

    def __str__(self):
        return self.full_address

class Role(Base):
    __tablename__ = "account_role"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    permissions = Column(Integer(), default=Permission.LOGIN)

class UserRole(Base):
    __tablename__ = "user_role"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer())
    role_id = Column(Integer())


# new_user = User(name='John Doe', email='[john.doe@example.com](mailto:john.doe@example.com)')
# session.add(new_user)
# session.commit()