## This my python repository in which i have stored my python code and the main project that i have saved in this repository is the pro2.py python file .This pro2.py file contains the python program for a calculator application 

# Calculator Application

## Overview

This is a simple GUI-based calculator application built using Python's Tkinter library. The calculator can perform basic arithmetic operations including addition, subtraction, multiplication, division, modulus, exponentiation, and floor division. The application features a user-friendly interface with an attractive background image.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Exponentiation
- Floor Division
- Clear input fields
- Exit the application

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python)
- Pillow library for image handling

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/calculator-app.git
    cd calculator-app
    ```

2. **Install the Pillow library**:
    ```bash
    pip install Pillow
    ```

3. **Run the application**:
    ```bash
    python calculator.py
    ```

## Usage

1. **Enter the first number** in the provided entry field.
2. **Enter the second number** in the provided entry field.
3. **Select the desired operation** by clicking the corresponding button (`+`, `-`, `*`, `/`, `%`, `**`, `//`).
4. **View the result** in a message box that appears after performing the operation.
5. **Clear the input fields** by clicking the `clear` button.
6. **Exit the application** by clicking the `exit` button.

## Code Explanation

### Import Libraries
```python
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
```

### Initialize the Main Window
```python
root = Tk()
root.geometry("350x350")
root.title('Calculator')
root.resizable(width=False, height=False)
```

### Set Up the Canvas with Background Image
```python
canvas = Canvas(root, width=600, height=400)
my_image = ImageTk.PhotoImage(Image.open("path/to/your/image.jpg"))
canvas.create_image(0, 0, anchor=NW, image=my_image)
canvas.pack()
```

### Create Entry Widgets for Input
```python
n1 = Label(root, text="firstnum").place(x=100, y=30)
n2 = Label(root, text="secnum").place(x=100, y=90)
e1 = Entry(root, bg="white")
e1.place(x=150, y=30)
e2 = Entry(root, bg="white")
e2.place(x=150, y=90)
```

### Define Functions for Arithmetic Operations
```python
def addition():
    a = e1.get()
    b = e2.get()
    result = int(a) + int(b)
    messagebox.showinfo("The result", result)

def sub():
    a = e1.get()
    b = e2.get()
    result = int(a) - int(b)
    messagebox.showinfo("The result", result)

def multi():
    a = e1.get()
    b = e2.get()
    result = int(a) * int(b)
    messagebox.showinfo("The result", result)

def div():
    a = e1.get()
    b = e2.get()
    result = int(a) / int(b)
    messagebox.showinfo("The result", result)

def mod():
    a = e1.get()
    b = e2.get()
    result = int(a) % int(b)
    messagebox.showinfo("The result", result)

def expo():
    a = e1.get()
    b = e2.get()
    result = int(a) ** int(b)
    messagebox.showinfo("The result", result)

def floor():
    a = e1.get()
    b = e2.get()
    result = int(a) // int(b)
    messagebox.showinfo("The result", result)

def clear():
    e1.delete(0, END)
    e2.delete(0, END)

def close():
    root.destroy()
```

### Create Buttons for Operations
```python
b1 = Button(root, text="+", command=addition, padx=20, pady=20, bg="white")
canvas.create_window(50, 160, window=b1)

b2 = Button(root, text="-", command=sub, padx=20, pady=20, bg="white")
canvas.create_window(100, 160, window=b2)

b3 = Button(root, text="*", command=multi, padx=20, pady=20, bg="white")
canvas.create_window(150, 160, window=b3)

b4 = Button(root, text="/", command=div, padx=20, pady=20, bg="white")
canvas.create_window(200, 160, window=b4)

b5 = Button(root, text="%", command=mod, padx=20, pady=20, bg="white")
canvas.create_window(250, 160, window=b5)

b6 = Button(root, text="**", command=expo, padx=20, pady=20, bg="white")
canvas.create_window(300, 160, window=b6)

b7 = Button(root, text="//", command=floor, padx=20, pady=20, bg="white")
canvas.create_window(130, 230, window=b7)

b8 = Button(root, text="clear", command=clear, padx=20, pady=20, bg="white")
canvas.create_window(200, 230, window=b8)

b9 = Button(root, text="exit", command=close, padx=20, pady=20, bg="white")
canvas.create_window(170, 300, window=b9)
```

### Run the Main Loop
```python
root.mainloop()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses the Tkinter library for GUI and Pillow for image handling.
- Background image sourced from [freepik](https://www.freepik.com).

---

Feel free to modify and expand the project as needed. Contributions are welcome!
