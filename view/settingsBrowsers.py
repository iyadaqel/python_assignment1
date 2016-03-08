# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:06:09 2016

@author: begum
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

win_root = tk.Tk()
win_root.title("Settings")
win_root.resizable(width=True , height=False)


# file
browseFile = ttk.Label(win_root , text="Browse File" , font=("Helevetica",10), foreground="black")
browseFile.grid(column=0 , row=0)


# directory
browseFolder = ttk.Label(win_root , text="Browse Folder" , font=("Helevetica",10), foreground="black")
browseFolder.grid(column=0 , row=1)

#download
download = ttk.Label(win_root , text="Download the back-up file" , font=("Helevetica",10), foreground="black")
download.grid(column=0 , row=2)

#change the theme
theme = ttk.Label(win_root , text="Change background theme" , font=("Helevetica",10), foreground="black")
theme.grid(column=0 , row=3)

def askFolder():
    dirname = askdirectory()
    print(dirname)
      
def askFile():
    filepath = askopenfilename()
    print(filepath)



# Buttons
action = ttk.Button(win_root, text="Browse File", command=askFile)
action.grid(column=1 , row=0)
action = ttk.Button(win_root, text="Browse Folder", command=askFolder)
action.grid(column=1 , row=1)
action = ttk.Button(win_root, text="Download", command=asksaveasfilename)
action.grid(column=1 , row=2)
action = ttk.Button(win_root, text="Change the Theme")
action.grid(column=1 , row=3)



win_root.mainloop()

