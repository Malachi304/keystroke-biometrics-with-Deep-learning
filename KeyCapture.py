from pynput.keyboard import Listener, Key       #key capturing, and event listener modules from pynput
import matplotlib.pyplot as plt    #for plotting data
import time     #timer for key press
import pandas as pd
import numpy as np
import csv


#======================================================================================================================================
#READ ME
#Password of length 11 (includes enter key at end), typed 50 times across 8 sessions, totalling 400 unique key strokes.
#Day between each session totalling 8 days if done concurently.
#Program uses key press/release times to record total key HOLD (H) time, UP DOWN (UD) time, and DOWN DOWN (DD) time (Explained further in code comments).
#Data is then appended to Data.csv for training. 

# password for referance :  .tie5Roanl

#Categories from Data set for referance : 
#subject,sessionIndex,rep,H.period,DD.period.t,UD.period.t,H.t,DD.t.i,UD.t.i,H.i,DD.i.e,UD.i.e,H.e,DD.e.five,UD.e.five,H.five,DD.five.Shift.r,
#UD.five.Shift.r,H.Shift.r,DD.Shift.r.o,UD.Shift.r.o,H.o,DD.o.a,UD.o.a,H.a,DD.a.n,UD.a.n,H.n,DD.n.l,UD.n.l,H.l,DD.l.Return,UD.l.Return,H.Return
#======================================================================================================================================

keys = ['.','t', 'i', 'e', '5', 'o', 'a','n', '1']

#UPDATE THIS NUMBER EACH SESSION (8 sessions)
session_count = 1
#Resets at 50 (50 passwords typed in a session)
rep_count = 0

#new row of data to add to dataset. Already includes userUniqueID, Session count, and Rep count
rep_row = ['s060',session_count, rep_count]

start_times = {}; 
hold_time = None
DownDown = None
UpDown = None

previous_press_time = None
previous_up_time = None

def press(key):
    #Access varible globally
    global previous_press_time
    global DownDown
    global UpDown
    global rep_count
    global keys
    global rep_row
    global start_times

    
    #time of press
    current_time = time.time()

    if key == Key.esc:
     
        return False

    #Check if key is type 'char' and in Keys
    if hasattr(key, 'char') and key.char in keys or key == Key.enter or key == Key.shift:
        print(key)


        #Essentially if there was a key press prior
        if previous_press_time is not None:
                #time between last key press and current, ie. time starts when previous key is pressed, and stops when current key is pressed (DD)
                time_between = current_time - previous_press_time
                DownDown = time_between

                #adding to row 
                rep_row.append(DownDown)

        
            #If there was a key prior
        if previous_up_time is not None:
            #This serves as Up Down time, ie. Timer starts when previous key is let go, and stops when current key is pressed (UD)
            time_between = current_time - previous_up_time
            UpDown = time_between
            rep_row.append(UpDown)

        start_times[key] = current_time

        #Update previous time as current time (Current key will become previous key for the next key press)
        previous_press_time = current_time
     

        
        #if key is not 'shift,' or in Keys
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
    #time of release
    current_time = time.time()

   
    #If released key is pressed key (insured with listner.join)
    if hasattr(key, 'char') and key.char in keys or key == Key.enter or key == Key.shift:
        #Hold time. ie. time starts when key is pressed, and stops when key is lifted (H)
        time_between = current_time - start_times[key]
        hold_time = time_between
        rep_row.append(hold_time)

        #Used for UP DOWN time
        previous_up_time = current_time

        if key == Key.enter and len(rep_row) == 34:
            print(len(rep_row))
            previous_press_time = None
            previous_up_time = None
            hold_time = None
            DownDown = None
            UpDown = None

            if rep_count == 50:
                print("Session Complete")
                return
            rep_count = rep_count + 1

            #append new row to csv       
            with open('myData.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(rep_row)
 
             # print message
            print(f"Data appended successfully. REP: {rep_count}")
            rep_row.clear()
            rep_row = ['s060',session_count, rep_count]
        elif key == Key.enter and len(rep_row) != 34:
            previous_press_time = None
            previous_up_time = None
            hold_time = None
            DownDown = None
            UpDown = None
            rep_row.clear()
            rep_row = ['s060',session_count, rep_count]
            print("Invalid, reseting")



        #clear key in preporation for next
        del start_times[key]
    





    # Start the listener
with Listener(on_press=press, on_release=release) as listener:
    listener.join()


'''
        if key == Key.enter and len(rep_row)==34:
            if rep_count == 50:
                return
            rep_count = rep_count + 1

            #append new row to csv       
            with open('myData.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(rep_row)
 
             # print message
            print(f"Data appended successfully. REP: {rep_count}")
            rep_row = ['s060',session_count, rep_count]
        elif key == Key.enter and len(rep_row) != 34:

            rep_row = ['s060',session_count, rep_count]
            print(len(rep_row))
            print("Invalid, reseting")
'''
