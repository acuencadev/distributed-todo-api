from flask import Flask


__app = Flask(__name__, instance_relative_config=True)


def create_app(settings_override=None):
    """
    Create a Flask application using the factory pattern

    :return: Flask application instance
    """
    global __app

    __app.config.from_object('config.settings')
    __app.config.from_pyfile('config.py', silent=True)

    if settings_override:
        __app.config.update(settings_override)

    register_extensions(__app)
    register_blueprints(__app)

    return __app


def get_app():
    global __app

    return __app


def register_extensions(app: Flask):
    """
    Register one or more flask extensions. Mutates the flask app.

    :param app: Flask application instance.
    :return: None
    """
    from todo_api.extensions import db

    db.init_app(app)


def register_blueprints(app: Flask):
    """
    Register all blueprints.

    :param app: Flask application instance
    :return: None
    """
    from todo_api.blueprints import admin, auth, todos

    app.register_blueprint(admin)
    app.register_blueprint(auth)
    app.register_blueprint(todos)
