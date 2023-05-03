try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import math
import os

bg_color = '#333333'
button_color = '#1D1D1D'
output_form = "Function:"
language_ = "English"

root = Tk()

root.title("Binary tree generator")
root.iconphoto(False, tk.PhotoImage(file="img/icon.png"))
root.geometry('1300x950')
root.resizable(False, False)
root.configure(bg=bg_color)

output_value = IntVar()

def cd():
    path = filedialog.askdirectory()
    cd_entry.delete(0, END)
    cd_entry.insert(0, path)

def change_out():
    global output_form
    if language_combobox.get() == "English":
        if output_value.get() == 0:
            output_form = "Function:"
        else:
            output_form = "Command:"
        value2_spinbox.grid_configure(padx=200)
    else:
        if output_value.get() == 0:
            output_form = "Función:"
        else:
            output_form = "Comando:"
        value2_spinbox.grid_configure(padx=250)
    output_label.config(text=output_form)

def setup(dir_path, func_or_cmd, language_):
    try:
        os.mkdir(rf"{dir_path}\search")
        if func_or_cmd == 0:
            os.mkdir(rf"{dir_path}\output")
    except FileExistsError:
            if language_ == "English":
                messagebox.showerror(title="Error", message="The path already exists.")
                return
            else:
                messagebox.showerror(title="Error", message="El directorio ya existe.")
                return
    generate(int(value1_spinbox.get()), int(value2_spinbox.get()), cd_entry.get(), func_path_entry.get(), namespace_entry.get(), te_entry.get(), scoreboard_entry.get(), func_cmd_entry.get(), func_or_cmd)

    if language_ == "English":
        messagebox.showinfo(title="Done", message="Binary tree generated successfully.")
    else:
        messagebox.showinfo(title="Hecho", message="El árbol binario se generó satisfactoriamente.")

def generate(min, max, dir_path, func_path, nmspc, te, score, code, func_or_cmd):
    mid = math.floor((min + max) / 2)
    output = ""
    filename = f"{dir_path}/search/{str(min)}_{str(max)}.mcfunction"
    if min != mid:
        output = f"execute if score {te} {score} matches {str(min)}..{str(mid)} run function {nmspc}:{func_path}/search/{str(min)}_{str(mid)}"
        generate(min, mid, dir_path, func_path, nmspc, te, score, code, func_or_cmd)
    else:
        if func_or_cmd == 0:
            output = f"execute if score {te} {score} matches {str(min)} run function {nmspc}:{func_path}/output/{str(min)}"
            o = open(f"{dir_path}/output/{str(min)}.mcfunction", "w")
            o.write(code)
            o.close()
        else:
            output = f"execute if score {te} {score} matches {str(min)} run {code}"
    if mid+1 != max:
        output += f"\nexecute if score {te} {score} matches {str(mid+1)}..{str(max)} run function {nmspc}:{func_path}/search/{str(mid+1)}_{str(max)}"
        generate(mid+1, max, dir_path, func_path, nmspc, te, score, code, func_or_cmd)
    else:
        if func_or_cmd == 0:
            output += f"\nexecute if score {te} {score} matches {str(max)} run function {nmspc}:{func_path}/output/{str(max)}"
            o = open(f"{dir_path}/output/{str(max)}.mcfunction", "w")
            o.write(code)
            o.close()
        else:
            output = f"execute if score {te} {score} matches {str(max)} run {code}"
    f = open(filename, "w")
    f.write(output)
    f.close()

def language(event):
    global btg_label
    global loct_label
    global values_label
    global to_label
    global func_path_label
    global te_label
    global cmd_label
    global func_label
    global cd_button
    global generate_button
    if language_combobox.get() == "Español":
        btg_label.config(text="Generador de árboles binarios")
        loct_label.config(text="Selecciona un directorio:")
        values_label.config(text="Valores:")
        to_label.config(text="hasta")
        func_path_label.config(text="Directorio de la función:")
        te_label.config(text="Entidad objetivo:")
        cmd_label.config(text="Comando")
        func_label.config(text="Función")
        cd_button.config(text="Selecciona")
        generate_button.config(text="Generar")
        # ToolTip(cd_button, msg="Selecciona el directorio donde se generará.", delay=0.4, parent_kwargs={"bg": "black", "padx": 5, "pady": 5}, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)
        # ToolTip(generate_button, msg="Genera el árbol.", delay=0.4, parent_kwargs={"bg": "black", "padx": 5, "pady": 5}, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)
    else:
        btg_label.config(text="Binary Tree Generator")
        loct_label.config(text="Select a directory:")
        values_label.config(text="Values:")
        to_label.config(text="to")
        func_path_label.config(text="Function's path:")
        te_label.config(text="Target entity:")
        cmd_label.config(text="Command")
        func_label.config(text="Function")
        cd_button.config(text="Select")
        generate_button.config(text="Generate")
        # ToolTip(cd_button, msg="Select the directory where it will generate.", delay=0.4, parent_kwargs={"bg": "black", "padx": 5, "pady": 5}, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)
        # ToolTip(generate_button, msg="Generate the tree.", delay=0.4, parent_kwargs={"bg": "black", "padx": 5, "pady": 5}, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)
    change_out()

root.tk.call("source", "Azure/azure.tcl")
root.tk.call("set_theme", "dark")

style = ttk.Style()
style.configure("Button.TButton", foreground="black", background="white", borderwidth=0)
style.configure("Entry.TEntry", foreground="white", background="white")
style.configure("Combobox.TCombobox", foreground="black", background="white")

# Widgets:
btg_label = tk.Label(root, text="Binary Tree Generator", font=("Arial", 30), bg=bg_color, foreground="black")
loct_label = tk.Label(root, text="Select a directory:", font=("Arial", 20), bg=bg_color, foreground="black")
cd_entry = ttk.Entry(root, font=("Arial", 12), width=30, style="Entry.TEntry", cursor="xterm")
cd_button = ttk.Button(root, text="Select", command=cd, style="Button.TButton", cursor="hand2")
values_label = tk.Label(root, text="Values:", font=("Arial", 20), bg=bg_color, foreground="black")
value1_spinbox = ttk.Spinbox(root, increment=1, from_=0, to=999999999999999999999999999999999999999999999999999999999999, wrap=True, width=10)
to_label = tk.Label(root, text="to", font=("Arial", 20), bg=bg_color, foreground="black")
value2_spinbox = ttk.Spinbox(root, increment=1, from_=0, to=999999999999999999999999999999999999999999999999999999999999, wrap=True, width=10)
func_path_label = tk.Label(root, text="Function's path:", font=("Arial", 20), bg=bg_color, foreground="black")
func_path_entry = ttk.Entry(root, font=("Arial", 12), width=40, style="Entry.TEntry", cursor="xterm")
namespace_label = tk.Label(root, text="Namespace:", font=("Arial", 20), bg=bg_color, foreground="black")
namespace_entry = ttk.Entry(root, font=("Arial", 12), width=20, style="Entry.TEntry", cursor="xterm")
language_combobox = ttk.Combobox(root, values=["English","Español"], state="readonly")
language_combobox.current(0)
language_combobox.bind("<<ComboboxSelected>>", language)
scoreboard_label = tk.Label(root, text="Scoreboard:", font=("Arial", 20), bg=bg_color, foreground="black")
te_label = tk.Label(root, text="Target entity:", font=("Arial", 20), bg=bg_color, foreground="black")
te_entry = ttk.Entry(root, font=("Arial", 12), width=20, style="Entry.TEntry", cursor="xterm")
scoreboard_entry = ttk.Entry(root, font=("Arial", 12), width=20, style="Entry.TEntry", cursor="xterm")
cmd_label = tk.Label(root, text="Command", font=("Arial", 20), bg=bg_color, foreground="black")
cmd_or_func_switch = ttk.Checkbutton(root, style='Switch.TCheckbutton', command=change_out, variable=output_value)
func_label = tk.Label(root, text="Function", font=("Arial", 20), bg=bg_color, foreground="black")
output_label = tk.Label(root, text=output_form, font=("Arial", 20), bg=bg_color, foreground="black")
func_cmd_entry = ttk.Entry(root, font=("Arial", 12), width=50, style="Entry.TEntry", cursor="xterm")
generate_button = ttk.Button(root, text="Generate", style="Button.TButton", cursor="hand2", command= lambda: setup(cd_entry.get(), output_value.get(), language_combobox.get()))

# Place:
btg_label.grid(column=0, row=0, sticky="nwe", columnspan=2, pady=5)
loct_label.grid(column=0, row=2, sticky="ws", padx=30)
cd_entry.grid(column=0, row=3, sticky="w", padx=30, pady=5)
cd_button.grid(column=0, row=3, sticky="w", padx=325)
values_label.grid(column=0, row=4, sticky="ws", padx=30, pady=20)
value1_spinbox.grid(column=0, row=5, sticky="nw", padx=30)
to_label.grid(column=0, row=5, sticky="nw", padx=140)
value2_spinbox.grid(column=0, row=5, sticky="nw", padx=200)
func_path_label.grid(column=0, row=6, sticky="w", padx=30, rowspan=2, pady=30)
func_path_entry.grid(column=0, row=7, sticky="wn", padx=30, rowspan=2, pady=80)
namespace_label.grid(column=0, row=8, sticky="ws", padx=30)
namespace_entry.grid(column=0, row=9, sticky="wn", padx=30, pady=10)
language_combobox.grid(column=0, row=10, sticky="ws", padx=30, pady=380)
scoreboard_label.grid(column=1, row=2, sticky="ne", padx=250)
scoreboard_entry.grid(column=1, row=3, sticky="ne", padx=210, pady=5)
te_label.grid(column=1, row=2, sticky="nw")
te_entry.grid(column=1, row=3, sticky="nw", pady=5)
func_label.grid(column=1, row=5, sticky="nw", padx=30)
cmd_or_func_switch.grid(column=1, row=5, sticky="nw", padx=190)
cmd_label.grid(column=1, row=5, sticky="n", padx=90)
output_label.grid(column=1, row=6, sticky="nw", rowspan=2, pady=30)
func_cmd_entry.grid(column=1, row=7, sticky="wn", rowspan=2, pady=80)
generate_button.grid(column=1, row=9, sticky="wns", padx=200, pady=10)

# Hover info:
# ToolTip(cd_button, msg="Select the directory where it will generate.", delay=0.4, parent_kwargs={"bg": "black", "padx": 5, "pady": 5}, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)
# ToolTip(generate_button, msg="Generate the tree.", delay=0.4, parent_kwargs={"bg": "black", "padx": 5, "pady": 5}, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)

root.mainloop()