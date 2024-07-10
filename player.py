import time
import pyautogui

def play_actions(actions, speed=1.0):
    if not actions:
        return

    start_time = actions[0]['time']
    last_time = start_time

    for action in actions:
        current_time = action['time']
        sleep_time = (current_time - last_time) / speed

        # Only sleep if the time difference is significant
        if sleep_time > 0.01:  # You can adjust this threshold
            time.sleep(sleep_time)

        last_time = current_time

        if action['type'] == 'move':
            pyautogui.moveTo(action['position'][0], action['position'][1], duration=0)
        elif action['type'] == 'click':
            pyautogui.click(x=action['position'][0], y=action['position'][1], button=action['button'].split('.')[-1])
        elif action['type'] == 'keyboard':
            if action['event_type'] == 'press':
                pyautogui.press(action['key'])
            elif action['event_type'] == 'release':
                pyautogui.keyUp(action['key'])

