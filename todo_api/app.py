from flask import Flask


def create_app():
    """
    Create a Flask application using the factory pattern

    :return: Flask application instance
    """
    app = Flask(__name__)

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
