from datetime import datetime

def main():
    #times and dates can be formatted with string codes
    now = datetime.now()
    

    ## DATE FORMATTING ##

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

    # # print(now.strftime("The current year is : %Y"))
    # print(now.strftime("%a, %d %b, %y"))

    # # %c - local date and time, %x - local date, %X - local time

    # print(now.strftime("The local date and time is: %c"))
    # print(now.strftime("The local date is: %x"))
    # print(now.strftime("The local time is: %X"))

    ## TIME FORMATTING ##

    # %I/%H - 12/24 hour, %M - minute, %S - second, %p - local am/pm

    print(now.strftime("Current Time: %I:%M:%S %p"))
    print(now.strftime("Current 24-Hour Time: %H:%M %p"))

if __name__ == "__main__":
    main()
