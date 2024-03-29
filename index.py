from pynput.keyboard import Listener, Key       #key capturing, and event listener modules from pynput
import matplotlib.pyplot as plt    #for plotting data
import time     #timer for key press
import pandas as pd
import csv 

# password :  .tie5Roanl

#subject,sessionIndex,rep,H.period,DD.period.t,UD.period.t,H.t,DD.t.i,UD.t.i,H.i,DD.i.e,UD.i.e,H.e,DD.e.five,UD.e.five,H.five,DD.five.Shift.r,UD.five.Shift.r,H.Shift.r,DD.Shift.r.o,UD.Shift.r.o,H.o,DD.o.a,UD.o.a,H.a,DD.a.n,UD.a.n,H.n,DD.n.l,UD.n.l,H.l,DD.l.Return,UD.l.Return,H.Return

start_times = {}; 
hold_time = []
DownDown = []
UpDown = []
previous_press_time = None
previous_up_time = None

print('TEST')

def switch_case(arg):
    return {
        1: '.',
        2: 't',
        3: 'i',
        4: 'e',
        5: '5',
        6: 'R',
        7: 'o',
        8: 'a',
        9: 'n',
        10: 'l'
    }.get(arg, 'INVALID')


def press(key):
    #Access varible globally
    global previous_press_time
    #time of press
    current_time = time.time()

    #Essentially if there was a key press prior
    if previous_press_time is not None:
        #time between last key press and current, ie. time starts when previous key is pressed, and stops when current key is pressed (DD)
        time_between = current_time - previous_press_time
        DownDown.append(time_between)
        print('DD', DownDown)
    
    #If there was a key prior
    if previous_up_time is not None:
        #This serves as Up Down time, ie. Timer starts when previous key is let go, and stops when current key is pressed (UD)
        time_between = current_time - previous_up_time
        UpDown.append(time_between)
        print('UD', UpDown)

    #Time of press for current key
    start_times[key] = current_time
    #Update previous time as current time (Current key will become previous key for the next key press)
    previous_press_time = current_time

def release(key):

    if key == Key.esc:
        # Stop listener
        return False
    
    global previous_up_time
    #time of release
    current_time = time.time()
    #If released key is pressed key (insured with listner.join)
    if (key in start_times):
        #Hold time. ie. time starts when key is pressed, and stops when key is lifted (H)
        hold = current_time - start_times[key]
        hold_time.append(hold)
        print('Hold', hold_time)
        #clear key in preporation for next
        del start_times[key]
    
    #Used for UP DOWN time
    previous_up_time = current_time


    # Start the listener
with Listener(on_press=press, on_release=release) as listener:
    listener.join()


        

