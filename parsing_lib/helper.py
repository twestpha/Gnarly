# helper.py
# Trevor Westphal

import datetime
import urllib.request
from urllib import *

def openDbFiles(category):
	dbFilePathString = ("db/%s/%s.db" % (category, category))
	dbMetaDataString = ("db/%s/%s.dbm" % (category, category))

	try:
		dbMeta = open(dbMetaDataString, "r")
	except:
		errorFile = open("error_log.txt", "a")
		errorFile.write("Error accessing db: %s, %s, %s\n" % (dbFilePathString, dbMetaDataString, datetime.datetime.now()))
		errorFile.close()
		return

	dbFile = open(dbFilePathString, "a")

	return (dbFile, dbMeta)

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