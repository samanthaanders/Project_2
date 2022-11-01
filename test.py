import tkinter as tk
import datetime

window = tk.Tk()

date = tk.Label(text = (datetime.datetime.now()))

text = tk.Label(text = "hello", foreground = "blue", background = "yellow")
date.pack()
text.pack()
window.configure(bg="yellow")
window.mainloop()