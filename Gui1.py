
import tkinter
from tkinter import Button,messagebox

pantalla=tkinter.Tk()
pantalla.title('Patalla')
canv= tkinter.Canvas(pantalla,bg='white', height=500, width=800)
# must make function fir button before making button
def click1():
    messagebox.showwarning("Alert","CONSOLE WILL BE CLOSING")
    pantalla.destroy()#close Window 
def click2():
    from andom import num# calling file to import variables
    messagebox.showinfo("Hello", num)#printing current date/time
    messagebox.showinfo("HELLO","hello World")
#buttons
#making the button and adding its attributes
close_btn=Button(pantalla,text="Close", fg='red', command=click1, activebackground='#e32636')
#brings button to the canvas
close_btn.pack(side=tkinter.TOP)

time_btn=Button(pantalla,text='Date', fg='blue',command=click2)
time_btn.pack(side=tkinter.RIGHT,anchor= tkinter.SW)

Useless_btn=Button(pantalla,text='Useless Button',height=5)
Useless_btn.pack(anchor= tkinter.CENTER,side=tkinter.RIGHT)


canv.pack()
pantalla.mainloop()
