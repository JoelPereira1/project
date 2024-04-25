from flask import Blueprint, redirect, render_template, request, url_for, flash
from shop.forms.admin.dashboard import (
    AttributeForm,
    CategoryForm,
    CollectionForm,
    ProductCreateForm,
    ProductForm,
    ProductTypeForm,
    VariantForm,
)
from shop.models.product import (
    Category,
    Collection,
    Product,
    ProductAttribute,
    ProductImage,
    ProductType,
    ProductVariant,
)
from .utils import save_img_file, wrap_partial, item_del

admin_product = Blueprint('admin_product', __name__, url_prefix='/admin')

@admin_product.route('attributes')
def attributes():
  page = request.args.get('page', type=int, default=1)
  pagination = ProductAttribute.query.paginate(page=page, per_page=10)
  props = {
    'id': 'ID',
    'title': 'Title',
    'values_label': 'Value',
    'types_label': 'ProductType'
  }
  context = {
    'title': 'Product Attribute',
    'items': pagination.items,
    'props': props,
    'pagination': pagination,
    'identity': 'attributes',
  }
  return render_template('dashboard/general_list.html', **context)

@admin_product.route('attributes/create', methods=["GET", "POST"])
@admin_product.route('attributes/<int:id>/edit', methods=["GET", "POST"])
def attributes_manage(id=None):
  if id:
    attr = ProductAttribute.get_by_id(id)
    form = AttributeForm(obj=attr)
  else:
    attr = ProductAttribute()
    form = AttributeForm()
  form.product_types_ids.choices = [(p.id, p.title) for p in ProductType.query.all()]
  if form.validate_on_submit():
    attr.title = form.title.data
    attr.save()
    attr.update_types(form.product_types_ids.data)
    attr.update_values(form.values_label.data.split(','))
    flash('Attribute saved.', "success")
    return redirect(url_for('dashboard.attributes'))
  return render_template(
    'general_edit.html', form=form, title='Attribute'
  )

# attribute_del = wrap_partial(item_del, ProductAttribute)
# @admin_product.route('attributes/<int:id>/delete', view_func=attribute_del, methods=["DELETE"])

@admin_product.route('collections')
def collections():
    page = request.args.get("page", type=int, default=1)
    pagination = Collection.query.paginate(page=page, per_page=10)
    props = {
        "id": "ID",
        "title": "Title",
        "created_at": "Created At",
    }
    context = {
        "title": "Product Collection",
        "items": pagination.items,
        "props": props,
        "pagination": pagination,
        "identity": "collections",
    }
    return render_template("dashboard/general_list.html", **context)

@admin_product.route('categories')
def categories():
    page = request.args.get("page", type=int, default=1)
    pagination = Category.query.paginate(page=page, per_page=10)
    props = {
        "id": "ID",
        "title": "Title",
        "parent": "Parent",
        "created_at": "Created At",
    }
    context = {
        "title": "Product Category",
        "items": pagination.items,
        "props": props,
        "pagination": pagination,
        "identity": "categories",
    }
    return render_template("dashboard/general_list.html", **context)

@admin_product.route('collections/create', methods=["GET", "POST"])
@admin_product.route('collections/<int:id>/edit', methods=["GET", "POST"])
def collections_manage(id=None):
    if id:
        collection = Collection.get_by_id(id)
        form = CollectionForm(obj=collection)
    else:
        collection = Collection()
        form = CollectionForm()
    form.products_ids.choices = [(p.id, p.title) for p in Product.query.all()]
    if form.validate_on_submit():
        collection.title = form.title.data
        image = form.bgimg_file.data
        if image:
            collection.background_img = save_img_file(image)
        collection.save()
        collection.update_products(form.products_ids.data)
        flash("Collection saved.", "success")
        return redirect(url_for("dashboard.collections"))
    return render_template("product/collection.html", form=form)

# collection_del = wrap_partial(item_del, Collection)
# @admin_product.route('collections/<int:id>/delete', view_func=collection_del, methods=["DELETE"])

@admin_product.route('categories/create', methods=["GET", "POST"])
@admin_product.route('categories/<int:id>/edit', methods=["GET", "POST"])
def categories_manage(id=None):
    if id:
        category = Category.get_by_id(id)
        form = CategoryForm(obj=category)
    else:
        category = Category()
        form = CategoryForm()
    form.parent_id.choices = [(c.id, c.title) for c in Category.first_level_items()]
    form.parent_id.choices.insert(0, (0, "None"))
    if form.validate_on_submit():
        form.populate_obj(category)
        image = form.bgimg_file.data
        if image:
            category.background_img = save_img_file(image)
        category.save()
        flash("Category saved.", "success")
        return redirect(url_for("dashboard.categories"))
    return render_template("product/category.html", form=form)

# category_del = wrap_partial(item_del, Category)
# @admin_product.route('categories/<int:id>/delete', view_func=category_del, methods=["DELETE"])

@admin_product.route('product_types')
def product_types():
    page = request.args.get("page", type=int, default=1)
    pagination = ProductType.query.paginate(page=page, per_page=10)
    props = {
        "id": "ID",
        "title": "Title",
        "has_variants": "Has Variants",
        "is_shipping_required": "Is Shipping Required",
        "created_at": "Created At",
    }
    context = {
        "title": "Product Type",
        "items": pagination.items,
        "props": props,
        "pagination": pagination,
        "identity": "product_types",
    }
    return render_template("dashboard/general_list.html", **context)

@admin_product.route('product_types/create', methods=["GET", "POST"])
@admin_product.route('product_types/<int:id>/edit', methods=["GET", "POST"])
def product_types_manage(id=None):
    if id:
        product_type = ProductType.get_by_id(id)
        form = ProductTypeForm(obj=product_type)
    else:
        product_type = ProductType()
        form = ProductTypeForm()
    form.product_attributes_ids.choices = [
        (p.id, p.title) for p in ProductAttribute.query.all()
    ]
    if form.validate_on_submit():
        tmp_pa = form.product_attributes_ids.data
        del form.product_attributes_ids
        form.populate_obj(product_type)
        product_type.save()
        product_type.update_product_attr(tmp_pa)
        flash("Product type saved.", "success")
        return redirect(url_for("dashboard.product_types"))
    return render_template(
        "general_edit.html", form=form, title="Product Type"
    )

# product_type_del = wrap_partial(item_del, ProductType)
# @admin_product.route('product_types/<int:id>/delete', view_func=product_type_del, methods=["DELETE"])

@admin_product.route('products')
def products():
    page = request.args.get("page", type=int, default=1)
    query = Product.query

    on_sale = request.args.get("sale", type=int)
    if on_sale is not None:
        query = query.filter_by(on_sale=on_sale)
    category = request.args.get("category", type=int)
    if category:
        query = query.filter_by(category_id=category)
    title = request.args.get("title", type=str)
    if title:
        query = query.filter(Product.title.like(f"%{title}%"))
    created_at = request.args.get("created_at", type=str)
    if created_at:
        query = query.filter(Product.created_at >= created_at)
    ended_at = request.args.get("ended_at", type=str)
    if ended_at:
        query = query.filter(Product.created_at <= ended_at)

    pagination = query.paginate(page=page, per_page=10)
    props = {
        "id": "ID",
        "title": "Title",
        "on_sale_human": "On Sale",
        "sold_count": "Sold Count",
        "price_human": "Price",
        "category": "Category",
    }
    context = {
        "items": pagination.items,
        "props": props,
        "pagination": pagination,
        "categories": Category.query.all(),
    }
    return render_template("product/list.html", **context)

@admin_product.route('products/<int:id>')
def product_detail(id):
    product = Product.get_by_id(id)
    return render_template("product/detail.html", product=product)

@admin_product.route('products/<int:id>/edit', methods=['GET', 'POST'])
@admin_product.route('products/create/step2', methods=['GET', 'POST'])
def product_manage(id=None):
    if id:
        product = Product.get_by_id(id)
        form = ProductForm(obj=product)
        product_type = product.product_type
    else:
        form = ProductForm()
        product_type_id = request.args.get("product_type_id", 1, int)
        product_type = ProductType.get_by_id(product_type_id)
        product = Product(product_type_id=product_type_id)
    form.category_id.choices = [(c.id, c.title) for c in Category.query.all()]
    if form.validate_on_submit():
        product.update_images(form.images.data)
        product.update_attributes(form.attributes.data)
        del form.images
        del form.attributes
        form.populate_obj(product)
        product.save()
        upload_imgs = request.files.getlist("new_images")
        for img in upload_imgs:
            # request.files.getlist always not return empty, even not upload files
            if not img.filename:
                continue
            ProductImage.create(
                image=save_img_file(img),
                product_id=product.id,
            )
        flash("Product saved.", "success")
        return redirect(url_for("dashboard.product_detail", id=product.id))
    context = {"form": form, "product_type": product_type}
    return render_template("product/product.html", **context)

# product_del = wrap_partial(item_del, Product)
# @admin_product.route('products/<int:id>/delete', view_func=product_del, methods=['DELETE'])

@admin_product.route('products/create/step1', methods=['GET', 'POST'])
def product_create_step1():
    form = ProductCreateForm()
    form.product_type_id.choices = [(p.id, p.title) for p in ProductType.query.all()]
    if form.validate_on_submit():
        return redirect(
            url_for(
                "dashboard.product_manage",
                product_type_id=form.product_type_id.data,
            )
        )
    return render_template(
        "general_edit.html", form=form, title="Product Step 1"
    )

@admin_product.route('products/variant/create', methods=['GET', 'POST'])
@admin_product.route('products/variant/<int:id>/edit', methods=['GET', 'POST'])
def variant_manage(id=None):
    if id:
        variant = ProductVariant.get_by_id(id)
        form = VariantForm(obj=variant)
    else:
        variant = ProductVariant()
        form = VariantForm()
    if form.validate_on_submit():
        form.populate_obj(variant)
        product_id = request.args.get("product_id")
        if product_id:
            variant.product_id = product_id
        variant.sku = str(variant.product_id) + "-" + str(form.sku_id.data)
        variant.save()
        flash("Variant saved.", "success")
        return redirect(url_for("dashboard.product_detail", id=variant.product_id))
    return render_template(
        "general_edit.html", form=form, title="Variant"
    )

# variant_del = wrap_partial(item_del, ProductVariant)
# @admin_product.route('variants/<int:id>/delete', view_func=variant_del, methods=['DELETE'])