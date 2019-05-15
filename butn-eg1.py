#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
butn-eg1.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   font="Verdana 26 bold",
                   command=root.destroy)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Hello",
                   font="Verdana 26 bold",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
