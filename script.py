import datetime
from playsound import playsound

hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
am_pm = input("am/pm: ")

if am_pm == "pm":
    if hour != 12:
        hour = hour + 12
    else:
        hour = 12
    
while True:
    if hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute:
        print("Alarm ON!")
        playsound("alarm.mp3")
        break

