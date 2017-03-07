#!/usr/bin/python
#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off". 

#alarm_clock(1, False) - '7:00'
#alarm_clock(5, False) - '7:00'
#alarm_clock(0, False) - '10:00'

def alarm_clock(day, vacation):
    if(vacation==False):
        if(day==0):
            alarmtime='10.00'
        else:
            alarmtime='7:00'
    else:
        if(day==0):
            alarmtime="OFF"
        else:
            alarmtime='10:00'
    print `day`+': '+alarmtime

alarm_clock(1, False)
alarm_clock(5, False)
alarm_clock(0, False)
alarm_clock(1, True)
alarm_clock(5, True)
alarm_clock(0, True)
alarm_clock(1, False)
alarm_clock(5, False)
alarm_clock(0, False)
alarm_clock(1, True)
alarm_clock(5, True)
alarm_clock(0, True)
alarm_clock(1, False)
alarm_clock(5, False)
alarm_clock(0, False)
alarm_clock(1, True)
alarm_clock(5, True)
alarm_clock(0, True)
