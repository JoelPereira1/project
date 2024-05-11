from .public import public as public_blueprint
from .product import product as product_blueprint
from .auth import auth as auth_blueprint
from .order import order as order_blueprint
from .checkout import checkout as checkout_blueprint
from .account import account as account_blueprint

from .challenge import challenge as challenge_blueprint
from .community import community as community_blueprint

from .admin.dashboard import dashboard as admin_dashboard_blueprint
from .admin.order import admin_order as admin_order_blueprint
from .admin.product import admin_product as admin_product_blueprint
def blueprint_manager(app):
  # Registering Shop blueprints
  # app.register_blueprint(auth_blueprint, template_folder='templates/auth')
  # app.register_blueprint(main_blueprint, template_folder='templates/auth')
  app.register_blueprint(public_blueprint)
  app.register_blueprint(account_blueprint)
  app.register_blueprint(product_blueprint)
  app.register_blueprint(auth_blueprint)
  app.register_blueprint(order_blueprint)
  app.register_blueprint(checkout_blueprint)
  # Registering Challenges blueprints
  app.register_blueprint(challenge_blueprint)
  # Registering Community blueprints
  app.register_blueprint(community_blueprint)
  # Registering Admin blueprints
  app.register_blueprint(admin_dashboard_blueprint)
  app.register_blueprint(admin_order_blueprint)
  app.register_blueprint(admin_product_blueprint)

