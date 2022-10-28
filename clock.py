from datetime import date 
from datetime import datetime
import threading

periods = ["Warning", "Period 1","Break 1","Period 2","Lunch","Period 3","Break 2","Period 4"]

period = 0
start_time = 0
end_time = 0
difference = 0

def create_date_time(start_time):
   current_date = datetime.now()
   return current_date 

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

x = set_interval(def())
