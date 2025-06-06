import unittest
import os
import json
from app import app, TASKS_FILE

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        # Configure app for testing
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        
        # Use a test tasks file
        app.config['TASKS_FILE'] = 'test_tasks.json'
        global TASKS_FILE
        TASKS_FILE = 'test_tasks.json'
        
        # Clear any existing tasks
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)
            
    def tearDown(self):
        # Clean up after tests
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)
        
    def test_index_page(self):
        """Test that the index page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'To-Do List', response.data)
        
    def test_add_task(self):
        """Test adding a new task"""
        response = self.app.post('/add', data={'task': 'Test Task'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)
        self.assertIn(b'Task added successfully', response.data)
        
        # Verify task was saved to file
        self.assertTrue(os.path.exists(TASKS_FILE))
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            self.assertEqual(len(tasks), 1)
            self.assertEqual(tasks[0]['title'], 'Test Task')
        
    def test_add_empty_task(self):
        """Test adding an empty task"""
        response = self.app.post('/add', data={'task': ''}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task cannot be empty', response.data)
        
    def test_complete_task(self):
        """Test marking a task as complete"""
        # First add a task
        self.app.post('/add', data={'task': 'Complete Me'}, follow_redirects=True)
        # Then mark it as complete
        response = self.app.get('/complete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Complete Me', response.data)
        self.assertIn(b'completed', response.data)
        self.assertIn(b'Task completed', response.data)
        
        # Verify task was updated in file
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            self.assertEqual(len(tasks), 1)
            self.assertTrue(tasks[0]['completed'])
        
    def test_delete_task(self):
        """Test deleting a task"""
        # First add a task
        self.app.post('/add', data={'task': 'Delete Me'}, follow_redirects=True)
        # Then delete it
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Delete Me', response.data)
        self.assertIn(b'Task deleted successfully', response.data)
        
        # Verify task was removed from file
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            self.assertEqual(len(tasks), 0)
            
    def test_invalid_task_id(self):
        """Test accessing an invalid task ID"""
        response = self.app.get('/complete/999', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid task ID', response.data)
        
        response = self.app.get('/delete/999', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid task ID', response.data)

if __name__ == '__main__':
    unittest.main()