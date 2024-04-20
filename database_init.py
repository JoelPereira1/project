# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from settings import DBConfig
# from shop.models.user import User

# # Replace these values with your own PostgreSQL connection details
# DATABASE_URI = DBConfig.db_uri

# engine = create_engine(DATABASE_URI)
# Session = sessionmaker(bind=engine)
# Base = declarative_base()


# # Create the database and tables
# Base.metadata.create_all(engine)

# # Insert some sample data
# # session = Session()
# # user = User(username='joel', email='joel@example.com', password='password')
# # session.add(user)
# # session.commit()



# from shop import app
# from shop.extensions import db
# from flask_migrate import Migrate
# # from shop.models.user import User
# from settings import DBConfig
# from flask_script import Manager

# # Initialize Flask-Migrate
# migrate = Migrate()
# manager = Manager()

# migrate.init_app(app, db)
# manager.init_app(app)

# def create_tables():
#   with app.app_context():
#     db.create_all()

# def migrate_database():
#   with app.app_context():
#     migrate.init()
#     migrate.migrate()
#     migrate.upgrade()

# if __name__ == '__main__':
#   manager.run()
#   create_tables()
#   migrate_database()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config, DBConfig
from alembic import command
from alembic.config import Config as AlembicConfig
import psycopg

def create_app():
  # Initialize Flask app
  app = Flask(__name__)
  # Load configuration from your Flask app configuration
  app.config.from_object(Config)
  return app

def setup_database(app):
  # Initialize SQLAlchemy
  db = SQLAlchemy(app)
  return db

def setup_migrate(app, db):
  # Initialize Flask-Migrate
  migrate = Migrate(app, db)
  return migrate

def setup():
  # Initialize app, database, and migrations
  app = create_app()
  db = setup_database(app)
  migrate = setup_migrate(app, db)
  return app, db, migrate

def create_database():
  # Create the PostgreSQL database if it does not exist
  conn = psycopg.connect(
    dbname='postgres',
    user = DBConfig.user,
    host = DBConfig.host,
    password = DBConfig.passwd
  )
  conn.autocommit = True
  cursor = conn.cursor()
  cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = '%s'"%(DBConfig.db_name,))
  exists = cursor.fetchone()
  if not exists:
    cursor.execute("CREATE DATABASE %s"%(DBConfig.db_name))

def run_migrations(app):
  # Run migrations to ensure the database schema is up-to-date
  Migrate(compare_type=True)
  # alembic_cfg = AlembicConfig("alembic.ini")
  # command.upgrade(alembic_cfg, "head")

def replace_database_uri(database_uri):
  # Read the contents of the file
  with open('alembic.ini', 'r') as file:
    lines = file.readlines()

  # Find the index of the line containing 'sqlalchemy.url'
  target_index = None
  for i, line in enumerate(lines):
    if 'sqlalchemy.url' in line:
      target_index = i
      break

  # If the line containing 'sqlalchemy.url' is found, replace it with the new database URI
  if target_index is not None:
    lines[target_index] = f'sqlalchemy.url = {database_uri}\n'

    # Write the modified lines back to the file
    with open('alembic.ini', 'w') as file:
      file.writelines(lines)

if __name__ == '__main__':
  # change alembic.ini file
  replace_database_uri(DBConfig.db_uri)

  # Create the database
  create_database()

  # Initialize the app, database, and migrations
  app, db, migrate = setup()

  # # Run migrations
  run_migrations(app)

  # undo alembic.ini file
  replace_database_uri('')
