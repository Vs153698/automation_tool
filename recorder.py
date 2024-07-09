import time
import json
from pynput import mouse, keyboard

actions = []
recording = False

def on_move(x, y):
    if recording:
        actions.append({'type': 'move', 'position': (x, y), 'time': time.time()})

def on_click(x, y, button, pressed):
    if recording:
        actions.append({'type': 'click', 'button': str(button), 'position': (x, y), 'time': time.time()})

def on_press(key):
    if recording:
        try:
            actions.append({'type': 'keyboard', 'key': key.char, 'event_type': 'press', 'time': time.time()})
        except AttributeError:
            actions.append({'type': 'keyboard', 'key': key.name, 'event_type': 'press', 'time': time.time()})

def on_release(key):
    if recording:
        try:
            actions.append({'type': 'keyboard', 'key': key.char, 'event_type': 'release', 'time': time.time()})
        except AttributeError:
            actions.append({'type': 'keyboard', 'key': key.name, 'event_type': 'release', 'time': time.time()})

mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

def start_recording():
    global recording, actions
    actions = []
    recording = True
    mouse_listener.start()
    keyboard_listener.start()

def stop_recording():
    global recording
    recording = False
    mouse_listener.stop()
    keyboard_listener.stop()

def save_actions(filename):
    with open(filename, 'w') as f:
        json.dump(actions, f)

def load_actions(filename):
    with open(filename, 'r') as f:
        return json.load(f)
