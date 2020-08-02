import sys
import  feedparser
#http://www.geeksforgeeks.org/feed/

def channelinfo(feedogj):
    arr = ["title", "description" , "link","language","generator"]
    if "url" in feedobj:
        print("The url in this rss feed is %s"%(feedobj["url"]))

    if "version" in feedobj:
        print("The version of this rss feed is %s"%(feedobj["version"]))

    if "channel" in feedobj:
        for arg in arr:
            if arg in feedobj["channel"]:
                print( ("The channel %s  : \n %s ") % (arg,feedobj["channel"][arg]))
                
def channelfeedinfo(feedobj):
    items = feedobj["items"]
    args = ["title","summary","link"]
    for item in items:
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        for arg in args:
            if arg in item:
                print(("%s  : \n %s ") % (arg,item[arg]))

url = input("Enter the rss feed url of a website : ")
try:
    feedobj = feedparser.parse(url)
except:
    print(sys.exc_info()[0])
    sys.exit(0)
print("Object Created !!")
print(feedobj)
if feedobj["bozo"] == 0:
    print("--------------------------------------------------------------------------------------------------------")
    print("Parsing Successful !!")
    print("--------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")
    print("Printing Channel information ...")
    print("--------------------------------------------------------------------------------------------------------")
    channelinfo(feedobj)
    print("--------------------------------------------------------------------------------------------------------")
    print("Printing feed item information")
    print("--------------------------------------------------------------------------------------------------------")
    channelfeedinfo(feedobj)
else:
    print("Invalid Feed URL Error")






