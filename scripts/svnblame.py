#!/usr/bin/python
import sys
import urllib
import webbrowser

branch = sys.argv[1]
path = sys.argv[2]

pathPart = "/branches/%s/mscm/src/%s"%(branch,path)
qPathPart = urllib.quote_plus(pathPart)

url =  "http://websvn.hotel.com/blame.php?repname=hotel+Software&path=%s"%(qPathPart)

webbrowser.open(url)


#path=/branches/iteration-0060/mscm/src/com/hotel/msdb/vo/PublisherCampaign.java

