import tkinter as tk
from tkinter import ttk
import random as r
from PIL import Image , ImageTk








def paper():
    image_path = "paper.png"
    img = Image.open(image_path)

    resize_img = img.resize((100,100))
    tk_image = ImageTk.PhotoImage(resize_img)
    image_label.config(image=tk_image)
    image_label.image = tk_image
    user  = 'paper'
    print(f'You select = {user}')
    computer = ['paper.png' , 'rock.png' , 'secor.png']
    b = r.choice(computer)
    image_path = b
    img = Image.open(image_path)

    resize_img = img.resize((100,100))
    tk_image = ImageTk.PhotoImage(resize_img)
    image_label1.config(image=tk_image)
    image_label1.image = tk_image
    indux = computer.index(b)
    print(f'Computer = {b}')
    if indux == 0 and  user == 'paper':
        print('Draw\n')
        lable_outputvar.set("Draw")
    else:
        if indux == 1 and user == 'paper':
            print('You win\n')
            lable_outputvar.set("You win")
            score = lable_score_var.get()
            score2 = score + 1
            lable_score_var.set(score2)
        else:
            if indux == 2 and user  == 'paper':
                print('You lose\n') 
                lable_outputvar.set("You lose")  
    
    
def Rock():
    image_path = "rock.png"
    img = Image.open(image_path)

    resize_img = img.resize((100,100))
    tk_image = ImageTk.PhotoImage(resize_img)
    image_label.config(image=tk_image)
    image_label.image = tk_image
    user  = 'rock'
    print(f'You select = {user}')
    computer = ['paper.png' , 'rock.png' , 'secor.png']
    b = r.choice(computer)
    image_path = b
    img = Image.open(image_path)

    resize_img = img.resize((100,100))
    tk_image = ImageTk.PhotoImage(resize_img)
    image_label1.config(image=tk_image)
    image_label1.image = tk_image
    indux = computer.index(b)
    indux = computer.index(b)
    print(f'Computer = {b}')
    if indux == 0 and  user == 'rock':
        print('You lose\n')
        lable_outputvar.set("You lose")
    else:
        if indux == 1 and user == 'rock':
            print('Draw\n')
            lable_outputvar.set("Draw")
        else:
            if indux == 2 and user  == 'rock':
                print('You win\n') 
                lable_outputvar.set("You win")
                score = lable_score_var.get()
                score2 = score + 1
                lable_score_var.set(score2)
        
    
    
def secor():
    image_path = "secor.png"
    img = Image.open(image_path)

    resize_img = img.resize((100,100))
    tk_image = ImageTk.PhotoImage(resize_img)
    image_label.config(image=tk_image)
    image_label.image = tk_image
    

    user  = 'secor'
    print(f'You select = {user}')
    computer = ['paper.png' , 'rock.png' , 'secor.png']
    b = r.choice(computer)
    image_path = b
    img = Image.open(image_path)

    resize_img = img.resize((100,100))
    tk_image = ImageTk.PhotoImage(resize_img)
    image_label1.config(image=tk_image)
    image_label1.image = tk_image
    indux = computer.index(b)
    indux = computer.index(b)
    print(f'Computer = {b}')
    if indux == 0 and  user == 'secor':
        print('You win\n')
        lable_outputvar.set("You win")
        score = lable_score_var.get()
        score2 = score + 1
        lable_score_var.set(score2)
    else:
        if indux == 1 and user == 'secor':
            print('You lose\n')
            lable_outputvar.set("You lose")
        else:
            if indux == 2 and user  == 'secor':
                print('Draw') 
                lable_outputvar.set("Draw")

   






window = tk.Tk()
window.title('Game')
window.geometry('700x500')
window.maxsize(height = 500 , width = 700)
window.minsize(height = 500 , width = 700)
window.config(background='SlateBlue')

lable_of_game = ttk.Label(master=window,text='Rock Paper Sesor game' , font='CooperBlack 24 bold' , background='SlateBlue')
lable_of_game.place(x = 200 , y = 0)


paper_button_var = tk.StringVar(value='paper')
buttonvar2 = tk.StringVar(value='Rock')
BUtton1 = tk.Button(window, text = 'Paper', bg='green2' , textvariable=paper_button_var ,command=paper)
BUtton1.place(x = 100 , y = 400, height=50 ,width=100)

BUtton2 = tk.Button(window, text = 'Rock', bg='green2' , command=Rock)
BUtton2.place(x = 300 , y = 400, height=50 ,width=100)

BUtton3 = tk.Button(window, text = 'seseor', bg='green2' , command=secor)
BUtton3.place(x = 500 , y = 400, height=50 ,width=100)


lable_user = ttk.Label(window , text='YOU:'  , font='CooperBlack 18' , background='SlateBlue')
lable_user.place(x = 100  ,y = 150)


lable_user = ttk.Label(window , text='COMPUTER:'  , font='CooperBlack 18' , background='SlateBlue')
lable_user.place(x = 500  ,y = 150)

lable_score_var = tk.IntVar()
lable_score = ttk.Label(window , text='score' , background='SlateBlue' , font='CooperBlack 18', textvariable=lable_score_var)
lable_score.place(x = 440, y = 70)

lable_score = ttk.Label(window , text=' Your win score: ' , background='SlateBlue' , font='CooperBlack 18')
lable_score.place(x = 250, y = 70)



# imagevar  = tk.Image(secor)
image_label = ttk.Label(window, background='SlateBlue')
image_label.place(x =80 , y = 200)







lable_outputvar = tk.StringVar(value='output')
lable_output = ttk.Label(master = window , text='output'  ,font='CopperBlack 18' ,textvariable= lable_outputvar ,background='SlateBlue')
lable_output.place(x = 300 , y = 350)


image_label1 = ttk.Label(window, background='SlateBlue')
image_label1.place(x =500 , y = 200)









window.mainloop()