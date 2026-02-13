from arduino.app_bricks.cloud_llm import CloudLLM, CloudModel
from arduino.app_bricks.web_ui import WebUI
from arduino.app_utils import App, Bridge
import time

# --- CONFIGURATION ---
DEBUG_MODE = True  # Set to True for testing without real LLM costs

llm = CloudLLM(model=CloudModel.GOOGLE_GEMINI)
ui = WebUI()

def prompt_call_from_button(button):
    """
    Function triggered by the hardware button via Bridge.
    It handles the logic to switch between prompts and send updates to the WebUI.
    """
    print(f"Button {button} pressed!")

    # Notify the Web interface that the LLM is processing
    ui.send_message('llm_status', {'state': 'thinking'})

    # 1. Define the prompt based on the button index
    if button == 1:
        prompt = "Write the recipe for carbonara"
    elif button == 2:
        prompt = "Write an Arduino program to blink an LED"
    elif button == 3:
        prompt = "Weekend itinerary for Copenhagen"
    else:
        # If no valid button is pressed, return to idle state
        ui.send_message('llm_status', {'state': 'idle'})
        print("No prompt defined for this button index")
        return

    # 2. Handle the LLM Response (Simulated or Real)
    if DEBUG_MODE:
        # Simulate processing time
        time.sleep(3)
        # Create a big test message for the specific prompt
        debug_message = f"This is the response for the prompt: '{prompt}'.\n"
        response = debug_message * 30
    else:
        # Call the real LLM
        response = llm.chat(prompt)
    
    # 3. Send the final result back to the browser
    ui.send_message('llm_status', {
        'state': 'done',
        'response': response
    })

# Register the function so it can be called by the microcontroller
Bridge.provide("prompt_call_from_button", prompt_call_from_button)

# Start the application loop
App.run()