import re 
from bs4 import BeautifulSoup
import requests
import pickle

def feedExtractor(srcURL,regPat,targetFile = 'output.pkl'):
	source = requests.get(srcURL).text
	soup = BeautifulSoup(source,'lxml')
	match = soup.p.text
	test_str = match
	endMesg = "Feed gathering for" + re.sub("^[^\n]+/([^/]+)",r"\1",srcURL)  +  " from " + re.sub("https?://([^/]+)[^\n]+",r"\1",srcURL) + " completed."
	try:
		matches = re.finditer(regPat, test_str, re.MULTILINE)
		for matchNum, match in enumerate(matches):
			matchNum = matchNum + 1
			data = re.sub(regPat, r"\1", match.group())
			print(data)
		try:
			with open(targetFile, 'wb') as f:
				if data == "":
					print("ERROR::::: NO DATA RECIEVED")
				else:
					pickle.dump(data, f)

			return endMesg
		except Exception as e:
			print("Feed extractor write error: " + str(e))
	except Exception as e:
		print("Feed regex extractor error: " + str(e))



def main():
	# VAR Declaration
	URL_regex = "^[^,]+"
	pattern_regex = "[^,]+$"
	for x in ["ip","domain"]:
		try:
			sourceCSV = x + ".csv"
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
						filename = x + "/" + re.sub("^[^\n]+/([^/]+)",r"\1",url)  +  " - " + re.sub("https?://([^/]+)[^\n]+",r"\1",url) + ".pkl"
						print(filename)
						print(feedExtractor(url,patternData,filename))
			except Exception as e:
				print("Sub function error in "+str(x)+" : "+str(e))
		except Exception as e:
			print("Main function error: "+str(e))
	return "Completed all feeds"
            

print(main())