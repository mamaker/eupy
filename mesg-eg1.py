#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mesg-eg1.py
Created on Tue May 14 14:12:58 2019

@author: madhu
"""

import tkinter as tk

master = tk.Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(master, text = whatever_you_do)
msg.config(bg='lightgreen',
           padx = 20, pady = 20,
           font=('times', 24, 'italic'),
           width=2000)
msg.pack()

tk.mainloop()
