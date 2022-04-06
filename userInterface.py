#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:17:03 2017

@author: kmistri
"""
import numpy as np
from pyAudioAnalysis import audioTrainTest as aT
from Tkinter import *
import Tkinter,tkFileDialog
import tkMessageBox

def loadFile():
    global fileName
    fileName=tkFileDialog.askopenfilename()
    print fileName;
    selection = "Selected File : " + str(fileName)
    label1.config(text = selection)  
    try:
        print (fileName)
        global x
        f1=open(fileName,"r")
        x=f1.read()
        f1.close()
    except:
        print("NO such File")

def Test():
    isSignificant = 0.5 #try different values.
    
    # P: list of probabilities
    Result, P, classNames = aT.fileClassification(fileName, "svmModel", "svm")
    winner = np.argmax(P) #pick the result with the highest probability value.
    print (winner)
    
    
    # is the highest value found above the isSignificant threshhold? 
    print(P[winner])
    if P[winner] > isSignificant :
      print("File: " +fileName + " is in category: " + classNames[winner] + ", with probability: " + str(P[winner]))
      print(str(P))
      label2.config(text="FileName: "+str(fileName))
      label3.config(text="Predicted Category: "+str(classNames[winner]))
      label4.config(text="Probability: "+str(P[winner]))
    else :
      print("Can't classify sound: " + str(P))
      tkMessageBox.showinfo("Can't Classify",str(P))
      
root=Tkinter.Tk();
root.configure(background='#5d5a58')
root.minsize(width=500,height=200)
root.maxsize(width=800,height=600)

load=Tkinter.Button(root, text="Choose a File", bg = "#880e4f" ,fg = "#ffffff", command=loadFile, width=70 , font = "Verdana 10 bold", activebackground="#b71c1c", activeforeground="#ffffff")
load.pack(pady=10);


label1 = Tkinter.Label(root , text = "Selected File : " , bg = "#5d5a58" ,fg = "#90a4ae" , font = "Helvetica 8 bold")
label1.pack(padx=20)

testButton=Tkinter.Button(root, text="Test", bg = "#546e7a" ,fg = "#ffffff", command=Test ,width=70 , font = "Verdana 10 bold",activebackground="#b71c1c", activeforeground="#ffffff")
testButton.pack(pady=10);

label2 = Tkinter.Label(root , text = "File Name : " , bg = "#5d5a58" ,fg = "#ffeb3b" , font = "Helvetica 8 bold")
label2.pack(padx=20)

label3 = Tkinter.Label(root , text = "Predicted Category : " , bg = "#5d5a58" ,fg = "#ffeb3b" , font = "Helvetica 8 bold")
label3.pack(padx=20)

label4 = Tkinter.Label(root , text = "Accuracy : " , bg = "#5d5a58" ,fg = "#ffeb3b" , font = "Helvetica 8 bold")
label4.pack(padx=20)

root.mainloop()



"""
Confusion Matrix:
        reg     dis     cou     rock    cla     met     hip     jazz    blu
reg     7.8     0.6     0.3     0.3     0.0     0.2     1.2     0.3     0.5
dis     0.8     7.2     0.8     0.9     0.1     0.3     0.8     0.0     0.2
cou     0.2     0.6     6.8     2.1     0.0     0.5     0.0     0.1     0.8
rock    0.4     1.5     1.6     5.7     0.0     1.1     0.0     0.1     0.6
cla     0.0     0.0     0.0     0.4     10.2    0.0     0.0     0.5     0.0
met     0.0     0.6     0.1     1.0     0.0     9.4     0.1     0.0     0.0
hip     2.3     0.7     0.0     0.0     0.0     0.4     7.4     0.1     0.2
jazz    0.1     0.4     0.5     0.2     1.1     0.1     0.0     7.5     1.3
blu     0.2     0.2     1.1     0.4     0.1     0.4     0.2     0.5     8.0
Selected params: 0.01000
"""
