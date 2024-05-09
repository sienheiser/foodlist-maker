from Menu import Menu
from add_functions import add
from test import function
import toml
import tkinter as tk


with open("recepies.toml",'r') as f:
    recepies = toml.loads(f.read())

root = tk.Tk()
menu = Menu(root)
menu.add_items(recepies.keys())
root.mainloop()
