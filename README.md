# 🟢 Button-Controlled Cloud LLM with Arduino UNO Q

This project connects physical buttons to a cloud-based Large Language Model.
When a button is pressed, a predefined prompt is sent to a cloud LLM (_using Google Gemini in this example_).
The generated response is then displayed on a web page.

## HW Setup
- Arduino UNO Q
- Arduino Modulino Buttons
- QWIIC Cable

## How It Works
- The Arduino sketch handles all hardware interactions: it detects button presses on the Modulino and sends the corresponding button ID to Python via the Bridge.
- The Python application receives the button ID, maps it to a predefined prompt, sends the prompt to the cloud LLM, and then forwards the generated response to be displayed on the web page.

## Bricks
The bricks used are:
- **CloudLLM**: Provides a simple interface to interact with cloud LLMs (GPT, Claude, Gemini), handling prompts, responses, and context.
- **WebUI HTML**: Lightweight web server for hosting frontend apps and exposing APIs or WebSocket channels.
