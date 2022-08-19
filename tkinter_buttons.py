#practice User Interface (UI) there are 3 buttons and each one has a differnt function
#the CLOSE button will close the program but before closing it will present a message box notifying that it is closing
#the RANDOM button will be calling a file called 'andom' and will retrive one of the constants in that file 
# the ULESS button will run the function (which is a bunch of loops) from 'long_pro' 
# ULESS was to observe how the UI will react if it has a  long program to run in the background
# it also displays a little loading screen and an error message if there are any problems with the function running #
import tkinter 
from tkinter import *
from tkinter import Button, Image,messagebox,Label 
import sys

#creating a new screen
#pantalla is screen in spanish
pantalla=tkinter.Tk()
#name of the screen
pantalla.title('Patalla')

#creating function that will be used and binded to buttons

#this fuction closes the screen 
def click1():
    messagebox.showwarning("Alert","CONSOLE WILL BE CLOSING")
    pantalla.destroy()
#this function will import 'num' from file andom for and displays 2 pop up messages
def click2():
    from andom import num
    messagebox.showinfo("Hello", num)
    messagebox.showinfo("HELLO","Hello World")
#this function will hide the buttons and image and display a loading message
def hide(): 
    Widget.pack_forget(random_btn)
    Widget.pack_forget(Uless_btn)
    Widget.pack_forget(close_btn)
    Widget.pack_forget(limg)
    Widget.pack(label1)
    label1.pack(ipadx=50,ipady=50)
    Widget.pack(label2)
    label2.pack(ipadx=50)
#this function will reveal all the buttons that were hidden and then hide the loading message
def revl():
    Widget.pack(random_btn)
    random_btn.pack(side=tkinter.TOP, anchor=W)
    Widget.pack(Uless_btn)
    Uless_btn.pack(anchor= tkinter.W, side=tkinter.TOP, padx=(100,0))
    Widget.pack(close_btn)
    close_btn.pack(side=tkinter.TOP, anchor=E)
    Widget.pack(limg)
    limg.pack(fill=BOTH)
    Widget.pack_forget(label1)
    Widget.pack_forget(label2)
#this function is  mix of function it calls other functions     
def madness():
    hide()#calling hide function
    messagebox.showwarning('WARNING',"This may take a while")#display warning message
    runing=True
# a loop to run certian functions after certian conditions have been met
    while runing:    
        #will import function ED and run it
        try:
            from long_pro import ED
            ED()
        # if there are any errors they will be caught and display a message on the error
        except:
            messagebox.showerror('ERROR',sys.exc_info()[1])
        runing=False
    #displays a message that the function had finished runnning
    messagebox.showinfo("FINISHED","Its all done now")
    #will bring back original screen and leave the loading screen
    revl()

#making the buttons- formatting them and adding attributes
close_btn=Button(pantalla,text="CLOSE Button", fg='red', command=click1, activebackground='#e32636',height=3)
close_btn.pack(side=tkinter.TOP, anchor=E)

random_btn=Button(pantalla,text='RANDOM Button', fg='blue',command=click2)
random_btn.pack(side=tkinter.TOP, anchor=W)

Uless_btn=Button(pantalla,text='ULESS Button',height=3, command=madness)
Uless_btn.pack(anchor= tkinter.W, side=tkinter.TOP, padx=(100,0))
 
#making labels which will turn in to laoding message
label1=Label(pantalla,text= 'Runing.......',font=('Helvetica',36))
label2=Label(pantalla,text='Please stand by',font=('Helvetica',36))

#imports image file 
logo=tkinter.PhotoImage(file="tree.png")
#sets image to the background 
limg=Label(pantalla, i=logo)
limg.pack()

pantalla.mainloop()
