# User Greeting Page with Number Guessing Game

This repository contains a simple HTML page that greets users without using the word "hello" and includes a fun number guessing game.

## Files

- `index.html`: The main HTML file containing the user greeting and number guessing game
- `test_greeting.js`: A Node.js test script to verify the HTML greeting and game functionality

## How to Use

1. Open `index.html` in any web browser to see the greeting and play the game
2. For the game:
   - The computer will randomly select a number between 1 and 100
   - Enter your guess in the input field and click "Guess" or press Enter
   - You'll receive feedback if your guess is too high or too low
   - Keep guessing until you find the correct number
   - Click "Play Again" to start a new game

## Testing

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
- The HTML contains a game container
- The game has necessary input elements
- The game has JavaScript logic