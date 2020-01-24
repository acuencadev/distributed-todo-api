import jwt
from functools import wraps

from flask import request, jsonify

from todo_api.app import get_app
import todo_api.services.user_service as user_service


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        app = get_app()
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({ 'message': "Token is missing!" }, 401)

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_service.get_user_by_public_id(public_id=data['public_id'])
        except:
            return jsonify({'message': "Token is invalid!"}, 401)

        return f(current_user, *args, **kwargs)

    return decorated


def admin_permissions(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        app = get_app()
        token = request.headers['x-access-token']
        data = jwt.decode(token, app.config['SECRET_KEY'])

        current_user = user_service.get_user_by_public_id(public_id=data['public_id'])

        if not current_user.admin:
            return jsonify({'message': "Cannot access this route!"}, 401)

        return f(*args, **kwargs)

    return decorated
