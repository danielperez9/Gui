from cProfile import label
from tkinter import *
from tkinter import messagebox
import time
from tkinter import ttk
import tkinter

#windows size
window_width=1000
window_hieght=1000
#position of label1
int_pos_x=100
init_pos_y=100
#of spaces moving
mov=10
#refresh rate of movemnet 
fresh=0.001

def Window_animation():
    Winodow=Tk()
    Winodow.title="Practive window"
    Winodow.geometry(f'{window_width}x{window_hieght}') # fromat of window size
    return Winodow


def canvas_animatoin(Window):
    #label=ttk.Label(Window, text='L', font=('Times', 36))
    canvas=tkinter.Canvas(Window)
    canvas.configure(bg="White")
    