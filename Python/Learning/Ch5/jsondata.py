#https://www.goo.gl/g2nTxL #US GEO DATA FEED

import json
import jsondata
import urllib.request

def printResults(data):
    #use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    #now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    #output the number of events, plus the magnitude and each event name
    if "count" in theJSON["metadata"]:
        print("Events recorded:", theJSON["metadata"]["count"])

    #for each event, print the place where it occurred
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("-------------------------\n")

    #print the events that only have a magnitude greater than or equal to 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4:
            print(i["properties"]["place"])

    #print only the events where at least 1 person reported feeling something
    for i in theJSON["features"]:
        if i["properties"]["felt"] >= 1:
            print(i["properties"]["place"])

def main():
    #define a variable to hole the source URL
    urlData = "https://www.goo.gl/g2nTxL" #http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5

    #open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    if webUrl == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("ERROR: Web access unavailable")


if __name__ == "__main__":
    main()