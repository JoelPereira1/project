from sqlalchemy import create_engine
from settings import DBConfig

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(DBConfig.db_uri)
engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()