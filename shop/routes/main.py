from .admin.dashboard import dashboard as admin_dashboard_blueprint
from .admin.order import admin_order as admin_order_blueprint
from .public import public as public_blueprint
from .product import product as product_blueprint
from .auth import auth as auth_blueprint
from .order import order as order_blueprint
from .checkout import checkout as checkout_blueprint
from .account import account as account_blueprint

def blueprint_manager(app):
  # app.pluggy.hook.flaskshop_load_blueprints(app=app)
  # Registering blueprints
  # app.register_blueprint(auth_blueprint, template_folder='templates/auth')
  # app.register_blueprint(main_blueprint, template_folder='templates/auth')
  app.register_blueprint(public_blueprint)
  app.register_blueprint(account_blueprint)
  app.register_blueprint(product_blueprint)
  app.register_blueprint(auth_blueprint)
  app.register_blueprint(order_blueprint)
  app.register_blueprint(checkout_blueprint)
  # Admin routes
  app.register_blueprint(admin_dashboard_blueprint)
  app.register_blueprint(admin_order_blueprint)

