from tkinter import *
root = Tk()

variable = StringVar(root)
options = {"one": 1, "two": 2, "three": 3}
variable.set("one")

O_menu = OptionMenu(root, variable, *options.keys()).pack()


def sample():
    result = variable.get()
    print(options[result])

bu = Button(root, text="print", command=sample).pack()

root.mainloop()