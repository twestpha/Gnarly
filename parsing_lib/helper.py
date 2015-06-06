# helper.py
# Trevor Westphal

import datetime
import urllib.request
from urllib import *

def openDbFile(category):
	dbFilePathString = ("db/%s.db" % category)

	try:
		dbFile = open(dbFilePathString, "a+")
	except:
		errorFile = open("error_log.txt", "a")
		errorFile.write("Error accessing db: %s, %s\n" % (dbFilePathString, datetime.datetime.now()))
		errorFile.close()
		return

	return (dbFile)

def getHTMLDoc(url):
	try:
		request = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
		response = urllib.request.urlopen(request)
	except Exception as e:
		errorFile = open("error_log.txt", "a")
		errorFile.write("Error accessing site: %s, %s, %s\n" % (url, e, datetime.datetime.now()))
		errorFile.close()
		return
	
	return response.read().decode('utf-8')

def getLastPostTime(dbFile):
	dbFile.seek(0, 0)
	for line in dbFile:
		pass
	
	return line.split("|")[-1]

def dateFromBrothersBrickString(dateString):
	# 2015-06-05T18:05:50+00:00
	# 0123456789012345678901234

	year = int(dateString[0:4])
	month = int(dateString[5:7])
	day = int(dateString[8:10])
	hour = int(dateString[11:13])
	minute = int(dateString[14:16])
	second = int(dateString[17:19])
	d = datetime.datetime(year, month, day, hour, minute, second)

	return d