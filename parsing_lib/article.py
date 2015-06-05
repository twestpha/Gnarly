# article.py
# Trevor Westphal

class Article:
	def __init__(self):
		self.title = ""
		self.articleLink = ""
		self.discussionLink = ""
		self.imageLink = ""
		self.imageSrc = ""
		self.comment = ""
		self.time = ""

	def getDBString(self):
		return ("%s|%s|%s|%s|%s|%s|%s\n" % (self.title, self.articleLink, self.discussionLink, self.imageLink, self.imageSrc, self.comment, self.time))

	def getUniqueID(self):
		return self.title + self.time