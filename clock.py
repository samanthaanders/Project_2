import datetime
from datetime import date
from datetime import timedelta
import string
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


def set_interval(): 
    while True:
        date_now = datetime.datetime.now()
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
        
        # set up the clock
        clock.tick(1)
        theTime = str(hour) + ":" + minute + " " + ampm
        timeText=big_font.render(str(theTime), True,(0,0,0),(255,255,255))
        pygame.display.update()
        
        day = theFont.render(weekday, True, (0,0,0), (255,255,255))
        date = theFont.render((str(date_now).split(" ")[0]), True, (0,0,0), (255,255,255)) 
        period_countdown = theFont.render("0", True, (0,0,250), (255,255,255))
        pygame.display.update()

        # Saturday or Sunday
        if (date_now.strftime("%w") == "0") or (date_now.strftime("%w") == "6"):
            screen.fill(white)
            pygame.display.flip()
        else:
            # opportunity Wednesday
            if int(date_now.strftime("%w")) == 3:
                start_times = ["8:30","8:35","9:46","9:53","11:04","11:48","12:59","13:06","14:17"]
            else:
                start_times = ["8:30","8:35","10:02","10:09","11:36","12:15","13:43","13:50","15:17"]
            
            # test if current datetime is greater than period start time
            x = 0
            for i in periods:
                start_time = create_date_time(start_times[x])
                end_time = create_date_time(start_times[x + 1])
                if (time_now > start_time) and (time_now < end_time):
                    difference = end_time - date_now 
                    period = periods[x]
                    break
                else:
                    difference = datetime.timedelta(0, 0, 0) 
                    period = " "
                x = x + 1
            
            # countdown display
            if difference == datetime.timedelta(0, 0, 0) and start_time == create_date_time(start_times[8]):
                color = (255,255,255)
                period_countdown = theFont.render(str(difference).split(".")[0], True, (color), (255,255,255))
                # hides countdown at the end of the day
            color = 0,0,255
            two = datetime.timedelta(0, 120, 0)
            if difference < two:
                color = 255,255,0
                period_countdown = theFont.render(str(difference).split(".")[0], True,(color), (255,255,255))
                # sets countdown to yellow 
            else:
                color = 0,0,255
                period_countdown = theFont.render(str(difference).split(".")[0], True, (color), (255,255,255))
            
            # remove extra 0s in the countdown time
            one = datetime.timedelta(0, 3600, 0)
            if difference < one:
                period_countdown = theFont.render((str(difference).split(".")[0]).split("0:")[1], True, (color), (255,255,255))
                if (str(difference).split(".")[0]).split("0:")[1].__contains__(":") == False:
                    period_countdown = theFont.render((str(difference).split(".")[0]).split("0:")[1] + "0" + ":" + (str(difference).split(".")[0]).split("0:")[2], True, (color), (255,255,255))    
                ten_min = datetime.timedelta(0,600, 0)
                if difference < ten_min:
                    period_countdown = theFont.render((str(difference).split(".")[0]).split("0:0")[1], True, (color), (255,255,255))


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

            # display all text
            screen.blit(day, ((450 - (day.get_width() / 2)),30))
            screen.blit(date, ((450 - (date.get_width() / 2)),90))
            screen.blit(timeText, ((450 - (timeText.get_width() / 2)),150))
            screen.blit(showPeriod , ((450 - (showPeriod.get_width() / 2)),270))
            screen.blit(period_countdown, ((450 - (period_countdown.get_width() / 2)),330))

        


        pygame.display.update()

        # close the window 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    
while True:
    set_interval()
    

