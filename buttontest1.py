# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:59:06 2020

@author: chenc
"""

def click1():
    textvar.set("我已經被按過了！")

import tkinter as tk

win = tk.Tk()
win.geometry("250x300")
textvar = tk.StringVar()
button1 = tk.Button(win, textvariable=textvar, command=click1, bg = "white", fg = "black")
textvar.set("按鈕")
button1.pack()
win.title("這是按鈕視窗")
win.mainloop()
