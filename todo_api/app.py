from flask import Flask


def create_app(settings_override=None):
    """
    Create a Flask application using the factory pattern

    :return: Flask application instance
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('config.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    register_extensions(app)

    @app.route('/')
    def index():
        return "Hello World"

    return app


def register_extensions(app: Flask):
    """
    Register one or more flask extensions. Mutates the flask app.

    :param app: Flask application instance.
    :return: None
    """
    from todo_api.extensions import db

    db.init_app(app)
