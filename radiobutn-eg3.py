#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
radiobutn-eg3.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

root = tk.Tk()
v = tk.IntVar()
v.set(20)  # initializing the choice, i.e. Python

languages = [
    ("Python",10),
    ("Perl",20),
    ("Java",30),
    ("C++",40),
    ("C",50)
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         font = 'Verdana 26 bold',
         padx = 20).pack()

#for val, language in enumerate(languages):
for language in languages:
    tk.Radiobutton(root, 
                  text=language[0],
                  font = 'Verdana 26 bold',
                  width=20,
                  indicatoron = 0,
                  padx = 20, 
                  variable=v, 
#                  value=val,
                  value=language[1],
                  command=ShowChoice).pack(anchor=tk.W)

root.mainloop()
