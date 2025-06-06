# To-Do List Web Application

This repository contains a Python web application for managing a to-do list.

## Files

- `app.py`: The main Python Flask application
- `templates/index.html`: The HTML template for the to-do list interface
- `static/`: Directory for static assets (CSS, JavaScript)
- `test_todo.py`: Python unit tests for the to-do list functionality
- `index.html`: Original greeting page (legacy)
- `test_greeting.js`: Original Node.js test script (legacy)

## Requirements

- Python 3.6 or higher
- Flask

## Installation

1. Install the required dependencies:
   ```
   pip install flask
   ```

## How to Use

1. Run the Flask application:
   ```
   python app.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/`
3. Use the interface to:
   - Add new tasks
   - Mark tasks as complete/incomplete
   - Delete tasks

## Features

- Add new tasks to your to-do list
- Mark tasks as complete or incomplete
- Delete tasks you no longer need
- Clean, responsive user interface

## Testing

To run the Python tests:
```
python -m unittest test_todo.py
```

The tests verify that:
- The application loads correctly
- Tasks can be added
- Tasks can be marked as complete
- Tasks can be deleted

To run the legacy Node.js tests:
```
node test_greeting.js
```