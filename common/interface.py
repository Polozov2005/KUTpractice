import tkinter as tk
from tkinter import ttk
from ctypes import windll

import equation
import built_in_integration
import my_integration

windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title("")
root.geometry("1600x900")
root.resizable(False, False)

# Задание темы
root.tk.call("source", "common/azure.tcl")
root.tk.call("set_theme", "light")

root.columnconfigure(index=0, weight=2)
root.columnconfigure(index=1, weight=1)
for index in [0, 2]:
    root.rowconfigure(index=index, weight=1)

graph_frame = ttk.Frame(root)
graph_frame.grid(
    row=0, column=0, sticky="nsew", rowspan=3
)

conditions_frame = ttk.LabelFrame(root, text="Начальные условия", padding=(20, 10))
conditions_frame.grid(
    row=0, column=1, padx=10, pady=(20, 10), sticky="nsew"
)
for index in range(5):
    conditions_frame.rowconfigure(index=index, weight=1)

solve_frame = ttk.Frame(root, padding=(0, 10))
solve_frame.grid(
    row=1, column=1, padx=0, pady=(20, 0), sticky="nsew"
)

answer_frame = ttk.LabelFrame(root, text="Ответ", padding=(20, 10))
answer_frame.grid(
    row=2, column=1, padx=10, pady=(20, 10), sticky="nsew"
)
for index in range(2):
    answer_frame.rowconfigure(index=index, weight=1)

graph_image = tk.PhotoImage(file='gfx/graph.png')
graph_label = ttk.Label(graph_frame, image=graph_image)
graph_label.grid(row=0, column=0)

equation_resistance_frame = ttk.Frame(conditions_frame)
equation_resistance_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky="nsew"
)
equation_resistance_image = tk.PhotoImage(file='gfx/resistance.png')
equation_resistance_label = ttk.Label(equation_resistance_frame, image=equation_resistance_image)
equation_resistance_label.grid(
    row=0, column=0, sticky='nsew'
)

equation_y_frame = ttk.Frame(conditions_frame)
equation_y_frame.grid(
    row=1, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
equation_y_image = tk.PhotoImage(file='gfx/y.png')
equation_y_label = ttk.Label(equation_y_frame, image=equation_y_image)
equation_y_label.grid(
    row=0, column=0, sticky='nsew'
)

l_frame = ttk.Frame(conditions_frame)
l_frame.grid(
    row=2, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
l_label = ttk.Label(l_frame, text="l = ")
l_label.grid(
    row=0, column=0, sticky='nsew'
)
l_var = tk.DoubleVar(value=100)
l_entry = ttk.Entry(l_frame, textvariable=l_var)
l_entry.grid(
    row=0, column=1, sticky='nsew'
)
l_unit_label = ttk.Label(l_frame, text="м")
l_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

resist_optionmenu_frame = ttk.Frame(conditions_frame)
resist_optionmenu_frame.grid(
    row=3, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
resist_optionmenu_dictionary = {
    "Серебрo, 0.015 Ом*мм^2/м" : 0.015,
    "Серебро, 0.015 Ом*мм^2/м" : 0.015,
    "Медь, 0.018 Ом*мм^2/м" : 0.018,
    "Золото, 0.023 Ом*мм^2/м" : 0.023,
    "Алюминий, 0.028 Ом*мм^2/м" : 0.028
}
resist_optionmenu_var = tk.StringVar(resist_optionmenu_frame)
resist_optionmenu_var.set("Серебро, 0.015 Ом*мм^2/м")
resist_optionmenu = ttk.OptionMenu(
    resist_optionmenu_frame, resist_optionmenu_var, *resist_optionmenu_dictionary.keys()
)
resist_optionmenu.config(width = 33)
resist_optionmenu.grid(
    row=0, column=0, sticky='nsew'
)


optionmenu_frame = ttk.Frame(conditions_frame)
optionmenu_frame.grid(
    row=4, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
optionmenu_list = ["", "Решение встроенной функцией", "Решение реализованной функцией"]
optionmenu_var = tk.StringVar(value=optionmenu_list[1])
optionmenu = ttk.OptionMenu(
    optionmenu_frame, optionmenu_var, *optionmenu_list
)
optionmenu.config(width = 33)
optionmenu.grid(
    row=0, column=0, sticky='nsew'
)

def solve_command():
    length = l_entry.get()
    rho = resist_optionmenu_dictionary[resist_optionmenu_var.get()]

    if optionmenu_var.get() == "Решение встроенной функцией":
        area = built_in_integration.area()

    if optionmenu_var.get() == "Решение реализованной функцией":
        area = my_integration.area()

    resistance = equation.resistance(rho, area, length)

    area = round(area, 3)
    area_var.set(area)

    resistance = round(resistance, 3)
    resistance_var.set(resistance)

solve_button = ttk.Button(
    solve_frame, text="Решить", style="Accent.TButton", command=solve_command
)
solve_button.config(width=30)
solve_button.grid(row=0, column=0, padx=(250, 0), sticky="nsew")

area_frame = ttk.Frame(answer_frame)
area_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
area_label = ttk.Label(area_frame, text="S = ")
area_label.grid(
    row=0, column=0, sticky='nsew'
)
area_var = tk.DoubleVar(value=0)
area_entry = ttk.Entry(area_frame, state="readonly", textvariable=area_var)
area_entry.grid(
    row=0, column=1, sticky='nsew'
)
area_unit_label = ttk.Label(area_frame, text="см^2")
area_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

resistance_frame = ttk.Frame(answer_frame)
resistance_frame.grid(
    row=1, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
resistance_label = ttk.Label(resistance_frame, text="R = ")
resistance_label.grid(
    row=0, column=0, sticky='nsew'
)
resistance_var = tk.DoubleVar(value=0)
resistance_entry = ttk.Entry(resistance_frame, state="readonly", textvariable=resistance_var)
resistance_entry.grid(
    row=0, column=1, sticky='nsew'
)
resistance_unit_label = ttk.Label(resistance_frame, text="Ом")
resistance_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

root.update()
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

root.mainloop()