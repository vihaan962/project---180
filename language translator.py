# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:43:13 2022

@author: VIHAAN KATHURIA
"""

from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root=Tk()
root.geometry("800x500")
root.configure(bg = "red")

title = Label(root,text = "Language Translator",bg = "red",font = ("Calibri",20,"bold"))
title.place(relx = 0.5,rely = 0.1,anchor = CENTER)

input_label = Label(root,text = "Enter Text",bg = "red",font = ("Calibri",15,"bold"))
input_label.place(relx = 0.08,rely = 0.3,anchor = CENTER)

input_text = Text(root,bg = "white",font =("calibri",15,"italic"),height = "7",wrap = WORD, width = "20",padx = 5,pady = 10,bd = 0)
input_text.place(relx = 0.15, rely = 0.6, anchor = CENTER)
root.mainloop()