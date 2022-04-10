from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.geometry("350x350")
root.title('Calculator')
#root.resizable(width=False,height=False)
frame=Frame(root)
frame.pack()

#creating canvas
canvas = Canvas(root,width=600 ,height=400)
my_image= ImageTk.PhotoImage(Image.open("C:\\Users\\taliy\\Downloads\\studies\\doodle-math-pattern-seamless-vector-1112253.jpg"))
canvas.create_image(0,0,anchor=NW,image = my_image)

canvas.pack()



#entry widgets for first and second number
n1=Label(root,text="firstnum").place(x=100,y=30)
n2=Label(root,text="secnum").place(x=100,y=90)
global e1
e1=Entry(root,bg="white")
e1.place(x=150,y=30)
global e2
e2=Entry(root,bg="white")
e2.place(x=150,y=90)


def addition():
    a=e1.get()
    b=e2.get()
    x=int(a)
    y=int(b)
    result=x+y
    messagebox.showinfo("the result",result)
    return

def sub():
    a=e1.get()
    b=e2.get()
    x=int(a)
    y=int(b)
    result=x-y
    messagebox.showinfo("the result",result)
    return

def multi():
    a=e1.get()
    b=e2.get()
    x=int(a)
    y=int(b)
    result=x*y
    messagebox.showinfo("the result",result)
    return

def div():
    a=e1.get()
    b=e2.get()
    x=int(a)
    y=int(b)
    result=x/y
    messagebox.showinfo("the result",result)
    return

def mod():
    a=e1.get()
    b=e2.get()
    x=int(a)
    y=int(b)
    result=x%y
    messagebox.showinfo("the result",result)
    return
def expo():
    a=e1.get()
    b=e2.get()
    x=int(a)
    y=int(b)
    result=x**y
    messagebox.showinfo("the result",result)
    return
def floor():
    a=e1.get()
    b=e2.get()
    x=int(a)
    y=int(b)
    result=x//y
    messagebox.showinfo("the result",result)
    return

def clear():
    e1.delete(0,END)
    e2.delete(0,END)

def close():
    root.destroy()
#make buttons

b1 = Button(root,text="+",command=addition,padx=20,pady=20,bg="white")
c1w=canvas.create_window(50,160,window=b1)

b2 = Button(root,text="-",command=sub,padx=20,pady=20,bg="white")
c1w=canvas.create_window(100,160,window=b2)

b3 = Button(root,text="*",command=multi,padx=20,pady=20,bg="white")
c1w=canvas.create_window(150,160,window=b3)

b4 = Button(root,text="/",command=div,padx=20,pady=20,bg="white")
c1w=canvas.create_window(200,160,window=b4)

b5 = Button(root,text="%",command=mod,padx=20,pady=20,bg="white")
c1w=canvas.create_window(250,160,window=b5)

b6 = Button(root,text="**",command=expo,padx=20,pady=20,bg="white")
c1w=canvas.create_window(300,160,window=b6)

b7 = Button(root,text="//",command=floor,padx=20,pady=20,bg="white")
c1w=canvas.create_window(130,230,window=b7)

b8= Button(root,text="clear",command=clear,padx=20,pady=20,bg="white")
c1w=canvas.create_window(200,230,window=b8)

b9= Button(root,text="exit",command=close,padx=20,pady=20,bg="white")
c1w=canvas.create_window(170,300,window=b9)

root.mainloop()
