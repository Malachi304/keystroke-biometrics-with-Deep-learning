from pynput.keyboard import Key, Listener       #key capturing, and event listener modules from pynput
import matplotlib.pyplot as plt    #for plotting data
import time     #timer for key press

# password :  .tie5Roanl

start_times = {}; 
press_time_total=0
count=0
file1 = open("keys.txt", "w+") 

#DD
#UD
#H

def switch_case(arg):
    switch ={
        1: '.'
        2: 't'
        3: 'i'
        4: 'e'
        5: '5'
        6: 'R'
        7: 'o'
        8: 'a'
        9: 'n'
        10: 'l'
    }

#on key press
def press(key):
    start_times[key] = time.time()
    print(f"Press")

#on key release
def release(key):
    global press_time_total, count
    count+=1
    print(f"release")
    if key == Key.esc:  #end listener
        file1.write(f"PRESS TIME TOTAL={press_time_total} {count} ")
        return False
    
    start_time = start_times.get(key,0)
    press_time = time.time() - start_time  # Calculate the time taken to press the key

    print(f"{press_time:.5f}")
    file1.write(f"{press_time} \n")
    press_time_total += press_time  # Sum of all press_times


# Collect events until released
with Listener(
        on_press=press,
        on_release=release) as listener:
    listener.join()

file1.close() 
