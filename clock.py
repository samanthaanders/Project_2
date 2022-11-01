import datetime
from datetime import datetime
from math import trunc
import string
import threading
import tkinter as tk

window = tk.Tk()

periods = ["Warning", "Period 1","Break 1","Period 2","Lunch","Period 3","Break 2","Period 4"]

period = 0
start_time = 0
end_time = 0
difference = 0

def create_date_time(): #removed start time as a parameter
   current_date = datetime.now()
   return current_date 

#def set_interval(func, sec):
    #def func_wrapper():
       # set_interval(func, sec)
        #func()
   # t = threading.Timer(sec, func_wrapper)
   # t.start()
   # return t


def set_interval(): 
    date_now = datetime.datetime(create_date_time())
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    weekday = weekdays[date_now]
    hour = date_now.stfrtime("%H") 
    ampm = "AM"
    if hour > 11:
        ampm = "PM"
    if hour > 12:
        hour = hour - 12
    minute = date_now.stfrtime("%M")
    if minute < 10:
        minute = "0" + minute
 
    day = tk.Label(text=weekday)
    date = tk.Label(text = string(date_now).split("T"[0]))
    time = tk.Label (text = (hour, ":", minute, " ", ampm))
    period_countdown = tk.Label(foreground = "blue")

    if (date_now == 0) or (date_now == 6):
        window.configure(bg = "202020")
    else:
        if date_now == 3:
            start_times = ["8:30","8:35","9:46","9:53","11:04","11:48","12:59","13:06","14:17"]
        else:
            start_times = ["8:30","8:35","10:02","10:09","11:36","12:15","13:43","13:50","15:17"]
        for i in periods:
            start_time = create_date_time(start_times[i])
            end_time = create_date_time(start_times[i + 1])
            if (date_now > start_time) and (date_now < end_time):
                difference = end_time - date_now
                period = periods[i]
                break
            else:
                difference = ""
                period = ""
    
        hours = trunc(difference % (1000 * 60 * 60 * 24) / (1000 * 60 * 60))
        minutes = trunc((difference % (1000 * 60 * 60)) / (1000 * 60))
        seconds = trunc((difference % (1000 * 60)) / 1000)

        if seconds < 10:
            seconds = "0" + seconds
        if hours > 0:
            if minutes < 10:
                minutes = "0" + minutes
            period_countdown = tk.Label(text = (hours, ":", minutes, ":", seconds))
        else:
            period_countdown = tk.Label(text = (minutes, ":", seconds))
            if minutes < 2:
                period_countdown = tk.Label(foreground = "yellow")
            if (minutes == 0) and (seconds == 0):
                period_countdown = tk.Label(foreground = "white")
        
        period = tk.Label(text = period, foreground = "blue")

    # reload each morining for an update
    date.pack()
    day.pack()
    time.pack()
    period_countdown.pack()
    window.mainloop()
1000

set_interval()


