from tkinter import *
from math import *

class Calculator():

    def __init__(self):

        window = Tk()
        window.title("Calculator")

        self.string = StringVar()
        display = Entry(window, textvariable=self.string, bd = 5)
        display.grid(row=0, column=0, columnspan=6)
        display.focus()

        values = ["%", "√", "x²", "1/x", "CE", "C", "<-", "/", "7", "8", "9", "*", "4",
                  "5", "6", "-", "1", "2", "3", "+", "+/-", "0", ".", "="]

        button_height, button_width = 1, 2
        row, col = 1, 0

        for txt in values:

            if(col == 4 or col == 8 or col == 12 or col == 16 or col == 20):
                row += 1
                col = 0

            if(txt == "="):
                btn = Button(window, height=button_height, text=txt, width=button_width, command= lambda: self.equals())
                btn.grid(row=row, column=col)

            elif(txt == "CE" or txt == "<-"):
                btn = Button(window, height=button_height, text=txt, width=button_width, command=lambda: self.delete())
                btn.grid(row=row, column=col)

            elif(txt == "C"):
                btn = Button(window, height=button_height, text=txt, width=button_width, command=lambda: self.clear())
                btn.grid(row=row, column=col)

            else:
                btn = Button(window, height=button_height, text=txt, width=button_width, command= lambda txt=txt: self.add_char(txt))
                btn.grid(row=row, column=col)

            col+=1
        window.mainloop()

    def clear(self):
        self.string.set("")

    def delete(self):
        self.string.set(self.string.get()[0:-1])

    def equals(self):
        result = ""

        try:
            result = eval(self.string.get())
        except:
            self.string.set("Error")

        self.string.set(result)

    def add_char(self, char):

        if(char == "√"):
            self.string.set(sqrt(float(self.string.get())))
        elif(char == "x²"):
            self.string.set(self.string.get() + "**2")
        elif(char == "1/x"):
            self.string.set("1/" + self.string.get())
        elif(char == "+/-"):
            self.string.set("-" + self.string.get())
        else:
            self.string.set(self.string.get() + str(char))

Calculator()