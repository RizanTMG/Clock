import time
import os

# variables
second = 0
minute = 0
hour = 0

while True:
    # clearing screen
    os.system("clear")
    
    # printing time with while loop
    hour = str(hour)
    minute = str(minute)
    second = str(second)
    print(hour + " : " + minute + " : " + second)
        
    #  Increasing time
    time.sleep(1)
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    
    # managing second
    if second < 60:
        second += 1
    elif second == 60:
        second = 0
        minute += 1
    
    # managing minute
    if minute < 2:
        pass
    elif minute == 60:
        minute = 0
        hour += 1
        
    # managing hour
    if hour < 24:
        pass
    elif hour == 24:
        hour = 0
