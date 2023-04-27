try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
import tkinter.ttk as ttk
from tktooltip import ToolTip
from tkinter import *
from tkinter import filedialog
from tkinter.tix import *

bg_color = '#333333'
button_color = '#1D1D1D'

root = Tk()

root.title("Binary tree generator")
# root.iconphoto(False, tk.PhotoImage(file="./img/icon.png"))
root.geometry('1300x950')
root.resizable(False, False)
root.configure(bg=bg_color)

tip = Balloon(root)

def cd():
    global path
    path = filedialog.askdirectory()
    cd_entry.delete(0, END)
    cd_entry.insert(0, path)

root.tk.call("source", "Azure/azure.tcl")
root.tk.call("set_theme", "dark")

style = ttk.Style()
style.configure("Button.TButton", foreground="black", background="white", borderwidth=0)
style.configure("Entry.TEntry", foreground="white", background="white")
style.configure("Combobox.TCombobox", foreground="black", background="white")

# Widgets:
btg_label = tk.Label(root, text="Binary Tree Generator", font=("Arial", 30), bg=bg_color, foreground="black")
loct_label = tk.Label(root, text="Select a directory:", font=("Arial", 20), bg=bg_color, foreground="black")
cd_entry = ttk.Entry(root, font=("Arial", 12), width=30, style="Label.TEntry", cursor="xterm")
cd_button = ttk.Button(root, text="Select", command=cd, style="Button.TButton", cursor="hand2")
values_label = tk.Label(root, text="Values:", font=("Arial", 20), bg=bg_color, foreground="black")
value1_spinbox = ttk.Spinbox(root, increment=1, from_=0, to=999999999999999999999999999999999999999999999999999999999999, wrap=True, width=10)
to_label = tk.Label(root, text="to", font=("Arial", 20), bg=bg_color, foreground="black")
value2_spinbox = ttk.Spinbox(root, increment=1, from_=0, to=999999999999999999999999999999999999999999999999999999999999, wrap=True, width=10)
func_path_label = tk.Label(root, text="Function's path:", font=("Arial", 20), bg=bg_color, foreground="black")
func_path_entry = ttk.Entry(root, font=("Arial", 12), width=40, style="Label.TEntry", cursor="xterm")
namespace_label = tk.Label(root, text="Namespace:", font=("Arial", 20), bg=bg_color, foreground="black")
namespace_entry = ttk.Entry(root, font=("Arial", 12), width=20, style="Label.TEntry", cursor="xterm")
language_combobox = ttk.Combobox(root, values=["English","Spanish"], state="readonly")
language_combobox.current(0)
scoreboard_label = tk.Label(root, text="Scoreboard:", font=("Arial", 20), bg=bg_color, foreground="black")
te_label = tk.Label(root, text="Target entity:", font=("Arial", 20), bg=bg_color, foreground="black")

# Place:
btg_label.grid(column=0, row=0, sticky="nwe", padx=450, columnspan=2, rowspan=2, pady=5)
loct_label.grid(column=0, row=1, sticky="w", padx=30)
cd_entry.grid(column=0, row=2, sticky="w", padx=30, pady=5)
cd_button.grid(column=0, row=2, sticky="w", padx=325)
values_label.grid(column=0, row=3, sticky="ws", padx=30, pady=20)
value1_spinbox.grid(column=0, row=4, sticky="nw", padx=30)
to_label.grid(column=0, row=4, sticky="nw", padx=140)
value2_spinbox.grid(column=0, row=4, sticky="nw", padx=200)
func_path_label.grid(column=0, row=5, sticky="w", padx=30, rowspan=2, columnspan=2, pady=30)
func_path_entry.grid(column=0, row=6, sticky="wn", padx=30, rowspan=2, columnspan=2, pady=80)
namespace_label.grid(column=0, row=7, sticky="ws", padx=30)
namespace_entry.grid(column=0, row=8, sticky="wn", padx=30, pady=10)
language_combobox.grid(column=0, row=9, sticky="ws", padx=30, pady=380)
scoreboard_label.grid(column=1, row=1, sticky="ne")
te_label.grid(column=1, row=1, sticky="wn")

# Hover info:
ToolTip(cd_button, msg="Select the directory where it will generate.", delay=0.4, parent_kwargs={"bg": "black", "padx": 5, "pady": 5}, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

root.mainloop()