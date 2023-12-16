from tkinter import *
from tkinter.ttk import *

from time  import strftime

root =Tk( )
root.title =('clock')

def time( ):
	string= strftime('%I:%M:%S,%p')
	
	lbl.config(text=string)
	
	lbl.after (1000, time)

lbl=Label(root,font=("bold",30),

       background='black', 
       
       foreground='red' )

lbl.pack(anchor='center',)

time( )

mainloop( )
