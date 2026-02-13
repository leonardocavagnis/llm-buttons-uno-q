const socket = io(`http://${window.location.host}`);
const statusText = document.getElementById('status-text');
const responseBox = document.getElementById('response-box');

socket.on('llm_status', (data) => {
    if (data.state === 'idle') {
        statusText.textContent = "I'm listening... press a button!";
        responseBox.style.display = 'none';
        responseBox.textContent = '';
    } else if (data.state === 'thinking') {
        statusText.textContent = "Let me think about that...";
        responseBox.style.display = 'none';
        responseBox.textContent = '';
    } else if (data.state === 'done') {
        statusText.textContent = "Done! Take a look:";
        responseBox.textContent = data.response;
        responseBox.style.display = 'block';
    }
});