# practicing  differnt python addons to make a GUI

# import PySimpleGUI as SmpG
# def simpleGui():
#     #making the button
#     layout=[[SmpG.Text("Hello ")],[SmpG.Button("Welcome")]]

#     #making display window
#     window=SmpG.Window("Practice",layout)

#     # Event loop to keep the window to 
#     while True:
#         event, values = window.read()
#         if event == "Welcome" or event == SmpG.WIN_CLOSED:
#             break

#     window.close()
# simpleGui()

from turtle import width, window_height, window_width
import wx

class Hello(wx.Frame):
    # just displaying Hello
    def __init__(self, *args, **kw):
        super(Hello,self).__init__(*args, **kw)  

        #creating apnnel to display on
        pnl=wx.Panel(self)

        #Text (label) large visual
        st= wx.StaticText(pnl,label="Loading")
        font=st.GetFont()
        font.PointSize +=10
        font=font.Italic()
        new_size= wx.BoxSizer(wx.VERTICAL)
        #new_size.Add(st, wx.SizerFlags().Border(wx.Top|wx.LEFT, 25))
        pnl.SetSizer(new_size)

        #status bar- Bar at bottom displaying events/actions
        self.CreateStatusBar()
        self.SetStatusText("Hello")
    def OnExit(self, event):
        self.Close(True)
    def Message():
        wx.MessageBox("This is a message box")
    def infobox():
        #messagebox with information
        wx.MessageBox("This is practice","this will display info", wx.OK|wx.ICON_INFORMATION)

if __name__=='__main__':
    app=wx.App()
    frm=Hello(None,title="Practice")
    frm.Show()
    app.MainLoop()

from tkinter import *
from tkinter import messagebox
root= Tk()
frame =Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side = BOTTOM)
def clik():
    print ("hello")
    root.configure(bg='#856ff8')
    if root['bg']!='Red':
      messagebox.showinfo('','That is not red')      


redbutton=Button(frame,text ='Red', fg='red', command=clik, activebackground='#00ff00')
redbutton.pack(side = LEFT)

brownbutton=Button(frame,text ='Brown', fg='brown')
brownbutton.pack(side = RIGHT)

bluebutton=Button(frame,text ='Blue', fg='blue')
bluebutton.pack(side = LEFT)

blackbutton=Button(bottomframe,text ='Black', fg='black')
blackbutton.pack(side = BOTTOM)

root.mainloop()

