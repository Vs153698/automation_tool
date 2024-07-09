import time
import pyautogui

def play_actions(actions, speed=1.0):
    start_time = actions[0]['time']
    for action in actions:
        time.sleep((action['time'] - start_time) / speed)
        start_time = action['time']

        if action['type'] == 'move':
            pyautogui.moveTo(action['position'][0], action['position'][1])
        elif action['type'] == 'click':
            pyautogui.click(x=action['position'][0], y=action['position'][1], button=action['button'].split('.')[-1])
        elif action['type'] == 'keyboard':
            if action['event_type'] == 'press':
                pyautogui.press(action['key'])
            elif action['event_type'] == 'release':
                pyautogui.keyUp(action['key'])
