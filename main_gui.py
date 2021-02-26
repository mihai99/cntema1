# This is a sample Python script.
from task1 import run as run_task1
from task2 import run_addition as run_task2_addition
from task3 import calc_tan_simple, calc_tan_10000_runs
import tkinter as tk

#

#
# frame = tk.Frame(window, width=800, height=800)
# frame.pack()
#
# lbl = tk.Label(frame, text='aa', font=("Helvetica", 12))
# lbl.place(x=200, y=10)
#
# def run_task_1():
#     task1_result = run_task1()
#     print("bb", task1_result)
#     lbl.config(text="vb")
#
#
# button1 = tk.Button(frame, text="show task 1", command=run_task1, width=20, font=("Helvetica", 12))
# button1.place(x=0, y=0)
# button1.pack()
# lbl.pack();
# window.mainloop()

win = tk.Frame()
win.pack()

message = tk.StringVar()
message.set('hi')

l1 = tk.Label(win,  text='Hello container world', font=("Helvetica", 12))
l1.pack(side=tk.TOP)
def press_btn1():
    l1.config(text="Precizie masina: " + str(run_task1()))

def press_btn2():
    l1.config(text="Precizia masina la asociativitatea adunatii: " + str(run_task2_addition()))

def press_btn3():
    result = calc_tan_simple()
    l1.config(text="Pentru " + str(result['number']) + "\nEroare fractii continue: " + str(result['fracError']) + "\nEroare fractii polinoame: " + str(result['poliErr']))

def press_btn4():
    result = calc_tan_10000_runs()
    l1.config(text="Pentru 10.000 numere\nEroare fractii continue: " + str(result['fracError']) + "\nEroare fractii polinoame: " + str(result['poliErr']))

tk.Button(win, text="Precizie masina la egalitate", width=25, command=press_btn1).pack(side=tk.LEFT)
tk.Button(win, text="Precizie masina la associativitate", width=25, command=press_btn2).pack(side=tk.LEFT)
tk.Button(win, text="Calculare tangenta", width=25, command=press_btn3).pack(side=tk.RIGHT)
tk.Button(win, text="Calculare tangenta (generare 10000 numere) ", width=35,  command=press_btn4).pack(side=tk.RIGHT)
win.mainloop()


