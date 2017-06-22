# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

#!/usr/bin/python 
# -*- coding: utf-8 -*-

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# sum the days till the month 
def daysTillMonth(month):
    i = 0
    days = 0
    while i < month - 1:
        days = days + daysOfMonths[i]
        i += 1
    return days


def isLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return 366
    else:
        return 365

def daysBetweenYear(y1, y2):
    i = y1
    days = 0
    while i < y2:
        days = days + isLeapYear(i)
        i += 1
    return days



def checkTimeTravel(y1, m1, d1, y2, m2, d2):
    if y1 > y2:
        return 1
    elif y1 == y2:
        daysTillMonth(m1) + d1 > daysTillMonth(m2) + d2
        return 1
    else:
        return 0

def daysBetweenDates(y1, m1, d1, y2, m2, d2):

    if checkTimeTravel(y1, m1, d1, y2, m2, d2):
        return 'NO TIME TRAVAL'
    
    else:
        if d2 >= d1:
            days = d2 - d1
            if m2 >= m1:
                days = days + daysTillMonth(m2) - daysTillMonth(m1)
            else:
                days = days + isLeapYear(y2-1) + daysTillMonth(m2) - daysTillMonth(m1)
            days =  days +  daysBetweenYear(y1, y2)
        else:
            days = d2 + daysOfMonths[m2-1] - d1
            if m2 - 1 >= m1:
                days = days + daysTillMonth(m2-1) - daysTillMonth(m1)
            else:
                days = days + isLeapYear(y2-1) + daysTillMonth(m2-1) - daysTillMonth(m1)
            days =  days +  daysBetweenYear(y1, y2-1)

        return days
        
   

print daysBetweenDates(2012, 6, 29, 2013, 6, 29)