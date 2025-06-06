#!/usr/bin/env python3
"""
Test module for the To-Do List Application.

This module contains unit tests for the TodoList class in todo_app.py.
"""

import unittest
import os
import json
from todo_app import TodoList


class TestTodoList(unittest.TestCase):
    """Test cases for the TodoList class."""
    
    def setUp(self):
        """Set up a test environment before each test."""
        # Use a test-specific storage file
        self.test_file = "test_todo_data.json"
        
        # Remove the test file if it exists
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
        # Create a new TodoList instance for testing
        self.todo_list = TodoList(storage_file=self.test_file)
    
    def tearDown(self):
        """Clean up after each test."""
        # Remove the test file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_task(self):
        """Test adding a task to the to-do list."""
        task_id = self.todo_list.add_task("Test Task", "Test Description", "2023-12-31", "high")
        
        # Check if the task was added correctly
        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0]["title"], "Test Task")
        self.assertEqual(self.todo_list.tasks[0]["description"], "Test Description")
        self.assertEqual(self.todo_list.tasks[0]["due_date"], "2023-12-31")
        self.assertEqual(self.todo_list.tasks[0]["priority"], "high")
        self.assertFalse(self.todo_list.tasks[0]["completed"])
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks from the to-do list."""
        # Add some tasks
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.add_task("Task 3")
        
        # Get all tasks
        tasks = self.todo_list.get_all_tasks()
        
        # Check if all tasks were retrieved
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0]["title"], "Task 1")
        self.assertEqual(tasks[1]["title"], "Task 2")
        self.assertEqual(tasks[2]["title"], "Task 3")
    
    def test_get_task(self):
        """Test retrieving a specific task by ID."""
        # Add some tasks
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        
        # Get a specific task
        task = self.todo_list.get_task(2)
        
        # Check if the correct task was retrieved
        self.assertIsNotNone(task)
        self.assertEqual(task["id"], 2)
        self.assertEqual(task["title"], "Task 2")
        
        # Try to get a non-existent task
        task = self.todo_list.get_task(999)
        self.assertIsNone(task)
    
    def test_update_task(self):
        """Test updating a task."""
        # Add a task
        task_id = self.todo_list.add_task("Original Title", "Original Description")
        
        # Update the task
        result = self.todo_list.update_task(
            task_id,
            title="Updated Title",
            description="Updated Description",
            priority="high"
        )
        
        # Check if the update was successful
        self.assertTrue(result)
        
        # Get the updated task
        task = self.todo_list.get_task(task_id)
        
        # Check if the task was updated correctly
        self.assertEqual(task["title"], "Updated Title")
        self.assertEqual(task["description"], "Updated Description")
        self.assertEqual(task["priority"], "high")
        
        # Try to update a non-existent task
        result = self.todo_list.update_task(999, title="New Title")
        self.assertFalse(result)
    
    def test_delete_task(self):
        """Test deleting a task."""
        # Add some tasks
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.add_task("Task 3")
        
        # Delete a task
        result = self.todo_list.delete_task(2)
        
        # Check if the deletion was successful
        self.assertTrue(result)
        self.assertEqual(len(self.todo_list.tasks), 2)
        
        # Check if the remaining tasks are correct
        tasks = self.todo_list.get_all_tasks()
        self.assertEqual(tasks[0]["title"], "Task 1")
        self.assertEqual(tasks[1]["title"], "Task 3")
        
        # Try to delete a non-existent task
        result = self.todo_list.delete_task(999)
        self.assertFalse(result)
    
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        # Add a task
        task_id = self.todo_list.add_task("Test Task")
        
        # Mark the task as complete
        result = self.todo_list.mark_task_complete(task_id)
        
        # Check if the operation was successful
        self.assertTrue(result)
        
        # Get the task and check if it's marked as complete
        task = self.todo_list.get_task(task_id)
        self.assertTrue(task["completed"])
        
        # Try to mark a non-existent task as complete
        result = self.todo_list.mark_task_complete(999)
        self.assertFalse(result)
    
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        # Add a task and mark it as complete
        task_id = self.todo_list.add_task("Test Task")
        self.todo_list.mark_task_complete(task_id)
        
        # Mark the task as incomplete
        result = self.todo_list.mark_task_incomplete(task_id)
        
        # Check if the operation was successful
        self.assertTrue(result)
        
        # Get the task and check if it's marked as incomplete
        task = self.todo_list.get_task(task_id)
        self.assertFalse(task["completed"])
        
        # Try to mark a non-existent task as incomplete
        result = self.todo_list.mark_task_incomplete(999)
        self.assertFalse(result)
    
    def test_save_and_load_tasks(self):
        """Test saving tasks to a file and loading them back."""
        # Add some tasks
        self.todo_list.add_task("Task 1", priority="low")
        self.todo_list.add_task("Task 2", priority="medium")
        self.todo_list.add_task("Task 3", priority="high")
        
        # Save tasks to file
        self.todo_list.save_tasks()
        
        # Check if the file exists
        self.assertTrue(os.path.exists(self.test_file))
        
        # Create a new TodoList instance that will load from the file
        new_todo_list = TodoList(storage_file=self.test_file)
        
        # Check if tasks were loaded correctly
        tasks = new_todo_list.get_all_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0]["title"], "Task 1")
        self.assertEqual(tasks[1]["title"], "Task 2")
        self.assertEqual(tasks[2]["title"], "Task 3")
        self.assertEqual(tasks[0]["priority"], "low")
        self.assertEqual(tasks[1]["priority"], "medium")
        self.assertEqual(tasks[2]["priority"], "high")


if __name__ == "__main__":
    unittest.main()