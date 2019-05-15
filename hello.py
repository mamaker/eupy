#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hello.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

root = tk.Tk()
root.title('Hello Screen')
w = tk.Label(root, text="Hello Tkinter!")
w.pack()

root.mainloop()
