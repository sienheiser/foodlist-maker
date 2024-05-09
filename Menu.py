import os
import tkinter as tk
from test import function

def move_selected(from_listbox, to_listbox):
    selected_indices = from_listbox.curselection()
    for i in selected_indices[::-1]:
        to_listbox.insert(tk.END, from_listbox.get(i))
        from_listbox.delete(i)

class Menu:
    def __init__(self,root):
        root.title("Food list generator")

        # Create frames
        self.frame1 = tk.Frame(root)
        self.frame1.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame2 = tk.Frame(root)
        self.frame2.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame3 = tk.Frame(root)
        self.frame3.pack(side=tk.LEFT, padx=10, pady=10)

        # First list box
        self.listbox1 = tk.Listbox(self.frame1, selectmode=tk.MULTIPLE)
        self.listbox1.pack(side=tk.LEFT)

        # Second list box
        self.listbox2 = tk.Listbox(self.frame2, selectmode=tk.MULTIPLE)
        self.listbox2.pack(side=tk.LEFT)

        # Button to move items
        self.move_button = tk.Button(self.frame3, text="Move Selected", command=lambda: move_selected(self.listbox1, self.listbox2))
        self.move_button.pack()
        # Button to generate list that depends on selected items
        self.generate_button = tk.Button(self.frame3,text="Generate", command=lambda: self.generate(function))
        self.generate_button.pack()

    def add_items(self,items:list)->None:
        for i in items:
            self.listbox1.insert(tk.END, i)
        return None

    def generate(self,function)->None:
        weekly_list = function(self.listbox2.get(0,tk.END))
        with open("weekly_list.txt","w") as f:
            f.write(weekly_list)
        print(weekly_list)
        return None



if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()
