import tkinter
from tkinter import BOTH, RIGHT, END, DISABLED, NORMAL

# Define the colors and the fonts
light_grey = "#D4D4D2"
eerie_black = "#1C1C1C"
dark_liver="#505050"
vivid_gamboge = "#FF9500"
FONT=("Helvetica",18)

# Define the window
root = tkinter.Tk()
root.title('Iphone Calculator GUI with Tkinter')
root.geometry('300x350')
root.resizable(0,0)
root.config(bg=eerie_black)
root.iconbitmap('calculator.png')


# Define the functions
def submitNumber(number):
    # Used to insert a number or decimal as an input
    displayEntry.insert(END,number)

    # If the decimal is pressed once disable it so that it cannot be pressed twice
    if "." in displayEntry.get():
        decimalButton.config(state=DISABLED)

def operate(operator):
    # Store the first number of the expression in the operation to be used

    global firstValue,operation

    # Get the operator pressed and current value of the display
    firstValue = displayEntry.get()
    operation = operator

    # Delete the value of the initial number
    displayEntry.delete(0,END)

    decimalButton['state'] = NORMAL

def enableButton():
    # This function is used to bring the decimal button to NORMAL state
    decimalButton['state'] = NORMAL

def equal():
    # This function performs the arithmatical operation based on the operator
    if operation == 'add':
        value = float(firstValue) + float(displayEntry.get())
    elif operation =='subtract':
        value = float(firstValue) - float(displayEntry.get())
    elif operation =='multiply':
        value = float(firstValue) * float(displayEntry.get())
    elif operation == 'divide':
        if displayEntry.get() == '0':
            value = 'ERROR'
        else:
            value = value = float(firstValue) / float(displayEntry.get())

    # Remove the current value of the display and update it with the result of the operation
    displayEntry.delete(0,END)
    displayEntry.insert(0,value)

    #Return the decimal button state to normal
    enableButton()

def negate_button():
    value = -1*float(displayEntry.get())

    displayEntry.delete(0,END)
    displayEntry.insert(0,value)

def percent():
    value = float(displayEntry.get()) / float(100)

    displayEntry.delete(0,END)
    displayEntry.insert(0,value)

def clear():
    # Clears the previous values of the entry box
    displayEntry.delete(0,END)

    #Return button states to normal
    enableButton()



# Define the frame where the texts will be shown
displayFrame = tkinter.Frame(root,bg=eerie_black)
buttonFrame = tkinter.LabelFrame(root,bg=eerie_black)
displayFrame.pack(padx=2, pady=(5,20),fill=BOTH)
buttonFrame.pack(padx=2,pady=5)

displayEntry = tkinter.Entry(displayFrame, font=FONT,bg=eerie_black, justify=RIGHT, fg="white", borderwidth = 5)
displayEntry.pack(padx=5,pady=5)

# Layout for the button frame
clearButton = tkinter.Button(buttonFrame, text="AC", font=FONT,
bg=light_grey,fg="black",command=clear)
negate_button = tkinter.Button(buttonFrame, text="+/-", font=FONT, fg="black", bg=light_grey,command=negate_button)
percentButton = tkinter.Button(buttonFrame, text="%", font=FONT, fg="black", bg=light_grey,command=percent)

divideButton = tkinter.Button(buttonFrame, text=" / ", font=FONT, bg=vivid_gamboge,command = lambda:operate('divide'))
multiplyButton = tkinter.Button(buttonFrame, text="*", font=FONT, bg=vivid_gamboge,command = lambda:operate('multiply'))
subtractButton = tkinter.Button(buttonFrame, text="-", font=FONT, bg=vivid_gamboge,command = lambda:operate('subtract'))
addButton = tkinter.Button(buttonFrame, text="+", font=FONT, bg=vivid_gamboge,command = lambda:operate('add'))
equalButton = tkinter.Button(buttonFrame, text="=", font=FONT, bg=vivid_gamboge,command=equal)
decimalButton = tkinter.Button(buttonFrame, text=".", font=FONT, fg="white", bg=dark_liver, command=lambda:submitNumber("."))

# Number buttons
nine = tkinter.Button(buttonFrame, text="9", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(9))
eight = tkinter.Button(buttonFrame, text="8", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(8))
seven = tkinter.Button(buttonFrame, text="7", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(7))
six = tkinter.Button(buttonFrame, text="6", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(6))
five = tkinter.Button(buttonFrame, text="5", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(5))
four = tkinter.Button(buttonFrame, text="4", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(4))
three = tkinter.Button(buttonFrame, text="3", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(3))
two = tkinter.Button(buttonFrame, text="2", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(2))
one = tkinter.Button(buttonFrame, text="1", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(1))
zero = tkinter.Button(buttonFrame, text="0", font=FONT, fg="white", bg=dark_liver,command = lambda:submitNumber(0))

# Pack the buttons according to their rows
clearButton.grid(row=1, column=0, sticky="WE", pady=1)
negate_button.grid(row=1, column=1, sticky="WE", pady=1)
percentButton.grid(row=1, column=2, sticky="WE", pady=1)
divideButton.grid(row=1, column=3, sticky="WE", pady=1)

seven.grid(row=2, column=0, sticky="WE", pady=1, ipadx=20)
eight.grid(row=2, column=1, sticky="WE", pady=1, ipadx=20)
nine.grid(row=2, column=2, sticky="WE", pady=1, ipadx=20)
multiplyButton.grid(row=2, column=3, sticky="WE", pady=1, ipadx=20)

four.grid(row=3, column=0, pady=1, sticky="WE", ipadx=20)
five.grid(row=3, column=1, pady=1, sticky="WE", ipadx=20)
six.grid(row=3, column=2, pady=1, sticky="WE", ipadx=20)
subtractButton.grid(row=3, column=3, pady=1, sticky="WE", ipadx=20)

one.grid(row=4, column =0, sticky="WE", pady=1)
two.grid(row=4, column =1, sticky="WE", pady=1)
three.grid(row=4, column =2, sticky="WE", pady=1)
addButton.grid(row=4, column =3, sticky="WE", pady=1)

zero.grid(row=5, column=0, sticky="WE", pady=1,columnspan=2)
decimalButton.grid(row=5, column=2, sticky="WE", pady=1)
equalButton.grid(row=5, column=3, sticky="WE", pady=1)


# Run the window's main loop
root.mainloop()