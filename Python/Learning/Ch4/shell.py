import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if (path.exists("textfile.txt")):
        # get the pate to the file in the current directory
        src = path.realpath("textfile.txt")

        # let's make a backup copy by appending "bak" to the name
        des = src + ".bak"

        # copy over the permissions, modification times, and other info
        # shutil.copy(src, des)
        # shutil.copystat(src, des)

        # rename the original file
        # os.rename("textfile.txt", "newfile.txt")

        # now put things into a ZIP archive
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)

        # more fine-tuned control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")



if __name__ == "__main__":
    main()