from pynput.keyboard import Listener, Key       # Key capturing, and event listener modules from pynput
import time     # Timer for key press
import csv

keys = ['.','t', 'i', 'e', '5', 'o', 'a','n', '1']

# UPDATE THIS NUMBER EACH SESSION (8 sessions)
session_count = 1
# Resets at 50 (50 passwords typed in a session)
rep_count = 0

# New row of data to add to dataset. Already includes userUniqueID, Session count, and Rep count
rep_row = ['s060',session_count, rep_count]

# Holds times of current keystroke 
start_times = {}; 
# Features
hold_time = None
DownDown = None
UpDown = None

# Used to calculate features from UD and DD
previous_press_time = None
previous_up_time = None

# On press
def press(key):
    global previous_press_time
    global DownDown
    global UpDown
    global rep_count
    global keys
    global rep_row
    global start_times

    
    # Time of press
    current_time = time.time()

    # End session early
    if key == Key.esc:
        return False

    # Check if key is type 'char' and in Keys
    if hasattr(key, 'char') and key.char in keys or key == Key.enter or key == Key.shift:
        print(key)

        # Essentially if there was a key press prior
        if previous_press_time is not None:
                # time between last key press and current, ie. time starts when previous key is pressed, and stops when current key is pressed (DD)
                time_between = current_time - previous_press_time
                DownDown = time_between

                # Adding to row
                rep_row.append(DownDown)

        
        # If there was a key prior
        if previous_up_time is not None:
            # This serves as Up Down time, ie. Timer starts when previous key is let go, and stops when current key is pressed (UD)
            time_between = current_time - previous_up_time
            UpDown = time_between
            # Adding to row
            rep_row.append(UpDown)

        # Moment key is pressed
        start_times[key] = current_time

        # Update previous time as current time (Current key will become previous key for the next key press)
        previous_press_time = current_time
    
    # If key is not 'shift,' or in Keys
    elif key not in keys:
        print("Invalid")
    

def release(key):
    
    global previous_up_time
    global hold_time
    global keys
    global rep_row
    global rep_count
    global session_count
    global start_times
    global previous_press_time
    global DownDown
    global UpDown

    # Time of release
    current_time = time.time()

   
    # If released key is pressed key
    if hasattr(key, 'char') and key.char in keys or key == Key.enter or key == Key.shift:

        # Hold time. ie. time starts when key is pressed, and stops when key is lifted (H)
        time_between = current_time - start_times[key]
        hold_time = time_between
        rep_row.append(hold_time)

        # Used for UP DOWN time, when previous key was released 
        previous_up_time = current_time

        # If password is entered and correct number of row attributes are present
        if key == Key.enter and len(rep_row) == 34:
            # Reset all time stamps
            previous_press_time = None
            previous_up_time = None
            hold_time = None
            DownDown = None
            UpDown = None

            # End session
            if rep_count == 49:
                print("Session Complete")
                return
            rep_count = rep_count + 1

            # Append new row to csv       
            with open('data/keyboards.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(rep_row)
 
            # Print appened message
            print(f"Data appended successfully. REP: {rep_count}, Data length: {len(rep_row)}")
            # Reset for next row of data
            rep_row.clear()
            rep_row = ['s060',session_count, rep_count]

        # This is essentially a fail-safe. 
        # If we press the enter key before the row is completed, it resets that row
        # Utalize this for when incorrect keys are pressed, such as 't' key being pressed too early.
        elif key == Key.enter and len(rep_row) != 34:
            previous_press_time = None
            previous_up_time = None
            hold_time = None
            DownDown = None
            UpDown = None
            rep_row.clear()
            rep_row = ['s060',session_count, rep_count]
            print("Invalid, reseting")

        # Clear key in preporation for next
        del start_times[key]
    

# Start the listener
with Listener(on_press=press, on_release=release) as listener:
    listener.join()

