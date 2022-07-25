#test on wifi (duh)

import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print(webUrl.getcode())

    data = webUrl.read()
    print(data)
if __name__ == "__main__":
    main()