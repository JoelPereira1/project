from flask import Flask
from . import commands
from settings import Config, DBConfig
from minio import Minio
from shop.extensions import (
  bcrypt,
  bootstrap,
  csrf_protect,
  db,
  login_manager,
  migrate
)
from shop.corelib.utils import jinja_global_varibles
import shop.corelib.rethinkdb.initdb as RethinkBD

def create_app(config_object=Config):
  app = Flask(__name__.split(".")[0])
  app.config.from_object(config_object)
  register_extensions(app)
  register_blueprints(app)
  register_commands(app)
  register_minio(app)

  return app

def register_extensions(app):
  db.init_app(app)
  migrate.init_app(app, db)
  RethinkBD.init_database(DBConfig.rethinkdb_uri, DBConfig.rethinkdb_port, DBConfig.rethinkdb, DBConfig.rethinkdb_pwd, DBConfig.rethinkdb_tbl)
  bcrypt.init_app(app)
  csrf_protect.init_app(app)
  login_manager.init_app(app)
  bootstrap.init_app(app)
  jinja_global_varibles(app)

def register_blueprints(app):
  from .routes.main import blueprint_manager
  blueprint_manager(app)

def register_minio(app):
  Minio(Config.MINIO_API_URI, access_key=Config.MINIO_ACCESS_KEY, secret_key=Config.MINIO_SECRET_KEY, secure=False)
  # Create client with custom HTTP client using proxy server.
  # import urllib3
  # client = Minio(
  #     Config.MINIO_API_URI,
  #     access_key=Config.MINIO_ACCESS_KEY,
  #     secret_key=Config.MINIO_SECRET_KEY,
  #     secure=False,
  #     http_client=urllib3.ProxyManager(
  #         "https://PROXYSERVER:PROXYPORT/",
  #         timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
  #         cert_reqs="CERT_REQUIRED",
  #         retries=urllib3.Retry(
  #             total=5,
  #             backoff_factor=0.2,
  #             status_forcelist=[500, 502, 503, 504],
  #         ),
  #     ),
  # )

def register_commands(app):
  """Register Click commands."""
  app.cli.add_command(commands.test)
  app.cli.add_command(commands.lint)
  app.cli.add_command(commands.clean)
  app.cli.add_command(commands.urls)
  app.cli.add_command(commands.createdb)
  app.cli.add_command(commands.seed)
  app.cli.add_command(commands.reindex)