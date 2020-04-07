#!/usr/bin/env python3.6
import time

"""
Timer Utility
User will be prompted when the timer has started
User will press enter to stop the timer
Total run time of the script will then be displayed
"""

start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

#Wait for user to stop timer
input("Press 'Enter' to stop the timer. ")

stop_time = time.localtime()

difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")