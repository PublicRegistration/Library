from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
from time import strftime

# construct a basic timedelta and print it

print(timedelta(days = 365, hours = 5, minutes = 1))

# print today's date

now = datetime.now()
print("today is ", now)

# print today's date one year from now

print("one year from now it will be", now + timedelta(days = 365))

# create a timedelta that uses more than one argument

print("in 2 days and 3 weeks, it will be", now + timedelta(days = 2, weeks = 3))

# calculate the date 1 week age, formatted as a string

t = datetime.now() - timedelta(weeks = 1)
s = t.strftime("%A, %B %d, %y")
print("one week ago it was " + s)

# how many days until april fools day?

today = date.today()
afd = date(today.year, 4, 1)

if (afd < today):
    print("April Fools Day already went by %d days ago" % ((today - afd).days)) #note the ((today - afd).days) being same type so .days can be called
    afd = afd.replace(year = today.year + 1)

timeToAfd = afd - today
print("It's just", timeToAfd.days, "days until April Fool's Day")