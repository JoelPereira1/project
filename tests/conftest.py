# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
from pathlib import Path

import pytest
from shop.app import create_app
from shop.corelib.utils import jinja_global_varibles
from tests.settings import Config

@pytest.fixture
def app():
  """An application for the tests."""
  _app = create_app(Config)
  jinja_global_varibles(_app)
  ctx = _app.test_request_context()
  ctx.push()
  yield _app
  ctx.pop()

@pytest.fixture
def client(app):
  return app.test_client()

@pytest.fixture()
def runner(app):
  return app.test_cli_runner()
