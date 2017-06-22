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






def isLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return 366
    else:
        return 365


# sum the days till the month 
def daysTillMonth(y, m):
    i = 0
    days = 0
    if isLeapYear(y) == 366:
        daysOfMonths[1] = 29
    else:
        daysOfMonths[1] = 28

    while i < m - 1:
        days = days + daysOfMonths[i]
        i += 1
    return days



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

    days = 0

    if checkTimeTravel(y1, m1, d1, y2, m2, d2):
        return 'NO TIME TRAVAL'
    
    else:
        if y1 == y2:
            days = daysTillMonth(y2, m2) + d2 - daysTillMonth(y1, m1) - d1
        else:
            days = isLeapYear(y1) - daysTillMonth(y1, m1) - d1 + daysBetweenYear(y1+1, y2-1) + daysTillMonth(y2, m2) + d2

        return days
        


print daysBetweenDates(2016, 6, 1, 2017, 6, 1)
print isLeapYear(2016)
print daysTillMonth(2016, 6)
print daysBetweenYear(2017, 2016)
