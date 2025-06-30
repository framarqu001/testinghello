// Simple test script to verify the HTML greeting
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
    
    if (content.includes('Welcome') || content.includes('glad to see you') || content.includes('Hi there')) {
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

// Function to test if the HTML contains "Do something" functionality
function testDoSomething() {
    const filePath = path.join(__dirname, 'index.html');
    const content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes('Do something') && content.includes('doSomethingBtn')) {
        console.log('✅ Test passed: HTML contains "Do something" functionality');
        return true;
    } else {
        console.error('❌ Test failed: HTML does not contain "Do something" functionality');
        return false;
    }
}

// Run all tests
function runTests() {
    console.log('Running tests for greeting HTML...');
    
    const fileExists = testFileExists();
    if (!fileExists) return;
    
    const hasGreeting = testHasGreeting();
    const noHello = testNoHello();
    const hasDoSomething = testDoSomething();
    
    if (fileExists && hasGreeting && noHello && hasDoSomething) {
        console.log('🎉 All tests passed!');
    } else {
        console.error('⚠️ Some tests failed.');
    }
}

// Execute tests
runTests();