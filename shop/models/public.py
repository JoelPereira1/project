from flask import url_for
from shop.corelib.db import PropsItem
from shop.database import Column, Model, db
from settings import Config

class MenuItem(Model):
    __tablename__ = "public_menuitem"
    title = Column(db.String(255), nullable=False)
    order = Column(db.Integer(), default=0)
    url_ = Column("url", db.String(255))
    category_id = Column(db.Integer(), default=0)
    collection_id = Column(db.Integer(), default=0)
    position = Column(db.Integer(), default=0)
    page_id = Column(db.Integer(), default=0)
    parent_id = Column(db.Integer(), default=0)

    def __str__(self):
        return self.title

    @property
    def parent(self):
        return MenuItem.get_by_id(self.parent_id)

    @property
    def children(self):
        return (
            MenuItem.query.filter(MenuItem.parent_id == self.id).order_by("order").all()
        )

    @property
    def linked_object_url(self):
        if self.page_id:
            return Page.get_by_id(self.page_id).url
        elif self.category_id:
            return url_for("product.show_category", id=self.category_id)
        elif self.collection_id:
            return url_for("product.show_collection", id=self.collection_id)

    @property
    def url(self):
        return self.url_ if self.url_ else self.linked_object_url

    @classmethod
    def first_level_items(cls):
        return cls.query.filter(cls.parent_id == 0).order_by("order").all()


class Page(Model):
    __tablename__ = "public_page"
    title = Column(db.String(255), nullable=False)
    slug = Column(db.String(255))
    content = Column(db.Text())
    is_visible = Column(db.Boolean(), default=True)
    if Config.USE_REDIS:
        content = PropsItem("content", "")

    def get_absolute_url(self):
        identity = self.slug or self.id
        return url_for("public.show_page", identity=identity)

    @classmethod
    def get_by_identity(cls, identity):
        try:
            int(identity)
        except ValueError:
            return Page.query.filter(Page.slug == identity).first()
        return Page.get_by_id(identity)

    @property
    def url(self):
        return self.get_absolute_url()

    def __str__(self):
        return self.title