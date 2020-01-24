from flask import Blueprint, request, jsonify

import todo_api.services.user_service as user_service
from todo_api.infrastructure.view_decorators import token_required, admin_permissions

admin: Blueprint = Blueprint('admin', __name__)


@admin.route('/users', methods=['GET'])
@token_required
@admin_permissions
def get_all_users(current_user):
    users = user_service.get_all_users()
    users_data = []

    for user in users:
        user_data = {
            'public_id': user.public_id,
            'username': user.username,
            'admin': user.admin
        }

        users_data.append(user_data)

    return jsonify({
        'users': users_data
    })


@admin.route('/users/<public_id>', methods=['GET'])
@token_required
@admin_permissions
def get_one_user(current_user, public_id):
    user = user_service.get_user_by_public_id(public_id)

    if not user:
        return '', 404

    user_data = {
        'public_id': user.public_id,
        'username': user.username,
        'admin': user.admin
    }

    return jsonify({
        'user': user_data
    }), 200


@admin.route('/users', methods=['POST'])
@token_required
@admin_permissions
def create_user(current_user):
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


@admin.route('/users/<public_id>', methods=['PUT'])
@token_required
@admin_permissions
def update_user(current_user, public_id):
    data = request.get_json()

    updated_user = user_service.update_user(public_id=public_id, username=data.get('username', None),
                                            admin=data.get('admin', False))

    if not updated_user:
        return '', 404

    return '', 204


@admin.route('/users/<public_id>', methods=['PATCH'])
@token_required
@admin_permissions
def promote_user(current_user, public_id):
    promoted_user = user_service.promote_user(public_id)

    if not promoted_user:
        return '', 404

    return '', 204


@admin.route('/users/<public_id>', methods=['DELETE'])
@token_required
@admin_permissions
def delete_user(current_user, public_id):
    deleted_user = user_service.delete_user(public_id)

    if not deleted_user:
        return '', 404

    return '', 204


@admin.route('/users', methods=['DELETE'])
@token_required
@admin_permissions
def delete_all_users(current_user):
    users_deleted = user_service.delete_all_users()

    return '', 204
