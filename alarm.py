from datetime import datetime
from playsound import playsound

#Creating input:
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS (Remember to use international hour, 11 pm = 23 hours) \n").split(":")

alarm_hour, alarm_minute = alarm_time[0], alarm_time[1]

print("Setting up alarm")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    
    if (alarm_hour==current_hour) and (alarm_minute==current_minute):
        playsound('alarm.mp3')
        break