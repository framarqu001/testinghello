// Simple test script to verify the HTML greeting and game functionality
const fs = require('fs');
const path = require('path');

// Function to test if the HTML file exists
function testFileExists() {
    const filePath = path.join(__dirname, 'index.html');
    if (fs.existsSync(filePath)) {
        console.log('✅ Test passed: index.html file exists');
        return true;
    } else {
        console.error('❌ Test failed: index.html file does not exist');
        return false;
    }
}

// Function to test if the HTML content contains a greeting
function testHasGreeting() {
    const filePath = path.join(__dirname, 'index.html');
    const content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes('Welcome') || content.includes('glad to see you')) {
        console.log('✅ Test passed: HTML contains a greeting');
        return true;
    } else {
        console.error('❌ Test failed: HTML does not contain a greeting');
        return false;
    }
}

// Function to test that the HTML does not contain "hello"
function testNoHello() {
    const filePath = path.join(__dirname, 'index.html');
    const content = fs.readFileSync(filePath, 'utf8').toLowerCase();
    
    if (!content.includes('hello')) {
        console.log('✅ Test passed: HTML does not contain "hello"');
        return true;
    } else {
        console.error('❌ Test failed: HTML contains "hello"');
        return false;
    }
}

// Function to test if the game container exists
function testGameExists() {
    const filePath = path.join(__dirname, 'index.html');
    const content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes('game-container')) {
        console.log('✅ Test passed: HTML contains a game container');
        return true;
    } else {
        console.error('❌ Test failed: HTML does not contain a game container');
        return false;
    }
}

// Function to test if the game has necessary input elements
function testGameInputElements() {
    const filePath = path.join(__dirname, 'index.html');
    const content = fs.readFileSync(filePath, 'utf8');
    
    const hasInput = content.includes('guess-input');
    const hasButton = content.includes('guess-button');
    const hasMessage = content.includes('game-message');
    
    if (hasInput && hasButton && hasMessage) {
        console.log('✅ Test passed: Game has necessary input elements');
        return true;
    } else {
        console.error('❌ Test failed: Game is missing necessary input elements');
        return false;
    }
}

// Function to test if the game has JavaScript logic
function testGameLogic() {
    const filePath = path.join(__dirname, 'index.html');
    const content = fs.readFileSync(filePath, 'utf8');
    
    const hasRandomNumber = content.includes('Math.random()');
    const hasCheckGuess = content.includes('checkGuess');
    const hasEventListeners = content.includes('addEventListener');
    
    if (hasRandomNumber && hasCheckGuess && hasEventListeners) {
        console.log('✅ Test passed: Game has JavaScript logic');
        return true;
    } else {
        console.error('❌ Test failed: Game is missing JavaScript logic');
        return false;
    }
}

// Run all tests
function runTests() {
    console.log('Running tests for greeting HTML and game functionality...');
    
    const fileExists = testFileExists();
    if (!fileExists) return;
    
    // Original tests
    const hasGreeting = testHasGreeting();
    const noHello = testNoHello();
    
    // New game tests
    const gameExists = testGameExists();
    const gameHasInputElements = testGameInputElements();
    const gameHasLogic = testGameLogic();
    
    if (fileExists && hasGreeting && noHello && gameExists && gameHasInputElements && gameHasLogic) {
        console.log('🎉 All tests passed!');
    } else {
        console.error('⚠️ Some tests failed.');
    }
}

// Execute tests
runTests();