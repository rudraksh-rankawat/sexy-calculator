import tkinter as tk
from tkinter import ttk
import ast

root = tk.Tk()
root.geometry('600x400')
root.title('Sexy Calculator')
i = 0
def display_text(num):
    global i
    entry.insert(i, num)
    i+=1

def display_operators(op):
    global i
    length = len(op)
    entry.insert(i, op)
    i+=length

def clear_all():
    entry.delete(0, 'end')
    # global i
    # i=0


def undo():
    entire_string = entry.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        entry.insert(0, new_string)


def calculate():
    expression = entry.get()
    print(f"Expression evaluated as: '{expression}'")
    try:
        node = ast.parse(expression, mode="eval")
        result = eval(compile(node,'<string>','eval'))
        output_label.config(text=result)
        # output_label.config(text=result)
    except Exception as e:
        print(f"Error {type(e).__name__}: {e}")
        output_label.config(text="")
        clear_all()
        entry.insert(0, f"Error")



bind_text = tk.StringVar()
entry = tk.Entry(root, textvariable=bind_text)
entry.grid(row=1, columnspan=10)

output_label = tk.Label(root)
output_label.grid()
#
# bind_text.trace_add(
#     "write",
#     lambda *args: output_label.config(text=bind_text.get())
# )

label_nums = tk.Label(root)
label_nums.grid()

nums = [1,2,3,4,5,6,7,8,9]

counter = 0
for x in range(3):
    for y in range(3):
        button_text = nums[counter]
        button = tk.Button(label_nums, text = nums[counter], height=2, width=2, command= lambda text=button_text: display_text(text))
        button.grid(row=x, column=y)
        counter += 1

button = tk.Button(label_nums, text=0, height=2, width=2, command= lambda text=0: display_text(text))
button.grid(row=3, column=1)

operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]

counter = 0
for x in range(4):
    for y in range(3):
        if counter < 10:
            button = tk.Button(label_nums, text=operations[counter], height=2, width=2, command = lambda text=operations[counter]: display_operators(text))
            button.grid(row=x, column=y+3)
            counter+=1

tk.Button(label_nums, text= "AC", width=2, height=2, command=clear_all).grid(row=3,column=0)
tk.Button(label_nums, text= "=", width=2, height=2, command=calculate).grid(row=3,column=2)
tk.Button(label_nums, text= "<-", width=2, height=2, command=lambda : undo()).grid(row=3,column=4)


root.mainloop()


