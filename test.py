import tkinter as tk
import datetime

window = tk.Tk()

day = datetime.datetime(2022, 11, 2)
date = tk.Label(text = (day.strftime("%w")))

day_split = str(day).split()

day2 = datetime.datetime.now()
test = tk.Label(text = day2)

text = tk.Label(text = "hello", foreground = "blue", background = "yellow")
date.pack()
text.pack()
test.pack()
window.configure(bg="yellow")
window.mainloop()