#include <Arduino_Modulino.h>
#include <Arduino_RouterBridge.h>

ModulinoButtons buttons;

void setup() {
  Bridge.begin();
  Monitor.begin();
  
  Modulino.begin();
  buttons.begin();
}

void loop() {
  if (buttons.update()) {
    if (buttons.isPressed('A')) {
      Monitor.println("Button A pressed!");
      Bridge.call("prompt_call_from_button", 1).result();
    } else if (buttons.isPressed("B")) {
      Monitor.println("Button B pressed!");
      Bridge.call("prompt_call_from_button", 2).result();
    } else if (buttons.isPressed('C')) {
      Monitor.println("Button C pressed!");
      Bridge.call("prompt_call_from_button", 3).result();
    }
  }
}