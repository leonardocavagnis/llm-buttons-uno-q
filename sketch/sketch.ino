#include <Arduino_Modulino.h>
#include <Arduino_RouterBridge.h>

ModulinoButtons buttons;

void setup() {
  // Initialize communication between microcontroller and processor
  Bridge.begin();
  Monitor.begin();
  
  // Initialize Modulino
  Modulino.begin();
  buttons.begin();
}

void loop() {
  // Check for button state changes
  if (buttons.update()) {
    
    if (buttons.isPressed('A')) {
      Monitor.println("Button A pressed!");
      // Trigger Python function with Button index 1
      Bridge.call("prompt_call_from_button", 1).result();
      
    } else if (buttons.isPressed('B')) {
      Monitor.println("Button B pressed!");
      // Trigger Python function with Button index 2
      Bridge.call("prompt_call_from_button", 2).result();
      
    } else if (buttons.isPressed('C')) {
      Monitor.println("Button C pressed!");
      // Trigger Python function with Button index 3
      Bridge.call("prompt_call_from_button", 3).result();
    }
  }
}