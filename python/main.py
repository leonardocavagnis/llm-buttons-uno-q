from arduino.app_bricks.cloud_llm import CloudLLM, CloudModel
from arduino.app_bricks.web_ui import WebUI
from arduino.app_utils import App, Bridge
import time

DEBUG_MODE = True

llm = CloudLLM(model=CloudModel.GOOGLE_GEMINI)
ui = WebUI()

def prompt_call_from_button(button):
    print("Button", button, "pressed!")

    ui.send_message('llm_status', {'state': 'thinking'})

    if button == 1:
        prompt = "Write the recipe for carbonara"
    elif button == 2:
        prompt = "Write an Arduino program to blink an LED"
    elif button == 3:
        prompt = "Weekend itinerary for Copenhagen"
    else:
        ui.send_message('llm_status', {'state': 'idle'})
        print("No prompt for this button")
        return

    print(prompt)
    
    if DEBUG_MODE:
        # LLM Emulation
        time.sleep(3)
        response = f"TEST RESPONSE: You requested info for button {button}."
    else:
        # Real LLM Call
        response = llm.chat(prompt)
    
    print(response)

    ui.send_message('llm_status', {
        'state': 'done',
        'response': response
    })

Bridge.provide("prompt_call_from_button", prompt_call_from_button)

App.run()