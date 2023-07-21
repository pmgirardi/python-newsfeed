from flask import Flask

from app.routes import home, dashboard

def create_app(test_config=None):
    # set up app config
    # The app should serve any static resources from the root directory and not from the default /static directory
  app = Flask(__name__, static_url_path='/')
    # Trailing slashes are optional (meaning that /dashboard and /dashboard/ load the same route)
  app.url_map.strict_slashes = False
    # The app should use the key called 'super_secret_key' when creating server-side sessions
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
    # the decorator @app.route('/hello') turns the hello() function into a route
  @app.route('/hello')
  def hello():
    # The function's return becomes the route's response
    return 'hello world'

# register the home and dashboard blueprint
  app.register_blueprint(home)
  app.register_blueprint(dashboard)


  return app