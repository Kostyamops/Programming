import tkinter
from tkinter import ttk
from math import sqrt


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry("240x110")

        self.number_entry = ttk.Entry(self.master, width=37)
        self.number_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.button_clear = ttk.Button(self.master, text="C", command=self.button_clear)
        self.button_plus = ttk.Button(self.master, text="+", command=self.button_plus)
        self.button_minus = ttk.Button(self.master, text="-", command=self.button_minus)

        self.button_multiply = ttk.Button(self.master, text="*", command=self.button_multiply)
        self.button_div = ttk.Button(self.master, text="/", command=self.button_div)
        self.button_round_div = ttk.Button(self.master, text="//", command=self.button_round_div)

        self.button_square = ttk.Button(self.master, text="2", command=self.button_square)
        self.button_sqrt = ttk.Button(self.master, text="√", command=self.button_sqrt)
        self.button_calculate = ttk.Button(self.master, text="=", command=self.button_calculate)

        self.button_clear.grid(row=1, column=1)
        self.button_plus.grid(row=1, column=2)
        self.button_minus.grid(row=1, column=3)

        self.button_multiply.grid(row=2, column=1)
        self.button_div.grid(row=2, column=2)
        self.button_round_div.grid(row=2, column=3)

        self.button_square.grid(row=3, column=1)
        self.button_sqrt.grid(row=3, column=2)
        self.button_calculate.grid(row=3, column=3)

        self.f_num = 0
        self.last_command = ""


    def button_click(self, number):
        current = self.number_entry.get()
        self.number_entry.delete(0, tkinter.END)
        self.number_entry.insert(0, str(current) + str(number))

    def button_clear(self):
        self.number_entry.delete(0, tkinter.END)

    def button_plus(self):
        first_number = self.number_entry.get()
        self.last_command = "plus"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tkinter.END)

    def button_minus(self):
        first_number = self.number_entry.get()
        self.last_command = "minus"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tkinter.END)

    def button_multiply(self):
        first_number = self.number_entry.get()
        self.last_command = "multiply"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tkinter.END)

    def button_div(self):
        first_number = self.number_entry.get()
        self.last_command = "div"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tkinter.END)

    def button_round_div(self):
        first_number = self.number_entry.get()
        self.last_command = "round_div"
        self.f_num = float(first_number)
        self.number_entry.delete(0, tkinter.END)

    def button_square(self):
        number = float(self.number_entry.get())
        result = number**2
        if result % 1 == 0:
            result = int(result)
        self.number_entry.delete(0, tkinter.END)
        self.number_entry.insert(0, result)

    def button_sqrt(self):
        number = float(self.number_entry.get())
        result = sqrt(number)
        if result % 1 == 0:
            self.number_entry.delete(0, tkinter.END)
            self.number_entry.insert(0, int(result))
        else:
            self.number_entry.delete(0, tkinter.END)
            self.number_entry.insert(0, result)

    def button_calculate(self):
        second_number = self.number_entry.get()
        self.number_entry.delete(0, tkinter.END)

        if self.last_command == "plus":
            self.number_entry.insert(0, self.f_num + float(second_number))

        if self.last_command == "minus":
            self.number_entry.insert(0, self.f_num - float(second_number))

        if self.last_command == "multiply":
            self.number_entry.insert(0, self.f_num * float(second_number))

        if self.last_command == "div":
            self.number_entry.insert(0, self.f_num / float(second_number))

        if self.last_command == "round_div":
            self.number_entry.insert(0, self.f_num // float(second_number))


if __name__ == '__main__':
    root = tkinter.Tk()
    calculator1 = Calculator(root)
    root.mainloop()