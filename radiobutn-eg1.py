#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
radiobutn-eg1.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

root = tk.Tk()
v = tk.IntVar()

tk.Label(root, 
        text="""Choose a 
programming language:""",
        font = "Verdana 26 bold",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root, 
              text="Python",
              font = "Verdana 26 bold",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="Perl",
              font = "Verdana 26 bold",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=tk.W)

root.mainloop()
