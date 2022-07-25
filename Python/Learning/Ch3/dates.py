from datetime import date
from datetime import time
from datetime import datetime

def main():
    ##DATE OBJECTS
    #get today's date from today() method in date class

    # today = date.today()
    # print("Today's date is", today)

    # #print out date's individual components
    # print("Date components:", today.day, today.month, today.year)

    # #retrieve todat's weekday (0 = monday, 6 = sunday)
    # print("Today's weekday is:", today.weekday())
    # days = ["mon", "tues", "wed", "thru", "fri", "sat", "sun"]
    # print("Which is a:", days[today.weekday()])

    ##DATETIME OBJECTS
    #get today's date from datetime class

    today = datetime.now()
    print ("The current date and time is", today)

    #get the current time

    t = datetime.time(today)
    print("The current time is", t)

if __name__ == "__main__":
    main()