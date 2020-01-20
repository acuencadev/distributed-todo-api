import jwt
from functools import wraps

from flask import request, jsonify

from todo_api.app import get_app
import todo_api.services.admin_service as admin_service


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
            current_user = admin_service.get_user_by_public_id(public_id=data['public_id'])
        except:
            return jsonify({'message': "Token is invalid!"}, 401)

        return f(current_user, *args, **kwargs)

    return decorated
