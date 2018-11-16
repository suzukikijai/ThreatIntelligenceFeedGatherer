import re 
from bs4 import BeautifulSoup
import requests
import pickle

def squidblacklist(srcURL,regPat,targetFile = 'output.pkl'):
	source = requests.get(srcURL).text
	soup = BeautifulSoup(source,'lxml')
	match = soup.p.text
	test_str = match
	endMesg = "Feed gathering for" + re.sub("https?://([^/]+)[^\n]+",r"\1",srcURL) + " from " + re.sub("^[^\n]+/([^/]+)",r"\1",srcURL)  + " completed."
	matches = re.finditer(regPat, test_str, re.MULTILINE)
	try:
		for matchNum, match in enumerate(matches):
			matchNum = matchNum + 1
			data = re.sub(regPat, r"\1", match.group())
			print(data)
		with open(targetFile, 'wb') as f:
			pickle.dump(data, f)
		return endMesg
	except Exception as e:
		print(e)



def main():
	# VAR Declaration
	sourceCSV = "patterns_url.csv"
	URL_regex = "^[^,]+"
	pattern_regex = "[^,]+$"
	try:
		with open(sourceCSV) as collector:
			next(collector)
			for line in collector: 
				#print(line)
				URLMatches = re.findall(URL_regex,line)
				for URLMatched in URLMatches:
					url = URLMatched
					# print(url)
				patternMatches = re.findall(pattern_regex,line)
				for patternMatched in patternMatches:
					patternData = patternMatched
					# print(patternData)
				print(squidblacklist(url,patternData))
	except Exception as e:
		print(e)
	return "Completed all feeds"
            

print(main())