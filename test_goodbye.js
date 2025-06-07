// Test script to verify the goodbye HTML page
const fs = require('fs');
const path = require('path');

// Function to test if the goodbye HTML file exists
function testFileExists() {
    const filePath = path.join(__dirname, 'goodbye.html');
    if (fs.existsSync(filePath)) {
        console.log('✅ Test passed: goodbye.html file exists');
        return true;
    } else {
        console.error('❌ Test failed: goodbye.html file does not exist');
        return false;
    }
}

// Function to test if the HTML content contains a goodbye message
function testHasGoodbye() {
    const filePath = path.join(__dirname, 'goodbye.html');
    const content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes('Farewell') || content.includes('Goodbye') || content.includes('see you again')) {
        console.log('✅ Test passed: HTML contains a goodbye message');
        return true;
    } else {
        console.error('❌ Test failed: HTML does not contain a goodbye message');
        return false;
    }
}

// Function to test that the HTML does not contain "hello"
function testNoHello() {
    const filePath = path.join(__dirname, 'goodbye.html');
    const content = fs.readFileSync(filePath, 'utf8').toLowerCase();
    
    if (!content.includes('hello')) {
        console.log('✅ Test passed: HTML does not contain "hello"');
        return true;
    } else {
        console.error('❌ Test failed: HTML contains "hello"');
        return false;
    }
}

// Run all tests
function runTests() {
    console.log('Running tests for goodbye HTML...');
    
    const fileExists = testFileExists();
    if (!fileExists) return;
    
    const hasGoodbye = testHasGoodbye();
    const noHello = testNoHello();
    
    if (fileExists && hasGoodbye && noHello) {
        console.log('🎉 All tests passed!');
    } else {
        console.error('⚠️ Some tests failed.');
    }
}

// Execute tests
runTests();