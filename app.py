# app.py

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from models import create_task, get_all_tasks, get_task, update_task, delete_task

app = Flask(__name__)
api = Api(app)

class TaskList(Resource):
    def get(self):
        return jsonify(get_all_tasks())

    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        task = create_task(title, description)
        return jsonify(task), 201

class Task(Resource):
    def get(self, task_id):
        task = get_task(task_id)
        if task:
            return jsonify(task)
        return jsonify({'message': 'Task not found'}), 404

    def put(self, task_id):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        completed = data.get('completed')
        task = update_task(task_id, title, description, completed)
        if task:
            return jsonify(task)
        return jsonify({'message': 'Task not found'}), 404

    def delete(self, task_id):
        task = delete_task(task_id)
        if task:
            return jsonify({'message': 'Task deleted'}), 200
        return jsonify({'message': 'Task not found'}), 404

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)