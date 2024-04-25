
# Pipeline for the Analysis Of Keystroke Authentication Across Different Systems Utilizing Deep Learning

### GOALS:
Assess the Accuracy of Deep learning model for keystroke authentication across different systems (keyboards), to study
the potential use of dynamic, non-local biometric systems in the future.

Preprocessing the keystroke dataset produced in a study by Roy Maxion (School of Computer Science of Carnegie Mellon University),
to better understand the relationship between keystroke extraction.

Present a foundational pipeline 
for keystroke biometrics study, with a keystroke logger, data processing, model creation/prediction, and data/model statistics.

### METHOD:
Original Dataset by Roy Maxion is comprised of keystrokes from over 50 typists

https://www.kaggle.com/datasets/carnegiecylab/keystroke-dynamics-benchmark-data-set/data

I collected new data from subject s060 using a self-made keystroke capturing script,
which collects time-stamp data of keys pressed to form a password. 

Subject s060's keystrokes are combined with the original dataset for training.

After training, I will pass a new set of keystrokes from s060 for prediction, using various keyboard models.
This will measure the potential accuracy of deep learning models with keystrokes across different systems. 

### DETAILS OF DATA CAPTURE AND PROCESSING:

Text used to capture data:  .tie5Roanl

A password of length 11 (includes 'enter' key at end), typed 50 times across 8 sessions, totaling 400 unique keystrokes.
A day between each session totaling 8 days if done concurrently.

KeyCapture program uses key press/release times to record total key HOLD (H) time, UP DOWN (UD) time, and DOWN DOWN (DD) time (Explained further in code).
Data is then appended to newData.csv, before being processed in ProcessData.py, and then being output as ProcessedData.csv. 
ProcessedData is then combined with the original data of over 50 unique typists before training. 

Categories from the Data set for reference: 
subject,sessionIndex,rep,H.period,DD.period.t,UD.period.t,H.t,DD.t.i,UD.t.i,H.i,DD.i.e,UD.i.e,H.e,DD.e.five,UD.e.five,H.five,DD.five.Shift.r,
UD.five.Shift.r,H.Shift.r,DD.Shift.r.o,UD.Shift.r.o,H.o,DD.o.a,UD.o.a,H.a,DD.a.n,UD.a.n,H.n,DD.n.l,UD.n.l,H.l,DD.l.Return,UD.l.Return,H.Return

subjects are labled s002-s057, new subject's data is named s060.
>[!NOTE]
> To add more data, start from s061 or further

The subject is the label we are training for with accuracy.
Rep and session index are not important for training and may be redacted before training, to avoid neurons using them as training data.
The final 31 Categories are the features being passed to the model. 

### PREPROCESSING:

### STATISTICAL ANALYSIS:

Before any data processing, I wanted to see the correlation between the original Roy Maxion dataset, and my own keystroke data set.

I did this with Panda's correlation function. 
The results are contained in DataStats/Stat Information, under Pre-Outlier Stats.

Here, we see that many of the 'Hold' features are not very correlated with values close to 0 in both directions.
This indicates that there is potentially some discrepancy with how hold times were recorded between the two datasets.



### CONCLUSION:

### FUTURE WORK:


