import jwt
import datetime

from flask import Blueprint, request, jsonify, make_response

from todo_api.app import get_app
import todo_api.services.user_service as user_service


auth = Blueprint('auth', __name__)


@auth.route('/auth', methods=['GET'])
def login():
    authorization = request.authorization

    if not authorization or not authorization.username or not authorization.password:
        return make_response("Could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = user_service.get_user_by_username(authorization.username)

    if not user:
        return make_response("Could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    public_id = user_service.validate_user(authorization.username, authorization.password)

    if public_id:
        app = get_app()
        token = jwt.encode({
            'public_id': public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return jsonify({
            'token': token.decode('UTF-8')
        })

    return make_response("Could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


@auth.route('/auth', methods=['POST'])
def register():
    data = request.get_json()
    new_user = user_service.create_user(username=data['username'], unhashed_password=data['password'],
                                        admin=data['admin'])

    if not new_user:
        return '', 400

    user_data = {
        'public_id': new_user.public_id,
        'username': new_user.username,
        'admin': new_user.admin
    }

    return jsonify({
        'user': user_data
    }), 201
