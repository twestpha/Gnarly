# brothersbrick.py
# Trevor Westphal

def parseBrothersBrick(source, url, category):
	print("Source:%s, URL:%s, Category:%s" % (source, url, category))

	# Open the db files needed
	dbFilePathString = ("db/%s/%s.db" % (category, category))
	dbMetaDataString = ("db/%s/%s.dbm" % (category, category))

	try:
		dbMeta = open(dbMetaDataString, "r")
	except:
		of = open("error_log.txt", "a")
		of.write("Error accessing db: %s, %s, %s\n" % (dbFilePathString, dbMetaDataString, datetime.datetime.now()))
		of.close()

	dbFile = open(dbFilePathString, "a")

	for line in dbMeta:
		print(line)

	dbFile.close()
	dbMeta.close()