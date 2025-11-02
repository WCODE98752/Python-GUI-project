import tkinter as tk
from tkinter import ttk
import re
import time

def load_tasks():
    lable4.delete(0, tk.END)
    try:
        with open('Data_base_of_todo_app', "r") as file:
            for task in file:
                lable4.insert(tk.END, task.strip())
    except FileNotFoundError:
        open('Data_base_of_todo_app', "w").close()
        
        
def addtasks():
    task = Entery1.get().strip()
    if task:
        with open('Data_base_of_todo_app', "a") as file:
            file.write(task + "\n")
        load_tasks()  # now Python knows this function exists
        Entery1.delete(0, tk.END)  # refresh immediately after any change


def removetasks():

    word_to_remove = Entery1var.get()
    with open("Data_base_of_todo_app", "r") as file:
        text = file.read()
    new_text = re.sub(rf"\b{word_to_remove}\b", "", text)
    with open("Data_base_of_todo_app", "w") as file:
        file.write(new_text)
    load_tasks()

    
def deletetext():
    Entery1.delete(0, tk.END)



def main():
    addtasks()
    deletetext()


def main2():
    removetasks()
    deletetext()





window  = tk.Tk()
window.geometry('400x600')

window.maxsize(height = 600 , width = 400)

window.minsize(height = 600 , width= 400)

window.title('To-do app')

window.config(bg='gray54')

# listbox = tk.Listbox(window, width=25, height=10)
# listbox.place(x = 0 , y = 300) 


lable1 = ttk.Label(master=window, text='To-do app' ,font= 'Timesromane 20 bold', background='gray54')
lable1.place(x = 130 , y = 0)

lable2  = ttk.Label(master=window  , text='Manage your Today tasks:' , font='Timesromane 13', background='gray54')
lable2.place(x = 0 , y = 50)


lable3 = tk.Label(master=window ,text='Enter a tasks here:(without space)' , background='gray54')

lable3.place(x = 100 , y = 100)


Entery1var = tk.StringVar()

Entery1 = tk.Entry(master=window, background='gray54',textvariable=Entery1var) 
Entery1.place(x = 100 , y = 120 , width=200)

button1 = tk.Button(master=window , text='ADD' , bg='gray54' ,command=main)
button1.place(x = 120 , y = 150)


button2 = tk.Button(master = window , text= 'REMOVE' ,bg='gray54' ,command=main2)
button2.place(x = 200 , y=  150)

filea = open('Data_base_of_todo_app' ,'r')

lable4 = tk.Listbox(master=window ,width=50 , height=20 ,  background='gray54' )
lable4.place(x = 50 , y = 200)
    
load_tasks()

window.mainloop()