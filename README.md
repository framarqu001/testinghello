# Todo Web Application

A simple and elegant to-do list web application built with Python Flask.

## Features

- Add new tasks to your to-do list
- Mark tasks as complete/incomplete
- Delete tasks
- RESTful API for programmatic access

## Files and Structure

- `app.py`: Main Flask application with routes and database models
- `templates/index.html`: HTML template for the to-do list interface
- `static/css/style.css`: CSS styling for the application
- `static/js/script.js`: JavaScript for client-side interactivity
- `test_todo.py`: Python tests for the application
- `requirements.txt`: Python dependencies

## Setup and Installation

1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open your browser and navigate to `http://localhost:5000`

## API Endpoints

The application provides the following API endpoints:

- `GET /api/todos`: Get all to-do items
- `POST /api/todos`: Create a new to-do item
- `PUT /api/todos/<id>`: Update a to-do item
- `DELETE /api/todos/<id>`: Delete a to-do item

## Testing

To run the tests:

1. Make sure you have pytest installed:
   ```
   pip install pytest
   ```

2. Run the tests:
   ```
   pytest test_todo.py
   ```

The tests verify that:
- The application routes work correctly
- To-do items can be added, updated, and deleted
- The API endpoints function as expected