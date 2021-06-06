'''Python Program - Dice Rolling by DJ Harshit'''

# Importing the modules
from tkinter import *

# Fonts and colors
e_fnt = ('Rockwell', 20, 'bold')
fnt=('Rockwell', 15, 'bold')
blck = '#000000'
rd = '#ff0000'
dg = '#249d74'

# Globally declare the expression variable 
expr = "" 
  
# Function to update expressiom in the text entry box 
def press(num):
    global expr 
    expr = expr + str(num) 
    equ.set(expr) 
  
# Function to evaluate the final expr 
def equalpress(): 
    # Try statement is used for handling the errors like zero division error etc. 
    try: 
        global expr 
        total = str(eval(expr)) 
        equ.set(total) 
        expr = total
    except: 
        equ.set(" Error") 

# Function to clear the contents of text entry box 
def clear(): 
    global expr 
    expr = "" 
    equ.set("")

# Function to backspace one last entry
def back():
    global expr
    temp = expr[:len(expr)-1]
    equ.set(temp)
    expr = temp

def key(x):
    global expr
    if x=='=':
        try: 
            total = eval(expr)
            equ.set(str(total))
            expr = str(total)
        except: 
            equ.set(" Error")
    elif x=='b':
        temp = expr[:len(expr)-1]
        equ.set(temp)
        expr = temp
    elif x=='c':
        expr = "" 
        equ.set("")

# Main program 
wind = Tk()
wind.title("Simple Calculator")
wind.configure(bg=dg)
wind.geometry("540x370") 
wind.resizable(0,0)

l1 = Label(wind, text='Calculator', font=('SugarFont Bold', 30, 'bold'), bg=dg)
l1.grid(row=0, column=0, columnspan=4)
l2 = Label(wind, text='By Harshit', font=('Arial Rounded MT Bold', 15), bg=dg)
l2.grid(row=0, column=4)

equ = StringVar() 

expr_field = Entry(wind, textvariable=equ, font=e_fnt, width=35, justify='right') 
expr_field.grid(columnspan=5, padx=5) 
  
equ.set('Enter your expression') 

# Buttons setup
b1 = Button(wind, text='1', font=fnt, fg=blck, bg=rd, command=lambda: press(1), width=7)
b1.grid(row=2, column=0) 

b2 = Button(wind, text='2', font=fnt, fg=blck, bg=rd, command=lambda: press(2), width=7) 
b2.grid(row=2, column=1) 

b3 = Button(wind, text='3', font=fnt, fg=blck, bg=rd, command=lambda: press(3), width=7)
b3.grid(row=2, column=2) 

b4 = Button(wind, text='4', font=fnt, fg=blck, bg=rd, command=lambda: press(4), width=7) 
b4.grid(row=3, column=0) 

b5 = Button(wind, text='5', font=fnt, fg=blck, bg=rd, command=lambda: press(5), width=7) 
b5.grid(row=3, column=1) 

b6 = Button(wind, text='6', font=fnt, fg=blck, bg=rd, command=lambda: press(6),  width=7) 
b6.grid(row=3, column=2) 

b7 = Button(wind, text='7', font=fnt, fg=blck, bg=rd, command=lambda: press(7), width=7) 
b7.grid(row=4, column=0) 

b8 = Button(wind, text='8', font=fnt, fg=blck, bg=rd, command=lambda: press(8), width=7) 
b8.grid(row=4, column=1) 

b9 = Button(wind, text='9', font=fnt, fg=blck, bg=rd, command=lambda: press(9), width=7) 
b9.grid(row=4, column=2) 

b0 = Button(wind, text='0', font=fnt, fg=blck, bg=rd, command=lambda: press(0), width=7) 
b0.grid(row=5, column=0) 

plus = Button(wind, text='+', font=fnt, fg=blck, bg=rd, command=lambda: press("+"), width=7) 
plus.grid(row=2, column=3) 

minus = Button(wind, text='-', font=fnt, fg=blck, bg=rd, command=lambda: press("-"), width=7) 
minus.grid(row=3, column=3) 

multiply = Button(wind, text='*', font=fnt, fg=blck, bg=rd, command=lambda: press("*"), width=7) 
multiply.grid(row=4, column=3) 

divide = Button(wind, text='/', font=fnt, fg=blck, bg=rd, command=lambda: press("/"),  width=7) 
divide.grid(row=5, column=3) 

equal = Button(wind, text='=', font=fnt, fg=blck, bg=rd, command=equalpress, height=4, width=7) 
equal.grid(row=3, column=4, rowspan=3) 

clear = Button(wind, text='Clear', font=fnt, fg=blck, bg=rd, command=clear, width=7) 
clear.grid(row=5, column=2) 

deci = Button(wind, text='.', font=fnt, fg=blck, bg=rd, command=lambda: press('.'), width=7) 
deci.grid(row=5, column=1)

bck = Button(wind, text='<-Back', font=fnt, fg=blck, bg=rd, command=back, width=7) 
bck.grid(row=2, column=4)

hlp = 'You can use keyboard number for input\nPress Enter for equal\nPress Delete for clear\nPress Backspace for back'

l3 = Label(wind, text=hlp, font=('SugarFont Bold', 15), bg=dg, justify='left')
l3.grid(row=6, column=0, columnspan=5)

# If user press nos from keyboard
wind.bind('1', lambda x: press(1))
wind.bind('2', lambda x: press(2))
wind.bind('3', lambda x: press(3))
wind.bind('4', lambda x: press(4))
wind.bind('5', lambda x: press(5))
wind.bind('6', lambda x: press(6))
wind.bind('7', lambda x: press(7))
wind.bind('8', lambda x: press(8))
wind.bind('9', lambda x: press(9))
wind.bind('0', lambda x: press(0))
wind.bind('<+>', lambda x: press('+'))
wind.bind('-', lambda x: press('-'))
wind.bind('<*>', lambda x: press('*'))
wind.bind('</>', lambda x: press('/'))
wind.bind('<Return>', lambda x: key('='))
wind.bind('<BackSpace>', lambda x: key('b'))
wind.bind('<Delete>', lambda x: key('c'))

wind.mainloop()
