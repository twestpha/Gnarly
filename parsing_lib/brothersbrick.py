# brothersbrick.py
# Trevor Westphal
from parsing_lib.helper import openDbFile, getHTMLDoc, getLastPostTime, dateFromBrothersBrickString
from bs4 import BeautifulSoup
from parsing_lib.article import Article
from datetime import datetime
# from HTMLParser import HTMLParser

def parseBrothersBrick(source, url, category):

	# Open the db files needed
	dbFile = openDbFile(category)

	if(dbFile):

		# get the latest post (at the end!)
		lastPostTime = datetime(1, 1, 1, 0, 0, 0)
		try:
			lastPostTime = dateFromBrothersBrickString(getLastPostTime(dbFile))
		except:
			pass

		# get new content and append it to db file
		# ONLY FRONTPAGE RIGHT NOW
		articles = []
		soup = BeautifulSoup(getHTMLDoc(url))
		for article in soup.find_all("article"):

			a = Article()

			linkArray = article.find_all("a")
			a.title = linkArray[0].get_text()
			a.articleLink = linkArray[0].get("href")
			a.discussionLink = a.articleLink + "#comments"

			imgArray = article.find_all("img")
			a.imageLink = imgArray[0].get("src")
			a.imageSrc = imgArray[0].parent.get("href")
			if(not a.imageSrc):
				a.imageSrc = imgArray[0].previous_sibling.get("href")

			paragraphArray = article.find_all("p")
			comment = paragraphArray[0].get_text()
			a.comment = comment[:97] + "..."

			dateTimeArray = article.find_all("time")
			a.time = dateTimeArray[0].get("datetime")

			articleDateTime = dateFromBrothersBrickString(a.time)

			if(articleDateTime > lastPostTime): 
				print("Should add to end: %s>%s" % (articleDateTime, lastPostTime))
				articles.append(a)

		for article in reversed(articles):
			dbFile.write(article.getDBString())


	dbFile.close()