import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(
            self.root,
            textvariable=self.input_text,
            font=('Arial', 20),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
            ('C',5,0)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(self.root, text=text, width=5, height=2,
                                command=self.calculate)
                btn.grid(row=row, column=col)
            elif text == 'C':
                btn = tk.Button(self.root, text=text, width=22, height=2,
                                command=self.clear)
                btn.grid(row=row, column=col, columnspan=4)
            else:
                btn = tk.Button(self.root, text=text, width=5, height=2,
                                command=lambda t=text: self.press(t))
                btn.grid(row=row, column=col)

    def press(self, value):
        self.expression += value
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.clear()
        except:
            messagebox.showerror("Error", "Invalid Input")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
