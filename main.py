from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

root = Tk()
root.geometry("800x600")
root.title("Simple Text Editor")
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Function for opening a file
def open_file():
    """Open a file for editor"""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    root.title(f"Simple Text Editor - {filepath}")

# Function for saving a file
def save_file():
    """Save the current file"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    root.title(f"Simple Text Editor - {filepath}")

# UI Elements
fr_buttons = Frame(root, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

# Layout
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit = Text(root)
txt_edit.grid(row=0, column=1, sticky="nsew")

root.mainloop()