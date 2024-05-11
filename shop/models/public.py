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


from elasticsearch.exceptions import ConflictError, NotFoundError
from elasticsearch.helpers import parallel_bulk
from elasticsearch_dsl import Boolean, Date, Document, Float, Integer, Text
from elasticsearch_dsl.connections import connections
from flask_sqlalchemy.pagination import Pagination

def get_item_data(item):
  return {
    "meta": {"id": item.id},
    "title": item.title,
    "description": item.description,
    "first_img": item.first_img,
    "basic_price": item.basic_price,
    "price": item.price,
    "on_sale": item.on_sale,
    "is_discounted": item.is_discounted,
  }

class Item(Document):
    id = Integer()
    title = Text()
    description = Text()
    first_img = Text()
    basic_price = Float()
    price = Float()
    on_sale = Boolean()
    is_discounted = Boolean()
    created_at = Date()

    class Index:
      name = "flaskshop"

    @classmethod
    def add(cls, item):
      obj = cls(**get_item_data(item))
      obj.save()
      return obj

    @classmethod
    def update_item(cls, item):
      try:
        obj = cls.get(item.id)
      except NotFoundError:
        return cls.add(item)

      kw = get_item_data(item)
      try:
        obj.update(**kw)
      except ConflictError:
        obj = cls.get(item.id)
        obj.update(**kw)
      return True

    @classmethod
    def delete(cls, item):
      rs = cls.get(item.id)
      if rs:
        super(cls, rs).delete()
        return True
      return False

    @classmethod
    def bulk_update(cls, items, chunk_size=5000, op_type="update", **kwargs):
      index = cls._index._name
      _type = cls._doc_type.name
      obj = [
        {
          "_op_type": op_type,
          "_id": f"{doc.id}",
          "_index": index,
          "_type": _type,
          "_source": get_item_data(doc),
        }
        for doc in items
      ]
      client = cls.get_es()
      rs = list(parallel_bulk(client, obj, chunk_size=chunk_size, **kwargs))
      return rs

    @classmethod
    def get_es(cls):
      return connections.get_connection()

    @classmethod
    def new_search(cls, query, page, order_by=None, per_page=16):
      s = cls.search()
      s = s.query("multi_match", query=query, fields=SERACH_FIELDS)
      start = (page - 1) * per_page
      s = s.extra(**{"from": start, "size": per_page})
      s = s if order_by is None else s.sort(order_by)
      rs = s.execute()
      return CustomPagination(page, per_page, rs=rs, query=query)

class CustomPagination(Pagination):
  def __init__(self, page, per_page, **kwargs):
    self.rs = kwargs.get('rs')
    self.query = kwargs.get('query')
    super().__init__(page, per_page, **kwargs)

  def _query_items(self):
    for item in self.rs:
      item.id = item.meta.id
      item.first_img = ProductImage.query.filter(ProductImage.product_id == item.id).first()
    return self.rs

  def _query_count(self):
    return self.rs.hits.total.value