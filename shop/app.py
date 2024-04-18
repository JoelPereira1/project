import sys
from flask import Flask, render_template
from . import commands
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
from settings import Config
from shop.extensions import (
  bcrypt,
  bootstrap,
  csrf_protect,
  db,
  login_manager,
  migrate
)

from shop.corelib.utils import jinja_global_varibles

def create_app(config_object=Config):
  app = Flask(__name__.split(".")[0])
  app.config.from_object(config_object)
  register_extensions(app)
  register_blueprints(app)
  register_commands(app)
  jinja_global_varibles(app)

  return app

# def register_extensions(app):
#   db.init_app(app)
#   migrate.init_app(app, db)
#   login_manager.init_app(app)

#   login = LoginManager(app)
#   login.login_view = 'auth.login'

def register_extensions(app):
  bcrypt.init_app(app)
  db.init_app(app)
  csrf_protect.init_app(app)
  login_manager.init_app(app)
  migrate.init_app(app, db)
  bootstrap.init_app(app)
  jinja_global_varibles(app)

def register_blueprints(app):
  from .routes.main import blueprint_manager
  blueprint_manager(app)

def register_commands(app):
  """Register Click commands."""
  app.cli.add_command(commands.test)
  app.cli.add_command(commands.lint)
  app.cli.add_command(commands.clean)
  app.cli.add_command(commands.urls)
  app.cli.add_command(commands.createdb)
  app.cli.add_command(commands.seed)
  app.cli.add_command(commands.reindex)