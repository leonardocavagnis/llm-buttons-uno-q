// Initialize the Socket.io connection to the host server
const socket = io(`http://${window.location.host}`);

// Get references to HTML elements for updating the UI
const statusText = document.getElementById('status-text');
const responseBox = document.getElementById('response-box');

// Listen for status updates sent from the Python backend
socket.on('llm_status', (data) => {
    if (data.state === 'idle') {
        // Initial state: reset the UI and wait for user interaction
        statusText.textContent = "I'm listening... press a button!";
        responseBox.style.display = 'none';
        responseBox.textContent = '';
        
    } else if (data.state === 'thinking') {
        // Processing state: show a waiting message while the AI generates a response
        statusText.textContent = "Let me think about that...";
        responseBox.style.display = 'none';
        responseBox.textContent = '';
        
    } else if (data.state === 'done') {
        // Completion state: display the final AI response in the scrollable box
        statusText.textContent = "Done! Take a look:";
        responseBox.textContent = data.response;
        responseBox.style.display = 'block';
    }
});