"""
date_time_playground.py
This program is used to experiment various methods related to date and time functionality.
@author: Can Akman @ the Laboratory
@version: 30.12.2017_v1.0
"""


import datetime, time, calendar

# Get the current date (requires "datetime" module):
currentDate = datetime.date.today()

# Get the current local time (requires "time" module):
currentTime = time.asctime(time.localtime())

# Get the calendar for a specific month (requires "calendar" module):
monthCalendar = calendar.month(2018, 1)

# Get the calendar for the year:
calendarOne = calendar.calendar(2018, w=2,l=1,c=5)

# Sleep for given number of seconds:
time.sleep(1)                                 