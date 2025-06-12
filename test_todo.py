import os
import tempfile
import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    # Create a temporary database file
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['TESTING'] = True
    
    # Create the database and the database table
    with app.app_context():
        db.create_all()
    
    # Create a test client using the Flask application
    with app.test_client() as client:
        yield client
    
    # Close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)

def test_index(client):
    """Test that the index page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Todo List' in response.data

def test_add_todo(client):
    """Test adding a new todo item"""
    response = client.post('/add', data={'content': 'Test Todo'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Todo' in response.data
    
    # Check that it was added to the database
    with app.app_context():
        assert Todo.query.count() == 1
        assert Todo.query.first().content == 'Test Todo'

def test_update_todo(client):
    """Test updating a todo item's completion status"""
    # First add a todo
    client.post('/add', data={'content': 'Update Test'}, follow_redirects=True)
    
    # Get the ID of the added todo
    with app.app_context():
        todo_id = Todo.query.first().id
    
    # Update the todo
    response = client.post(f'/update/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    
    # Check that it was updated in the database
    with app.app_context():
        assert Todo.query.first().completed == True

def test_delete_todo(client):
    """Test deleting a todo item"""
    # First add a todo
    client.post('/add', data={'content': 'Delete Test'}, follow_redirects=True)
    
    # Get the ID of the added todo
    with app.app_context():
        todo_id = Todo.query.first().id
    
    # Delete the todo
    response = client.get(f'/delete/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    
    # Check that it was deleted from the database
    with app.app_context():
        assert Todo.query.count() == 0

def test_api_get_todos(client):
    """Test the API endpoint for getting todos"""
    # First add a todo
    client.post('/add', data={'content': 'API Test'}, follow_redirects=True)
    
    # Get todos via API
    response = client.get('/api/todos')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 1
    assert json_data[0]['content'] == 'API Test'

def test_api_add_todo(client):
    """Test the API endpoint for adding a todo"""
    response = client.post('/api/todos', 
                          json={'content': 'API Add Test'},
                          content_type='application/json')
    assert response.status_code == 201
    
    # Check that it was added to the database
    with app.app_context():
        assert Todo.query.count() == 1
        assert Todo.query.first().content == 'API Add Test'

def test_api_update_todo(client):
    """Test the API endpoint for updating a todo"""
    # First add a todo
    client.post('/api/todos', 
               json={'content': 'API Update Test'},
               content_type='application/json')
    
    # Get the ID of the added todo
    with app.app_context():
        todo_id = Todo.query.first().id
    
    # Update the todo via API
    response = client.put(f'/api/todos/{todo_id}',
                         json={'completed': True},
                         content_type='application/json')
    assert response.status_code == 200
    
    # Check that it was updated in the database
    with app.app_context():
        assert Todo.query.first().completed == True

def test_api_delete_todo(client):
    """Test the API endpoint for deleting a todo"""
    # First add a todo
    client.post('/api/todos', 
               json={'content': 'API Delete Test'},
               content_type='application/json')
    
    # Get the ID of the added todo
    with app.app_context():
        todo_id = Todo.query.first().id
    
    # Delete the todo via API
    response = client.delete(f'/api/todos/{todo_id}')
    assert response.status_code == 204
    
    # Check that it was deleted from the database
    with app.app_context():
        assert Todo.query.count() == 0