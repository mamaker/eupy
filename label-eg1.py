#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
label-eg1.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python-image.gif")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()
