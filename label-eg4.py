#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
label-eg4.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

root = tk.Tk()

tk.Label(root, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times 26").pack()

tk.Label(root, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 26 bold italic").pack()

tk.Label(root, 
		 text="Blue Text in Verdana bold",
         padx = 20,
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 26 bold").pack()


root.mainloop()
