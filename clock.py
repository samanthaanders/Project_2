import datetime
from datetime import date
from datetime import timedelta
from math import trunc
import string
import threading
import tkinter as tk
import time
import sys
from pygame.locals import *
import pygame

pygame.init()
theFont = pygame.font.Font(None, 70)
big_font = pygame.font.Font(None, 150)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 500))
white = (255,255,255)
screen.fill(white)
pygame.display.flip()
pygame.display.set_caption('clock')

window = tk.Tk()

periods = ["Warning", "Period 1","Break 1","Period 2","Lunch","Period 3","Break 2","Period 4"]

period = 0 
showPeriod = ""
start_time = 0
end_time = 0
difference = 0 

def create_date_time(start_time): 
   hours = start_time.split(":")[0]
   minutes = start_time.split(":")[1]
   seconds = 0
   date = datetime.date.today()
   year = date.strftime("%Y")
   month = date.strftime("%m")
   day = date.strftime("%d")
   current_date = datetime.datetime(int(year), int(month), int(day), int(hours), int(minutes), seconds)
   return current_date 

#def set_interval(func, sec):
    #def func_wrapper():
       # set_interval(func, sec)
        #func()
   # t = threading.Timer(sec, func_wrapper)
   # t.start()
   # return t


def set_interval(): 
    while True:
        date_now = datetime.datetime.now()
        #time_now = date_now.strftime("%H:%M:%S")
        time_now = datetime.datetime(int((datetime.date.today()).strftime("%Y")),int((datetime.date.today()).strftime("%m")),int((datetime.date.today()).strftime("%d")),int(date_now.strftime("%H")), int(date_now.strftime("%M")), int(date_now.strftime("%S")))
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
        
        # new clock
        clock.tick(1)
        theTime = str(hour) + ":" + minute + " " + ampm
        #displayTime = theTime.split(",")[0]
        timeText=big_font.render(str(theTime), True,(0,0,0),(255,255,255))
        #colour = (0,0,0)
        #screen.fill(colour)
        pygame.display.update()
        
        
        day = theFont.render(weekday, True, (0,0,0), (255,255,255))
        date = theFont.render((str(date_now).split(" ")[0]), True, (0,0,0), (255,255,255)) 
        #theTime = hour, ":", int(minute), ampm
        #displayTheTime = theFont.render(str(theTime), True, (0,0,0), (255,255,255))
        #time = tk.Label(textvariable = displayTheTime)
        period_countdown = theFont.render("0", True, (0,0,250), (255,255,255))
        pygame.display.update()

        if (date_now.strftime("%w") == 0) or (date_now.strftime("%w") == 6):
            window.configure(bg = "202020")
        else:
            if int(date_now.strftime("%w")) == 3:
                start_times = ["8:30","8:35","9:46","9:53","11:04","11:48","12:59","13:06","14:17"]
            else:
                start_times = ["8:30","8:35","10:02","10:09","11:36","12:15","13:43","13:50","15:17"]
            x = 0
            for i in periods:
                start_time = create_date_time(start_times[x])
                end_time = create_date_time(start_times[x + 1])
                if (time_now > start_time) and (time_now < end_time):
                    #end_time = datetime.datetime(int(date_now.strftime("%Y")), int(date_now.strftime("%m")), int(date_now.strftime("%D")), (end_time))
                    difference = end_time - date_now 
                    period = periods[x]
                    break
                else:
                    difference = 0 # changed from ""
                    period = 0
                x = x + 1
            
            #difference = int(difference)
            #hours = trunc((difference) % (1000 * 60 * 60 * 24) / (1000 * 60 * 60))
            #minutes = trunc((difference % (1000 * 60 * 60)) / (1000 * 60))
            #seconds = trunc((difference % (1000 * 60)) / 1000)
            
        
            #if difference < 2:
                #period_countdown = theFont.render(str(theTime), True,(0,0,255), (255,255,255))
            
            '''
            if seconds < 10:
                seconds = "0", seconds
            if hours > 0:
                if minutes < 10:
                    minutes = "0" + minutes
                theTime = (hours, ":", minutes, ":", seconds)
                period_countdown = theFont.render(str(theTime),True,(0,0,250), (255,255,255))
                pygame.display.update()
            else:
                theTime = (minutes, ":", seconds)
                period_countdown = theFont.render(str(theTime), True, (0,0,250), (255,255,255))
                if minutes < 2:
                    period_countdown = theFont.render(str(theTime), True, (255,255,0), (255,255,255))
                if (minutes == 0) and (seconds == 0):
                    period_countdown = theFont.render(str(theTime), True, (0,0,0), (255,255,255))
            '''
            period_countdown = theFont.render(str(difference).split(".")[0], True, (0,0,0), (255,255,255))
            showPeriod = theFont.render(str(period), True, (0,0,255), (255,255,255))

        # reload each morining for an update
        #day.pack()
        #date.pack()
        #time.pack()
        #period.pack()
        #period_countdown.pack()
        #window.geometry("900x500")
        #window.mainloop()
        #set_interval()

        screen.blit(day, (350,30))
        screen.blit(date, (340,90))
        screen.blit(timeText, (270,150))
        screen.blit(showPeriod , (360,270))
        screen.blit(period_countdown, (370,330))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    
while True:
    set_interval()
    

