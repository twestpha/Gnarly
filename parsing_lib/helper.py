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