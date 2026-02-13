from arduino.app_bricks.cloud_llm import CloudLLM, CloudModel
from arduino.app_utils import App, Bridge

llm = CloudLLM(
    model=CloudModel.GOOGLE_GEMINI
)

def prompt_call_from_button(button):
    print("Button", button, "pressed!")

    if button == 1:
        prompt = "Write the recipe for carbonara"
    elif button == 2:
        prompt = "Write an Arduino program to blink an LED"
    elif button == 3:
        prompt = "Weekend itinerary for Copenhagen"
    else:
        print("No prompt for this button")
        return

    print(prompt)
    response = llm.chat(prompt)
    print(response)

Bridge.provide("prompt_call_from_button", prompt_call_from_button)

App.run()
