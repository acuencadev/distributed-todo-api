from flask import Flask


def create_app():
    """
    Create a Flask application using the factory pattern

    :return: Flask application instance
    """
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello World"

    return app
