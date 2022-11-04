import datetime
#from datetime import datetime
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
running = True 

def create_date_time(start_time): 
   hours = start_time.split(":")[0]
   minutes = start_time.split(":")[1]
   seconds = 0
   current_date = datetime.time(int(hours), int(minutes), seconds)
   return current_date 

#def set_interval(func, sec):
    #def func_wrapper():
       # set_interval(func, sec)
        #func()
   # t = threading.Timer(sec, func_wrapper)
   # t.start()
   # return t


def set_interval(): 
    while running == True:
        print('testing')
        date_now = datetime.datetime.now()
        time_now = date_now.strftime("%H:%M:%S")
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        weekday_number = date_now.strftime("%w")
        weekday = weekdays[int(weekday_number)] 
        hour = (date_now.strftime("%H"))
        ampm = "AM"
        if int(hour) > 11:
            ampm = "PM"
        if int(hour) > 12:
            hour = int(hour) - 12
        minute = date_now.strftime("%M")
        if int(minute) < 10:
            minute = "0" + minute
        

        day = tk.Label(text=weekday)
        date = tk.Label(text = str(date_now).split(" ")[0]) 
        displayTheTime = tk.StringVar()
        displayTheTime.set((hour, ":", minute, " ", ampm))
        time = tk.Label(textvariable = displayTheTime)
        period_countdown = tk.Label(foreground = "blue")

        if (date_now.strftime("%w") == 0) or (date_now.strftime("%w") == 6):
            window.configure(bg = "202020")
        else:
            if date_now.strftime("%w") == 3:
                start_times = ["8:30","8:35","9:46","9:53","11:04","11:48","12:59","13:06","14:17"]
            else:
                start_times = ["8:30","8:35","10:02","10:09","11:36","12:15","13:43","13:50","15:17"]
            x = 0
            for i in periods:
                start_time = create_date_time(start_times[x])
                end_time = create_date_time(start_times[x + 1])
                if (time_now > str(start_time)) and (time_now < str(end_time)):
                    #difference = (end_time - time_now)
                    period = periods[x]
                    break
                else:
                    difference = 0 # changed from ""
                    period = 0
                x = x + 1
        
            hours = trunc(int(difference) % (1000 * 60 * 60 * 24) / (1000 * 60 * 60))
            minutes = trunc((difference % (1000 * 60 * 60)) / (1000 * 60))
            seconds = trunc((difference % (1000 * 60)) / 1000)

            if seconds < 10:
                seconds = "0", seconds
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
        day.pack()
        date.pack()
        time.pack()
        period.pack()
        period_countdown.pack()
        window.geometry("900x500")
        window.mainloop()
        #set_interval()
    

set_interval()


