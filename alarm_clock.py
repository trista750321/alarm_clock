from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the alarm time:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
print("Setting up alarm")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    if alarm_hour == current_hour:
        if alarm_minute == current_minute:
            if alarm_second == current_seconds:
                print("Alarm!")
                playsound("alarm.wav")
                break

