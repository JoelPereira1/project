# public.py
import os
import random
import smtplib
import string
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, current_app, send_from_directory
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf.csrf import CSRFProtect
from shop.extensions import login_manager
from shop.models.user import User
from shop.models.product import Product

csrf_protect = CSRFProtect()
public = Blueprint('public', __name__)

@login_manager.user_loader
def load_user(user_id):
  """Load user by ID."""
  return User.get_by_id(int(user_id))

@public.route('/')
def home():
  products = Product.get_featured_product()
  return render_template("public/home.html", products=products)

@public.route('/public/style')
def style():
  return render_template("public/style_guide.html")

@public.route('/public/favicon.ico')
def favicon():
  return send_from_directory("static", "favicon-32x32.png")

@public.route('/public/search')
def search():
    query = request.args.get("q", "")
    page = request.args.get("page", default=1, type=int)
    if current_app.config["USE_ES"]:
        pagination = Product.new_search(query, page)
    else:
        pagination = Product.query.filter(Product.title.ilike(f"%{query}%")).paginate(
            page=page, per_page=10
        )
    return render_template(
        "public/search_result.html",
        products=pagination.items,
        query=query,
        pagination=pagination,
    )

# @public.route('/public/page/<identity>')
# def show_page(identity):
#     page = Page.get_by_identity(identity)
#     return render_template("public/page.html", page=page)

