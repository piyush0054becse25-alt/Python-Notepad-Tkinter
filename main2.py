import tkinter as tk
from tkinter import filedialog , messagebox

root = tk.Tk()
root.title("my notepad")
root.geometry("800x600")
# root.mainloop()
text=tk.text(
    root,
    wrap=tk.WORD,
    font=("Helvetica,18")
)
text.pack(expand=True,fill=tk.BOTH)

def new_file():
    text.delete(1.0,tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file_path:
        with open(file_path,"r") as files:
            text.delete(1.0,tk.END)
            text.insert(tk.END,files.read()) 
def save_file():
    file_path = filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Text Files","*.txt")]
    )
    if file_path:
        with open (file_path,"W") as files:
            files.write(text.get(1.0,tk.END))

    messagebox.showinfo("Info","File saved successfully")

menu = tk.menu(root)
root.config(menu=menu)
file