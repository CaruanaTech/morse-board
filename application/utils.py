from application.config import dash_time
from pynput.keyboard import Controller
from application.dictionary import chars

def determine_character_press(time):
    if time >= dash_time:
        return "-"
    else:
        return "."
    
def morse_to_character(morse_input):
    for char in chars:
        if morse_input == char:
            print(f"converted {morse_input} to {chars[char]}")
            return chars[char]
        
    return False  # only called if no match is found