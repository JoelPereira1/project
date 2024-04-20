import random
import smtplib
import string
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import current_user, login_required, login_user, logout_user

from shop.models.checkout import Cart
from shop.forms.add_cart import AddCartForm
from shop.models.product import Category, Product, ProductCollection, ProductVariant

product = Blueprint('product', __name__)

@product.route('/product/<int:id>')
def show(id, form=None):
    product = Product.get_by_id(id)
    if not form:
        form = AddCartForm(request.form, product=product)
    return render_template("products/details.html", product=product, form=form)

@login_required
@product.route('/product/api/variant_price/<int:id>', methods=["GET", "POST"])
def product_add_to_cart(id):
    """this method return to the show method and use a form instance for display validater errors"""
    product = Product.get_by_id(id)
    form = AddCartForm(request.form, product=product)

    if form.validate_on_submit():
      Cart.add_to_currentuser_cart(form.quantity.data, form.variant.data)
    return redirect(url_for("product.show", id=id))

@product.route('/product/<int:id>/add', methods=["GET", "POST"])
def variant_price(id):
    variant = ProductVariant.get_by_id(id)
    return jsonify({"price": float(variant.price), "stock": variant.stock})

@product.route('/product/category/<int:id>', methods=["GET", "POST"])
def show_category(id):
    page = request.args.get("page", 1, type=int)
    ctx = Category.get_product_by_category(id, page)
    return render_template("category/index.html", **ctx)

@product.route('/product/collection/<int:id>', methods=["GET", "POST"])
def show_collection(id):
    page = request.args.get("page", 1, type=int)
    ctx = ProductCollection.get_product_by_collection(id, page)
    return render_template("category/index.html", **ctx)

