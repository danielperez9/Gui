
import tkinter
from tkinter import *
from tkinter import Button, Image,messagebox
from PIL import Image,ImageTk 

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
close_btn=Button(pantalla,text="Close", fg='red', command=click1, activebackground='#e32636', height=4)
#brings button to the canvas
close_btn.pack(side=tkinter.TOP, anchor=W)

random_btn=Button(pantalla,text='Random', fg='blue',command=click2)
random_btn.pack(side=tkinter.TOP, anchor=W)

Useless_btn=Button(pantalla,text='Useless Button',height=3)
Useless_btn.pack(anchor= tkinter.W, side=tkinter.TOP, padx=(100,0))
# importing image 
logo=ImageTk.PhotoImage(Image.open("Ar.png"))

label1=tkinter.Label(text="Argonne National Laboratory", font=('calibri', 20))
label1.pack(pady=(50,1), padx=(200,0),anchor=tkinter.W, side= tkinter.TOP)


canv.create_image(200,200,image=logo,anchor=tkinter.CENTER)# making image appear on the canvas
canv.pack()
pantalla.mainloop()
