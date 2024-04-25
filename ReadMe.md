
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

Keyboards used here: 
```
Keyboard1 : lenovo | Slim Pro-7 14ARP8
Keyboard2 : HP | 803181-001
Keyboard3 : Dell | L100
Keyboard4 : IBUYPower | GKB100
Keyboard5 : HyperX | AG001
Keyboard6 : Microsoft |  Natural Ergonomic 1048
Keyboard7 : Havit | Mechanical Gaming HV-KB380L

```

### DETAILS OF DATA CAPTURE AND PROCESSING:

Text used to capture data:  .tie5Roanl

A password of length 11 (includes 'enter' key at end), typed 50 times across 8 sessions, totaling 400 unique keystrokes.
A day between each session totaling 8 days if done concurrently.

KeyCapture program uses key press/release times to record total key HOLD (H) time, UP DOWN (UD) time, and DOWN DOWN (DD) time (Explained further in code).
Data is then appended to newData.csv, before being processed in ProcessData.py, and then being output as ProcessedData.csv. 
ProcessedData is then combined with the original data of over 50 unique typists before training. 

Categories from the Data set for reference: 
```
subject,sessionIndex,rep,H.period,DD.period.t,UD.period.t,H.t,DD.t.i,UD.t.i,H.i,DD.i.e,UD.i.e,H.e,DD.e.five,UD.e.five,H.five,DD.five.Shift.r,UD.five.Shift.r,H.Shift.r,DD.Shift.r.o,UD.Shift.r.o,H.o,DD.o.a,UD.o.a,H.a,DD.a.n,UD.a.n,H.n,DD.n.l,UD.n.l,H.l,DD.l.Return,UD.l.Return,H.Return

```

subjects are labled s002-s057, new subject's data is named s060.
>[!NOTE]
> To add more data, start from s061 or further

The subject is the label we are training for with accuracy.
Rep and session index are not important for training and may be redacted before training, to avoid neurons using them as training data.
The final 31 Categories are the features being passed to the model. 

### PREPROCESSING:

The new subject's data is combined with the original dataset.
Then a target column is added to each row of data for label encoding.
This target is set to 1 (the subject we want to train on), or zero.
This becomes our y split when creating the model.

Resulting, processed data for the target user looks like this:

```
0.0772,0.2314,0.1542,0.0804,0.0965,0.0161,0.0974,0.0974,0.0,0.1028,0.1658,0.0629,0.0863,0.3533,0.267,0.1952,0.2421,0.0469,0.0981,0.1294,0.0313,0.1299,0.1612,0.1487,0.0933,0.1648,0.0715,0.0862,0.135,0.0488,0.0668,1

```

The subject, rep, and sessionIndex columns are removed before training.

### ANALYSIS/ RESULTS:

```
Keyboard False Acceptance Rates
-------------------------------------------------------------
Lenovo (50 predictions) = 0.06
HP (10 predictions) = 0.3
Dell (10 predictions) = 0.1
HyperX (15 predictions) = 0.0
Havit (15 predictions) = 0.0666
iBuyPower (15 predictions) = 1.0
Microsoft (10 predictions) = 0.4
```

### CONCLUSION:
Although data used for keyboard predictions was low in quantity, these results give us a general 
idea of how keystroke systems transfer across systems and have hopeful results.

### FUTURE WORK/ HOW TO CONTRIBUTE:
To get a better analysis, there needs to be more data from each keyboard used 
in testing. Rather than 10-15 prediction data points, it would be prefered to 
have data on each keyboard in the range of 50-100 or more for accurate stats.

Outliers remain a point of interest in this study.
The consequences of removing outliers at different thresholds 
are not fully understood.

The system could eventually be expanded to allow for free text keystrokes, as
this would be required for live authentication, whereas this pipeline
is currently based on password authentication.

The foundations for a pipeline to study keystroke biometrics are set.
To contribute, add keystrokes to the original dataset,along with various 
keystrokes from different systems. 



