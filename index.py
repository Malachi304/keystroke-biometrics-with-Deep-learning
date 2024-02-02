#key capturing, and event listener modules from pynput
from pynput.keyboard import Key, Listener
#timer for key press
import time

start_times = {}
file1 = open("keys.txt", "w+") 


def press(key):
    start_times[key] = time.time(); 
    print(f"{key} Press")


def release(key):
    print(f" {key} release")
    if key == Key.esc:
        # Stop listener
        return False
    start_time = start_times.get(key,0)
    press_time = time.time() - start_time  # Calculate the time taken to press the key
    print(f"{key} pressed for {press_time:.5f} seconds")
    file1.write(f"press_time: {press_time} hello \n")


# Collect events until released
with Listener(
        on_press=press,
        on_release=release) as listener:
    listener.join()

file1.close() 
