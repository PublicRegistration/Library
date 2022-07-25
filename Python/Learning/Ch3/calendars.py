# import the calendar module
import calendar

# create a plain text calendar
#c = calendar.TextCalendar(calendar.SUNDAY)
#st = c.formatmonth(2017, 1, 0, 0)
#print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# st = hc.formatmonth(2017, 1)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2017, 8):
#     print(i)

# the calendar module provides useful utilities for the given local
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)

# for name in calendar.day_name:
#     print(name)


# calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for the each month,
# we can use this script:

for m in range(1,13):
    c = calendar.monthcalendar(2022, m)
    weekone = c[0]
    weektwo = c[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print(calendar.month_name[m], meetday)