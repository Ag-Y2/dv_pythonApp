#-*- coding: utf-8 -*-
from tkinter import *

#import tkinter
'''
from tkinter import *
from tkinter import messagebox
'''

count = 0
window = Tk()
root = window
frame = Frame(window)
def init_gui():

    sb_xyis = Scrollbar(window, orient="horizontal")
    sb_xyis.pack(side = BOTTOM, fill = X)

    window.title("gui interface")
    window.geometry("640x400+300+50")
    window.resizable(False, False)

    label=Label(window, text="hi, there")
    label.pack()

    label_count= Label(window, text=0)
    label_count.pack()

    def countUp():
        global count
        count += 1
        label_count.config(text=str(count))
        #add_to_list()
 

    button = Button(window, overrelief="solid", width=15, command=countUp, repeatdelay=1000, repeatinterval=100)
    button.pack()

    frame.pack()
    window.mainloop()



def add_to_list(db_list):
    print('add to list')
    sb_yyis = Scrollbar(frame)
    sb_yyis.pack(side = RIGHT, fill= Y)
    listbox = Listbox(frame, selectmode="extended",width=60, height=10, yscrollcommand=sb_yyis.set)
    listcount = 0

    '''
        while listcount < 40:
            list_value = "i ate {0} apple".format(listcount)
            listbox.insert(listcount, list_value)
            listcount += 1
    '''

    for i in db_list:
        listbox.insert(listcount, i)
        listcount += 1

    listbox.pack(side='left')

