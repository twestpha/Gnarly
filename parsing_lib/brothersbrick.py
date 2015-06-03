# brothersbrick.py
# Trevor Westphal
from parsing_lib.helper import openDbFiles

def parseBrothersBrick(source, url, category):
	print("Source:%s, URL:%s, Category:%s" % (source, url, category))

	# Open the db files needed
	dbFile, dbMeta = openDbFiles(category)

	if(fbFile and dbMeta):

		for line in dbMeta:
			print(line)

	dbFile.close()
	dbMeta.close()