# a program of looop within loops to increase the loading time for the GUI
# the variable  n if increased will increase the range and over all time 
#when n=50 takes ~2minutes to load but when n=100+ it can take more than 5 minutes
import sys
from tkinter import messagebox
def ED():
    n=50
    j=1
    for i in range(n):
        print (i,"i")
        j=j+i
        print (j,'j')
        m=j
        for n in range(j):
            m=j*m
            print (m,'m')
        k=j
  
    for h in range(n):
        k=k*j
        print(k,'k')
        number=m/k
        print (number,'E')
    
ED()
