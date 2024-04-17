"""The app module, containing the app factory function."""
from shop.app import create_app

app = create_app()

if __name__ == 'app':
  app.run(host="0.0.0.0", debug=True, reload=True, port=8088)