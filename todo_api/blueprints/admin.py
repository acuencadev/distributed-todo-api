from flask import Blueprint


admin: Blueprint = Blueprint('admin', __name__)


@admin.route('/users', methods=['GET'])
def get_all_users():
    return ''


@admin.route('/users/<public_id>', methods=['GET'])
def get_one_user(public_id):
    return ''


@admin.route('/users', methods=['POST'])
def create_user():
    return ''


@admin.route('/users/<public_id>', methods=['PUT'])
def update_user(public_id):
    return ''


@admin.route('/users/<public_id>', methods=['PATCH'])
def promote_user(public_id):
    return ''


@admin.route('/users/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    return ''


@admin.route('/users', methods=['DELETE'])
def delete_all_users():
    return ''
