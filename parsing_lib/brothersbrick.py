# brothersbrick.py
# Trevor Westphal
from parsing_lib.helper import openDbFile, getHTMLDoc, getLastPostTime
from bs4 import BeautifulSoup
from parsing_lib.article import Article
# from HTMLParser import HTMLParser

def parseBrothersBrick(source, url, category):

	# Open the db files needed
	dbFile = openDbFile(category)

	if(dbFile):

		# get the latest post (at the end!)
		try:
			lastPostTime = getLastPostTime(dbFile)
			print(lastPostTime)
		except:
			pass

		# get new content and append it to db file

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

			timeArray = article.find_all("time")
			a.time = timeArray[0].get("datetime")

			articles.append(a)

		for article in articles:
			dbFile.write(article.getDBString())


	dbFile.close()