
# Analysis Of Keystoke Authentication Across Different Systems Utalizing Deep Learning

### GOAL:
Deep learning model for keystroke authenticaion across different systems (keyboards).

### METHOD:
Dataset is trained on over 50 typists. Specifics for how that data was collected by origional researchers is below. 

I collected my own keystroke data using a self-made keystoke (logger) capturing python script,
which collects time-stamp data of keys pressed in order to form a password. 
My keystrokes are added to the training dataset in order to predict 
my keystroke patterns when typing a specific password mentioned below.

After training, I will pass a new set of keystrokes for prediction, using two seperate keyboards.
This will measure the potential accuracy of deep learning models
with keystokes across different systems. 

### DETAILS OF DATA CAPTURE AND PROCESSING:

password for referance :  .tie5Roanl

Password of length 11 (includes 'enter' key at end), typed 50 times across 8 sessions, totaling 400 unique key strokes.
Day between each session totalling 8 days if done concurently.

KeyCapture program uses key press/release times to record total key HOLD (H) time, UP DOWN (UD) time, and DOWN DOWN (DD) time (Explained further in code).
Data is then appended to newData.csv, before being processed in ProcessData.py, and then being output as ProcessedData.csv. 
ProcessedData is then combined with the orional data of over 50 unique typists before training. 

Categories from Data set for referance : 
subject,sessionIndex,rep,H.period,DD.period.t,UD.period.t,H.t,DD.t.i,UD.t.i,H.i,DD.i.e,UD.i.e,H.e,DD.e.five,UD.e.five,H.five,DD.five.Shift.r,
UD.five.Shift.r,H.Shift.r,DD.Shift.r.o,UD.Shift.r.o,H.o,DD.o.a,UD.o.a,H.a,DD.a.n,UD.a.n,H.n,DD.n.l,UD.n.l,H.l,DD.l.Return,UD.l.Return,H.Return

NOTE: Subject is the label we are training for, rep and sessionindex are not important for training and may be redacted.
      The final 31 Categories are the features being passed to the model. 
      Example of features: "UD.period.t" traslates to time between releasing '.' key (UPtime), and time pressing 't' key (DOWNtime)

