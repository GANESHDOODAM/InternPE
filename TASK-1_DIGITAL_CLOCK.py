import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg="black")
root.resizable(False, False)

label = tk.Label(root, font=("Courier", 50, "bold"), bg="black", fg="cyan")
label.pack(expand=True)

def update_time():
    label.config(text=strftime('%H:%M:%S %p'))
    label.after(1000, update_time)

update_time()
root.mainloop()
