from flask import Blueprint


todos: Blueprint = Blueprint('todos', __name__)


@todos.route('/todos', methods=['GET'])
def get_all_todos():
    return ''


@todos.route('/todos/<public_id>', methods=['GET'])
def get_one_todo(public_id):
    return ''


@todos.route('/todos', methods=['POST'])
def create_todo():
    return ''


@todos.route('/todos/<public_id>', methods=['PUT'])
def update_todo(public_id):
    return ''


@todos.route('/todos/<public_id>', methods=['PATCH'])
def complete_todo(public_id):
    return ''


@todos.route('/todos/<public_id>', methods=['DELETE'])
def delete_todo(public_id):
    return ''


@todos.route('/todos', methods=['DELETE'])
def delete_all_todos():
    return ''
