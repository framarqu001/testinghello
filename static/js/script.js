// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // You can add client-side functionality here
    console.log('Todo app loaded!');
    
    // Example: Add event listeners for dynamic updates without page reload
    // This is a placeholder for future AJAX functionality
    
    // For now, we're using traditional form submissions
    // but this file can be expanded for more interactive features
});

// Function to add a new todo via AJAX (for future implementation)
function addTodoAjax(content) {
    fetch('/api/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: content })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Refresh the todo list or add the new item to the DOM
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Function to toggle todo completion status via AJAX (for future implementation)
function toggleTodoAjax(id, completed) {
    fetch(`/api/todos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ completed: completed })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Update the UI to reflect the new status
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Function to delete a todo via AJAX (for future implementation)
function deleteTodoAjax(id) {
    fetch(`/api/todos/${id}`, {
        method: 'DELETE',
    })
    .then(response => {
        console.log('Todo deleted successfully');
        // Remove the todo item from the DOM
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}