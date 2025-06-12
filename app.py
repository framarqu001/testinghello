from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Todo {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'completed': self.completed,
            'date_created': self.date_created.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    todos = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo_content = request.form.get('content')
    if todo_content:
        new_todo = Todo(content=todo_content)
        try:
            db.session.add(new_todo)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"An error occurred while adding the task: {e}"
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    try:
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"An error occurred while updating the task: {e}"

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    try:
        db.session.delete(todo)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"An error occurred while deleting the task: {e}"

# API endpoints for AJAX operations
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.date_created).all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/api/todos', methods=['POST'])
def api_add_todo():
    data = request.json
    if 'content' in data and data['content']:
        new_todo = Todo(content=data['content'])
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(new_todo.to_dict()), 201
    return jsonify({'error': 'Content is required'}), 400

@app.route('/api/todos/<int:id>', methods=['PUT'])
def api_update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.json
    if 'completed' in data:
        todo.completed = data['completed']
    if 'content' in data:
        todo.content = data['content']
    db.session.commit()
    return jsonify(todo.to_dict())

@app.route('/api/todos/<int:id>', methods=['DELETE'])
def api_delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)