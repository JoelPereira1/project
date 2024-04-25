# -*- coding: utf-8 -*-
"""Test configs."""
from shop.app import create_app
from settings import Config

def test_test_config():
	"""Development config."""
	app = create_app(Config)
	assert app.config["ENV"] == "test"
	# assert app.config["FLASK_DEBUG"] is True

