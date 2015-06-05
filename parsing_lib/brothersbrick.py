# brothersbrick.py
# Trevor Westphal
from parsing_lib.helper import openDbFiles, getHTMLDoc
from bs4 import BeautifulSoup
# from HTMLParser import HTMLParser

def parseBrothersBrick(source, url, category):

	# Open the db files needed
	dbFile, dbMeta = openDbFiles(category)

	if(dbFile and dbMeta):

		soup = BeautifulSoup(getHTMLDoc(url))

		for article in soup.find_all("article"):
			for articleElement in article.contents:
				print(articleElement)

	dbFile.close()
	dbMeta.close()