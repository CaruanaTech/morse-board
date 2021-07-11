from pynput import keyboard
from pynput.keyboard import Key, Controller
from keyboard import block_key

from application.utils import determine_character_press, morse_to_character
from application.config import morse_key, submit_key

import time


controller = Controller()

block_key(morse_key)  # dont press the morse key itself
block_key(submit_key)  # dont press the submit key itself

current_letter = ""

def on_key_release(key):
    global current_letter
    key = str(key).replace("'", "")
    
    if key == morse_key:
        time_taken = round(time.time() - t, 2)
        character = determine_character_press(time_taken)
        controller.press(character)
        current_letter += character
        print(current_letter)
    
    if key == submit_key:
        backspace_amount = len(current_letter)
        
        for x in range(backspace_amount):  # remove our current morse entry
            controller.press(Key.backspace)
            print("pressed backspace")
            time.sleep(0.01)
        
        final_character = morse_to_character(current_letter)

        if final_character:
            controller.press(final_character)
        
        current_letter = ""  # reset our morse string
        return False

    return False

def on_key_press(key):
    return False


while True:
    with keyboard.Listener(on_press = on_key_press) as press_listener:
        press_listener.join()
    
    t = time.time()  # count time pressed

    with keyboard.Listener(on_release = on_key_release) as release_listener:
        release_listener.join()
