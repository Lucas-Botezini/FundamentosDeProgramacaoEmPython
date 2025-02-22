#Usando biblioteca Tkinter
#Geralmente a biblioteca ja é instalada junto ao Python, mas caso precise instalar
# pip install tk
import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

root = tk.Tk()
root.title("Calculadora Simples")

entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: click_button(t)).grid(row=row, column=col)

tk.Button(root, text="C", width=5, height=2, font=('Arial', 18), command=clear).grid(row=5, column=0)

root.mainloop()