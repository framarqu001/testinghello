#!/usr/bin/env python3
"""
To-Do List Application

A simple command-line to-do list application that allows users to manage their tasks.
"""

import json
import os
from datetime import datetime

class TodoList:
    """A class to manage a to-do list with basic CRUD operations."""
    
    def __init__(self, storage_file="todo_data.json"):
        """Initialize the to-do list with an empty list of tasks."""
        self.tasks = []
        self.storage_file = storage_file
        self.load_tasks()
    
    def add_task(self, title, description="", due_date=None, priority="medium"):
        """
        Add a new task to the to-do list.
        
        Args:
            title (str): The title of the task
            description (str, optional): A description of the task
            due_date (str, optional): Due date in YYYY-MM-DD format
            priority (str, optional): Priority level (low, medium, high)
            
        Returns:
            int: The ID of the newly created task
        """
        task_id = len(self.tasks) + 1
        
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date,
            "priority": priority,
            "completed": False
        }
        
        self.tasks.append(task)
        self.save_tasks()
        return task_id
    
    def get_all_tasks(self):
        """
        Get all tasks in the to-do list.
        
        Returns:
            list: A list of all tasks
        """
        return self.tasks
    
    def get_task(self, task_id):
        """
        Get a specific task by ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            dict: The task with the specified ID, or None if not found
        """
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def update_task(self, task_id, **kwargs):
        """
        Update a task with new values.
        
        Args:
            task_id (int): The ID of the task to update
            **kwargs: Key-value pairs of task attributes to update
            
        Returns:
            bool: True if the task was updated, False otherwise
        """
        task = self.get_task(task_id)
        if not task:
            return False
        
        # Update only the provided attributes
        for key, value in kwargs.items():
            if key in task and key != "id":  # Prevent changing the ID
                task[key] = value
        
        self.save_tasks()
        return True
    
    def delete_task(self, task_id):
        """
        Delete a task from the to-do list.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False otherwise
        """
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False
    
    def mark_task_complete(self, task_id):
        """
        Mark a task as complete.
        
        Args:
            task_id (int): The ID of the task to mark as complete
            
        Returns:
            bool: True if the task was marked as complete, False otherwise
        """
        return self.update_task(task_id, completed=True)
    
    def mark_task_incomplete(self, task_id):
        """
        Mark a task as incomplete.
        
        Args:
            task_id (int): The ID of the task to mark as incomplete
            
        Returns:
            bool: True if the task was marked as incomplete, False otherwise
        """
        return self.update_task(task_id, completed=False)
    
    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.storage_file, 'w') as f:
            # Convert datetime objects to strings for JSON serialization
            json.dump(self.tasks, f, indent=2)
    
    def load_tasks(self):
        """Load tasks from a JSON file if it exists."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                # If the file is corrupted, start with an empty task list
                self.tasks = []


def display_task(task):
    """Format and display a single task."""
    status = "✓" if task["completed"] else "✗"
    priority_display = {
        "low": "Low",
        "medium": "Medium",
        "high": "High"
    }
    
    print(f"\nTask #{task['id']}: {task['title']} [{status}]")
    print(f"Priority: {priority_display.get(task['priority'], task['priority'])}")
    
    if task["description"]:
        print(f"Description: {task['description']}")
    
    print(f"Created: {task['created_at']}")
    
    if task["due_date"]:
        print(f"Due: {task['due_date']}")
    
    print("-" * 40)


def display_all_tasks(tasks):
    """Display all tasks in a formatted way."""
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print("\n===== Your To-Do List =====")
    for task in tasks:
        display_task(task)


def get_user_input(prompt, required=False):
    """Get input from the user with optional requirement."""
    while True:
        value = input(prompt)
        if required and not value:
            print("This field is required. Please try again.")
        else:
            return value


def main():
    """Main function to run the to-do list application."""
    todo_list = TodoList()
    
    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. View a specific task")
        print("4. Update a task")
        print("5. Delete a task")
        print("6. Mark a task as complete")
        print("7. Mark a task as incomplete")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "1":
            # Add a new task
            title = get_user_input("Enter task title: ", required=True)
            description = get_user_input("Enter task description (optional): ")
            due_date = get_user_input("Enter due date (YYYY-MM-DD) (optional): ")
            
            print("Priority levels: low, medium, high")
            priority = get_user_input("Enter priority (default: medium): ")
            if not priority:
                priority = "medium"
            
            task_id = todo_list.add_task(title, description, due_date, priority)
            print(f"\nTask added successfully with ID: {task_id}")
        
        elif choice == "2":
            # View all tasks
            tasks = todo_list.get_all_tasks()
            display_all_tasks(tasks)
        
        elif choice == "3":
            # View a specific task
            try:
                task_id = int(get_user_input("Enter task ID: ", required=True))
                task = todo_list.get_task(task_id)
                if task:
                    display_task(task)
                else:
                    print(f"\nTask with ID {task_id} not found.")
            except ValueError:
                print("\nInvalid task ID. Please enter a number.")
        
        elif choice == "4":
            # Update a task
            try:
                task_id = int(get_user_input("Enter task ID to update: ", required=True))
                task = todo_list.get_task(task_id)
                
                if not task:
                    print(f"\nTask with ID {task_id} not found.")
                    continue
                
                print("\nLeave fields blank to keep current values.")
                print("Current values:")
                display_task(task)
                
                title = get_user_input(f"Enter new title (current: {task['title']}): ")
                description = get_user_input(f"Enter new description (current: {task['description']}): ")
                due_date = get_user_input(f"Enter new due date (current: {task['due_date']}): ")
                priority = get_user_input(f"Enter new priority (current: {task['priority']}): ")
                
                updates = {}
                if title:
                    updates["title"] = title
                if description:
                    updates["description"] = description
                if due_date:
                    updates["due_date"] = due_date
                if priority:
                    updates["priority"] = priority
                
                if updates:
                    if todo_list.update_task(task_id, **updates):
                        print(f"\nTask {task_id} updated successfully.")
                    else:
                        print(f"\nFailed to update task {task_id}.")
                else:
                    print("\nNo changes made.")
            
            except ValueError:
                print("\nInvalid task ID. Please enter a number.")
        
        elif choice == "5":
            # Delete a task
            try:
                task_id = int(get_user_input("Enter task ID to delete: ", required=True))
                
                if todo_list.delete_task(task_id):
                    print(f"\nTask {task_id} deleted successfully.")
                else:
                    print(f"\nTask with ID {task_id} not found.")
            
            except ValueError:
                print("\nInvalid task ID. Please enter a number.")
        
        elif choice == "6":
            # Mark a task as complete
            try:
                task_id = int(get_user_input("Enter task ID to mark as complete: ", required=True))
                
                if todo_list.mark_task_complete(task_id):
                    print(f"\nTask {task_id} marked as complete.")
                else:
                    print(f"\nTask with ID {task_id} not found.")
            
            except ValueError:
                print("\nInvalid task ID. Please enter a number.")
        
        elif choice == "7":
            # Mark a task as incomplete
            try:
                task_id = int(get_user_input("Enter task ID to mark as incomplete: ", required=True))
                
                if todo_list.mark_task_incomplete(task_id):
                    print(f"\nTask {task_id} marked as incomplete.")
                else:
                    print(f"\nTask with ID {task_id} not found.")
            
            except ValueError:
                print("\nInvalid task ID. Please enter a number.")
        
        elif choice == "8":
            # Exit the application
            print("\nThank you for using the To-Do List Application. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()