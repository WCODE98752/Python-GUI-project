import tkinter as tk
from tkinter import ttk
from time import strftime
import time
import datetime
import threading



def time():
    formatted_time = strftime("%I:%M:%S %p")
    lable2.config(text = formatted_time)
    lable2.after(1000,time)




window = tk.Tk()
window.title('Digital CLock')
window.config(bg='black')
window.geometry('400x200')
window.maxsize(height=200 , width= 400)
window.minsize(height=200 , width= 400)
notebook = ttk.Notebook(window)



frame_home = ttk.Frame(notebook)
frame_help = ttk.Frame(notebook)


label3 = ttk.Label(master=frame_help , text = 'This is help section!', font= 'TimesNewRoman 10 bold')
label3.place(x = 150 , y = 0)
lalbe4 = ttk.Label(master=frame_help , text='How can i help you!')
lalbe4.place(x = 0 , y = 50)
    
    
    
    
lable1 = ttk.Label(master=frame_home , text='CLOCK' , font='TimesNewRoman 20')

lable2 = tk.Label(master=frame_home, font='TimesNewRoman 26')

notebook.add(frame_home , text='Home')
notebook.add(frame_help , text = 'Help')
time()




lable1.place(x= 150, y = 0)
lable2.place(x= 130 , y = 50)
notebook.pack(expand=True, fill="both")





window.mainloop()
    
