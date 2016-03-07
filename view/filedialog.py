# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:57:43 2016

@author: begum
"""
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.title("Settings")
root.resizable(width=True , height=False)

root.withdraw()

"""
file_path = askopenfilename()
print(file_path)
"""

"""
dirname = askdirectory()
print(dirname)
"""

def askFolder():
  foldername = tkFileDialog.askdirectory()
  print(foldername)
  
def askFile():
  filename = tkFileDialog.askopenfilename()
  print(filename)

action = ttk.Button(root, text="Browse File" , command=askFile())
action.grid(column=1 , row=1)

action2 = ttk.Button(root, text="Browse Directory" , command=askFolder())
action.grid(column=1 , row=2)

root.mainloop()
