# Repository Contents

This repository contains two applications:

1. A simple HTML greeting page
2. A Python to-do list application

## Python To-Do List Application

A command-line application for managing your tasks with the following features:
- Add new tasks with title, description, due date, and priority
- View all tasks or a specific task
- Update existing tasks
- Delete tasks
- Mark tasks as complete or incomplete
- Persistent storage using JSON

### Files

- `todo_app.py`: The main Python application file
- `test_todo_app.py`: Unit tests for the to-do list application

### How to Use the To-Do List Application

1. Make sure you have Python 3 installed
2. Run the application:
   ```
   python todo_app.py
   ```
3. Follow the on-screen menu to manage your tasks

### Testing the To-Do List Application

To run the tests:
1. Make sure you have Python 3 installed
2. Run the test script:
   ```
   python test_todo_app.py
   ```

## HTML Greeting Page

A simple HTML page that greets users without using the word "hello".

### Files

- `index.html`: The main HTML file containing the user greeting
- `test_greeting.js`: A Node.js test script to verify the HTML greeting functionality

### How to Use the Greeting Page

1. Open `index.html` in any web browser to see the greeting

### Testing the Greeting Page

To run the tests:

1. Make sure you have Node.js installed
2. Run the test script:
   ```
   node test_greeting.js
   ```

The tests verify that:
- The HTML file exists
- The HTML contains a greeting
- The HTML does not contain the word "hello"