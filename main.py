# main.py
# Trevor Westphal

import datetime
from parsing_lib.brothersbrick import parseBrothersBrick

class parseController:

	def __init__(self):
		self.setupKeywordParsingDict()

	def setupKeywordParsingDict(self):
		self.parsingDict = {
			"brothersbrick":parseBrothersBrick
		}

	def parse(self, array):
		try:
			self.parsingDict[array[1]](array[0], array[2], array[3])
		except:
			of = open("error_log.txt", "a")
			of.write("Error parsing keyword: %s, %s, %s, %s\n" % (array[0], array[1], array[2], datetime.datetime.now()))
			of.close()

# Entry point
p = parseController()
f = open("sourcelist.txt", "r")

for line in f:
	line_array = line.strip().split("|")
	if(line[0] != "#"):
		p.parse(line_array)

f.close()