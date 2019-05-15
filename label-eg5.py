#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
label-eg4.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green", font="Verdana 26")
label.pack()
counter_label(label)
tk.Button(root, text='Stop', width=25, font="Verdana 26",
                   command=root.destroy).pack()

root.mainloop()
