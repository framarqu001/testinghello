from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json

app = Flask(__name__)
app.secret_key = 'todo_app_secret_key'  # Required for flash messages

# File to store tasks (simple persistence)
TASKS_FILE = 'tasks.json'

# Initialize tasks list
tasks = []

# Load tasks from file if it exists
def load_tasks():
    global tasks
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                tasks = json.load(f)
    except Exception as e:
        print(f"Error loading tasks: {e}")
        tasks = []

# Save tasks to file
def save_tasks():
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f)
    except Exception as e:
        print(f"Error saving tasks: {e}")

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task and task.strip():
        tasks.append({'id': len(tasks), 'title': task.strip(), 'completed': False})
        save_tasks()
        flash('Task added successfully!', 'success')
    else:
        flash('Task cannot be empty!', 'error')
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    try:
        if 0 <= task_id < len(tasks):
            tasks[task_id]['completed'] = not tasks[task_id]['completed']
            status = 'completed' if tasks[task_id]['completed'] else 'marked as incomplete'
            flash(f'Task {status}!', 'success')
            save_tasks()
        else:
            flash('Invalid task ID!', 'error')
    except Exception as e:
        flash(f'Error updating task: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    try:
        if 0 <= task_id < len(tasks):
            del tasks[task_id]
            # Update IDs for remaining tasks
            for i, task in enumerate(tasks):
                task['id'] = i
            flash('Task deleted successfully!', 'success')
            save_tasks()
        else:
            flash('Invalid task ID!', 'error')
    except Exception as e:
        flash(f'Error deleting task: {str(e)}', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Load existing tasks
    load_tasks()
    
    app.run(debug=True)