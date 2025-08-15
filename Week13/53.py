# p53.py
# Han Rockhill
# python 3.12.2
# 04/22/2024
# Calculator GUI
# commented out template below from Alex Stoykov (instructor)
'''
import tkinter
from tkinter import messagebox

w=[]
window =tkinter.Tk()
window.title("calculator")
#window.geometry("200x70")

e = tkinter.Entry(window, width=48)
e.grid(row=0,columnspan=4)

buttonNumber = 0
for r in range(1,4): # rows
    for c in range(0,3): # columns
        w.append(tkinter.Button(window,
                                text= buttonNumber +1,
                                width=10, height=5,
                                command = lambda n=buttonNumber +1: myFunction(0)))
        w[buttonNumber].grid(row=r,columnspan=c)
        buttonNumber =  buttonNumber +1


w.append(tkinter.Button(window,
                        text="-",
                        width=10, height=5,
                        command = lambda : myFunction("-")))
w[9].grid(row=2, column=3)

w.append(tkinter.Button(window,
                        text ="0",
                        width=21, height=5,
                        command = lambda n=0: myFunction(0)))
w[10].grid(row=4, columnspan=2)

w.append(tkinter.Button(window,
                        text=".",
                        width=10, height=5,
                        command = lambda : myFunction(".")))
w[11].grid(row=4, column=2)

w.append(tkinter.Button(window,
                        text="+",
                        width=10, height=5,
                        command = lambda : myFunction("+")))
w[12].grid(row=1, column=3)

w.append(tkinter.Button(window,
                        text="=",
                        width=10, height=11,
                        command  = lambda : myFunction("=")))
w[13].grid(row=3, column=3, rowspan=2)

def myFunction(buttonNumber):
    e.insert(50, buttonNumber)

    equation = e.get()
    if buttonNumber == '=':
        splitEquation = equation.split("=")
        answer = eval(splitEquation[0])
        e.insert(50,answer)

window.mainloop()

'''

# revised calculater

import tkinter
from tkinter import messagebox

w = []
window = tkinter.Tk()
window.title("Calculator")

e = tkinter.Entry(window, width=48)
e.grid(row=0, columnspan=4)

def myFunction(buttonNumber):
    global e
    if buttonNumber == '=':
        equation = e.get()
        try:
            answer = eval(equation)
            e.delete(0, tkinter.END)  # Clear the entry
            e.insert(0, answer)  # Insert the answer
        # catch errors so I dont crash
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        e.insert(tkinter.END, buttonNumber)

# Creating buttons 1-9
for r in range(1, 4):  # rows
    for c in range(0, 3):  # columns
        buttonNumber = r * 3 + c - 2  # Calculate button number
        w.append(tkinter.Button(window,
                                text=str(buttonNumber),
                                width=10, height=5,
                                command=lambda n=buttonNumber: myFunction(str(n))))
        w[-1].grid(row=r, column=c)

# Creating other buttons
w.append(tkinter.Button(window,
                        text="-",
                        width=10, height=5,
                        command=lambda: myFunction("-")))
w[-1].grid(row=2, column=3)

w.append(tkinter.Button(window,
                        text="0",
                        width=24, height=5,
                        command=lambda: myFunction("0")))
w[-1].grid(row=4, columnspan=2)

w.append(tkinter.Button(window,
                        text=".",
                        width=10, height=5,
                        command=lambda: myFunction(".")))
w[-1].grid(row=4, column=2)

w.append(tkinter.Button(window,
                        text="+",
                        width=10, height=5,
                        command=lambda: myFunction("+")))
w[-1].grid(row=1, column=3)

w.append(tkinter.Button(window,
                        text="=",
                        width=10, height=11,
                        command=lambda: myFunction("=")))
w[-1].grid(row=3, column=3, rowspan=2)

window.mainloop()

'''
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: /Users/42o/Documents/53.py =====================

'''