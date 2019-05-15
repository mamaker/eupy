#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
label-eg2.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python-image.gif")


explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root, 
          text=explanation, 
          font = "Verdana 26 bold",
          justify=tk.LEFT,
          padx = 10, 
          compound = tk.LEFT,
          image=logo).pack(side="right")

root.mainloop()
