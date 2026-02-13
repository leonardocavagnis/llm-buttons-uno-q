from arduino.app_utils import *

def prompt_call_from_button(button: int) -> None:
    print(f"Button {button} pressed!")

Bridge.provide("prompt_call_from_button", prompt_call_from_button)

App.run()