#practice User Interface (UI) there are 3 buttons and each one has a differnt function
#the CLOSE button will close the program but before closing it will present a message box notifying that it is closing
#the RANDOM button will be calling a file called 'andom' and will retrive one of the constants in that file 
# the ULESS button will run the function (which is a bunch of loops) from 'long_pro' 
# ULESS was to observe how the UI will react if it has a  long program to run in the background
# it also displays a little loading screen and an error message if there are any problems with the function running 
# the JAVASCRIPT button tus java script code that was scripted in the python function
# the c_code button is intended to run a c progrm  inwhich will be in the terminal- a quiz #
import tkinter
from tkinter import *
from tkinter import Button, Image,messagebox,Label,Tk
import sys
from tkstylesheet import TkThemeLoader # a style sheet for the widgets on the screen 
import js2py#a plug in that will allow you add java script and run it 
# import sys, os, getopt  # plugins for the c code
#creating a new screen 
pantalla=Tk()
#name of the screen
pantalla.title('Patalla')

#creating function that will be used and binded to buttons
#this fuction closes the screen 
def click1():
    #message that will be displayed
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
    # Widget.pack_forget(c_code_btn)
    Widget.pack_forget(js_btn)
#this function will reveal all the buttons that were hidden and then hide the loading message
def revl():
    Widget.pack(random_btn)
    random_btn.pack(side=tkinter.TOP, anchor=W)
    Widget.pack(Uless_btn)
    Uless_btn.pack(anchor= tkinter.W, side=tkinter.TOP, padx=(100,0))
    Widget.pack(close_btn)
    close_btn.pack(side=tkinter.TOP, anchor=E)
    
    # Widget.pack(c_code_btn)
    # c_code_btn.pack (anchor= tkinter.CENTER, side=tkinter.TOP, padx=(100,0))
    Widget.pack(js_btn)
    js_btn.pack (anchor= tkinter.CENTER, side=tkinter.TOP, padx=(100,0))
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
#following function will be running java impemented script seen in the terminal
def Javas():
    print ("java script program ")
    JS1="console.log('Hallo')"
    JS2='''function lots()
    {
        let num1=100;
        let num2=1;
        for (let i=0; i<num1; i++)
        {
            num2=num2+4;
            let num3=0;
            console.log(num2);

            if (num2%5==0)
            {
                num3=num2;
                console.log("loop result: "+num3);
            }
        }
    }
    let x = lots();
    console.log('The End')
    '''
    resl=js2py.eval_js(JS1)
    result=js2py.eval_js(JS2)
    result

# def c_code():
    
#     c_file='c_Prac_file.c '
#     exe_file='tkinter_buttons.py'
#     opts,args=getopt.getopt(args,"i",['c_prac_file.c'])
#     for o, a in opts:
    
#             if o in ("-i","--ifile"):
#                 c_file=a+'.c'
#                 exe_file=a+'.exe'
#     os.system('g++'+c_file+'-o'+exe_file)
#     print ("Running "+exe_file)    
#     os.system(exe_file)
    

#making the buttons- formatting them and adding attributes
close_btn=Button(pantalla,text="CLOSE Button", fg='red', command=click1, activebackground='#e32636',height=3)
close_btn.pack(side=tkinter.TOP, anchor=E)
btnId=id(close_btn)

random_btn=Button(pantalla,text='RANDOM Button', fg='blue',command=click2)
random_btn.pack(side=tkinter.TOP, anchor=W)

Uless_btn=Button(pantalla,text='ULESS Button',height=3, command=madness)
Uless_btn.pack(anchor= tkinter.W, side=tkinter.TOP, padx=(100,0))

js_btn= Button(pantalla, text="JavaScipt Button",command=Javas,height=3)
js_btn.pack (anchor= tkinter.CENTER, side=tkinter.TOP, padx=(100,0))
 
# c_code_btn= Button(pantalla, text="C program Button",command=c_code,height=3)
# c_code_btn.pack (anchor= tkinter.CENTER, side=tkinter.TOP, padx=(100,0)) 

#making labels which will turn in to laoding message
label1=Label(pantalla,text= 'Running.......',font=('Helvetica',36))
label2=Label(pantalla,text='Please stand by',font=('Helvetica',36))

#imports image file (PNG)
logo=tkinter.PhotoImage(file="tree.png")
#sets image to the background 
limg=Label(pantalla, i=logo)
limg.pack()

#the style sheet being imported to change colors of screen and buttons
theme=TkThemeLoader(pantalla)
theme.loadStyleSheet("python_style.tss")

#keeps UI runing
pantalla.mainloop()