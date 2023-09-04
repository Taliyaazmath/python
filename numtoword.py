import num2words as n2w
from tkinter import *

def num_to_words():
    given_num = foat(num.get())
    num_words = n2w.num2words(given_num)
    display.config(text=str(num_in_words).captialize())

root = Tk()
root.title("Number to words")
root.geometry("650x400")

num = StringVar()

title = Label(root,text="Number to words convertion",fg = "Blue" , font =("Arial" , 20 , 'bold')).place(x=220,y=10)


root.mainloop()
