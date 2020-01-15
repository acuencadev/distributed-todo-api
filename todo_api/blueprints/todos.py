from flask import Blueprint, request, jsonify

import todo_api.services.todo_service as todo_service


todos: Blueprint = Blueprint('todos', __name__)


@todos.route('/todos', methods=['GET'])
def get_all_todos():
    todos = todo_service.get_all_todos()
    todos_data = []

    for todo in todos:
        todo_data = {
            'public_id': todo.public_id,
            'text': todo.text,
            'completed': todo.completed
        }

        todo_data.append(todo_data)

    return jsonify({
        'users': todos_data
    })


@todos.route('/todos/<public_id>', methods=['GET'])
def get_one_todo(public_id):
    todo = todo_service.get_todo_by_public_id(public_id)

    if not todo:
        return '', 404

    todo_data = {
        'public_id': todo.public_id,
        'text': todo.text,
        'completed': todo.completed
    }

    return jsonify({
        'todo': todo_data
    }), 200


@todos.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = todo_service.create_todo(text=data['todo'], user_id=1)

    if not new_todo:
        return '', 400

    todo_data = {
        'public_id': new_todo.public_id,
        'text': new_todo.text,
        'completed': new_todo.completed
    }

    return jsonify({
        'todo': todo_data
    }), 201


@todos.route('/todos/<public_id>', methods=['PUT'])
def update_todo(public_id):
    data = request.get_json()

    updated_todo = todo_service.update_todo(public_id=public_id, text=data['text'], completed=data['completed'])

    if not updated_todo:
        return '', 404

    return '', 204


@todos.route('/todos/<public_id>', methods=['PATCH'])
def complete_todo(public_id):
    completed_todo = todo_service.complete_todo(public_id)

    if not completed_todo:
        return '', 404

    return '', 204


@todos.route('/todos/<public_id>', methods=['DELETE'])
def delete_todo(public_id):
    deleted_todo = todo_service.delete_todo(public_id)

    if not deleted_todo:
        return '', 404

    return '', 204


@todos.route('/todos', methods=['DELETE'])
def delete_all_todos():
    todos_deleted = todo_service.delete_all_todos()

    return '', 204
