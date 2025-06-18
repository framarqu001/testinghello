# User Greeting Page and Calculator

This repository contains a simple HTML page that greets users without using the word "hello" and a Python calculator module.

## Files

- `index.html`: The main HTML file containing the user greeting
- `test_greeting.js`: A Node.js test script to verify the HTML greeting functionality
- `calculator.py`: A Python module with mathematical functions
- `test_calculator.py`: A Python unittest module for testing calculator functions

## How to Use

### Web Greeting
1. Open `index.html` in any web browser to see the greeting

### Calculator
1. Import the calculator module in your Python code:
   ```python
   from calculator import add
   
   result = add(5, 3)  # Returns 8
   ```

## Testing

### HTML Greeting Tests
To run the HTML tests:

1. Make sure you have Node.js installed
2. Run the test script:
   ```
   node test_greeting.js
   ```

The tests verify that:
- The HTML file exists
- The HTML contains a greeting
- The HTML does not contain the word "hello"

### Calculator Tests
To run the calculator tests:

1. Make sure you have Python installed
2. Run the test script:
   ```
   python -m unittest test_calculator.py
   ```

The tests verify that the add function correctly handles:
- Integer addition
- Float addition
- Mixed integer and float addition