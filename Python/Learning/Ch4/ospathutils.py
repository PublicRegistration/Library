import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # print the name of the OS
    # print(os.name)

    # # check for item existence and type
    # print("Item exists:", path.exists("textfile.txt"))
    # print("Item is a file:", path.isfile("textfile.txt"))
    # print("Item is a directory:", path.isdir("textfile.txt"))

    # work with file paths
    # print("File path:", path.realpath("textfile.txt"))
    # print("File path and name:", path.split(path.realpath("textfile.txt")))

    # # get modification time
    # t = time.ctime(path.getmtime("textfile.txt"))
    # print("Modification time:", t)
    # print("Modification time:", datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("Item was modified", td, "ago.")
    print("Or", td.total_seconds(), "ago.")


if __name__ == "__main__":
    main()